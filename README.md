# Notebooks

Notebooks using the Edge Impulse libraries

- [01 - Collect data from your development kit](./notebooks/01-collect-data-from-board.ipynb)
- [02 - Object counting on device using a FOMO model](./notebooks/02-object-counting-using-fomo.ipynb)
- [03 - Generating a Keyword dataset using Google Text to Speech](./notebooks/03-generate-keyword-spotting-dataset.ipynb)
- [03 - Use OpenAI Dall-E to generate an image dataset for image classification](./notebooks/03-generate-dall-e-image-dataset.ipynb)
- [04 - Use PyBullet to generate a physics simulation based dataset](./notebooks/04-generate-physics-simulation-dataset.ipynb)
- [05 - How to Customize and Run the AutoML EON Tuner Programmatically](./notebooks/05-customize-the-EON-tuner.ipynb)


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
