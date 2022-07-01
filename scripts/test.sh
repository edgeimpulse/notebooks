#!/usr/bin/env bash
set -e # Exit on error

cd notebooks
pipenv run jupyter nbconvert --clear-output --inplace notebooks.ipynb
# Check for changes (ignore mode changes)
if [ -z "$(git -c core.fileMode=false status --porcelain)" ]; then
  echo "Repository is clean."
else
  echo "Repository not clean, test failed."
  exit -1
fi