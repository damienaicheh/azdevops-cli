#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import traceback
import sys
import yaml
from git import Repo
from base.commands.cli.cli_command import CliCommand
from models.azure_devops_credentials import AzureDevOpsCredentials
from helpers.azure_devops import (
    configuration_from_dict,
    create_pull_request,
    get_repositories_to_process
)
from repos_updater.helpers.files_actions import( 
    apply_action,
    commit_and_push_changes
)
from repos_updater.exceptions.repo_updater_exception import RepoUpdaterException

class RunCommand(CliCommand):

    def __init__(self, logger):
        """initializes a new instance of the class"""
        super().__init__(logger)

    def get_configuration_path_file(self, obj):
        """Define the absolute configuration path file"""
        result = os.getenv('AZDEVOPS_CONFIGURATION_PATH')
        if 'configuration_file' in obj:
            result = obj['configuration_file']
        if not result or result.strip() == '':
            raise RepoUpdaterException(f'The configuration file is required.')
        if not os.path.isabs(result):
            result = os.path.join(os.getcwd(), result)
        if not os.path.exists(result):
            raise RepoUpdaterException(f'The configuration file \'{result}\' not found.')
        if not os.path.isfile(result):
            raise RepoUpdaterException(f'The configuration file \'{result}\' is not valid.')
        return result
    
    def get_organization_url(self, obj):
        """Define the Azure DevOps organization Url see : https://learn.microsoft.com/en-us/azure/devops/extend/develop/work-with-urls?view=azure-devops&tabs=http"""
        result = os.getenv('AZDEVOPS_ORGANIZATION_URL')
        if 'organization_url' in obj:
            result = obj['organization_url']
        if not result or result.strip() == '':
            raise RepoUpdaterException('The organization URL is required.')
        pattern = '^https:\/\/(dev\.azure\.com\/(?P<org1>[^\/]+)|(?P<org2>[^\.]+)\.visualstudio\.com)(\/)?$'
        if not re.match(pattern, result):
            raise RepoUpdaterException(f'The organization URL {result} is not valid. see https://learn.microsoft.com/en-us/azure/devops/extend/develop/work-with-urls?view=azure-devops&tabs=http')
        return result
    
    def get_pat_token(self, obj):
        """Define the Azure DevOps PAT token"""
        result = os.getenv('AZDEVOPS_PAT_TOKEN')
        if 'pat_token' in obj:
            result = obj['pat_token']
        if not result or result.strip() == '':
            raise RepoUpdaterException('The PAT Token is required.')
        return result

    def get_dry_run(self, obj):
        """Define the flag 'dry run'"""
        result = False
        if 'dry_run' in obj:
            result = bool(obj['dry_run'])
        return result

    def get_output(self, obj):
        """Define the absolute output directory path"""
        result = os.getcwd()
        if 'output' in obj:
            result = obj['output']
        if not os.path.isabs(result):
            result = os.path.join(os.getcwd(), result)
        if not os.path.isdir(result):
            raise RepoUpdaterException(f'The Output directory {result} is not valid.')
        return result
    
    def load_configuration(self, configuration_file):
        """Load the configuration from the YAML file"""
        with open(configuration_file, 'r') as file:
            self.logger.info('Load configuration...')
            yaml_configuration = yaml.load(file, Loader=yaml.FullLoader)
            configuration = configuration_from_dict(yaml_configuration)
            self.logger.debug(configuration.project.name)
            return configuration

    def _on_execute(self, obj):
        try:
            dry_run = self.get_dry_run(obj)
            configuration_file = self.get_configuration_file(obj)
            organization_url = self.get_organization_url(obj)
            pat_token = self.get_pat_token(obj)
            output = self.get_output(obj)
            azure_devops_creds = AzureDevOpsCredentials(organization_url, pat_token)
            configuration = self.load_configuration(configuration_file)
            for repository in get_repositories_to_process(azure_devops_creds, configuration):
                # For each repository apply all actions 
                git_client = Repo.clone_from(repository.remote_url, to_path=os.path.join(output, repository.name), branch= configuration.repository.default_branch)
                for action in configuration.actions:
                    # add , remove, update files
                    apply_action(configuration.assets_directory, output, repository, action, self.logger)
                if not dry_run:
                    # commit and push source on new branch
                    commit_and_push_changes(git_client, configuration.pull_request, self.logger)
                    # create a new pull request
                    create_pull_request(azure_devops_creds, repository, configuration)
        except:
            traceback.print_exc()
            sys.exit(1)