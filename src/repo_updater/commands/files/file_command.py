from logging import Logger
from abc import ABC, abstractmethod
from src.repo_updater.commands.files.file_command_args import FileCommandArgs

class FileCommand(ABC):
    def __init__(self, logger: Logger):
        self.logger = logger

    def execute(self, args: FileCommandArgs) -> None:
        self._on_execute(args)

    @abstractmethod
    def _on_execute(self, args: FileCommandArgs) -> None:
        pass
