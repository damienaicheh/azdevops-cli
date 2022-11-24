#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from exceptions.azdevops_exception import AzDevOpsException

class RepoUpdaterException(AzDevOpsException):

    def __init__(self, message):
        super().__init__('Repo Updater', message)
