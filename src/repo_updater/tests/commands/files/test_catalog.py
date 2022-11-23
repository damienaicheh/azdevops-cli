
import unittest
from unittest.mock import Mock 
from repo_updater.commands.files.catalog import get_catalog

class TestCatalog(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = Mock()

    def test_should_be_not_empty(self) -> None:
       expected = get_catalog(self.logger)
       self.assertTrue(len(expected.keys())>0)