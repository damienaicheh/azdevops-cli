import json
import git
import os

from src.exceptions.azdevops_exception import AzDevOpsException

def generate_manifest(project_path: str, application_name: str, output: str):
    if not os.path.exists(output):
        os.makedirs(output)

    git_path = os.path.join(project_path, '.git')
    if not (os.path.exists(git_path) and os.path.isdir(git_path)):
        raise AzDevOpsException(f'The project path is not a git repository: {project_path}')
    
    git_client = git.Git(project_path if project_path != None else os.path)
    initial_commit = git_client.rev_parse('HEAD')
    latest_tag = git_client.describe('--abbrev=0')

    with open(os.path.join(output, 'manifest.json'), 'w') as file:
        manifest = {
            "ApplicationName": application_name,
            "PipelineName" : os.getenv("BUILD_DEFINITIONNAME"),
            "BuildId": os.getenv("BUILD_BUILDID"),
            "BuildNumber": os.getenv("BUILD_BUILDNUMBER"),
            "SourceBranchName": os.getenv("BUILD_SOURCEBRANCHNAME"),
            "Scm": os.getenv("BUILD_REPOSITORY_NAME"),
            "Sha1": initial_commit,
            "LatestTag": latest_tag
        }

        file.write(json.dumps(manifest))