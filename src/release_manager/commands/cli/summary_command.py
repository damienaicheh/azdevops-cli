import traceback
import sys
from src.base.commands.cli.cli_command import CliCommand
from src.exceptions.azdevops_exception import AzDevOpsException
from src.helpers.azure_devops import get_credentials
from src.release_manager.helpers.os_util import get_valid_folder_path
from src.release_manager.helpers.summary_generator import generate_summary

class SummaryCommand(CliCommand):

    def __init__(self, logger):
        """initializes a new instance of the class"""
        super().__init__(logger)

    def _on_execute(self, obj):
        regex = obj['regex']
        project_name = obj['project_name']
        wiki_folder = obj['wiki_folder']
        upload = obj['upload']
        output = get_valid_folder_path(obj, 'output')
        credential = get_credentials()

        try:
            if upload and wiki_folder == None:
                raise AzDevOpsException(None, 'If you want to upload the RELEASE_SUMMARY you also should set the --wiki-folder option')
            generate_summary(credential, project_name, wiki_folder, upload, output, regex, self.logger)
        except:
            traceback.print_exc()
            sys.exit(1)