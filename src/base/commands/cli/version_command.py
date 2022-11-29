from src.base.commands.cli.cli_command import CliCommand
from src.models.version_infos import VersionInfos

class VersionCommand(CliCommand):

    def __init__(self, logger):
        """initializes a new instance of the class"""
        super().__init__(logger)
  
    def _on_execute(self, obj):
        version_infos = VersionInfos()
        version_infos.get_version_from_package()
        print(f'{version_infos.description} - {version_infos.version}')