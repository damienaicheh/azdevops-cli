import click
from src.helpers.logger import create_logger
from src.repo_updater.commands.cli.run_command import RunCommand

@click.group(name='repo-updater')
def repo_updater():
    """Commands related to compiling"""
    pass

@repo_updater.command(help='configuration file to process')
@click.option('-c', '--configuration-file', help='The path to the config.yml file or set the AZDEVOPS_CONFIG_PATH env variable')
@click.option('-o', '--output-dir', default='', help='Local outputs results')
@click.option('--dry-run', is_flag=True,  default=False, help='Test deployment without applying it.')
@click.option('-v', '--verbose', is_flag=True, default=False, help='activate verbose log.')
def run(configuration_file, output_dir, dry_run, verbose):
    """Run the script to apply the configuration file"""
    logger = create_logger(verbose)
    obj = {
        'configuration_file' : configuration_file,
        'output': output_dir,
        'dry_run': dry_run
    } 
    RunCommand(logger).execute(obj)

if __name__ == '__main__':
    repo_updater()