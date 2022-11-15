#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from models.configuration import *
from models.repository import *
from logging import Logger
from models.configuration import *
from models.repository import *
from logging import Logger
from repos_updater.commands.files.add_command import AddFileCommand
from repos_updater.commands.files.update_command import UpdateFileCommand
from repos_updater.commands.files.delete_command import DeleteFileCommand
from repos_updater.commands.files.file_command_args import FileCommandArgs

def apply_action(assets_directory: str, output: str, repository: Repository, action: Action, logger: Logger):
    """Apply the action specified in the YAML file"""
    args = FileCommandArgs(
        assets_directory=os.path.join(os.getcwd(), assets_directory),
        output=output,
        repository=repository,
        files=action.files
    )
    match action.name:
        case 'add':
            AddFileCommand(logger).execute(args)
        case 'delete':
            DeleteFileCommand(logger).execute(args)
        case 'update':
            UpdateFileCommand(logger).execute(args)
        case _:
            logger.error(f'The action {action.name} is not found')

def commit_and_push_changes(git_client, pull_request: PullRequest, logger: Logger):
    """Commit and push changes on the repository"""
    current = git_client.create_head(pull_request.branch)
    current.checkout()
    git_client.git.add(A=True)
    logger.debug(git_client.git.status())
    git_client.git.commit(m=pull_request.name)
    git_client.git.push('--set-upstream', 'origin', current)
    logger.debug(git_client.git.status())