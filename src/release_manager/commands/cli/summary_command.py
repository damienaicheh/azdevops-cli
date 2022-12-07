import traceback
import os
import sys
from src.base.commands.cli.cli_command import CliCommand
from src.release_manager.helpers.os_util import get_valid_folder_path
from src.release_manager.helpers.summary_generator import generate_summary
from src.models.azure_devops_credentials import AzureDevOpsCredentials

class SummaryCommand(CliCommand):

    def __init__(self, logger):
        """initializes a new instance of the class"""
        super().__init__(logger)

    def _on_execute(self, obj):
        organization_url = obj['organization_url']
        pat_token = obj['pat_token']
        project_name = obj['project_name']
        output = get_valid_folder_path(obj, 'output')
        azure_devops_creds = AzureDevOpsCredentials(organization_url=os.getenv("AZDEVOPS_ORGANIZATION_URL"),
                               pat_token=os.getenv("AZDEVOPS_PAT_TOKEN"))
        try:
            generate_summary(azure_devops_creds, project_name, output)
        except:
            traceback.print_exc()
            sys.exit(1)