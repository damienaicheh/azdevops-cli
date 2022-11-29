import click
from src.release_manager.commands.cli.changelog_command import ChangeLogCommand
from src.release_manager.commands.cli.manifest_command import ManifestCommand
from src.helpers.logger import create_logger

# Command Group
@click.group(name='release-manager')
def release_manager():
    """Tool related commands"""
    pass

@release_manager.command(name='changelog', help='generate changelog')
@click.option('-p', '--project-path', required=True, help='project path.')
@click.option('-o', '--output', default='.', help='Output path for the CHANGELOG.md')
@click.option('-v', '--verbose', is_flag=True, default=False, help='activate verbose log.')
def changelog(project_path, output, verbose):
    """Run the script to generate a CHANGELOG.md"""
    logger = create_logger(verbose)
    obj = {
        'project_path' : project_path,
        'output': output
    } 
    ChangeLogCommand(logger).execute(obj)

@release_manager.command(name='manifest', help='generate a manifest')
@click.option('-p', '--project-path', required=True, help='project path.')
@click.option('-an', '--application-name', required=True, help='application name.')
@click.option('-o', '--output', default='.', help='Output path for the manifest.json')
@click.option('-v', '--verbose', is_flag=True, default=False, help='activate verbose log.')
def changelog(project_path, application_name, output, verbose):
    """Create a JSON manifest for a repository"""
    logger = create_logger(verbose)
    obj = {
        'project_path' : project_path,
        'application_name': application_name,
        'output': output
    } 
    ManifestCommand(logger).execute(obj)

if __name__ == '__main__':
    release_manager()