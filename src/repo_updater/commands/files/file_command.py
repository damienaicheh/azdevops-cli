from logging import Logger
from abc import ABC, abstractmethod
from repo_updater.commands.files.file_command_args import FileCommandArgs
from repo_updater.exceptions.repo_updater_exception import RepoUpdaterException
import os 
class FileCommand(ABC):
    def __init__(self, logger: Logger):
        self.logger = logger

    def execute(self, args: FileCommandArgs) -> None:
        self._on_execute(args)

    @abstractmethod
    def _on_execute(self, args: FileCommandArgs) -> None:
        pass
