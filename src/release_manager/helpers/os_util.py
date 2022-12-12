import os
from src.release_manager.exceptions.release_manager_exception import ReleaseManagerException

def get_valid_folder_path(obj, key: str) -> str:
    """Define an absolute directory path"""
    result = os.getcwd()
    if key in obj and obj[key] != None:
        result = obj[key]
    if not os.path.isabs(result):
        result = os.path.join(os.getcwd(), result)
    if not os.path.isdir(result):
        raise ReleaseManagerException(f'The {key} directory {result} is not valid.')
    return result