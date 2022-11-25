import os
import re
import traceback
import sys
import yaml
from git import Repo
from base.commands.cli.cli_command import CliCommand
from models.azure_devops_credentials import AzureDevOpsCredentials
from helpers.azure_devops import (
    create_pull_request,
    get_repositories_to_process,
    commit_and_push_changes
)
from repo_updater.commands.files.catalog import get_catalog
from repo_updater.exceptions.repo_updater_exception import RepoUpdaterException
from repo_updater.commands.files.file_command_args import FileCommandArgs
from cerberus import Validator
from repo_updater.schema import Schema
from models.helper import dic2object
import shutil
class RunCommand(CliCommand):

    def __init__(self, logger):
        """initializes a new instance of the class"""
        super().__init__(logger)

    def get_configuration_path_file(self, obj) -> str:
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
    
    def get_organization_url(self, obj) -> str:
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
    
    def get_pat_token(self, obj) -> str:
        """Define the Azure DevOps PAT token"""
        result = os.getenv('AZDEVOPS_PAT_TOKEN')
        if 'pat_token' in obj:
            result = obj['pat_token']
        if not result or result.strip() == '':
            raise RepoUpdaterException('The PAT Token is required.')
        return result

    def get_dry_run(self, obj) -> bool:
        """Define the flag 'dry run'"""
        result = False
        if 'dry_run' in obj:
            result = bool(obj['dry_run'])
        return result

    def get_output(self, obj) -> str:
        """Define the absolute output directory path"""
        result = os.getcwd()
        if 'output' in obj:
            result = obj['output']
        if not os.path.isabs(result):
            result = os.path.join(os.getcwd(), result)
        if not os.path.isdir(result):
            raise RepoUpdaterException(f'The Output directory {result} is not valid.')
        return result
    
    def load_configuration(self, configuration_file: str):
        """Load the configuration from the YAML file"""
        try:
            with open(configuration_file, 'r') as file:
                self.logger.info('Load configuration...')
                document = yaml.load(file, Loader=yaml.FullLoader)
                v = Validator(Schema)
                if not v.validate(document):
                    self.logger.error(v._errors)
                    raise RepoUpdaterException(f'The configuration file \'{configuration_file}\' don\'t have a valid schema.')
                configuration = dic2object(document)
                self.logger.debug(configuration.project.name)
                return configuration
        except RepoUpdaterException as ruex:
            raise ruex
        except:
            raise RepoUpdaterException(f'The configuration file \'{configuration_file}\' don\'t have a valid format.')

    def build_command_args(self, configuration, output, repository, action) -> FileCommandArgs:
        """Get file command args"""
        assets_directory = configuration.assets_directory
        if not assets_directory:
            assets_directory = os.getcwd()
        if not os.path.isabs(assets_directory):
            assets_directory = os.path.join(os.getcwd(), assets_directory)
        return  FileCommandArgs(
            assets_directory = assets_directory,
            output = output,
            repository = repository,
            action = action
        )

    def _on_execute(self, obj):
        try:
            dry_run = self.get_dry_run(obj)
            configuration_file = self.get_configuration_path_file(obj)
            organization_url = self.get_organization_url(obj)
            pat_token = self.get_pat_token(obj)
            output = self.get_output(obj)
            azure_devops_creds = AzureDevOpsCredentials(organization_url, pat_token)
            configuration = self.load_configuration(configuration_file)
            command_catalog = get_catalog(self.logger)
        
            for repository in get_repositories_to_process(azure_devops_creds, configuration):
                to_path = os.path.join(output, repository.name)
                if os.path.exists(to_path):
                    shutil.rmtree(to_path)
                # For each repository apply all actions 
                git_client = Repo.clone_from(repository.remoteUrl, to_path=os.path.join(output, repository.name), branch= configuration.repository.default_branch)
                for action in configuration.actions:
                    args = self.build_command_args(configuration, output, repository, action)
                    if hasattr(action, 'add'):
                        command_catalog['add'].execute(args)
                    elif hasattr(action, 'delete'):
                        command_catalog['delete'].execute(args)
                    else:
                        command_catalog['update'].execute(args)
                if not dry_run:
                    # commit and push source on new branch
                    commit_and_push_changes(git_client, configuration.pull_request, self.logger)
                    # create a new pull request
                    create_pull_request(azure_devops_creds, repository, configuration)
        except:
            traceback.print_exc()
            sys.exit(1)