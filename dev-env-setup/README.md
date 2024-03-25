# Development Environment Setup

- Install XCode command-line tools

  ```shell script
  xcode-select --install
  ```

- [Install HomeBrew](https://brew.sh)

  ```shell script
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)" && \
  echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile && \
  eval "$(/opt/homebrew/bin/brew shellenv)"
  ```

- Install Binary Packages (Required)

  ```shell script
  brew install apache-arrow openblas cmake docker zulu8 openjdk@11 libpq cyrus-sasl pyenv gimme-aws-creds openssl terraform && \
  brew link --force openblas cmake xz libpq cyrus-sasl pyenv gimme-aws-creds openssl
  ```

- Install Binary Packages (Optional)

  ```shell script
  brew install visual-studio-code pycharm dbeaver-community gh
  ```

- Install PyEnv-Update

  ```shell script
  git clone https://github.com/pyenv/pyenv-update.git $(pyenv root)/plugins/pyenv-update
  ```

  This adds the command `pyenv update`, which is a faster means of
  updating pyenv (necessary in order to get the latest python versions, etc.),
  than `brew upgrade pyenv`.

- Install and enable the latest patch version of all minor versions of python
  available from 3.8-3.12:

  ```shell script
  pyenv install --skip-existing 3.8 3.9 3.10 3.11 3.12 && \
  pyenv global\
   "$(pyenv install --list | grep -E '^\s*3\.8\.\d+($|\n)' | tail -n 1 | sed 's/^ *//g')"\
   "$(pyenv install --list | grep -E '^\s*3\.9\.\d+($|\n)' | tail -n 1 | sed 's/^ *//g')"\
   "$(pyenv install --list | grep -E '^\s*3\.10\.\d+($|\n)' | tail -n 1 | sed 's/^ *//g')"\
   "$(pyenv install --list | grep -E '^\s*3\.11\.\d+($|\n)' | tail -n 1 | sed 's/^ *//g')"\
   "$(pyenv install --list | grep -E '^\s*3\.12\.\d+($|\n)' | tail -n 1 | sed 's/^ *//g')"
  ```

- Configure your profile:
  - Bootstrap pyenv
  - Set some environment variables in your zsh profile (`zsh` is the default shell
    for Mac OS)
  - Disable fork safety (needed for multiprocessing on Mac OS)

  ```shell script
  echo 'eval "$(pyenv init --path)"' >> ~/.zprofile && \
  echo 'export -f pyenv' >> ~/.zprofile && \
  echo 'export LDFLAGS="-L/opt/homebrew/opt/openssl/lib"' >> ~/.zprofile && \
  echo 'export CPPFLAGS="-I/opt/homebrew/opt/openssl/include"' >> ~/.zprofile && \
  echo 'export PATH="/opt/homebrew/opt/cyrus-sasl/sbin:$PATH"' >> ~/.zprofile && \
  echo 'export PKG_CONFIG_PATH="/opt/homebrew/opt/cyrus-sasl/lib/pkgconfig:$PKG_CONFIG_PATH"' >> ~/.zprofile && \
  echo 'export PKG_CONFIG_PATH="/opt/homebrew/opt/openssl@3/lib/pkgconfig:$PKG_CONFIG_PATH"' >> ~/.zprofile && \
  echo "export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES" >> ~/.zprofile && \
  echo 'export JAVA_HOME=/Library/Java/JavaVirtualMachines/zulu-8.jdk/Contents/Home'  >> ~/.zprofile && \
  . ~/.zprofile


- Setup Multiple GitHub Accounts: Follow the instructions [here](https://blog.gitguardian.com/8-easy-steps-to-set-up-multiple-git-accounts/) 
to set up Multiple GitHub accounts in local environment, to enable working on personal and work related projects.


- Configure Visual Studio Code (Optional):

  - Install the Python extension (extension ID: ms-python.python)

  - Set a few linting and UI parameters in your user settings ("Preferences:
    Open Settings (JSON)" in the Visual Studio Code command palette):
  
    ```jsonc
    {
      "window.nativeTabs": true,
      "terminal.integrated.defaultProfile.osx": "zsh",
      // region Code Quality
      "python.pythonPath": "venv/bin/python",
      "python.linting.enabled": true,
      "python.linting.pylintEnabled": false,
      "python.linting.mypyEnabled": true,
      "python.linting.flake8Enabled": true,
      "python.testing.pytestEnabled": true,
      "editor.wordWrapColumn": 79,
      "editor.rulers": [79],
      "python.defaultInterpreterPath": "venv/bin/python",
      "python.autoComplete.extraPaths": [
          "venv"    
      ],
      "python.linting.flake8Path": "flake8",
      "python.formatting.provider": "black",
      "python.testing.pytestPath": "py.test",
      "python.analysis.extraPaths": [
          "venv"
      ],
      "mypy-type-checker.importStrategy": "fromEnvironment",
      "black-formatter.importStrategy": "fromEnvironment",
      "flake8.importStrategy": "fromEnvironment",
      "isort.importStrategy": "fromEnvironment",
      "editor.defaultFormatter": "ms-python.black-formatter",
      "isort.check": true,
      "isort.args": [
          "."
      ],
      "black-formatter.args": [
          "."
      ],
      "black-formatter.showNotifications": "onError",
    }

- Install and Configure PyCharm (Optional):

  - Install PyCharm:

    ```shell script
    brew install pycharm
    ```


### Q & A

**What is `apache-arrow`?**

`Apache Arrow` is a language-agnostic software framework for developing data analytics applications that
process columnar data. It contains a standardized column-oriented memory format that is able to represent flat
and hierarchical data for efficient analytic operations on modern CPU and GPU hardware. Apache Arrow is used in data analytics, machine learning, and data engineering. 


**What is `openblas`?**

`OpenBLAS` is an open-source implementation of the Basic Linear Algebra Subprograms (BLAS) library. It is used to
perform linear algebra operations, such as matrix multiplication, matrix factorization, and solving systems of linear
equations. OpenBLAS is useful because it provides high-performance implementations of these operations that are optimized
for modern CPU and GPU hardware. It is used in a wide range of applications, including data analytics, machine learning,
and scientific computing.

**How is `cmake` useful on Mac?**

`CMake` is a cross-platform build system that can be used to build software on Mac, Windows, and Linux.
It is useful on Mac because it can be used to build software that is not available on Mac.
For example, if you have a Windows application that you want to run on Mac, you can use CMake to build the
application on Mac. CMake can also be used to build software that is not available on Mac, such as
software that is only available on Windows or Linux.

**What is `zulu8`?**

`Zulu` is a build of OpenJDK that is fully compliant with the Java SE standard. It is useful because it provides a
high-quality, open-source implementation of the Java platform that is compatible with the Java SE standard. Zulu is used
in a wide range of applications, including web applications, mobile applications, and enterprise applications.


**What is `openjdk11`?**

`OpenJDK` is an open-source implementation of the Java Platform, Standard Edition (Java SE). It
provides a high-quality, open-source implementation of the Java platform that is compatible with the Java SE standard.
OpenJDK is used in a wide range of applications, including web applications, mobile applications, and enterprise
applications.

**What is `libpq`?**

`libpq` is the C application programmer's interface to PostgreSQL. libpq is useful because it provides a low-level
interface for connecting to a PostgreSQL database and executing SQL commands. It is used in a wide range of applications,
including web applications, mobile applications, and enterprise applications.

**What is `cyrus-sasl`?**

Cyrus SASL (Simple Authentication and Security Layer) is a method for adding authentication support to connection-based
protocols. It is used in a wide range of applications, including email, instant messaging, and remote access. t is useful because it
provides a standardized way to add authentication support to connection-based protocols.

**What is `pyenv`?**

Pyenv is a tool for managing multiple versions of Python on a single machine. pyenv lets you easily switch between
multiple versions of Python. It's simple, unobtrusive, and follows the UNIX tradition of single-purpose tools
that do one thing well This project is a fork of rbenv (for Ruby). Pyenv does for Python what rbenv does for Ruby.
- In contrast with pythonbrew and pythonz, pyenv doesn't depend on Python itself. Pyenv was made from pure shell scripts.
Thus, there is no bootstrapping problem.
- pyenv's shim approach works  by adding directory to your $PATH.
- pyenv does not manage virtual environments. It is only for managing Python versions.


**What is SHIM?**
- A shim is a small piece of code that is inserted between two software components to translate between different
interfaces. In the context of pyenv, a shim is a small piece of code that is inserted between the user's shell and the
Python interpreter to translate between different versions of Python.

ex:
```shell
$ echo $PATH
/Users/smary1/.pyenv/shims:/opt/homebrew/opt/cyrus-sasl/sbin:
/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:
/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:
/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:
/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:
/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin
$ cd ~/.pyenv/shims
$ shims % ls
2to3			pip3.11			python3.11
2to3-3.10		pip3.7			python3.11-config
2to3-3.11		pip3.8			python3.11-gdb.py
2to3-3.7		pip3.9			python3.7
2to3-3.8		pydoc			python3.7-config
2to3-3.9		pydoc3			python3.7-gdb.py
easy_install		pydoc3.10		python3.7m
easy_install-3.7	pydoc3.11		python3.7m-config
idle			pydoc3.7		python3.8
idle3			pydoc3.8		python3.8-config
idle3.10		pydoc3.9		python3.8-gdb.py
idle3.11		python			python3.9
idle3.7			python-config		python3.9-config
idle3.8			python3			python3.9-gdb.py
idle3.9			python3-config		pyvenv
pip			python3.10		pyvenv-3.7
pip3			python3.10-config
pip3.10			python3.10-gdb.py
```


Through a process called rehashing, pyenv maintains shims in that directory to match every Python command across every
installed version of Python—python, pip, and so on.

When you run pip, your OS will do the following:
* Search your PATH for an executable file named pip
* Find the pyenv shim named pip at the beginning of your PATH
* Run the shim named pip, which in turn passes the command along to pyenv

**What is `gimme-aws-creds`?**

`gimme-aws-creds` is a tool that makes it easy to obtain temporary AWS credentials. It is useful because it provides a
simple and secure way to obtain temporary AWS credentials that can be used to access AWS services.

**What is `openssl`?**

OpenSSL is a software library for secure communication over computer networks. It is widely used in applications
such as web servers, email servers, and virtual private networks. OpenSSL is useful because it provides a
standardized way to implement secure communication over computer networks.

**What is `terraform`?**

Terraform is an open-source infrastructure as code software tool that provides a consistent CLI workflow to manage
hundreds of cloud services. It codifies APIs into declarative configuration files, creating infrastructure as code.

**What is Make?**

Make is a build automation tool that is used to build software on Unix-like operating systems.

**What is dbeaver?**

DBeaver is a free and open-source universal database tool for developers and database administrators. It provides a
graphical user interface for managing databases and executing SQL commands. DBeaver is useful because it provides a
simple and intuitive way to interact with databases.
