#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from helpers.envs import get_env
from models.azure_devops_credentials import AzureDevOpsCredentials
import yaml
import traceback
import sys
from git import Repo
from base.commands.cli.cli_command import CliCommand
from models.configuration import *
from models.repository import *
from helpers.azure_devops import *
from repos_updater.helpers.files_actions import *

class RunCommand(CliCommand):

    def __init__(self, logger):
        """initializes a new instance of the class"""
        super().__init__(logger)
  
    def _on_execute(self, obj):
        configuration_file = obj['configuration_file']
        output = obj['output']
        dry_run = obj['dry_run']
        organization_url = obj['organization_url'] if obj['organization_url'] != None else get_env('AZDEVOPS_ORGANIZATION_URL')
        pat_token = obj['pat_token'] if obj['pat_token'] != None else get_env('AZDEVOPS_PAT_TOKEN')

        azure_devops_creds = AzureDevOpsCredentials(organization_url, pat_token)
        
        try:
            # Load YAML file content
            with open(os.path.join(os.getcwd(), configuration_file), 'r') as file:
                self.logger.info('Load configuration...')
                yaml_configuration = yaml.load(file, Loader=yaml.FullLoader)
                configuration = configuration_from_dict(yaml_configuration)
                self.logger.debug(configuration.project.name)
                self.logger.debug('')

                repositories = get_repositories_to_process(azure_devops_creds, configuration)
                
                for repository in repositories:
                    # For each repository apply all actions 
                    git_client = Repo.clone_from(repository.remote_url, to_path=os.path.join(output, repository.name), branch= configuration.repository.default_branch)
                    for action in configuration.actions:
                        apply_action(configuration.assets_directory, output, repository, action, self.logger)
                    if not dry_run:
                        commit_and_push_changes(git_client, configuration.pull_request, self.logger)
                        create_pull_request(azure_devops_creds, repository, configuration)
        except:
            traceback.print_exc()
            sys.exit(1)