import unittest
from unittest.mock import Mock 
from src.models.helper import dic2object
from src.repo_updater.commands.files.update_file_command import UpdateFileCommand
from src.repo_updater.commands.files.file_command_args import FileCommandArgs
from src.repo_updater.exceptions.repo_updater_exception import RepoUpdaterException

class TestDeleteFileCommand(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = Mock()
        self.command = UpdateFileCommand(self.logger)

    def test_should_be_get_pattern_regex_is_valid(self):
        action = {}
        action['update'] = {}
        action['update']['pattern'] = {}
        action['update']['pattern']['regex'] = 'test'
        action = dic2object(action)
        args = FileCommandArgs(
            assets_directory = '/tmp',
            output = None,
            repository = None,
            action = action
        )
        excepted = self.command.get_pattern_regex(args)
        self.assertEqual( excepted, 'test')

    def test_should_be_get_pattern_regex_throw_exception(self):
        action = {}
        action['update'] = {}
        action['update']['pattern'] = {}
        action['update']['pattern']['regex'] = ''
        action = dic2object(action)
        args = FileCommandArgs(
            assets_directory = '/tmp',
            output = None,
            repository = None,
            action = action
        )
        with self.assertRaises(RepoUpdaterException) as ex:
            self.command.get_pattern_regex(args)
            self.assertTrue('The pattern regex is required on Update File Action.' in ex.exception.message)

    def test_should_be_get_pattern_group_name_is_valid(self):
        action = {}
        action['update'] = {}
        action['update']['pattern'] = {}
        action['update']['pattern']['group_name'] = 'test'
        action = dic2object(action)
        args = FileCommandArgs(
            assets_directory = '/tmp',
            output = None,
            repository = None,
            action = action
        )
        excepted = self.command.get_pattern_group_name(args)
        self.assertEqual( excepted, 'test')

    def test_should_be_get_pattern_group_name_is_valid_with_default(self):
        action = {}
        action['update'] = {}
        action['update']['pattern'] = {}
        action = dic2object(action)
        args = FileCommandArgs(
            assets_directory = '/tmp',
            output = None,
            repository = None,
            action = action
        )
        excepted = self.command.get_pattern_group_name(args)
        self.assertEqual( excepted, 'replace')

    def test_should_be_get_pattern_group_name_throw_exception(self):
        action = {}
        action['update'] = {}
        action['update']['pattern'] = {}
        action['update']['pattern']['group_name'] = ''
        action = dic2object(action)
        args = FileCommandArgs(
            assets_directory = '/tmp',
            output = None,
            repository = None,
            action = action
        )
        with self.assertRaises(RepoUpdaterException) as ex:
            self.command.get_pattern_group_name(args)
            self.assertTrue('The pattern group name is required on Update File Action.' in ex.exception.message)

    def test_should_be_get_target_path_is_valid(self):
        action = {}
        action['update'] = {}
        action['update']['target_path'] = 'b'
        action = dic2object(action)
        repository = {}
        repository['name'] = 'a'
        repository = dic2object(repository)
        args = FileCommandArgs(
            assets_directory = '/tmp',
            output = '/tmp',
            repository = repository,
            action = action
        )
        excepted = self.command.get_target_path(args)
        self.assertEqual(excepted, '/tmp/a/b')


    def test_should_be_get_mode_is_valid(self):
        action = {}
        action['update'] = {}
        action['update']['mode'] = 'at-beginning'
        action = dic2object(action)
        repository = {}
        repository['name'] = 'a'
        repository = dic2object(repository)
        args = FileCommandArgs(
            assets_directory = '/tmp',
            output = '/tmp',
            repository = repository,
            action = action
        )
        excepted = self.command.get_mode(args)
        self.assertEqual(excepted, 'at-beginning')

    def test_should_be_get_mode_throw_exception(self):
        action = {}
        action['update'] = {}
        action['update']['mode'] = 'at-the-beginning'
        action = dic2object(action)
        repository = {}
        repository['name'] = 'a'
        repository = dic2object(repository)
        args = FileCommandArgs(
            assets_directory = '/tmp',
            output = '/tmp',
            repository = repository,
            action = action
        )
        with self.assertRaises(RepoUpdaterException) as ex:
            self.command.get_mode(args)
            self.assertTrue(f'The mode \'at-the-beginning\' is invalid on Update File Action. possible values are: at-beginning, at-the-end, delete, insert-after, insert-before, replace-with' in ex.exception.message)
       