# cerberus-assistant

[![test](https://github.com/siddartham/data-engineering-ecosystem/cerberus-assistant/actions/workflows/test.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/cerberus-assistant/actions/workflows/test.yml)
[![distribute](https://github.com/siddartham/data-engineering-ecosystem/cerberus-assistant/actions/workflows/distribute.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/cerberus-assistant/actions/workflows/distribute.yml)

[Development Environment Setup](https://github.com/siddartham/data-engineering-ecosystem/dev-env-setup)

This package provides a CLI and library for retrieving and setting Cerberus secrets
without needing to explicitly specify an AWS profile.

## Install

You can install this package from PYPI:

```shell script
pip3 install cerberus-assistant
```

## Usage

Note: When using `cerberus-assistant` locally, you will need to run
[`gimme-aws-creds`](https://github.com/Nike-Inc/gimme-aws-creds) first in
order to generate temporary auth tokens.

### CLI

#### cerberus-assistant get

```console
$ cerberus-assistant get -h
usage: cerberus-assistant get [-h] [-u URL] [-arn AMAZON_RESOURCE_NAME]
                                   path

Retrieve a Cerberus secret.

positional arguments:
  path                  The Cerberus path containing the desired secret,
                        *including* a dictionary key. For example:
                        "path/to/secrets/key".

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     The base URL for the Cerberus API (default value:
                        https://prod.cerberus.mycould.com).
  -arn AMAZON_RESOURCE_NAME, --amazon-resource-name AMAZON_RESOURCE_NAME
                        The ARN of a role to assume.
```

Example:

```console
$ cerberus-assistant get app/secure-drop-box/path/key
my-cerberus-secret
```

#### cerberus-assistant put

```console
$ cerberus-assistant put -h
usage: cerberus-assistant put [-h] [-u URL] [-arn AMAZON_RESOURCE_NAME]
                                   path secret

Put a secret in a Cerberus secure drop box

positional arguments:
  path                  The Cerberus path containing the desired secret,
                        *including* a dictionary key. For example:
                        "path/to/secrets/key".
  secret                The secret to put in the specified path.

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     The base URL for the Cerberus API (default value:
                        https://prod.cerberus.mycloud.com).
  -arn AMAZON_RESOURCE_NAME, --amazon-resource-name AMAZON_RESOURCE_NAME
                        The ARN of a role to assume.
```

Example:

```bash
cerberus-assistant put app/secure-drop-box/path/key value
```

#### cerberus-assistant delete

```console
$ cerberus-assistant delete -h
usage: cerberus-assistant delete [-h] [-u URL]
                                      [-arn AMAZON_RESOURCE_NAME]
                                      path

Delete a Cerberus secret path.

positional arguments:
  path                  The Cerberus path containing the desired secrets,
                        *not* including a dictionary key. For example:
                        "path/to/secrets".

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     The base URL for the Cerberus API (default value:
                        https://prod.cerberus.mycloud.com).
  -arn AMAZON_RESOURCE_NAME, --amazon-resource-name AMAZON_RESOURCE_NAME
                        The ARN of a role to assume.
```

### Library

#### cerberus_assistant.get

##### get_secret

This function retrieves a Cerberus secret at the provided path (including key).

Example:

```python
>>> from cerberus_assistant.get import get_secret
... print(get_secret("app/a-secure-drop-box/gid-passwords/a.GID.USER"))
a-gid-password
```

##### get_secrets

This function retrieves a dictionary of Cerberus secrets at the
specified (3-part) path (not including the key).

Example:

```python
>>> from cerberus_assistant.get import get_secret
... print(get_secret("app/a-secure-drop-box/gid-passwords"))
{"a.GID.USER": "a-gid-password"}
```

#### cerberus_assistant.put

##### put_secret

This function puts a secret to a Cerberus SDB path.

Example:

```python
>>> from cerberus_assistant.put import put_secret
... print(put_secret("app/secure-drop-box/path", {"mykey": "myvalue"}))
True
```


#### cerberus_assistant.delete

##### delete_secret_path

This function deletes a secret path.

Example:

```python
>>> from cerberus_assistant.delete import delete_secret_path
... print(delete_secret_path("app/secure-drop-box/test-secret-path"))
True
```

#### cerberus_assistant.decorate

##### apply_cerberus_path_arguments

This decorator maps parameters for explicit inputs with parameters which
provide a Cerberus path where aforementioned inputs can be obtained.

```python
>>> from cerberus_assistant.decorate import apply_cerberus_path_arguments
... @apply_cerberus_path_arguments(password="password_cerberus_path")
... def return_value(
...     password: str = "",
...     password_cerberus_path: str = ""
... ) -> str:
...     return value
... print(return_value(password="a-gid-password"))
a-gid-password
>>> print(return_value(
...     password_cerberus_path="app/my-secure-drop-box/passwords/a.GID.USER"
... ))
a-gid-password
```
