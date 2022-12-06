import os
import unittest
from unittest.mock import patch

from src.release_manager.helpers.os_util import get_valid_folder_path
from src.exceptions.azdevops_exception import AzDevOpsException

class TestOsUtil(unittest.TestCase):

    def test_should_be_path_default(self) -> None:
       obj = {}
       actual = os.getcwd()
       excepted = get_valid_folder_path(obj, 'path')
       self.assertEqual(actual, excepted)

    def test_should_be_path_from_cli(self) -> None:
       obj = {'path': os.path.join(os.getcwd()) }
       actual = os.path.join(os.getcwd())
       excepted = get_valid_folder_path(obj, 'path')
       self.assertEqual(actual, excepted)

    @patch('os.path.isdir')
    def test_should_be_path_relatif_from_cli(self, mock_isdir) -> None:
       mock_isdir.return_value = True
       obj = {'path': 'tmp/aa/bb' }
       actual = os.path.join(os.getcwd(),'tmp/aa/bb')
       excepted = get_valid_folder_path(obj, 'path')
       self.assertEqual(actual, excepted)

    def test_should_be_path_throw_exception_not_valid(self) -> None:
        with self.assertRaises(AzDevOpsException) as ex:
            obj = {'path': os.path.join(os.getcwd(),'tmp/a') }
            get_valid_folder_path(obj, 'path')
        self.assertTrue('not valid' in ex.exception.message)