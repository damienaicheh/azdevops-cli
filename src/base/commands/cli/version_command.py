#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base.commands.cli.cli_command import CliCommand
from models.version_infos import VersionInfos

class VersionCommand(CliCommand):

    def __init__(self, logger):
        """initializes a new instance of the class"""
        super().__init__(logger)
  
    def _on_execute(self, obj):
        version_infos = VersionInfos()
        print(f'{version_infos.description} - {version_infos.version}')