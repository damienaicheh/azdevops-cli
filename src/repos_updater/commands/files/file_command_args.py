#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models.configuration import (
    File,
    List
)
from models.repository import Repository

class FileCommandArgs(object):
    def __init__(self, assets_directory: str, output: str, repository: Repository, files: List[File]):
        self.assets_directory = assets_directory
        self.output = output
        self.repository = repository
        self.files = files