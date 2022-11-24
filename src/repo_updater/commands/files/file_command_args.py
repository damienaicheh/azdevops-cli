class FileCommandArgs(object):
    def __init__(self, assets_directory: str, output: str, repository, files, search):
        self.assets_directory = assets_directory
        self.output = output
        self.repository = repository
        self.files = files
        self.search = search