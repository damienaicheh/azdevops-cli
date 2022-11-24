import os
import unittest
from unittest.mock import Mock

from release_manager.commands.cli.manifest_command import ManifestCommand
from release_manager.exceptions.release_manager_exception import ReleaseManagerException

class TestManifestCommand(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = Mock()
        self.command = ManifestCommand(self.logger)

    def test_should_be_application_name_from_parameter(self) -> None:
       obj = {'application_name': 'azdevops-cli'}
       actual = 'azdevops-cli'
       excepted = self.command.get_application_name(obj)
       self.assertEqual(actual, excepted)

    def test_should_be_application_name_throw_exception_required(self) -> None:
        with self.assertRaises(ReleaseManagerException) as ex:
            obj = {}
            self.command.get_application_name(obj)
<<<<<<< HEAD
        self.assertTrue('required' in ex.exception.message)

    def test_should_be_output_default(self) -> None:
       obj = {}
       actual = os.getcwd()
       excepted = self.command.get_output(obj)
       self.assertEqual(actual, excepted)

    def test_should_be_output_from_cli(self) -> None:
       obj = {'output': os.path.join(os.getcwd(),'../') }
       actual = os.path.join(os.getcwd(),'../')
       excepted = self.command.get_output(obj)
       self.assertEqual(actual, excepted)

    def test_should_be_output_throw_exception_not_valid(self) -> None:
        with self.assertRaises(ReleaseManagerException) as ex:
            obj = {'output': os.path.join(os.getcwd(),'../a') }
            self.command.get_output(obj)
        self.assertTrue('not valid' in ex.exception.message)
=======
        self.assertTrue('required' in ex.exception.message)
>>>>>>> bb6f874 (feat: Mutualize code and tests.)
