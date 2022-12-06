import unittest
from unittest.mock import Mock

from src.release_manager.commands.cli.manifest_command import ManifestCommand
from src.release_manager.exceptions.release_manager_exception import ReleaseManagerException

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
        self.assertTrue('required' in ex.exception.message)
