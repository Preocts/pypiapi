[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

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

## Local developer installation

It is **highly** recommended to use a `venv` for installation. Leveraging a `venv` will ensure the installed dependency files will not impact other python projects.

Clone this repo and enter root directory of repo:
```bash
$ git clone https://github.com/preocts/pypiapi
$ cd pypiapi
```

Create and activate `venv`:
```bash
# Linux/MacOS
python3 -m venv venv
. venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate.bat
# or
py -m venv venv
venv\Scripts\activate.bat
```

Your command prompt should now have a `(venv)` prefix on it.

Install editable library and development requirements:
```bash
# Linux/MacOS
pip install -r requirements-dev.txt
pip install --editable .

# Windows
python -m pip install -r requirements-dev.txt
python -m pip install --editable .
# or
py -m pip install -r requirements-dev.txt
py -m pip install --editable .
```

Install pre-commit hooks to local repo:
```bash
pre-commit install
pre-commit autoupdate
```

Run tests
```bash
tox
```

To exit the `venv`:
```bash
deactivate
```

---

### Makefile

This repo has a Makefile with some quality of life scripts if your system supports `make`.

- `install` : Clean all artifacts, update pip, install requirements with no updates
- `update` : Clean all artifacts, update pip, update requirements, install everything
- `build-dist` : Build source distribution and wheel distribution
- `clean-pyc` : Deletes python/mypy artifacts
- `clean-tests` : Deletes tox, coverage, and pytest artifacts
- `clean-build` : Deletes build artifacts
- `clean-all` : Runs all clean scripts
