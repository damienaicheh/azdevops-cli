import base64
import json
import os
import re
from logging import Logger
from git import Repo
from requests import request
from src.models.azure_devops_credentials import AzureDevOpsCredentials
from src.models.azure_devops_definition import AzureDevOpsDefinition
from src.exceptions.azdevops_exception import AzDevOpsException
from src.models.helper import dic2object

def get_organization_url() -> str:
    """Define the Azure DevOps organization Url see : https://learn.microsoft.com/en-us/azure/devops/extend/develop/work-with-urls?view=azure-devops&tabs=http"""
    result = os.getenv('AZDEVOPS_ORGANIZATION_URL')
    if not result or result.strip() == '':
        raise AzDevOpsException(None, 'The organization URL is required.')
    pattern = '^https:\/\/(dev\.azure\.com\/(?P<org1>[^\/]+)|(?P<org2>[^\.]+)\.visualstudio\.com)(\/)?$'
    if not re.match(pattern, result):
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

def call_api(azure_devops_creds: AzureDevOpsCredentials, method: str, path: str, body = None) -> str:
    """Generic method to do api calls to the API"""
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': get_authorization_header(azure_devops_creds)
    }
    response = request(
                method=method,
                url = f'{azure_devops_creds.organization_url}{path}',
                headers = headers,
                json = body
            )
    return response.text

def get_repositories(azure_devops_creds: AzureDevOpsCredentials, project_name: str):
    """Get all repositories from the project and filter them to find the list of them to edit"""
    result = []
    repositories_result = call_api(azure_devops_creds, 'GET', f'/{project_name}/_apis/git/repositories?api-version=6.0')
    for item in json.loads(repositories_result)['value']:
        result.append(dic2object(item))
    return result

def create_pull_request(azure_devops_creds: AzureDevOpsCredentials, repository, configuration) -> None:
    """Create a pull request for a specific repository"""
    body = {
        'sourceRefName': f'refs/heads/{configuration.pull_request.branch}',
        'targetRefName': f'refs/heads/{configuration.repository.default_branch}',
        'title': f"{configuration.pull_request.name}"
    }
    call_api(azure_devops_creds, 'POST', f"/{configuration.project.name}/_apis/git/repositories/{repository.id}/pullrequests?api-version=6.0", body)

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
    return AzureDevOpsCredentials(
        organization_url = organization_url,
        pat_token = personal_access_token
    )

def get_release_definitions_by_project(azure_devops_creds: AzureDevOpsCredentials, project_name: str):
    """Get release definitions by project"""
    json_release_definitions = call_api(azure_devops_creds, 'GET', f'/{project_name}/_apis/release/definitions?api-version=7.0')
    result = []
    for item in json.loads(json_release_definitions)['value']:
        definition =  dic2object(item)
        result.append(AzureDevOpsDefinition(definition.id, definition.name))
    return result

def get_release_by_definition(azure_devops_creds: AzureDevOpsCredentials, project_name: str, definition_id):
    """Get release by definition"""
    json_release = call_api(azure_devops_creds, 'GET', f'/{project_name}/_apis/release/definitions/{definition_id}?api-version=7.0')
    release = dic2object(json.loads(json_release))
    return release

def get_release_by_id(azure_devops_creds: AzureDevOpsCredentials, project_name: str, release_id):
    """Get release defail by id"""
    json_release_detail = call_api(azure_devops_creds, 'GET', f'/{project_name}/_apis/release/releases/{release_id}?api-version=7.0')
    release_detail = dic2object(json.loads(json_release_detail))
    return release_detail
