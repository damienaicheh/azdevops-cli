#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import traceback
import sys
from base.commands.cli.cli_command import CliCommand
from release_manager.helpers.changelog_generator import *
from release_manager.helpers.os_util import get_valid_folder_path

class ChangeLogCommand(CliCommand):

    def __init__(self, logger):
        """initializes a new instance of the class"""
        super().__init__(logger)

    def _on_execute(self, obj):
        project_path = get_valid_folder_path(self, obj, 'project_path')
        output = get_valid_folder_path(self, obj, 'output')
        try:
            generate_changelog(project_path, output)
        except:
            traceback.print_exc()
            sys.exit(1)