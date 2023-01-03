import unittest
from unittest.mock import Mock 
from src.models.helper import dic2object
from src.repo_updater.commands.files.delete_file_command import DeleteFileCommand
from src.repo_updater.commands.files.file_command_args import FileCommandArgs

class TestDeleteFileCommand(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = Mock()
        self.command = DeleteFileCommand(self.logger)

    def test_should_be_get_target_path_is_valid(self):
        action = {}
        action['delete'] = {}
        action['delete']['target_path'] = 'b'
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
