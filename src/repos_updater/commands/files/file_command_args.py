#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models.configuration import *
from models.repository import *
from models.configuration import *
from models.repository import *

class FileCommandArgs(object):
    def __init__(self, assets_directory: str, output: str, repository: Repository, files: List[File]):
        self.assets_directory = assets_directory
        self.output = output
        self.repository = repository
        self.files = files