import unittest
from unittest.mock import Mock 
from src.repo_updater.commands.files.helper import get_catalog

class TestHelper(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = Mock()

    def test_should_be_not_empty(self) -> None:
       expected = get_catalog(self.logger)
       self.assertTrue(len(expected.keys())>0)