#!/usr/bin/env python3
from models.version_infos import VersionInfos

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
        "Programming Language :: Python :: 3.11.0"
    ],
    install_requires = [
        'certifi==2022.9.24',
        'charset-normalizer==2.1.1',
        'click==8.1.3',
        'gitdb==4.0.9',
        'GitPython==3.1.29',
        'idna==3.4',
        'PyYAML==6.0',
        'requests==2.28.1',
        'smmap==5.0.0',
        'urllib3==1.26.12'
    ],
    packages = find_packages(exclude=["tests/*"]),
    scripts = [
        'bin/azdevops'
    ]
)