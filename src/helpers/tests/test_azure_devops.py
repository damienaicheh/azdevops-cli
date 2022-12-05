
import os
import unittest
from unittest.mock import Mock 
from unittest.mock import patch 
from src.exceptions.azdevops_exception import AzDevOpsException

from src.helpers.azure_devops import (
    get_organization_url,
    get_personal_access_token,
    get_credentials,
    get_authorization_header
)

class TestRunCommand(unittest.TestCase):

    @patch.dict(os.environ, {'AZDEVOPS_ORGANIZATION_URL': 'https://dev.azure.com/damienaicheh0990/'}, clear=True)
    def test_should_be_organization_url(self):
        expected = get_organization_url()
        actual = 'https://dev.azure.com/damienaicheh0990/'
        self.assertEqual(expected, actual)
    
    def test_should_be_organization_url_throw_exception_is_required(self):
        with self.assertRaises(AzDevOpsException) as ex:
            get_organization_url()
        self.assertTrue('is required' in ex.exception.message)

    @patch.dict(os.environ, {'AZDEVOPS_ORGANIZATION_URL': 'https://www.google.fr'}, clear=True)
    def test_should_be_organization_url_throw_exception_not_valid(self):
        with self.assertRaises(AzDevOpsException) as ex:
            get_organization_url()
        self.assertTrue('not valid' in ex.exception.message)

    @patch.dict(os.environ, {'AZDEVOPS_PAT_TOKEN': 'azertyuio'}, clear=True)
    def test_should_be_personal_access_token(self):
        expected = get_personal_access_token()
        actual = 'azertyuio'
        self.assertEqual(expected, actual)
    
    def test_should_be_pat_token_throw_exception_is_required(self):
        with self.assertRaises(AzDevOpsException) as ex:
            obj = {}
            get_personal_access_token()
        self.assertTrue('is required' in ex.exception.message)

    @patch.dict(os.environ, {'AZDEVOPS_PAT_TOKEN': 'azertyuio', 'AZDEVOPS_ORGANIZATION_URL': 'https://dev.azure.com/damienaicheh0990/' }, clear=True)
    def test_should_be_azure_devops_credential_token(self):
        expected = get_credentials()
        self.assertEqual(expected.organization_url, 'https://dev.azure.com/damienaicheh0990/')
        self.assertEqual(expected.pat_token,'azertyuio')

    @patch.dict(os.environ, {'AZDEVOPS_PAT_TOKEN': 'azertyuio', 'AZDEVOPS_ORGANIZATION_URL': 'https://dev.azure.com/damienaicheh0990/' }, clear=True)
    def test_get_authorization_header_valid(self):
        credential = get_credentials()
        expected = get_authorization_header(credential)
        print(expected)
        self.assertTrue(expected == 'Basic OmF6ZXJ0eXVpbw==' )


 