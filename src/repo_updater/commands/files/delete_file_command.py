import os
import shutil
from src.repo_updater.commands.files.file_command import FileCommand
from src.repo_updater.commands.files.file_command_args import FileCommandArgs
from src.repo_updater.exceptions.repo_updater_exception import RepoUpdaterException

class DeleteFileCommand(FileCommand):

    def __init__(self, logger):
        """initializes a new instance of the class"""
        super().__init__(logger)

    def get_target_path(self, args: FileCommandArgs) -> str:
        target_path = None
        if 'target_path' in args.action.delete._fields:
            target_path = args.action.delete.target_path
        if not target_path or target_path.strip() == '':
            raise RepoUpdaterException('The target path is required on Add File Action.')
        return os.path.join(
            args.output, 
            args.repository.name,
            target_path
        )  

    def _on_execute(self, args: FileCommandArgs) -> None:
        """Delete list of files from the repository"""
        target_path = self.get_target_path(args)
        if os.path.isdir(target_path):
            shutil.rmtree(target_path)
        if os.path.isfile(target_path):
            os.remove(target_path)
