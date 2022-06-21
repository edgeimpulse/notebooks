#!/usr/bin/env bash
set -e # Exit on error

# We assume we are in python 3
pip install pipenv

# Tell pipenv to install all packages including dev dependencies
pipenv install --dev
# Tell pipenv to install all packages including dev dependencies
# and local directory as editable
#pipenv install --dev -e .

# Install the pre-commit hook
pipenv run pre-commit install