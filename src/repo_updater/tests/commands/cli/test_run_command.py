import os
import unittest
from unittest.mock import Mock 
from unittest.mock import patch 
from repo_updater.commands.cli.run_command import RunCommand
from repo_updater.exceptions.repo_updater_exception import RepoUpdaterException

class TestRunCommand(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = Mock()
        self.command = RunCommand(self.logger)

    def test_should_be_dry_run_true(self) -> None:
        obj = { 'dry_run': True }
        actual = self.command.get_dry_run(obj)
        self.assertTrue(actual)
    
    def test_should_be_dry_run_is_default(self) -> None:
        obj = {}
        actual = self.command.get_dry_run(obj)
        self.assertFalse(actual)
    
    @patch.dict(os.environ, {'AZDEVOPS_CONFIGURATION_PATH': '../templates/example/config.yml'}, clear=True)
    def test_should_be_configuration_file_from_environment(self):
        obj = {}
        expected = self.command.get_configuration_path_file(obj)
        actual = os.path.join(os.getcwd(), os.getenv('AZDEVOPS_CONFIGURATION_PATH'))
        self.assertEqual(expected, actual)

    def test_should_be_configuration_file_from_cli(self):
        obj = {'configuration_file' : '../templates/example/config.yml'}
        expected = self.command.get_configuration_path_file(obj)
        actual = os.path.join(os.getcwd(), obj['configuration_file'])
        self.assertEqual(expected, actual)

    def test_should_be_configuration_file_throw_exception_is_required(self):
        with self.assertRaises(RepoUpdaterException) as ex:
            obj = {}
            self.command.get_configuration_path_file(obj)
        self.assertTrue('is required' in ex.exception.message)

    def test_should_be_configuration_file_throw_exception_not_found(self):
        with self.assertRaises(RepoUpdaterException) as ex:
            obj = {'configuration_file' : '../templates/example/config2.yml'}
            self.command.get_configuration_path_file(obj)
        self.assertTrue('not found' in ex.exception.message)

    def test_should_be_configuration_file_throw_exception_not_valid(self):
        with self.assertRaises(RepoUpdaterException) as ex:
            obj = {'configuration_file' : '../templates/example'}
            self.command.get_configuration_path_file(obj)
        self.assertTrue('not valid' in ex.exception.message)

    @patch.dict(os.environ, {'AZDEVOPS_ORGANIZATION_URL': 'https://dev.azure.com/damienaicheh0990/'}, clear=True)
    def test_should_be_organization_url_from_environment(self):
        obj = {}
        expected = self.command.get_organization_url(obj)
        actual = 'https://dev.azure.com/damienaicheh0990/'
        self.assertEqual(expected, actual)

    def test_should_be_organization_url_from_cli(self):
        obj = { 'organization_url': 'https://damienaicheh0990.visualstudio.com/' }
        expected = self.command.get_organization_url(obj)
        actual = 'https://damienaicheh0990.visualstudio.com/'
        self.assertEqual(expected, actual)
    
    def test_should_be_organization_url_throw_exception_is_required(self):
        with self.assertRaises(RepoUpdaterException) as ex:
            obj = {}
            self.command.get_organization_url(obj)
        self.assertTrue('is required' in ex.exception.message)

    @patch.dict(os.environ, {'AZDEVOPS_ORGANIZATION_URL': 'https://www.google.fr'}, clear=True)
    def test_should_be_organization_url_throw_exception_not_valid(self):
        with self.assertRaises(RepoUpdaterException) as ex:
            obj = {}
            self.command.get_organization_url(obj)
        self.assertTrue('not valid' in ex.exception.message)

    @patch.dict(os.environ, {'AZDEVOPS_PAT_TOKEN': 'azertyuio'}, clear=True)
    def test_should_be_pat_token_from_environment(self):
        obj = {}
        expected = self.command.get_pat_token(obj)
        actual = 'azertyuio'
        self.assertEqual(expected, actual)

    def test_should_be_pat_token_from_cli(self):
        obj = { 'pat_token': 'azertyuio' }
        expected = self.command.get_pat_token(obj)
        actual = 'azertyuio'
        self.assertEqual(expected, actual)
    
    def test_should_be_pat_token_throw_exception_is_required(self):
        with self.assertRaises(RepoUpdaterException) as ex:
            obj = {}
            self.command.get_pat_token(obj)
        self.assertTrue('is required' in ex.exception.message)
        
    def test_should_be_output_default(self):
       obj = {}
       actual = os.getcwd()
       excepted = self.command.get_output(obj)
       self.assertEqual( actual, excepted)

    def test_should_be_output_from_cli(self):
       obj = {'output': os.path.join(os.getcwd(),'../') }
       actual = os.path.join(os.getcwd(),'../')
       excepted = self.command.get_output(obj)
       self.assertEqual( actual, excepted)

    def test_should_be_output_throw_exception_not_valid(self):
        with self.assertRaises(RepoUpdaterException) as ex:
            obj = {'output': os.path.join(os.getcwd(),'../a') }
            self.command.get_output(obj)
        self.assertTrue('not valid' in ex.exception.message)

    def test_should_be_load_configuration_valid(self):
        obj = {'configuration_file' : '../templates/example/config.yml'}
        configuration_file = self.command.get_configuration_path_file(obj)
        expected = self.command.load_configuration(configuration_file)
        self.assertTrue(len(expected.actions)>0)