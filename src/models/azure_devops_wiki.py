class AzureDevOpsWikiPage(object):
    def __init__(self, id: int, e_tag: str, content: str):
        self.id = id
        self.e_tag = e_tag
        self.content = content