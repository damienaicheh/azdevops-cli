import traceback
import sys
from src.base.commands.cli.cli_command import CliCommand
from src.release_manager.helpers.manifest_generator import generate_manifest
from src.release_manager.exceptions.release_manager_exception import ReleaseManagerException
from src.release_manager.helpers.os_util import get_valid_folder_path

class ManifestCommand(CliCommand):

    def __init__(self, logger):
        """initializes a new instance of the class"""
        super().__init__(logger)

    def get_application_name(self, obj) -> str:
        """Get the application name"""
        result = ''
        if 'application_name' in obj:
            result = obj['application_name']
        if not result or result.strip() == '':
            raise ReleaseManagerException(f'The application name is required.')
        return result

    def _on_execute(self, obj):
        project_path = get_valid_folder_path(obj, 'project_path')
        output = get_valid_folder_path(obj, 'output')
        application_name = self.get_application_name(obj)
        try:
            generate_manifest(project_path, application_name, output)
        except:
            traceback.print_exc()
            sys.exit(1)