import traceback
import sys
from src.base.commands.cli.cli_command import CliCommand
from src.release_manager.helpers.changelog_generator import generate_changelog
from src.release_manager.helpers.os_util import get_valid_folder_path

class ChangeLogCommand(CliCommand):

    def __init__(self, logger):
        """initializes a new instance of the class"""
        super().__init__(logger)

    def _on_execute(self, obj):
        project_path = get_valid_folder_path(obj, 'project_path')
        output = get_valid_folder_path(obj, 'output')
        try:
            generate_changelog(project_path, output)
        except:
            traceback.print_exc()
            sys.exit(1)