# Notebooks

This is a collection of Jupyter notebook examples and tutorials for helping users interact with Edge Impulse from Python environments. Refer to the [./notebooks/](notebooks) directory for a list of Jupyter notebook examples.

## Contributing

This repo uses `pipenv` to maintain a virtual development environment, therefore, it requires `python` 3.9 and `pip` to be installed in your development machine.

Some notes about creating a notebook:
 * The top-most cell should be a markdown cell with an H1 tag and title (e.g. `# My notebook title`) at the top of the cell
 * Use absolute links (e.g. `https://raw.githubusercontent.com/edgeimpulse/notebooks/main/...`) so that the notebook can be used as documentation elsewhere
 * When referring to code (functions, variables, etc.) in your markdown cells, enclose them in backticks (e.g. `int some_var`) to avoid getting picked up by the spellchecker (when converting your notebook to documentation)

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

```shell
pypenv shell
jupyter nbconvert --to markdown notebooks/<name-of-notebook>.ipynb
mv notebooks/<name-of-notebook>.md ~/Downloads
```

Your markdown file will be in your Downloads folder. When you are done, issue the `exit` command to leave the virtual environment.

> **Warning**
> Make sure you check the markdown file! You might need to copy images out from the [.assets/](.assets) directory and change the links in the markdown file to ensure that they appear correctly. Instead of copying the images, you can also use an absolute URL (e.g. `https://raw.githubusercontent.com/edgeimpulse/notebooks/main/.assets/images/<image-name>.png/jpg`) in your notebook link.
