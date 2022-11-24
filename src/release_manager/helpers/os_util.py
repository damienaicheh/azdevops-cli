#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from release_manager.exceptions.release_manager_exception import ReleaseManagerException

def get_valid_folder_path(self, obj, key: str) -> str:
    """Define an absolute directory path"""
    result = os.getcwd()
    if key in obj:
        result = obj[key]
    if not os.path.isabs(result):
        result = os.path.join(os.getcwd(), result)
    if not os.path.isdir(result):
        raise ReleaseManagerException(f'The {key} directory {result} is not valid.')
    return result