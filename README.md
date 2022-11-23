# AzDev CLI

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/gwendallg/rsql4net/blob/develop/LICENSE) [![Nuget](https://img.shields.io/nuget/v/rsql4net)]()

## Continuous integration

| Branch                      |  Build | Quality Gate |
|-----------------------------|--------|--------------|
| master                      | ![](https://dev.azure.com/damienaicheh/azdevops-cli/_apis/build/status/gwendallg.rsql4net?branchName=master)| [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=gwendallg_rsql4net&branch=master&metric=alert_status)](https://sonarcloud.io/dashboard?id=gwendallg_rsql4net&branch=master) |
| develop                     | ![](https://dev.azure.com/gwendallg/rsql4net/_apis/build/status/gwendallg.rsql4net?branchName=develop) | | 

## I.Introduction

This project is used to update all selected repositories in one single script define by a `config.yml` file.
The python script will automatically clone the repositories, modify it and propose a pull request on each repository inside Azure DevOps.

## II. Getting Started

Create a dev environment for the project:

```sh
python3 -m venv .venv
```

Activate the dev environment:

```sh
source .venv/bin/activate
```

Install python packages for the project:
```sh
pip install -r requirements.txt
```

Save the packages used in the project into the `requirements.txt`:
```sh
pip freeze > requirements.txt
```

Export credentials as environment variable to be able to run the API calls:
```
export AZURE_DEVOPS_PAT='<your_email>:<your_pat>'
```

## III - Models generation

Transform the `config.yml` into json with this website for instance:
https://jsonformatter.org/yaml-to-json

Then copy the generated json and paste it inside this other website:
https://app.quicktype.io/

Choose default settings with the Python language.

## IV - Install locally for testing only

```
python3 -m pip install --editable .
```

## V - Run the CLI

```
azdevops repo-updater run --configuration-file <path-to>/config.yml -o <output-path>
```

```
azdevops release-manager changelog -p <your-project-path> -o <output-path>
```