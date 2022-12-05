from src.exceptions.azdevops_exception import AzDevOpsException

class ReleaseManagerException(AzDevOpsException):

    def __init__(self, message):
        super().__init__('Release Manager', message)
