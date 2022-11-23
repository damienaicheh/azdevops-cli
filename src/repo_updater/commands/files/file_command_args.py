class FileCommandArgs(object):
    def __init__(self, assets_directory: str, output: str, repository, action):
        self.assets_directory = assets_directory
        self.output = output
        self.repository = repository
        self.action = action
