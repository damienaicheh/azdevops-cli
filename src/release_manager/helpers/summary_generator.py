import os
import re
from datetime import datetime
from dateutil import tz
from typing import List
from logging import Logger
from src.exceptions.azdevops_api_exception import AzDevOpsApiException
from src.helpers.azure_devops import (
    get_release_definitions_by_project,
    get_release_by_definition,
    get_release_by_id
)
from src.models.azure_devops_credentials import AzureDevOpsCredentials
from src.models.release_summary import (
    ReleaseSummary,
    ReleaseEnvSummary,
    ReleaseArtifactSummary
)

def generate_text_in_row(element: str, index: int, max_column: int) -> str:
    """Generate text in the identified column index in a table row"""
    line = '|'
    for x in range(max_column):
        if x == index:
            line += f'**{element}**'
        else:
            line += f' | '
    line += '|\n'
    return line

def generate_separator_for_header(max_column: int) -> str:
    """Generate a sepator to define the header of the table in markdown"""
    line = '|'
    for x in range(max_column):
        line += f' - |'
    line += '\n'
    return line

def format_artifact(artifacts: List) -> str: 
    """Format the artifacts to put all of them in the same cell"""
    lines = ''
    artifacts.sort(key=lambda r: r.name)
    for artifact in artifacts:
        lines += f' {artifact.name} : **{artifact.version}** <br />'
    return lines

def convert_string_to_date(date: str):
    from_zone = tz.tzutc()
    date_time_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
    return date_time_obj.replace(tzinfo=from_zone).date()

def generate_environment_row(environments: List) -> str:
    """Generate the environment row with the artifacts associated to it"""
    header_lines = '||'
    artifacts_lines = '||'
    if not environments:
        return '|| No deployment. |\n'
    else:
        for env in environments:
            header_lines += f' ***{env.name}*** <br /> ({convert_string_to_date(env.deployed_on)}) |'
            artifacts_lines += f' {format_artifact(env.artifacts)} |'
    header_lines += '\n'
    artifacts_lines += '\n'
        
    return header_lines + artifacts_lines

def get_last_deployment_date_by_environment(release_environments: List, env_name: str):
    """Filter the environments to find the correct one in the list and get the last deployment date"""
    for env in release_environments:
        if env.name == env_name:
            return env.modifiedOn
    
    return ''

def generate_markdown(output: str, releases_infos: List, max_column: int):
    """Generate markdown releases summary file"""
    with open(os.path.join(output, 'RELEASES_SUMMARY.md'), 'w') as file:    
        file.write(generate_text_in_row('Releases Definition', 0, max_column))
        file.write(generate_separator_for_header(max_column))
        for info in releases_infos:
            file.write(generate_text_in_row(info.name, 0, max_column))
            file.write(generate_environment_row(info.environments))

def create_environment_for_release_summary(azure_devops_creds: AzureDevOpsCredentials, project_name: str, environment_name: str, current_release_id: int):
    """Create the environment list for the release summary"""
    release_detail = get_release_by_id(azure_devops_creds, project_name, current_release_id)
    last_release_deployment_date = get_last_deployment_date_by_environment(release_detail.environments, environment_name)
    release_environments = ReleaseEnvSummary(environment_name, last_release_deployment_date)
    if  hasattr(release_detail, 'artifacts'):
        for artifact in release_detail.artifacts:
            # Get the artifacts for a release
            release_environments.artifacts.append(ReleaseArtifactSummary(artifact.alias, artifact.definitionReference.version.name))
    
    return release_environments

def generate_summary(azure_devops_creds: AzureDevOpsCredentials, project_name: str, output: str, release_definition_regex: str, logger: Logger):
    """Generate releases summary and export it as a Markdown file"""
    release_definitions = get_release_definitions_by_project(azure_devops_creds, project_name)
    release_definitions.sort(key=lambda r: r.name)
    if release_definition_regex != None:
        release_definitions = list(filter(lambda release_definition: re.match(release_definition_regex, release_definition.name), release_definitions))
    releases_summary = []
    max_environment_per_release = 0
    for release_definition in release_definitions:
         # Get the global informations for a release by definition
        release = get_release_by_definition(azure_devops_creds, project_name, release_definition.id)
        release_summary = ReleaseSummary(release.id, release.name)
        if  hasattr(release, 'environments'):
            for environment in release.environments:
                if max_environment_per_release < len(release.environments):
                    max_environment_per_release = len(release.environments) + 1
                # Get the detail informations for a release
                try:
                    if environment.currentRelease.id != 0:
                        release_summary.environments.append(create_environment_for_release_summary(azure_devops_creds, project_name, environment.name, environment.currentRelease.id))
                except AzDevOpsApiException as ex:
                    logger.error(ex.message)
        releases_summary.append(release_summary)

    generate_markdown(output, releases_summary, max_environment_per_release)
        
