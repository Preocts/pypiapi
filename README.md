[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Preocts/pypiapi/main.svg)](https://results.pre-commit.ci/latest/github/Preocts/pypiapi/main)
[![Python Tests](https://github.com/Preocts/pypiapi/actions/workflows/python-tests.yml/badge.svg?branch=main)](https://github.com/Preocts/pypiapi/actions/workflows/python-tests.yml)
[![codecov](https://codecov.io/gh/Preocts/pypiapi/branch/main/graph/badge.svg?token=9LL6DY1POA)](https://codecov.io/gh/Preocts/pypiapi)

# pypiapi

Pull project information from PyPI JSON API.

### Requirements
- Python >= 3.8
- urllib3 >= 1.26.7


## Example use:
```py
from pypiapi import PyPIClient

client = PyPIClient()
project = client.get_project("secretbox")
# project = client.get_project_by_version("secretbox", "2.0.1")

if project is not None:
    print(f"Project name: {project.info.name}")
    print(f"Author: {project.info.author}")
    for release, release_values in project.releases.items():
        print(f"Release '{release}'")
        for subrelease in release_values:
            print(f"\tFilename: {subrelease.filename}")
else:
    print("Project not found")
```

## Results

```
Project name: secretbox
Author: Preocts
Release '1.0.0'
        Filename: secretbox-1.0.0-py3-none-any.whl
        Filename: secretbox-1.0.0.tar.gz
Release '1.0.1'
        Filename: secretbox-1.0.1-py3-none-any.whl
        Filename: secretbox-1.0.1.tar.gz
Release '1.0.2'
        Filename: secretbox-1.0.2-py3-none-any.whl
        Filename: secretbox-1.0.2.tar.gz
Release '1.1.0'
        Filename: secretbox-1.1.0-py3-none-any.whl
        Filename: secretbox-1.1.0.tar.gz
Release '1.2.0'
        Filename: secretbox-1.2.0-py3-none-any.whl
        Filename: secretbox-1.2.0.tar.gz
...
```

---

---

# Local developer installation

It is **strongly** recommended to use a virtual environment
([`venv`](https://docs.python.org/3/library/venv.html)) when working with python
projects. Leveraging a `venv` will ensure the installed dependency files will
not impact other python projects or any system dependencies.

The following steps outline how to install this repo for local development. See
the [CONTRIBUTING.md](../CONTRIBUTING.md) file in the repo root for information
on contributing to the repo.

**Windows users**: Depending on your python install you will use `py` in place
of `python` to create the `venv`.

**Linux/Mac users**: Replace `python`, if needed, with the appropriate call to
the desired version while creating the `venv`. (e.g. `python3` or `python3.8`)

**All users**: Once inside an active `venv` all systems should allow the use of
`python` for command line instructions. This will ensure you are using the
`venv`'s python and not the system level python.

---

## Installation steps

Clone this repo and enter root directory of repo:

```bash
git clone https://github.com/Preocts/pypiapi
cd pypiapi
```

Create the `venv`:

```bash
python -m venv venv
```

Activate the `venv`:

```bash
# Linux/Mac
. venv/bin/activate

# Windows
venv\Scripts\activate
```

The command prompt should now have a `(venv)` prefix on it. `python` will now
call the version of the interpreter used to create the `venv`

Install editable library and development requirements:

```bash
# Update pip and tools
python -m pip install --upgrade pip wheel setuptools

# Install development requirements
python -m pip install -r requirements-dev.txt

# Install editable version of library
python -m pip install --editable .
```

Install pre-commit [(see below for details)](#pre-commit):

```bash
pre-commit install
```

---

## Misc Steps

Run pre-commit on all files:

```bash
pre-commit run --all-files
```

Run tests:

```bash
tox [-r] [-e py3x]
```

To deactivate (exit) the `venv`:

```bash
deactivate
```

---

## [pre-commit](https://pre-commit.com)

> A framework for managing and maintaining multi-language pre-commit hooks.

This repo is setup with a `.pre-commit-config.yaml` with the expectation that
any code submitted for review already passes all selected pre-commit checks.
`pre-commit` is installed with the development requirements and runs seemlessly
with `git` hooks.

---

## Makefile

This repo has a Makefile with some quality of life scripts if the system
supports `make`.  Please note there are no checks for an active `venv` in the
Makefile.

| PHONY             | Description                                                        |
| ----------------- | ------------------------------------------------------------------ |
| `init`            | Update pip, setuptools, and wheel to newest version                |
| `install`         | install the project                                                |
| `install-dev`     | install development requirements and project                       |
| `build-dist`      | Build source distribution and wheel distribution                   |
| `clean-artifacts` | Deletes python/mypy artifacts including eggs, cache, and pyc files |
| `clean-tests`     | Deletes tox, coverage, and pytest artifacts                        |
| `clean-build`     | Deletes build artifacts                                            |
| `clean-all`       | Runs all clean scripts                                             |
