import unittest
from unittest.mock import Mock 
from src.models.helper import dic2object
from src.repo_updater.commands.files.add_file_command import AddFileCommand
from src.repo_updater.commands.files.file_command_args import FileCommandArgs
from src.repo_updater.exceptions.repo_updater_exception import RepoUpdaterException

class TestAddFileCommand(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = Mock()
        self.command = AddFileCommand(self.logger)

    def test_should_be_get_asset_path_is_valid(self):
        action = {}
        action['add'] = {}
        action['add']['asset_path'] = 'a'
        action = dic2object(action)
        args = FileCommandArgs(
            assets_directory = '/tmp',
            output = None,
            repository = None,
            action = action
        )
        excepted = self.command.get_asset_path(args)
        self.assertEquals( excepted, '/tmp/a')

    def test_should_be_get_asset_path_is_valid(self):
        action = {}
        action['add'] = {}
        action['add']['asset_path'] = 'a'
        action = dic2object(action)
        args = FileCommandArgs(
            assets_directory = '/tmp',
            output = None,
            repository = None,
            action = action
        )
        excepted = self.command.get_asset_path(args)
        self.assertEquals( excepted, '/tmp/a')

    def test_should_be_get_asset_path_is_valid(self):
        action = {}
        action['add'] = {}
        action['add']['asset_path'] = 'a'
        action = dic2object(action)
        args = FileCommandArgs(
            assets_directory = '/tmp',
            output = None,
            repository = None,
            action = action
        )
        excepted = self.command.get_asset_path(args)
        self.assertEqual( excepted, '/tmp/a')

    def test_should_be_get_asset_path_throw_exception(self):
        action = {}
        action['add'] = {}
        action['add']['asset_path'] = ''
        action = dic2object(action)
        args = FileCommandArgs(
            assets_directory = '/tmp',
            output = None,
            repository = None,
            action = action
        )
        with self.assertRaises(RepoUpdaterException) as ex:
             self.command.get_asset_path(args)
        self.assertTrue('The assert path is required on Add File Action.' in ex.exception.message)


    def test_should_be_get_override_from_configuration(self):
        action = {}
        action['add'] = {}
        action['add']['override'] = False
        action = dic2object(action)
        args = FileCommandArgs(
            assets_directory = '/tmp',
            output = None,
            repository = None,
            action = action
        )
        excepted = self.command.get_override(args)
        self.assertFalse( excepted)

    def test_should_be_get_override_default(self):
        action = {}
        action['add'] = {}
        action = dic2object(action)
        args = FileCommandArgs(
            assets_directory = '/tmp',
            output = None,
            repository = None,
            action = action
        )
        excepted = self.command.get_override(args)
        self.assertTrue(excepted)