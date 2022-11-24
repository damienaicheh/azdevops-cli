#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
from helpers.logger import create_logger
from repo_updater.commands.cli.run_command import RunCommand

@click.group(name='repos-updater')
def repo_updater():
    """Commands related to compiling"""
    pass

@repo_updater.command(help='configuration file to process')
@click.option('-c', '--configuration-file', help='The path to the config.yml file or set the AZDEVOPS_CONFIG_PATH env variable')
@click.option('-ou', '--organization-url', help='The Azure DevOps organization url or set the AZDEVOPS_ORGANIZATION_URL env variable')
@click.option('-pt', '--pat-token', help='The Azure DevOps PAT Token or set the AZDEVOPS_PAT_TOKEN env variable')
@click.option('-o', '--output', default='', help='Local outputs results')
@click.option('--dry-run', is_flag=True,  default=False, help='Test deployment without applying it.')
@click.option('-v', '--verbose', is_flag=True, default=False, help='activate verbose log.')
def run(configuration_file, organization_url, pat_token, output, dry_run, verbose):
    """Run the script to apply the configuration file"""
    logger = create_logger(verbose)
    obj = {
        'configuration_file' : configuration_file,
        'organization_url': organization_url,
        'pat_token' : pat_token,
        'output': output,
        'dry_run': dry_run
    } 
    RunCommand(logger).execute(obj)

if __name__ == '__main__':
    repo_updater()