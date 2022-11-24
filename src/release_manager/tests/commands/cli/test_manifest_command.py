
import os
import unittest
from unittest.mock import Mock

from src.release_manager.commands.cli.manifest_command import ManifestCommand
from src.release_manager.exceptions.release_manager_exception import ReleaseManagerException

class TestManifestCommand(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = Mock()
        self.command = ManifestCommand(self.logger)

    def test_should_be_project_path_default(self):
       obj = {}
       actual = os.getcwd()
       excepted = self.command.get_project_path(obj)
       self.assertEqual(actual, excepted)

    def test_should_be_project_path_from_cli(self):
       obj = {'project_path': os.path.join(os.getcwd(),'../') }
       actual = os.path.join(os.getcwd(),'../')
       excepted = self.command.get_project_path(obj)
       self.assertEqual(actual, excepted)

    def test_should_be_project_path_throw_exception_not_valid(self):
        with self.assertRaises(ReleaseManagerException) as ex:
            obj = {'project_path': os.path.join(os.getcwd(),'../a') }
            self.command.get_output(obj)
        self.assertTrue('not valid' in ex.exception.message)

    def test_should_be_output_default(self):
       obj = {}
       actual = os.getcwd()
       excepted = self.command.get_output(obj)
       self.assertEqual(actual, excepted)

    def test_should_be_output_from_cli(self):
       obj = {'output': os.path.join(os.getcwd(),'../') }
       actual = os.path.join(os.getcwd(),'../')
       excepted = self.command.get_output(obj)
       self.assertEqual(actual, excepted)

    def test_should_be_output_throw_exception_not_valid(self):
        with self.assertRaises(ReleaseManagerException) as ex:
            obj = {'output': os.path.join(os.getcwd(),'../a') }
            self.command.get_output(obj)
        self.assertTrue('not valid' in ex.exception.message)