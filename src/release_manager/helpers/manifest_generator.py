#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import git
import os
from helpers.envs import get_env

def generate_manifest(project_path: str, application_name: str, output: str):
    git_client = git.Git(project_path if project_path != None else os.path)
    initial_commit = git_client.rev_parse('HEAD')
    lastest_tag = git_client.describe('--abbrev=0')

    file = open(os.path.join(output, 'manifest.json'), 'a')
    file.truncate(0)

    manifest = {
        "ApplicationName": application_name,
        "PipelineName" : get_env("BUILD_DEFINITIONNAME"),
        "BuildId": get_env("BUILD_BUILDID"),
        "BuildNumber": get_env("BUILD_BUILDNUMBER"),
        "SourceBranchName": get_env("BUILD_SOURCEBRANCHNAME"),
        "Scm": get_env("BUILD_REPOSITORY_NAME"),
        "Sha1": initial_commit,
        "LatestTag": lastest_tag
    }

    file.write(json.dumps(manifest))
    file.close()