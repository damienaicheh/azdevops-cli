import base64
import os
import re
from datetime import datetime
from logging import Logger
from git import Repo
from requests import request
from src.exceptions.azdevops_api_exception import AzDevOpsApiException
from src.models.azure_devops_credentials import AzureDevOpsCredentials
from src.models.azure_devops_definition import AzureDevOpsDefinition
from src.exceptions.azdevops_exception import AzDevOpsException
from src.models.helper import dic2object
from src.models.wiki import Wiki

"""
Organization url pattern that match both posibilities:
https://learn.microsoft.com/en-us/azure/devops/extend/develop/work-with-urls?view=azure-devops&tabs=http
"""
organization_url_pattern = '^https:\/\/(dev\.azure\.com\/(?P<org1>[^\/]+)|(?P<org2>[^\.]+)\.visualstudio\.com)(\/)?$'

"""Base url used for calling release definition API"""
vsrm_azure_devops_base_url = 'https://vsrm.dev.azure.com'

"""Azure DevOps Website url"""
azure_devops_base_url = 'https://dev.azure.com'

def get_organization_name() -> str:
    """Extract the organization name"""
    result = os.getenv('AZDEVOPS_ORGANIZATION_URL')
    if not result or result.strip() == '':
        raise AzDevOpsException(None, 'The organization URL is required.')
    matches = re.search(organization_url_pattern, result)
    org1 = matches.group('org1')
    org2 = matches.group('org2')
    if (not org1 and org2) or (org1.strip() == '' and org2.strip() == ''):
        raise AzDevOpsException(None, 'The organization name is not found in the organieation URL.')
    if org1 != None and org1.strip() != '':
        return org1 
    if org2 != None and org2.strip() != '':
        return org2 

def get_organization_url() -> str:
    """Define the Azure DevOps organization Url see : https://learn.microsoft.com/en-us/azure/devops/extend/develop/work-with-urls?view=azure-devops&tabs=http"""
    result = os.getenv('AZDEVOPS_ORGANIZATION_URL')
    if not result or result.strip() == '':
        raise AzDevOpsException(None, 'The organization URL is required.')
    if not re.match(organization_url_pattern, result):
        raise AzDevOpsException(None, f'The organization URL {result} is not valid. see https://learn.microsoft.com/en-us/azure/devops/extend/develop/work-with-urls?view=azure-devops&tabs=http')
    return result
    
def get_personal_access_token() -> str:
    """Define the Azure DevOps PAT token"""
    result = os.getenv('AZDEVOPS_PAT_TOKEN')
    if not result or result.strip() == '':
        raise AzDevOpsException(None, 'The Personal Access Token is required.')
    return result

def get_authorization_header(azure_devops_creds: AzureDevOpsCredentials) -> str:
    """Define the Authorization header"""
    data = f':{azure_devops_creds.pat_token}'
    encoded_pat_token = base64.b64encode(data.encode('utf-8'))
    return f'Basic {encoded_pat_token.decode("utf-8")}'

def create_headers(azure_devops_creds: AzureDevOpsCredentials) -> dict:
    """Create headers for authentication"""
    return {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': get_authorization_header(azure_devops_creds)
    }

def clone_repository(azure_devops_creds: AzureDevOpsCredentials, remote_url: str, to_path: str, branch = 'develop') -> Repo:
    """Clone repository"""
    return Repo.clone_from(
        remote_url, 
        to_path = to_path,
        branch = branch,
        multi_options = [
            f'-c http.extraHeader="Authorization: {get_authorization_header(azure_devops_creds)}"'
        ]
    )

def commit_and_push_changes(repository: Repo, pull_request, logger: Logger) -> None:
    """Commit and push changes on the repository"""
    current = repository.create_head(pull_request.branch)
    current.checkout()
    repository.git.add(A=True)
    logger.debug(repository.git.status())
    repository.git.commit(m=pull_request.name)
    repository.git.push('--set-upstream', 'origin', current)
    logger.debug(repository.git.status())

def get_credentials() -> AzureDevOpsCredentials:
    """Create a new Azure DevOps Credentials"""
    organization_url = get_organization_url()
    personal_access_token = get_personal_access_token()
    organization_name = get_organization_name()
    return AzureDevOpsCredentials(
        organization_url = organization_url,
        pat_token = personal_access_token,
        organization_name = organization_name
    )

def get_repositories(azure_devops_creds: AzureDevOpsCredentials, project_name: str):
    """Get all repositories from the project and filter them to find the list of them to edit"""
    response = request(
                method='GET',
                url = f'{azure_devops_creds.organization_url}/{project_name}/_apis/git/repositories?api-version=6.0',
                headers = create_headers(azure_devops_creds),
            )
    if response.status_code != 200:
        raise AzDevOpsApiException(response.content)
    result = []
    for item in response.json()['value']:
        result.append(dic2object(item))
    return result

def create_pull_request(azure_devops_creds: AzureDevOpsCredentials, repository, configuration) -> None:
    """Create a pull request for a specific repository"""
    body = {
        'sourceRefName': f'refs/heads/{configuration.pull_request.branch}',
        'targetRefName': f'refs/heads/{configuration.repository.default_branch}',
        'title': f"{configuration.pull_request.name}"
    }
    response = request(
                method='POST',
                url = f'{azure_devops_creds.organization_url}/{configuration.project.name}/_apis/git/repositories/{repository.id}/pullrequests?api-version=6.0',
                headers = create_headers(azure_devops_creds),
                json = body
            )
    if response.status_code != 201:
        raise AzDevOpsApiException(response.content)

def get_release_definitions_by_project(azure_devops_creds: AzureDevOpsCredentials, project_name: str):
    """Get release definitions by project"""
    response = request(
            method='GET',
            url = f'{vsrm_azure_devops_base_url}/{azure_devops_creds.organization_name}/{project_name}/_apis/release/definitions?api-version=7.0',
            headers = create_headers(azure_devops_creds),
        )
    if response.status_code != 200:
        raise AzDevOpsApiException(response.content)

    result = []
    for item in response.json()['value']:
        definition =  dic2object(item)
        result.append(AzureDevOpsDefinition(definition.id, definition.name))
    return result

def get_release_by_definition(azure_devops_creds: AzureDevOpsCredentials, project_name: str, definition_id):
    """Get release by definition"""
    response = request(
        method='GET',
        url = f'{vsrm_azure_devops_base_url}/{azure_devops_creds.organization_name}/{project_name}/_apis/release/definitions/{definition_id}?api-version=7.0',
        headers = create_headers(azure_devops_creds),
    )
    if response.status_code != 200:
        raise AzDevOpsApiException(response.content)

    return dic2object(response.json())

def get_release_by_id(azure_devops_creds: AzureDevOpsCredentials, project_name: str, release_id):
    """Get release defail by id"""
    response = request(
        method='GET',
        url = f'{vsrm_azure_devops_base_url}/{azure_devops_creds.organization_name}/{project_name}/_apis/release/releases/{release_id}?api-version=7.0',
        headers = create_headers(azure_devops_creds),
    )
    if response.status_code != 200:
        raise AzDevOpsApiException(response.content)
    return dic2object(response.json())


def init_wiki(azure_devops_creds: AzureDevOpsCredentials, project_name: str) -> str:
    """Get the current wiki or create one if not exist"""
    response = request(
            method='GET',
            url = f'{azure_devops_base_url}/{azure_devops_creds.organization_name}/{project_name}/_apis/wiki/wikis?api-version=7.0',
            headers = create_headers(azure_devops_creds),
        )
    if response.status_code != 200:
        raise AzDevOpsApiException(response.content)
    
    for first_item in response.json()['value']:
        wiki =  dic2object(first_item)
    return wiki.id

def create_wiki_header_page(azure_devops_creds: AzureDevOpsCredentials, project_name: str, wiki_id: str, wiki_folder: str) -> None:
    """Create a new wiki page"""
    response = request(
        method='PUT',
        url = f'{azure_devops_base_url}/{azure_devops_creds.organization_name}/{project_name}/_apis/wiki/wikis/{wiki_id}/pages/{wiki_folder}?api-version=7.0',
        headers = create_headers(azure_devops_creds),
    )

    if response.status_code == 500:
        type_key = response.json()['typeKey']
        if type_key == 'WikiPageAlreadyExistsException':
            return

    if response.status_code != 201:
        raise AzDevOpsApiException(response.content)

def get_wiki_page_by_name(azure_devops_creds: AzureDevOpsCredentials, project_name: str, wiki_id: str, wiki_path: str):
    response = request(
        method='GET',
        url = f'{azure_devops_base_url}/{azure_devops_creds.organization_name}/{project_name}/_apis/wiki/wikis/{wiki_id}/pages?path={wiki_path}$api-version=7.0',
        headers = create_headers(azure_devops_creds),
    )

    if response.status_code != 200:
        raise AzDevOpsApiException(response.content)

    wiki =  dic2object(response.json())
    e_tag = response.headers["etag"]

    return Wiki(wiki.id, e_tag)


def create_or_update_wiki_page(azure_devops_creds: AzureDevOpsCredentials, project_name: str, wiki_id: str, wiki_folder: str, content: str, page_name: str= None) -> None:
    """Create a new wiki page"""
    date_time = datetime.now()
    page_path = page_name if page_name != None else f'{date_time.date()}_{date_time.strftime("%H-%M-%S")}'

    response = request(
        method='PUT',
        url = f'{azure_devops_base_url}/{azure_devops_creds.organization_name}/{project_name}/_apis/wiki/wikis/{wiki_id}/pages/{wiki_folder}/{page_path}?api-version=7.0',
        headers = create_headers(azure_devops_creds),
        json = {
            "content": content
        }
    )
    if response.status_code == 500:
        type_key = response.json()['typeKey']
        if type_key == 'WikiPageAlreadyExistsException':
            wiki_path = f'{wiki_folder}/{page_name}'
            wiki = get_wiki_page_by_name(azure_devops_creds, project_name, wiki_id, f'/{wiki_path}')
            response = request(
                method='PUT',
                url = f'{azure_devops_base_url}/{azure_devops_creds.organization_name}/{project_name}/_apis/wiki/wikis/{wiki_id}/pages/{wiki_path}?api-version=7.0',
                headers = create_headers(azure_devops_creds).update({'if-Match': wiki.e_tag}),
                json = {
                    "content": content
                }
            )
            
    if response.status_code != 201:
        raise AzDevOpsApiException(response.content)