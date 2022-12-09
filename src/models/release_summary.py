class ReleaseArtifactSummary(object):
    def __init__(self, name: str, version: str):
        self.name = name
        self.version = version

class ReleaseEnvSummary(object):
    def __init__(self, name: str, deployed_on: str):
        self.name = name
        self.artifacts = []
        self.deployed_on = deployed_on

class ReleaseSummary(object):
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.environments = []