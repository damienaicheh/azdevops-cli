class AzureDevOpsCredentials(object):
    def __init__(self, organization_url, pat_token):
        self.organization_url = organization_url
        self.pat_token = pat_token