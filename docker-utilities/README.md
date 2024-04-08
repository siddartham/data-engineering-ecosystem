# docker-utilities

[![test](https://github.com/siddarthm/data-engineering-ecosystem/docker-utilities/actions/workflows/test.yml/badge.svg)](https://github.com/siddarthm/data-engineering-ecosystem/docker-utilities/actions/workflows/test.yml)
[![distribute](https://github.com/siddarthm/data-engineering-ecosystem/docker-utilities/actions/workflows/distribute.yml/badge.svg)](https://github.com/siddarthm/data-engineering-ecosystem/docker-utilities/actions/workflows/distribute.yml)

See [CONTRIBUTING.md](CONTRIBUTING.md) for information pertaining to
development of this package.

## Install

```shell script
pip3 install docker-utilities
```

## Usage

### CLI

```text
$ du -h
Usage:
  docker-utilities <command> [options]
  ndu <command> [options]

Commands:
  build
                              Build and (optionally) push an image
  login
                              Login to a server
  exists
                              Determine whether an image exists
```

#### docker-utilities build

```text
$ du build -h
usage: docker-utilities build [-h] [--tag TAG] [--file FILE]
                                   [--directory DIRECTORY]
                                   [--platform PLATFORM] [--skip-existing]
                                   [--user USER]
                                   [--user-cerberus-path USER_CERBERUS_PATH]
                                   [--password PASSWORD]
                                   [--password-cerberus-path PASSWORD_CERBERUS_PATH]
                                   [--no-push]

Build and (optionally) push an image

optional arguments:
  -h, --help            show this help message and exit
  --tag TAG, -t TAG
  --file FILE, -f FILE  The path to a Dockerfile
  --directory DIRECTORY, -d DIRECTORY
                        The build context directory (defaults to the current
                        directory)
  --platform PLATFORM   Which platform/architecture(s) to build for (for
                        example: "linux/amd64" or "linux/arm64").
  --skip-existing       If `True`, skip this build if the image already
                        exists on the remote server
  --user USER, -u USER
  --user-cerberus-path USER_CERBERUS_PATH, -ucp USER_CERBERUS_PATH
  --password PASSWORD, -p PASSWORD
  --password-cerberus-path PASSWORD_CERBERUS_PATH, -pcp PASSWORD_CERBERUS_PATH
  --no-push             If `True`, don't push this build
```

#### docker-utilities login

```text
$ du login -h
usage: docker-utilities login [-h] [--user USER] [--password PASSWORD]
                                   [--server SERVER]
                                   [--user-cerberus-path USER_CERBERUS_PATH]
                                   [--password-cerberus-path PASSWORD_CERBERUS_PATH]
                                   [--server-cerberus-path SERVER_CERBERUS_PATH]

Login to a Docker server

optional arguments:
  -h, --help            show this help message and exit
  --user USER, -u USER
  --password PASSWORD, -p PASSWORD
  --server SERVER, -s SERVER
  --user-cerberus-path USER_CERBERUS_PATH, -ucp USER_CERBERUS_PATH
  --password-cerberus-path PASSWORD_CERBERUS_PATH, -pcp PASSWORD_CERBERUS_PATH
  --server-cerberus-path SERVER_CERBERUS_PATH, -scp SERVER_CERBERUS_PATH
```

#### docker-utilities exists

```text
$ du exists -h
usage: docker-utilities exists [-h] [--user USER] [--password PASSWORD]
                                    [--server SERVER]
                                    [--user-cerberus-path USER_CERBERUS_PATH]
                                    [--password-cerberus-path PASSWORD_CERBERUS_PATH]
                                    [--server-cerberus-path SERVER_CERBERUS_PATH]
                                    uri

Check to see if a Docker image exists on a remote server

positional arguments:
  uri

optional arguments:
  -h, --help            show this help message and exit
  --user USER, -u USER
  --password PASSWORD, -p PASSWORD
  --server SERVER, -s SERVER
  --user-cerberus-path USER_CERBERUS_PATH, -ucp USER_CERBERUS_PATH
  --password-cerberus-path PASSWORD_CERBERUS_PATH, -pcp PASSWORD_CERBERUS_PATH
  --server-cerberus-path SERVER_CERBERUS_PATH, -scp SERVER_CERBERUS_PATH
```
