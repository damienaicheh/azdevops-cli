#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from repo_updater.commands.files.file_command import FileCommand
from repo_updater.commands.files.file_command_args import FileCommandArgs

class DeleteFileCommand(FileCommand):

    def __init__(self, logger):
        """initializes a new instance of the class"""
        super().__init__(logger)
  
    def _on_execute(self, args: FileCommandArgs) -> None:
        """Delete list of files from the repository"""
        self.logger.info(f"Delete files inside repository {args.repository.name}")
        for file in args.files:
            path = file.path if file.path != None else ''
            file_path = os.path.join(args.output, args.repository.name, path, file.name)
            if os.path.exists(file_path):
                os.remove(file_path)
                self.logger.info(f'File removed: {file_path}')