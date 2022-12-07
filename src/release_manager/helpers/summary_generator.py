import os
from typing import List
from src.helpers.azure_devops import (
    get_release_definitions_by_project,
    get_release_by_definition,
    get_release_by_id
)
from src.models.azure_devops_credentials import AzureDevOpsCredentials
from src.models.release_info import (
    ReleaseInfo,
    ReleaseEnvInfo,
    ReleaseArtifactInfo
)

def generate_row(element: str, index: int, maxColumn: int) -> str:
    line = '|'
    for x in range(maxColumn):
        if x == index:
            line += f' {element} '
        else:
            line += f' | '
    line += '|\n'
    return line

def format_artifact(artifacts: List) -> str: 
    """Format the artifacts to put all of them in the same cell"""
    lines = ''
    for artifact in artifacts:
        lines += f' {artifact.name} : {artifact.version} </br>'
    return lines

def generate_environment_row(environments: List) -> str:
    """Generate the environment row with the artifacts associated to it"""
    header_lines = '||'
    artifacts_lines = '||'
    for env in environments:
        header_lines += f' {env.name} |'
        artifacts_lines += f' {format_artifact(env.artifacts)} |'
    header_lines += '\n'
    artifacts_lines += '\n'
        
    return header_lines + artifacts_lines

def generate_markdown(output: str, releases_infos: List):
    """Generate markdown releases summary file"""
    with open(os.path.join(output, 'RELEASES_SUMMARY.md'), 'w') as file:    
        file.write(generate_row('Release Definition', 0, 4))
        file.write('| - | - | - | - |\n')
        for info in releases_infos:
            file.write(generate_row(info.name, 0, 4))
            file.write(generate_environment_row(info.environments))

def generate_summary(azure_devops_creds: AzureDevOpsCredentials, project_name: str, output: str):
    """Generate releases summary and export it as a Markdown file"""
    release_definitions = get_release_definitions_by_project(azure_devops_creds, project_name)
    release_definitions.sort(key=lambda r: r.name)
    releases_infos = []
    for release_definition in release_definitions:
        # Get the global informations for a release by definition
        release = get_release_by_definition(azure_devops_creds, project_name, release_definition.id)
        release_info = ReleaseInfo(release.id, release.name)
        if  hasattr(release, 'environments'):
            for release_env in release.environments:
                # Get the detail informations for a release
                release_detail = get_release_by_id(azure_devops_creds, project_name, release_env.currentRelease.id)
                release_environments = ReleaseEnvInfo(release_env.name)
                if  hasattr(release_detail, 'artifacts'):
                    for artifact in release_detail.artifacts:
                        # Get the artifacts for a release
                        release_environments.artifacts.append(ReleaseArtifactInfo(artifact.alias, artifact.definitionReference.version.name))
                        print(f'{release.id}: {release.name} / {release_env.name} / {release_env.currentRelease.id} / {artifact.alias} : {artifact.definitionReference.version.name} ')
                release_info.environments.append(release_environments)
        releases_infos.append(release_info)

    generate_markdown(output, releases_infos)
        
