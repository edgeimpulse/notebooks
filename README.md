# Notebooks

This is a collection of Jupyter notebook examples and tutorials for helping users interact with Edge Impulse from Python environments. Refer to the [./notebooks/](notebooks) directory for a list of Jupyter notebook examples.

## Contributing

This repo uses `pipenv` to maintain a virtual development environment, therefore, it requires `python` 3.9 and `pip` to be installed in your development machine.

### Setup your development environment

This will install pipenv and all the virtual environment dependencies

```shell
bash scripts/setup.sh
```

### Running pre-commit hooks

Pre-commit hooks must be run from the virtual development environment:

```shell
pipenv run pre-commit run --all-files
```

### Convert Notebook to Markdown

To convert a notebook to markdown for the purpose of hosting on a documentation page, use [nbconvert](https://pypi.org/project/nbconvert/).

First, make sure you have followed the setup instructions above. We'll use the pipenv virtual environment to create our markdown files.

```
pipenv run
jupyter nbconvert --to markdown notebooks/<name-of-notebook>.ipynb
mv notebooks/<name-of-notebook>.md ~/Downloads
```

Your markdown file will be in your Downloads folder. When you are done, issue the `exit` command to leave the virtual environment.

> **Warning**
> Make sure you check the markdown file! You might need to copy images out from the [.assets/](.assets) directory and change the links in the markdown file to ensure that they appear correctly. Instead of copying the images, you can also use an absolute URL (e.g. `https://raw.githubusercontent.com/edgeimpulse/notebooks/main/.assets/images/<image-name>.png/jpg`) in your notebook link.

### License

Unless otherwise specified, code in this repository is licensed under the APACHE 2.0 open source license.

Copyright 2023 EdgeImpulse, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
