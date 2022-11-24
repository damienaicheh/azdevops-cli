#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class FileCommandArgs(object):
    def __init__(self, assets_directory: str, output: str, repository, files):
        self.assets_directory = assets_directory
        self.output = output
        self.repository = repository
        self.files = files