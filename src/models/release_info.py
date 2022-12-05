class ReleaseArtifactInfo(object):
    def __init__(self, name: str, version: str):
        self.name = name
        self.version = version

class ReleaseEnvInfo(object):
    def __init__(self, name: str):
        self.name = name
        self.artifacts = []

class ReleaseInfo(object):
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.environments = []