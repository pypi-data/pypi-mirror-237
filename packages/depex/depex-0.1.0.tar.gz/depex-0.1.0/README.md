# DepEx

Extract Python project dependencies from a `pyproject.toml` file.

## Why?

I haven't completely dropped `requirements.txt` and `requirements-dev.txt` files yet so this helps me keep them in sync with the dependencies I have listed in the `pyproject.toml` file.


## Usage

Just provide the path to a Python project directory or a `pyproject.toml` file and extract base dependencies, optional dependencies, or all dependencies from the `pyproject.toml` file.

```bash
# generate a file with only the base dependencies of a package
$ depex --no-opts > requirements.txt

# or generate a file with all dependencies (including optional) of a package
depex > requirements-dev.txt
```

## Help


```bash
$ depex -h
usage: depex [-h] [--opts | --no-opts] [--version] path

Extract Python project requirements from a `pyproject.toml` file.

positional arguments:
  path               path to a project directory or pyproject.toml file

options:
  -h, --help         show this help message and exit
  --opts, --no-opts  include all dependencies
  --version          show program's version number and exit

Copyright 2023 Josh Duncan (joshbduncan.com)
```
