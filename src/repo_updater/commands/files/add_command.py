#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
from repo_updater.commands.files.file_command import FileCommand
from repo_updater.commands.files.file_command_args import FileCommandArgs

class AddFileCommand(FileCommand):

    def __init__(self, logger):
        """initializes a new instance of the class"""
        super().__init__(logger)
  
    def _on_execute(self, args: FileCommandArgs):
        """Add new files to the repository"""
        for file in args.files:
            if file.override != False:
                path = file.path if file.path != None else ''
                self.logger.info(f'args.assets_directory: {args.assets_directory}')
                self.logger.info(f'file.name: {file.name}')
                src = os.path.join(args.assets_directory, file.name)
                dst = os.path.join(args.output, args.repository.name, path, file.name)
                self.logger.info(f'Source: {src}')
                self.logger.info(f'Destination: {dst}')
                shutil.copyfile(src, dst)
                self.logger.info(f"Added file: {src} to repository: {dst}")