import os
import unittest
from unittest.mock import Mock 
from unittest.mock import patch 
from src.repo_updater.commands.cli.run_command import RunCommand
from src.repo_updater.exceptions.repo_updater_exception import RepoUpdaterException

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
    
    @patch.dict(os.environ, {'AZDEVOPS_CONFIGURATION_PATH': 'templates/example/config.yml'}, clear=True)
    def test_should_be_configuration_file_from_environment(self):
        obj = {}
        expected = self.command.get_configuration_path_file(obj)
        actual = os.path.join(os.getcwd(), os.getenv('AZDEVOPS_CONFIGURATION_PATH'))
        self.assertEqual(expected, actual)

    def test_should_be_configuration_file_from_cli(self):
        obj = {'configuration_file' : 'templates/example/config.yml'}
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
            obj = {'configuration_file' : 'templates/example/config2.yml'}
            self.command.get_configuration_path_file(obj)
        self.assertTrue('not found' in ex.exception.message)

    def test_should_be_configuration_file_throw_exception_not_valid(self):
        with self.assertRaises(RepoUpdaterException) as ex:
            obj = {'configuration_file' : 'templates/example'}
            self.command.get_configuration_path_file(obj)
        self.assertTrue('not valid' in ex.exception.message)

    def test_should_be_output_default(self):
       obj = {}
       actual = os.getcwd()
       excepted = self.command.get_output(obj)
       self.assertEqual(actual, excepted)

    def test_should_be_output_from_cli(self):
       obj = {'output': os.path.join(os.getcwd()) }
       actual = os.path.join(os.getcwd())
       excepted = self.command.get_output(obj)
       self.assertEqual(actual, excepted)

    @patch('os.path.isdir')
    def test_should_be_output_relatif_from_cli(self, mock_isdir) -> None:
       mock_isdir.return_value = True
       obj = {'output': 'tmp/aa/bb' }
       actual = os.path.join(os.getcwd(),'tmp/aa/bb')
       excepted = self.command.get_output(obj)
       self.assertEqual(actual, excepted)

    @patch('os.path.isdir')
    def test_should_be_output_relatif_from_cli(self, mock_isdir) -> None:
       mock_isdir.return_value = True
       obj = {'output': 'aa/bb' }
       actual = os.path.join(os.getcwd(),'aa/bb')
       excepted = self.command.get_output(obj)
       self.assertEqual(actual, excepted)

    @patch('os.path.isdir')
    def test_should_be_output_throw_exception_not_valid(self, mock_isdir) -> None:
        mock_isdir.return_value = False
        with self.assertRaises(RepoUpdaterException) as ex:
            obj = {'output': os.path.join(os.getcwd(),'../a') }
            self.command.get_output(obj)
        self.assertTrue('not valid' in ex.exception.message)

    def test_should_be_load_configuration_valid(self):
        obj = {'configuration_file' : 'src/repo_updater/tests/commands/cli/valid.yml'}
        configuration_file = self.command.get_configuration_path_file(obj)
        expected = self.command.load_configuration(configuration_file)
        self.assertTrue(len(expected.actions)>0)

    def test_should_be_load_configuration_invalid_format(self):
        obj = {'configuration_file' : 'src/repo_updater/tests/commands/cli/test_run_command.py'}
        with self.assertRaises(RepoUpdaterException) as ex:
            self.command.load_configuration(obj)
        self.assertTrue('don\'t have a valid format.' in ex.exception.message)

    def test_should_be_load_configuration_invalid_schema(self):
        obj = {'configuration_file' : 'src/repo_updater/tests/commands/cli/invalid.yml'}
        with self.assertRaises(RepoUpdaterException) as ex:
            self.command.load_configuration(obj)
        self.assertTrue("don't have a valid format." in ex.exception.message)
