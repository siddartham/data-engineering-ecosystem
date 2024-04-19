# python-package-template
[![cicd](https://github.com/siddartham/data-engineering-ecosystem/python-package-template/actions/workflows/test.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/python-package-template/actions/workflows/cicd.yml)


To create a repository based on this template:

- Execute the following commands (replacing "~/Code" with the path under which
  you want to create your new project)

- Also assuming id matches your github id, else replace it accordingly
  ```shell
  cd ~/Code
  pip3 install --upgrade pip && \
  pip3 install cookiecutter && \
  cookiecutter\
   "git+https://github.com/siddartham/data-engineering-ecosystem/python-package-template.git"
  ```
- Follow the prompts to enter template fields. For example:
  ```
  $ cookiecutter\
   "git+https://github.com/siddartham/data-engineering-ecosystem/python-package-template.git"

  ```
  The resulting directory/file structure created by the above example input
  looks as follows:
  ```
  $ tree -a python-project
    python-project
    ├── .editorconfig
    ├── .flake8
    ├── .github
    │   └── workflows
    │     ├── distribute.yml
    │     └── test.yml
    ├── .gitignore
    ├── CONTRIBUTING.md
    ├── MANIFEST.yml
    ├── Makefile
    ├── README.md
    ├── __init__.py
    ├── ci_requirements.txt
    ├── dev_requirements.txt
    ├── mypy.ini
    ├── pyproject.toml
    ├── python_project
    │   ├── __init__.py
    │   ├── __main__.py
    │   └── py.typed
    ├── requirements.txt
    ├── setup.cfg
    ├── setup.py
    ├── test_requirements.txt
    ├── tests
    │   └── test_python_project.py
    └── tox.ini

  ```
- Once you've created your new project, you can create your venv and
  install-in-place by running `make`:
  ```shell
  cd python-project
  make
  ```
- You will, of course, also need to create your repository on GitHub and...
- Initialize and configure your repository locally. For the project from
  preceding examples, those commands would be:
  ```shell
  git init
  git add .
  git commit -m "First Commit"
  git remote add origin "{your_repo_url}"
  ```

## Features

We are trying to follow PEP8 conventions and best practices for Python package development. As part of it, we are incorporating several tools in development workflow.

What are `pep8` conventions?

`pep8` conventions are a set of rules that are defined to maintain the code quality and readability. It is a style guide for Python code. It is a set of rules that specify how to format Python code for maximum readability.

What are the tools that are being used?
* `tox` - Tox is a generic virtualenv management and test command line tool you can use for: checking your package installs correctly with different Python versions and interpreters, running your tests in each of the environments, configuring your test tool of choice, be it nose, py.test, or unittest, testing other setups like building documentation with Sphinx, building wheels, building conda packages, etc.
* `mypy` - Mypy is a static type checker for Python. It combines the expressive power and convenience of Python with a powerful type system and compile-time type checking. Mypy type checks standard Python programs; run them using any Python VM with basically no runtime overhead.
* `isort` - isort is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type. It provides a command line utility, Python library and plugins for various editors to quickly sort all your imports.
* `pipdeptree` - pipdeptree is a command line utility for displaying the installed python packages in form of a dependency tree. It can also output the dependency tree in the form of requirements.txt file. It can also be used to check for security vulnerabilities in the installed packages.
* `black` - Black is the uncompromising Python code formatter. By using it, you can ensure that the code is formatted in a consistent manner and it will also help in reducing the time spent on code reviews.
* `pip` - pip is a package management system used to install and manage software packages written in Python. Many packages can be found in the Python Package Index (PyPI) and can be installed using pip.

