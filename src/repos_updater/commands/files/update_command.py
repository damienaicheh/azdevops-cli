#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from repos_updater.commands.files.file_command import FileCommand
from repos_updater.commands.files.file_command_args import FileCommandArgs

class UpdateFileCommand(FileCommand):

    def __init__(self, logger):
        """initializes a new instance of the class"""
        super().__init__(logger)
  
    def _on_execute(self, args: FileCommandArgs) -> None:
        """Update the files of a repository based on a regex"""
        for file in args.files:
            path = file.path if file.path != None else ''
            file_path = os.path.join(args.output, args.repository.name, path, file.name)
            if os.path.exists(file_path):
                self.logger.debug('process file {}'.format(file_path))
                tmp_path_file = '{}.tmp'.format(file_path)
                with open(file_path, 'r') as read_file:
                    with open(tmp_path_file, 'w') as write_file:
                        lines = read_file.readlines()
                        nb_line = 1
                        result = ''
                        for line in lines:
                            flags = re.IGNORECASE if file.ignore_case else 0
                            regex_result = re.search(file.pattern, line, flags)
                            if regex_result and regex_result.group('content') != None:
                                result+=line.replace(regex_result.group('content'), file.replace)
                            else:
                                result+=line
                        write_file.write(result)
                        if line.strip() != result.strip():
                            self.logger.debug(' line {} : {} -> {}'.format(nb_line, line.strip(), result.strip()))
                            nb_line = nb_line + 1
                    os.remove(file_path)
                    os.rename(tmp_path_file, file_path)