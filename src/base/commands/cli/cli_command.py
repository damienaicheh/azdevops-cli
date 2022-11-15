#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class CliCommand(ABC):
    def __init__(self, logger):
        self.logger = logger

    def execute(self, obj):
        self._on_execute(obj)

    @abstractmethod
    def _on_execute(self, obj):
        pass