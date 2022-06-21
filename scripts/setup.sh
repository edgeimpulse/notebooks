#!/usr/bin/env bash
set -e # Exit on error

# We assume we are in python 3
pip install pipenv
pipenv install
pipenv run pre-commit install