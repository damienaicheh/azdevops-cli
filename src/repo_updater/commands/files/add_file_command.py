import os
import shutil
from src.repo_updater.commands.files.file_command import FileCommand
from src.repo_updater.commands.files.file_command_args import FileCommandArgs
from src.repo_updater.exceptions.repo_updater_exception import RepoUpdaterException

class AddFileCommand(FileCommand):

    def __init__(self, logger):
        """initializes a new instance of the class"""
        super().__init__(logger)

    def get_asset_path(self, args: FileCommandArgs) -> str:
        assert_path = None
        if 'asset_path' in args.action.add._fields:
            assert_path = args.action.add.asset_path
        if not assert_path or assert_path.strip() == '':
            raise RepoUpdaterException('The assert path is required on Add File Action.')
        return os.path.join(
            args.assets_directory,
            assert_path
        )

    def get_override(self, args: FileCommandArgs) -> bool:
        if 'override' in args.action.add._fields:
             return args.action.add.override
        return True
  
    def get_target_path(self, args: FileCommandArgs) -> str:
        target_path = None
        if 'target_path' in args.action.add._fields:
            target_path = args.action.add.target_path
        if not target_path or target_path.strip() == '':
            raise RepoUpdaterException('The target path is required on Add File Action.')
        return os.path.join(
            args.output, 
            args.repository.name,
            target_path
        )

    def _on_execute(self, args: FileCommandArgs):
        """Add new directory or file to the repository"""
        asset_path = self.get_asset_path(args)
        override = self.get_override(args)
        target_path = self.get_target_path(args)
        if override:
            if os.path.exists(target_path):
                if os.path.isfile(target_path):
                    os.remove(target_path)
                if os.path.isdir(target_path):
                    shutil.rmtree(target_path)
        if os.path.isdir(asset_path):
            shutil.copytree(asset_path, target_path)
        if os.path.isfile(asset_path):
            shutil.copyfile(asset_path, target_path)
