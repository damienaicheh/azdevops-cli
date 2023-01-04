from logging import Logger
from src.repo_updater.commands.files.add_file_command import AddFileCommand
from src.repo_updater.commands.files.update_file_command import UpdateFileCommand
from src.repo_updater.commands.files.delete_file_command import DeleteFileCommand

def get_catalog(logger: Logger):
    """Get the catalog of file command"""
    return {
        'add': AddFileCommand(logger),
        'delete': DeleteFileCommand(logger),
        'update': UpdateFileCommand(logger)
    }