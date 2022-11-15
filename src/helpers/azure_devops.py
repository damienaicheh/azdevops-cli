#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import json
import os
import re
from models.azure_devops_credentials import AzureDevOpsCredentials
import requests
from models.configuration import *
from models.repository import *

def call_api(azure_devops_creds: AzureDevOpsCredentials, method: str, path: str, body = None) -> str:
    """Generic method to do api calls to the API"""
  
    encoded_pat_token = base64.b64encode(azure_devops_creds.pat_token.encode('utf-8'))
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': f"Basic {encoded_pat_token.decode('utf-8')}",
    }

    response = requests.request(
                method=method,
                url = f'{azure_devops_creds.organization_url}{path}',
                headers = headers,
                json = body
            )

    return response.text

def get_repositories_to_process(azure_devops_creds: AzureDevOpsCredentials, configuration: Configuration) -> List[Repository]:
    """Get all repositories from the project and filter them to find the list of them to edit"""
    repositories_result = call_api(azure_devops_creds, 'GET', f'/{configuration.project.name}/_apis/git/repositories?api-version=6.0')
    repositories = list[Repository]()
    for repository in json.loads(repositories_result)["value"]:
        repository_model = repository_from_dict(repository)
        flags = re.IGNORECASE if configuration.repository.ignore_case else 0
        if re.match(configuration.repository.pattern, repository_model.name, flags):
            repositories.append(repository_model)

    return repositories

def create_pull_request(azure_devops_creds: AzureDevOpsCredentials, repository: Repository, configuration: Configuration):
    """Create a pull request for a specific repository"""
    body = {
        'sourceRefName': f'refs/heads/{configuration.pull_request.branch}',
        'targetRefName': f'refs/heads/{configuration.repository.default_branch}',
        'title': f"{configuration.pull_request.name}"
    }
    call_api(azure_devops_creds, 'POST', f"/{configuration.project.name}/_apis/git/repositories/{repository.id}/pullrequests?api-version=6.0", body)