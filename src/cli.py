#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
from release_manager.cli import release_manager
from repos_updater.cli import repo_updater
from repos_updater.commands.cli.run_command import RunCommand
from base.commands.cli.version_command import VersionCommand
from release_manager.commands.cli.changelog_command import ChangeLogCommand
from helpers.logger import create_logger

@click.group()
def main():
    """Welcome to the Azure DevOps CLI"""

main.add_command(release_manager)
main.add_command(repo_updater)

if __name__ == '__main__':
    main()

@main.command(name='version', help='show CLI version')
@click.option('--verbose', is_flag=True, default=False, help='activate verbose log.')
def version(verbose):
    """Get the version of the cli"""
    logger = create_logger(verbose)
    VersionCommand(logger).execute({})

if __name__ == '__main__':
    main()