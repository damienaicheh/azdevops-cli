class AzDevOpsException(Exception):

    def __init__(self, cli, message):
        self.message = f'({cli}) : {message}'
