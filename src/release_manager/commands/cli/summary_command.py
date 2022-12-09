import traceback
import os
import sys
from src.base.commands.cli.cli_command import CliCommand
from src.helpers.azure_devops import get_credentials
from src.release_manager.helpers.os_util import get_valid_folder_path
from src.release_manager.helpers.summary_generator import generate_summary
from src.models.azure_devops_credentials import AzureDevOpsCredentials

class SummaryCommand(CliCommand):

    def __init__(self, logger):
        """initializes a new instance of the class"""
        super().__init__(logger)

    def _on_execute(self, obj):
        project_name = obj['project_name']
        output = get_valid_folder_path(obj, 'output')
        regex = obj['regex']
        credential = get_credentials()

        try:
            generate_summary(credential, project_name, output, regex, self.logger)
        except:
            traceback.print_exc()
            sys.exit(1)