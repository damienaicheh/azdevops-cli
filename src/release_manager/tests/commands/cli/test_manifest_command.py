
import unittest
from unittest.mock import Mock

from src.release_manager.commands.cli.manifest_command import ManifestCommand

class TestManifestCommand(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = Mock()
        self.command = ManifestCommand(self.logger)