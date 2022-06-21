# Notebooks

Notebooks using the Edge Impulse libraries

- [01 - Collect data from your development kit](./01-collect-data-from-board.ipynb)

## Contributing

This repo uses `pipenv` to maintain a virtual development environment.

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
