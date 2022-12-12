import click
from src.release_manager.cli import release_manager
from src.repo_updater.cli import repo_updater
from src.base.commands.cli.version_command import VersionCommand
from src.helpers.logger import create_logger

@click.group()
def main():
    """Welcome to the Azure DevOps CLI"""

main.add_command(release_manager)
main.add_command(repo_updater)

if __name__ == '__main__':
    main()

@main.command(name='version', help='Show CLI version')
@click.option('--verbose', is_flag=True, default=False, help='activate verbose log.')
def version(verbose):
    """Get the version of the cli"""
    logger = create_logger(verbose)
    VersionCommand(logger).execute({})

if __name__ == '__main__':
    main()