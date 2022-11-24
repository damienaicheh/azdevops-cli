#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import traceback
import sys
from base.commands.cli.cli_command import CliCommand
from release_manager.helpers.manifest_generator import generate_manifest
from src.release_manager.exceptions.release_manager_exception import ReleaseManagerException

class ManifestCommand(CliCommand):

    def __init__(self, logger):
        """initializes a new instance of the class"""
        super().__init__(logger)

    def get_application_name(self, obj) -> str:
        """Get the application name"""
        result = obj['application_name']
        if not result or result.strip() == '':
            raise ReleaseManagerException(f'The configuration file is required.')
        return result

    def get_project_path(self, obj) -> str:
        """Define the absolute project path"""
        return self._get_valid_folder_path(self, obj, 'project_path')

    def get_output(self, obj) -> str:
        """Define the absolute output directory path"""
        return self._get_valid_folder_path(self, obj, 'output')

    def _get_valid_folder_path(self, obj, key) -> str:
        """Define an absolute directory path"""
        result = os.getcwd()
        if key in obj:
            result = obj[key]
        if not os.path.isabs(result):
            result = os.path.join(os.getcwd(), result)
        if not os.path.isdir(result):
            raise ReleaseManagerException(f'The {key} directory {result} is not valid.')
        return result

    def _on_execute(self, obj):
        project_path = self.get_project_path(obj)
        application_name = self.get_application_name(obj)
        output = self.get_output(obj)
        try:
            generate_manifest(project_path, application_name, output)
        except:
            traceback.print_exc()
            sys.exit(1)