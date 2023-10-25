# Introduction

`CallingCardsTools` Provides both an API and a number of cmd line tools 
for processing raw Calling Cards data. This is used in the 
[nf-core/callingcards](https://github.com/nf-core/callingcards) pipeline, 
which provides a workflow to process both yeast and mammals Calling Cards data.

# Documentation

[Served Documentation](https://cmatkhan.github.io/callingCardsTools/) provides 
information on filetypes and the API. For help with the cmd line tools, 
simply install callingcardstools (see below) and do:

```
callingcardstools --help
```

Each of the cmd line tools also provides a `--help` message.

# Installation 

```
pip install callingcardstools
```

To start using the command line tools, see the help message with:

```
callingcardstools --help
```

Callingcardstools is containerized:

```
docker pull cmatkhan/callingcardstools
```

```
singularity pull cmatkhan/callingcardstools
```

# Development Installation

1. install [poetry](https://python-poetry.org/)
  - I prefer to set the default location of the virtual environment to the 
  project directory. You can set that as a global configuration for your 
  poetry installation like so: `poetry config virtualenvs.in-project true`

2. git clone the repo

3. cd into the repo and issue the command `poetry install`

4. shell into the virtual environment with `poetry shell`

5. build the package with `poetry build`

6. install the callingcardstools package into your virtual environment 
  `pip install dist/callingcardstools-...`
  - Note: you could figure out how to use the pip install `-e` flag to 
  have an interactive development environment. I don't think that is compatible 
  with only the `pyproject.toml` file, but if you look it up, you'll find good 
  stackoverflow instructions on how to put a dummy `setup.py` file in to make 
  this possible
