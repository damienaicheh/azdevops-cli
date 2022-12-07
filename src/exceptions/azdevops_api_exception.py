from src.exceptions.azdevops_exception import AzDevOpsException

class AzDevOpsApiException(AzDevOpsException):

    def __init__(self, message):
        super().__init__('Api Exception', message)
