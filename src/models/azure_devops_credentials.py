class AzureDevOpsCredentials(object):
    def __init__(self, organization_url: str, pat_token: str):
        self.organization_url = organization_url
        self.pat_token = pat_token