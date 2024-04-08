[![test](https://github.com/siddartham/data-engineering-ecosystem/mail-client/actions/workflows/test.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/mail-client/actions/workflows/test.yml)
[![distribute](https://github.com/siddartham/data-engineering-ecosystem/mail-client/actions/workflows/distribute.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/mail-client/actions/workflows/distribute.yml)

# mail-client

This package is a python library and CLI providing simple SMTP email
capabilities.

## Installation


```shell
pip3 install mail-client
```

To install *for development*:

- Clone the repository:
  ```shell script
  git clone\
   https://github.com/siddartham/data-engineering-ecosystem.git
  cd data-engineering-ecosystem/mail-client
  ```
- Create and activate a new virtual environment:
  ```shell
  python3 -m venv venv
  source venv/bin/activate
  ```
- Install the package in-place:
  ```shell script
  pip3 install -e '.[test,dev]'
  ```

## Commands

### Send

For CLI documentation execute `mail-client send --help` in your shell
of choice:
```text
usage: mail-client send [optional arguments]

optional arguments:
  -h, --help            show this help message and exit
  --to TO, -to TO       a comma-separated list of recipients to include in the
                        "to" header for this message
  --cc CC, -cc CC       a comma-separated list of recipients to include in the
                        "cc" header for this message
  --bcc BCC, -bcc BCC   a comma-separated list of recipients to include in the
                        "bcc" header for this message
  --from FROM, -f FROM  a "from" header for this message
  --reply-to REPLY_TO, -rt REPLY_TO
                        a "reply-to" header for this message
  --user USER, -u USER  a username with which to authenticate Note: if
                        providing a PASSWORD_CERBERUS_PATH where the username
                        is the secret key, and the secret key is appended to
                        the path provided in the PASSWORD_CERBERUS_PATH, this
                        can be left out if providing a PASSWORD_CERBERUS_PATH
                        *without* a secret key appended to the path, the USER
                        will be inferred to be the secret key
  --password PASSWORD, -p PASSWORD
                        a password with which to authenticate (this is not
                        needed if providing a PASSWORD_CERBERUS_PATH)
  --password-cerberus-path PASSWORD_CERBERUS_PATH, -pcp PASSWORD_CERBERUS_PATH
                        the path to a password stored in a My Cerberus vault
                        with which to authenticate
  --subject SUBJECT, -s SUBJECT
                        a subject header for this message
  --body BODY, -b BODY  The body of the message
```

## Library Modules

### mail_client.smtp

#### mail_client.smtp.send

This function sends an email using the SMTP protocol. If authentication
is required, either a `user` and `password` must be provided, or
a `password_cerberus_path`, which will cause a username and password
to be retrieved from one of My Cerberus vaults.

Parameters:
    
- to (str|[str]):
  A list of recipients to include in the "To:" header of this message
- cc (str|[str]):
  A list of recipients to include in the "Cc:" header of this message
- bcc (str):
  A list of recipients to include in the "Bcc:" header of this message.
  header of this message
- from_ (str):
  An email address to use in the "From:" header of this message
- reply_to (str):
  An email address to use in the "Reply-to:" header of this message
- user (str): A username with which to authenticate. Note:
  If providing a `password_cerberus_path` where the username
  is the secret key, and the secret key is appended to the path
  provided in the `password_cerberus_path`, this can be left out.
  If providing a `password_cerberus_path` *without* a secret key
  appended to the path, the `user` will be inferred to be the
  secret key.
- password (str): A password with which to authenticate (this is not
  needed if providing a `password_cerberus_path`)
- password_cerberus_path (str):
  The path to a password stored in a My Cerberus vault with which to
  authenticate
- subject (str): A subject header for this message
- body (str): The body of the message

Returns: `None` if successful, or raises an exception if errors occur.

## Updating this Package

Following any changes to this package (at least any changes for which you
want to trigger a build), the version number should be updated in `setup.py`,
in the `setup()` call's `version` parameter, and you should also run `source
scripts/update_requirements.sh` to ensure all installation requirements
are up-to-date. Deployment to Artifactory will occur when changes are merged
into the "main" branch.
  
## Testing

To run unit tests for this package, just execute `tox` in your shell of
choice.
