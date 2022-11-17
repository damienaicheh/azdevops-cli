# AzDev CLI

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