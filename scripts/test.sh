#!/usr/bin/env bash
set -e # Exit on error

pipenv run jupyter nbconvert --clear-output --inplace *.ipynb
# Check for changes (though ignore mode changes)
if [ -z "$(git -c core.fileMode=false status --porcelain)" ]; then
  echo "Repository is clean."
else
  echo "Repository not clean, test failed."
  exit -1
fi