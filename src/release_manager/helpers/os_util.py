#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from release_manager.exceptions.release_manager_exception import ReleaseManagerException

<<<<<<< HEAD
def get_valid_folder_path(obj, key: str) -> str:
=======
def get_valid_folder_path(self, obj, key: str) -> str:
>>>>>>> bb6f874 (feat: Mutualize code and tests.)
    """Define an absolute directory path"""
    result = os.getcwd()
    if key in obj:
        result = obj[key]
    if not os.path.isabs(result):
        result = os.path.join(os.getcwd(), result)
    if not os.path.isdir(result):
        raise ReleaseManagerException(f'The {key} directory {result} is not valid.')
    return result