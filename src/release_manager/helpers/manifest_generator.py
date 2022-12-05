import json
import git
import os

def generate_manifest(project_path: str, application_name: str, output: str):
    git_client = git.Git(project_path if project_path != None else os.path)
    initial_commit = git_client.rev_parse('HEAD')
    lastest_tag = git_client.describe('--abbrev=0')

    file = open(os.path.join(output, 'manifest.json'), 'a')
    file.truncate(0)

    manifest = {
        "ApplicationName": application_name,
        "PipelineName" : os.getenv("BUILD_DEFINITIONNAME"),
        "BuildId": os.getenv("BUILD_BUILDID"),
        "BuildNumber": os.getenv("BUILD_BUILDNUMBER"),
        "SourceBranchName": os.getenv("BUILD_SOURCEBRANCHNAME"),
        "Scm": os.getenv("BUILD_REPOSITORY_NAME"),
        "Sha1": initial_commit,
        "LatestTag": lastest_tag
    }

    file.write(json.dumps(manifest))
    file.close()