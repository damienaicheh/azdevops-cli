import os
import re
import traceback
import sys
import yaml
from cerberus import Validator
import shutil

from src.base.commands.cli.cli_command import CliCommand
from src.repo_updater.commands.files.helper import get_catalog
from src.repo_updater.exceptions.repo_updater_exception import RepoUpdaterException
from src.repo_updater.commands.files.file_command_args import FileCommandArgs
from src.repo_updater.schema import Schema
from src.models.helper import dic2object
from src.models.azure_devops_credentials import AzureDevOpsCredentials
from src.helpers.azure_devops import (
    get_repositories,
    clone_repository,
    commit_and_push_changes,
    create_pull_request,
    get_credentials
)

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
        if not os.path.exists(result):
            os.makedirs(result)
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

    def get_repositories(self, configuration, credential: AzureDevOpsCredentials):
        result = []
        for repository in get_repositories(credential, configuration.project.name):
            flags = 0
            if hasattr(configuration.repository, 'ignore_case'):
                flags = re.IGNORECASE if configuration.repository.ignore_case else 0
            if re.match(configuration.repository.pattern.regex, repository.name, flags):
                result.append(repository)
        return result

    def _on_execute(self, obj):
        try:
            dry_run = self.get_dry_run(obj)
            configuration_file = self.get_configuration_path_file(obj)
            output = self.get_output(obj)
            configuration = self.load_configuration(configuration_file)
            command_catalog = get_catalog(self.logger)
            credential = get_credentials()

            for repository in self.get_repositories(configuration, credential):
                self.logger.info(f'Process {repository.name}')
                to_path = os.path.join(output, repository.name)
                if os.path.exists(to_path):
                    shutil.rmtree(to_path)
                repo = clone_repository(credential, repository.remoteUrl, to_path, configuration.repository.default_branch)
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
                    commit_and_push_changes(repo, configuration.pull_request, self.logger)
                    # create a new pull request
                    create_pull_request(credential, repository, configuration)
        except:
            traceback.print_exc()
            sys.exit(1)