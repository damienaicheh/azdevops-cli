import importlib.metadata

class VersionInfos(object):
    def __init__(self):
        self.version = '0.0.0'
        self.description = 'Azure DevOps CLI'

    def get_version_from_package(self):
        self.version = importlib.metadata.version('azdevops_cli')