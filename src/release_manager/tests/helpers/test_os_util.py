import os
import unittest

from exceptions.azdevops_exception import AzDevOpsException
from release_manager.helpers.os_util import get_valid_folder_path

class TestOsUtil(unittest.TestCase):

    def test_should_be_path_default(self) -> None:
       obj = {}
       actual = os.getcwd()
       excepted = get_valid_folder_path(self, obj, 'path')
       self.assertEqual(actual, excepted)

    def test_should_be_path_from_cli(self) -> None:
       obj = {'path': os.path.join(os.getcwd(),'../') }
       actual = os.path.join(os.getcwd(),'../')
       excepted = get_valid_folder_path(self, obj, 'path')
       self.assertEqual(actual, excepted)

    def test_should_be_path_throw_exception_not_valid(self) -> None:
        with self.assertRaises(AzDevOpsException) as ex:
            obj = {'path': os.path.join(os.getcwd(),'../a') }
            get_valid_folder_path(self, obj, 'path')
        self.assertTrue('not valid' in ex.exception.message)