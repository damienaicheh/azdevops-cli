#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.models.version_infos import VersionInfos
from setuptools import setup, find_packages

version_infos = VersionInfos()

setup (
    name = 'azdevops-cli',
    include_package_data = True,
    version = version_infos.version,
    description= version_infos.description,
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8.0"
    ],
    install_requires = [
        'Cerberus==1.3.4',
        'certifi==2022.9.24',
        'charset-normalizer==2.1.1',
        'click==8.1.3',
        'coverage==6.5.0',
        'gitdb==4.0.9',
        'GitPython==3.1.29',
        'idna==3.4',
        'isodate==0.6.1',
        'msrest==0.6.21',
        'oauthlib==3.2.2',
        'PyYAML==6.0',
        'requests==2.28.1',
        'requests-oauthlib==1.3.1',
        'six==1.16.0',
        'smmap==5.0.0',
        'urllib3==1.26.12'
    ],
    packages = find_packages(exclude=["tests/*"]),
    scripts = [
        'bin/azdevops'
    ]
)