#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import traceback
import sys
from base.commands.cli.cli_command import CliCommand
from release_manager.helpers.manifest_generator import generate_manifest

class ManifestCommand(CliCommand):

    def __init__(self, logger):
        """initializes a new instance of the class"""
        super().__init__(logger)

    def _on_execute(self, obj):
        project_path = obj['project_path']
        application_name = obj['application_name']
        output = obj['output']
        try:
            generate_manifest(project_path, application_name, output)
        except:
            traceback.print_exc()
            sys.exit(1)