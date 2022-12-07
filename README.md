# AzDevOps CLI

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/gwendallg/rsql4net/blob/develop/LICENSE) [![Pypi](https://img.shields.io/pypi/v/PACKAGE?label=azdevops-cli)]()

## I.Continuous integration

| Branch  | Build                                                                                                                                                                                                                                        | Quality Gate |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| main    | [![Build Status](https://dev.azure.com/damienaicheh0990/azdevops-cli/_apis/build/status/damienaicheh.azdevops-cli?branchName=main)](https://dev.azure.com/damienaicheh0990/azdevops-cli/_build/latest?definitionId=95&branchName=main)       |              |
| develop | [![Build Status](https://dev.azure.com/damienaicheh0990/azdevops-cli/_apis/build/status/damienaicheh.azdevops-cli?branchName=develop)](https://dev.azure.com/damienaicheh0990/azdevops-cli/_build/latest?definitionId=95&branchName=develop) |              |

## II.Introduction

This project is used to update all selected repositories in one single script define by a `config.yml` file.
The python script will automatically clone the repositories, modify it and propose a pull request on each repository inside Azure DevOps.

## III. Getting Started

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
export AZDEVOPS_ORGANIZATION_URL='<your_azure_devops_organisation_url>'
export AZDEVOPS_PAT_TOKEN='<your_pat>'
```

## IV - Models generation

Transform the `config.yml` into json with this website for instance:
https://jsonformatter.org/yaml-to-json

Then copy the generated json and paste it inside this other website:
https://app.quicktype.io/

Choose default settings with the Python language.

## V - Install locally for testing only

```
python3 -m pip install --editable .
```

## VI - Run the CLI

```
azdevops repo-updater run --configuration-file <path-to>/config.yml -o <output-path>
```

```
azdevops release-manager changelog -p <your-project-path> -o <output-path>
```

## VII - Unit tests

### Run unit tests:

```
python3 -m unittest
```

or

```
coverage run -m unittest discover
```

### Generate covrage locally

```
coverage report
```