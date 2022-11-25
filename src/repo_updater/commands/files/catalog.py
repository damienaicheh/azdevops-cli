from logging import Logger
from repo_updater.commands.files.add_command import AddFileCommand
from repo_updater.commands.files.update_command import UpdateFileCommand
from repo_updater.commands.files.delete_command import DeleteFileCommand

def get_catalog(logger: Logger):
    """Get the catalog of file command"""
    return {
        'add': AddFileCommand(logger),
        'delete': DeleteFileCommand(logger),
        'update': UpdateFileCommand(logger)
    }