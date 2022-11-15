#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import traceback
import sys
from base.commands.cli.cli_command import CliCommand
from release_manager.helpers.changelog_generator import *

class ChangeLogCommand(CliCommand):

    def __init__(self, logger):
        """initializes a new instance of the class"""
        super().__init__(logger)

    def _on_execute(self, obj):
        project_path = obj['project_path']
        output = obj['output']
        try:
            generate_changelog(project_path, output)
        except:
            traceback.print_exc()
            sys.exit(1)