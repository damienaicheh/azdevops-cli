#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from helpers.azure_devops import *
from repos_updater.commands.files.file_command_args import FileCommandArgs

class FileCommand(ABC):
    def __init__(self, logger):
        self.logger = logger

    def execute(self, args: FileCommandArgs):
        self._on_execute(args)

    @abstractmethod
    def _on_execute(self, args: FileCommandArgs):
        pass