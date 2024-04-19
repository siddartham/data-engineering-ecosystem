# file-system-client

[![test](https://github.com/siddartham/data-engineering-ecosystem/file-system-client/actions/workflows/test.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/file-system-client/actions/workflows/test.yml)
[![distribute](https://github.com/siddartham/data-engineering-ecosystem/file-system-client/actions/workflows/distribute.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/file-system-client/actions/workflows/distribute.yml)

[Development Environment Setup](https://github.com/siddartham/data-engineering-ecosystem/dev-env-setup)

This library provides:

1) A common framework for interfacing with cloud and local file systems.
   Currently, clients for AWS S3 and locally mounted file systems are
   implemented as sub-classes of an abstract base class which defined common
   functionality.
2) Functionality for efficiently reading, writing, and sorting/parsing/finding
   date/time partitioned data directories/files.
3) Seamless authentication with and connection to S3:
   - Automatic detection of an appropriate profile to use to authenticate,
     when multiple AWS IAM profiles are available, in order to facilitate use
     of the same tests and commands when executing locally as when running in
     CI/CD.
   - Simplifies/automates connection to and use of localstack to test
     interaction with S3 locally.


## Install

```shell script
pip3 install git+https://github.com/siddartham/data-engineering-ecosystem/file-system-client
```

## Usage

### Local

To work with a local file system where the root directory is the user's
home directory:

```python
import os
from file_system_client.local import Local

file_system: Local = Local(root=os.expanduser("~"))
```

### S3

To work with Amazon S3 bucket "my-bucket", using the object prefix
"/my/root/directory" as your root directory, you can instantiate the
client class directly:

```python
file_system: s3.S3

# Create an S3 file system client instance
file_system = s3.S3(bucket_name="my-bucket-name", root="/my/root/prefix/")

# Create an S3 file system client instance which will use localstack
# instead of AWS (for testing)
file_system = s3.S3(
    bucket_name="my-bucket-name",
    root="/my/root/prefix/",
    endpoint_url="http://localhost:4566",
)

# Create an S3 file system client instance which will assume a specific ARN
file_system = s3.S3(
    bucket_name="my-bucket-name",
    root="/my/root/prefix/",
    arn="arn:aws:iam::123456789:role/my-role-name"
)
```

...or you can create a client class instance from an S3 URL:

```python
from file_system_client import s3

file_system: s3.S3

# Create an S3 file system client instance
file_system = s3.from_url("s3://my-bucket-name/my/root/prefix/")

# Create an S3 file system client instance which will use localstack
# instead of AWS (for testing)
file_system = s3.from_url(
    "s3://my-bucket-name/my/root/prefix/",
    endpoint_url="http://localhost:4566",
)

# Create an S3 file system client instance which will assume a specific ARN
file_system = s3.from_url(
    "s3://my-bucket-name/my/root/prefix/",
    arn="arn:aws:iam::123456789:role/my-role-name"
)
```

Your client will obtain credentials automatically, so long as you have valid,
current authentication tokens for at least one profile with access to the
specified bucket and prefix. When using the S3 file system client on your
local workstation, this means you'll need to have run `gimme-aws-creds` within
the past hour.


### Common Parameters/Properties

All file system clients have the following public properties, and take
the following initialization parameters (each initialization parameter
corresponds to a public property having the same name):

- root (str) = "": The absolute file path which serves as the file system root
  directory. If not provided, this will default to the file system root.

### Common Methods

#### put

Save a file to the specified path.

Common Parameters:

- file (typing.IO[bytes]|bytes): Either a file-like object from which
  the `.read()` method returns `bytes`, or an instance of `bytes`.
- path (str): A path, relative to `self.root`, to which the file object
  will be saved.

S3 Parameters

- metadata: Optional[Dict[str, Any]] = None: A dictionary (optional) containing
  metadata which should be associated with the file. See
  [the AWS metadata documentation](https://go.aws/3Xm7CxM) for a listing of
  system-defined metadata. Note: All keys which do not match system-defined
  metadata fields will be interpreted as user-defined metadata.

S3 Example:

```python
import os
from file_system_client import s3

file_system: s3.S3 = s3.from_url("s3://my-bucket-name/my/root/prefix/")

# Open a CSV file named "~/data.csv" and write the file to
# s3://my-bucket-name/my/root/prefix/path/to/file.csv
with open(os.path.expanduser("~/data.csv"), "rb") as data_csv_io:
    file_system.put(
        data_csv_io,
        "path/to/file.csv",
        metadata={"Content-Type": "text/csv"}
    )

# Open a gzipped CSV file named "~/data.csv.gz", write the file to
# s3://my-bucket-name/my/root/prefix/path/to/file.csv.gz
with open(os.path.expanduser("~/data.csv.gz"), "rb") as data_csv_gz_io:
    file_system.put(
        data_csv_gz_io,
        "path/to/file.csv.gz",
        metadata={
            "Content-Encoding": "gzip",
            "Content-Type": "text/csv",
        }
    )
```

#### delete

Delete a file.

Parameters:

- path (str)
- version (str) = "": If provided, delete only the specified version
  of a versioned file.

##### S3 File Deletion Example

S3 files can be deleted by their path relative to the file system root,
by their absolute path, or by S3 URL.

```python
import os
from file_system_client import s3

file_system: s3.S3 = s3.from_url("s3://my-bucket-name/my/root/prefix/")

# Delete a file by path relative to the root
file_system.delete("path/to/file-a.csv")

# Delete a file by absolute path
file_system.delete("/my/root/prefix/path/to/file-b.csv")

# Delete a file by S3 URL
file_system.delete("s3://my-bucket-name/my/root/prefix/path/to/file-c.csv")
```

#### get

Retrieve a file.

Parameters:

- path (str): The path of a file relative to the root directory.

S3 Parameters:

- version (str): A specific version of the file to delete.

##### S3 File Retrieval Example

```python
import os
from typing import IO
from file_system_client import s3

file_system: s3.S3 = s3.from_url("s3://my-bucket-name/my/root/prefix/")

# Download a file
file_csv_io: IO[bytes]
file_csv_write_io: IO[bytes]
with file_system.get("path/to/file.csv") as file_csv_read_io:
    with open(os.path.expanduser("~/file.csv"), "wb") as file_csv_write_io:
        file_csv_write_io.write(file_csv_read_io.read())
```

#### get_url

Get an absolute URL from a relative path.

Parameters:

- path (str): A file path relative to the file system root.

##### S3 Example of Getting a File URL from a Path

```python
import os
from file_system_client import s3

file_system: s3.S3 = s3.from_url("s3://my-bucket-name/my/root/prefix/")

# Delete a file by path relative to the root
print(file_system.get_url("path/to/file.csv"))
```

The above example will produce the following output:

```text
s3://my-bucket-name/my/root/prefix/path/to/file.csv
```

#### get_absolute_path

Return the absolute path of the specified file path, if the path
provided is expressed relative to the file system root. If the path
is already an absolute path, just return that path.

Parameters:

- path (str)

##### S3 Example of Resolving an Absolute File Path

```python
import os
from file_system_client import s3

file_system: s3.S3 = s3.from_url("s3://my-bucket-name/my/root/prefix/")

print(file_system.get_absolute_path("path/to/file.csv"))
```

The above example will produce the following output:

```text
/my/root/prefix/path/to/file.csv
```

#### get_relative_path

Given an absolute file path, return the same path expressed
relative to the file system root.

Parameters:

- path (str)

Returns: A file path relative to the file system root.

##### S3 Example of Resolving a Relative File Path

```python
import os
from file_system_client import s3

file_system: s3.S3 = s3.from_url("s3://my-bucket-name/my/root/prefix/")

print(file_system.get_relative_path("/my/root/prefix/path/to/file.csv"))
```

The above example will produce the following output:

```text
path/to/file.csv
```

#### iter_file_paths

Iterate over file paths in a directory.

Parameters:

- directory (str)
- recursive (bool)
- sort_key (file_system_client.base.FileSortKey) =
  file_system_client.base.FileSortKey.DEFAULT: This parameter indicates
  what property of the files to use for sorting returned file paths. By
  default, the file system default behavior will be used. The other sorting
  options available are:
  - MODIFIED: The date on which the file was most recently modified.
  - NAME: Alphabetical sorting.
- sort_reverse (bool) = False: By default, sorting is in ascending order.
  If `sort_reverse is True`, sorting will be the opposite (descending order).

Returns: An iterable of all files in `directory`.

##### S3 Examples of Iterating Over Files in a Directory

All of the following examples use an S3 file system with the
following directory/file structure:

```text
s3://my-bucket-name/my/root/prefix
   ├── path
   │    └── to
   │         ├── file-a.parquet
   │         ├── file-z.parquet
   │         ├── sub-directory-1
   │         │     ├── file-a.csv
   │         │     └── file-b.csv
   │         └── sub-directory-2
   │               ├── file-a.txt
   │               ├── file-b.txt
   │               └── file-c.txt
   └── another-path
        ├── another-sub-directory
        │    └── another-file.csv
        └── another-file.txt
```

This first example recursively iterates over all files under the specified
"directory" (S3 object prefix), yielding results sorted by name.

```python
import os
from file_system_client import s3
from file_system_client.base import FileSortKey

file_system: s3.S3 = s3.from_url("s3://my-bucket-name/my/root/prefix/")

# Recursively print the path of all files in a directory, sorted by name
path: str
for path in file_system.iter_file_paths(
    "/path/to/",
    sort_key=FileSortKey.NAME
):
    print(path)
```

...the above example would print:

```text
file-a.parquet
sub-directory-1/file-a.csv
sub-directory-1/file-b.csv
sub-directory-2/file-a.txt
sub-directory-2/file-b.txt
file-z.parquet
```

The following is an example operating on the same imaginary dataset as above,
but with the parameter `recursive=False`:

```python
import os
from file_system_client import s3
from file_system_client.base import FileSortKey

file_system: s3.S3 = s3.from_url("s3://my-bucket-name/my/root/prefix/")

# Print the path of all files in a directory, sorted by name
path: str
for path in file_system.iter_file_paths(
    "/path/to/",
    recursive=False,
    sort_key=FileSortKey.NAME
):
    print(path)
```

...the above example would print:

```text
file-a.parquet
file-z.parquet
```

#### iter_file_urls

Iterate over file URLs in a directory. This is the same as
[iter_file_paths](#iter_file_paths), but yields absolute URLs instead of
relative paths.

Parameters:

- directory (str)
- recursive (bool)
- sort_key (file_system_client.base.FileSortKey) =
  file_system_client.base.FileSortKey.DEFAULT: This parameter indicates
  what property of the files to use for sorting returned file paths. By
  default, the file system default behavior will be used. The other sorting
  options available are:
  - MODIFIED: The date on which the file was most recently modified.
  - NAME: Alphabetical sorting.
- sort_reverse (bool) = False: By default, sorting is in ascending order.
  If `sort_reverse is True`, sorting will be the opposite (descending order).

Returns: An iterable of all files in `directory`.

##### S3 Examples of Iterating Over the URLs of Files in a Directory

All of the following examples use an S3 file system with the
following directory/file structure:

```text
s3://my-bucket-name/my/root/prefix
   ├── path
   │    └── to
   │         ├── file-a.parquet
   │         ├── file-z.parquet
   │         ├── sub-directory-1
   │         │     ├── file-a.csv
   │         │     └── file-b.csv
   │         └── sub-directory-2
   │               ├── file-a.txt
   │               ├── file-b.txt
   │               └── file-c.txt
   └── another-path
        ├── another-sub-directory
        │    └── another-file.csv
        └── another-file.txt
```

This first example recursively iterates over all files under the specified
"directory" (S3 object prefix), yielding results sorted by name.

```python
import os
from file_system_client import s3
from file_system_client.base import FileSortKey

file_system: s3.S3 = s3.from_url("s3://my-bucket-name/my/root/prefix/")

# Recursively print the path of all files in a directory, sorted by name
url: str
for url in file_system.iter_file_urls(
    "/path/to/",
    sort_key=FileSortKey.NAME
):
    print(url)
```

...the above example would print:

```text
s3://my-bucket-name/my/root/prefix/file-a.parquet
s3://my-bucket-name/my/root/prefix/sub-directory-1/file-a.csv
s3://my-bucket-name/my/root/prefix/sub-directory-1/file-b.csv
s3://my-bucket-name/my/root/prefix/sub-directory-2/file-a.txt
s3://my-bucket-name/my/root/prefix/sub-directory-2/file-b.txt
s3://my-bucket-name/my/root/prefix/sub-directory-2/file-c.txt
s3://my-bucket-name/my/root/prefix/file-z.parquet
```

The following is an example operating on the same imaginary dataset as above,
but with the parameter `recursive=False`:

```python
import os
from file_system_client import s3
from file_system_client.base import FileSortKey

file_system: s3.S3 = s3.from_url("s3://my-bucket-name/my/root/prefix/")

# Print the path of all files in a directory, sorted by name
url: str
for url in file_system.iter_file_urls(
    "/path/to/",
    recursive=False,
    sort_key=FileSortKey.NAME
):
    print(url)
```

...the above example would print:

```text
s3://my-bucket-name/my/root/prefix/file-a.parquet
s3://my-bucket-name/my/root/prefix/file-z.parquet
```

#### iter_sub_directories

Iterate over all sub-directories of a specified directory.

Parameters:

- directory (str)
- recursive (bool) = False: If `False`, only *direct* descendants of the
  specified `directory` will be included. If `True`, *all* sub-directories,
  including sub-directories of each sub-directory, etc., will be included.

##### S3 Example of Iterating Over Sub-Directories

The examples below will reference the following directory structure:

```text
s3://my-bucket-name/my/root/prefix
   ├── path
   │    └── to
   │         ├── file-a.parquet
   │         ├── file-z.parquet
   │         ├── sub-directory-1
   │         │     ├── sub-sub-directory-1a
   │         │     │     └── file-a.csv
   │         │     └── sub-sub-directory-1b
   │         │           └── file-b.csv
   │         └── sub-directory-2
   │               ├── file-a.txt
   │               ├── file-b.txt
   │               └── file-c.txt
   └── another-path
        ├── another-sub-directory
        │    └── another-file.csv
        └── another-file.txt
```

This first example iterates over all "sub-directories" *directly* under the
specified "directory" (S3 object prefix).

```python
import os
from file_system_client import s3
from file_system_client.base import FileSortKey

file_system: s3.S3 = s3.from_url("s3://my-bucket-name/my/root/prefix/")

# Print the path of all files in a directory, sorted by name
path: str
for path in file_system.iter_sub_directories("/path/to/"):
    print(path)
```

...the above example would print the following:

```text
sub-directory-1/
sub-directory-2/
```

The below example iterates *recursively* over all "sub-directories" under the
specified "directory" (S3 object prefix).

```python
import os
from file_system_client import s3
from file_system_client.base import FileSortKey

file_system: s3.S3 = s3.from_url("s3://my-bucket-name/my/root/prefix/")

# Recursively print the path of all files under a directory, sorted by name
path: str
for path in file_system.iter_sub_directories("/path/to/", recursive=True):
    print(path)
```

...the above example would print the following:

```text
sub-directory-1/
sub-directory-1/sub-directory-1a/
sub-directory-1/sub-directory-1b/
sub-directory-2/
```

#### is_file

Return `True` if a file exists at the specified `path`.

Parameters:

- path (str): A path, relative to the file system root, at which to look
  for a file.

#### is_directory

Return `True` if a directory exists at the specified `path`.

Parameters:

- path (str): A path, relative to the file system root, at which to look
  for a directory.

Note: For some file systems which do not utilize directories, such as S3,
this method is really searching for any files having the specified *prefix*.

#### had_success

Check to see if files in the specified directory are part of a
successfully completed operation (as opposed to being created as part
of an operation which failed or was terminated prematurely). This is
indicated by the presence of an empty file named "_SUCCESS".

Note: If this directory does not exist, this method will return
`False`, the same as if it existed but had no success indicator.

Parameters:

- directory (str): A directory path, relative to the file system root, under
  which to look for a success indicator file.

#### put_success

Create a success indicator file in the specified `directory`,
if one does not already exist (this is an empty file named "_SUCCESS").

Note: If this `directory` does not exist, it will be created. If the
success indicator already exists, no error will be raised.

Parameters:

- directory (str): A directory path, relative to the file system root, under
  which to create a success indicator file.

#### delete_success

If present, remove from the specified `directory` the success
indicatory file. This is a file named "_SUCCESS", which indicates
that the last operation on this directory was successful (as
opposed to being still in-progress, or having failed).

Note: If this directory does not exist, no error is raised.

Parameters:

- directory (str): The path, relative to the file system root, of
  a directory.

#### iter_latest_directory_sub_directories

This method finds the most recently created sub-directory under
the specified `directory` (as determined by name, not file system
metadata), and returns a tuple containing two items:

- The first item in the returned tuple is the path of a timestamp-named
  sub-directory, located directly under `directory`, which was created
  most recently.
- The second item in the returned tuple is an iterable which yields the
  path of all sub-sub-directories, directly under the latest
  timestamp-named sub-directory. This iterable is equivalent to the
  response you would get from
  [FileSystem.iter_latest_directories](#iter_latest_directories) for
  the same `directory`.

Parameters:

- directory (str): A directory path, relative to the file system root,
  under which to look for the most recently created sub-directory
  as determined by the sub-directory name.

  The date and time associated with a sub-directory will be determined
  using the function
  `file_system_client.utilities.get_path_datetime_and_index`,
  which simply finds all segments of numeric digits in a sub-directory
  name, and assigns the first chunk of numeric digits to a year,
  the next to a month, the next to a day, hour, minute, second, etc.
  Separators can be anything (except for numeric digits, of course).

  Sub-directory names conforming to the needed format can be produced
  with consistent formatting using the function
  `file_system_client.utilities.get_date_directory_name`.

For example usage please refer to
[Date Partition Examples](#date-partition-examples).

#### iter_latest_directories

This method finds the most recently created sub-directory under
the specified `directory` (as determined by name, not file system
metadata), and returns an iterable of all sub-sub-directories directly
under that sub-directory.
The iterable returned by this method is equivalent to the second item
in the tuple returned by
`FileSystem.iter_latest_directory_sub_directories`.

Parameters:

- directory (str): A directory path, relative to the file system root,
  under which to look for the most recently created sub-directory
  as determined by the sub-directory name.

  Notes:

  The date and time associated with a sub-directory will be determined
  using the function
  `file_system_client.utilities.get_path_datetime_and_index`,
  which simply finds all segments of numeric digits in a sub-directory
  name, and assigns the first chunk of numeric digits to a year,
  the next to a month, the next to a day, hour, minute, second, etc.
  Separators can be anything (except for numeric digits, of course).

  Sub-directory names conforming to the needed format can be produced
  with consistent formatting using the function
  `file_system_client.utilities.get_date_directory_name`.

For example usage please refer to
[Date Partition Examples](#date-partition-examples).

#### iter_latest_directory_files

This method finds the most recently created sub-directory under
the specified `directory` (as determined by name, not file system
metadata), and returns a tuple containing two items:

- The first item in the returned tuple is the path of the
  timestamp-named sub-directory, located directly under `directory`,
  which was created most recently.
- The second item in the returned tuple is an iterable which yields the
  path of all files directly under the latest timestamp-named
  sub-directory. This iterable is equivalent to the response you would
  get from [FileSystem.iter_latest_files](#iter_latest_files) for the same
  `directory`.

Parameters:

- directory (str): A directory path, relative to the file system root,
  under which to look for the most recently created sub-directory
  as determined by the sub-directory name.

  Notes:

  The date and time associated with a sub-directory will be determined
  using the function
  `file_system_client.utilities.get_path_datetime_and_index`,
  which simply finds all segments of numeric digits in a sub-directory
  name, and assigns the first chunk of numeric digits to a year,
  the next to a month, the next to a day, hour, minute, second, etc.
  Separators can be anything (except for numeric digits, of course).

  Sub-directory names conforming to the needed format can be produced
  with consistent formatting using the function
  `file_system_client.utilities.get_date_directory_name`.

- recursive (bool) = True: If `False`, only files *directly* under
  the time-stamped sub-directory will be included. If `True` (the
  default), files will be discovered and yielded recursively under
  descendant sub-sub-directories, etc.

For example usage please refer to
[Date Partition Examples](#date-partition-examples).

#### iter_latest_files

This method finds the most recently created sub-directory under
the specified `directory` (as determined by name, not file system
metadata), and returns an iterable of all sub-sub-directories directly
under that sub-directory.

The iterable returned by this method is equivalent to the second item
in the tuple returned by
`FileSystem.iter_latest_directory_sub_directories`.

Parameters:

- directory (str): A directory path, relative to the file system root,
  under which to look for the most recently created sub-directory
  as determined by the sub-directory name.

  Notes:

  The date and time associated with a sub-directory will be determined
  using the function
  `file_system_client.utilities.get_path_datetime_and_index`,
  which simply finds all segments of numeric digits in a sub-directory
  name, and assigns the first chunk of numeric digits to a year,
  the next to a month, the next to a day, hour, minute, second, etc.
  Separators can be anything (except for numeric digits, of course).

  Sub-directory names conforming to the needed format can be produced
  with consistent formatting using the function
  `file_system_client.utilities.get_date_directory_name`.

- recursive (bool) = True: If `False`, only files *directly* under
  the time-stamped sub-directory will be included. If `True` (the
  default), files will be discovered and yielded recursively under
  descendant sub-sub-directories, etc.

For example usage please refer to
[Date Partition Examples](#date-partition-examples).

#### clear

Delete all files in a directory.

Parameters:

- directory (str): A directory path, relative to the file system root.

#### delete_directory

Delete a directory and all files in that directory. For some file systems,
this may be effectively the same as [FileSystem.clear](#clear).

Parameters:

- directory (str): A directory path, relative to the file system root.

#### get_unique_date_partition_directory

Given a date-partition directory path, return a variation
which is not already in existence by appending seconds/microseconds
as needed.

Parameters:

- path (str): A file path, relative to the file system root, at which
  to check for an existing file or directory.

##### S3 Example of Getting a Unique File Name

The examples below will reference the following directory structure:

```text
s3://my-bucket-name/my/root/prefix
   └── path
        ├── a
        │   ├── date_partition=2021-07-23-13-05
        │   │     ├── file-01.parquet
        │   │     ├── file-02.parquet
        │   │     └── file-03.parquet
        │   ├── date_partition=2021-07-23-13-06
        │   │     ├── file-01.parquet
        │   │     ├── file-02.parquet
        │   │     └── file-03.parquet
        │   └── date_partition=2021-08-12-49-33
        │         ├── file-01.parquet
        │         ├── file-02.parquet
        │         └── file-03.parquet
        └── b
            ├── date_partition=2021-07-23-13-05-000001
            │     ├── file-01.parquet
            │     ├── file-02.parquet
            │     └── file-03.parquet
            ├── date_partition=2021-07-23-13-05-000002
            │     ├── file-01.parquet
            │     ├── file-02.parquet
            │     └── file-03.parquet
            └── date_partition=2021-08-12-49-33
                  ├── file-01.parquet
                  ├── file-02.parquet
                  └── file-03.parquet
```

The following example obtains a unique date partition file name when
given a non-unique date partition file name:

```python
from file_system_client import s3

file_system: s3.S3 = s3.from_url("s3://my-bucket-name/my/root/prefix/")

print(
    file_system.get_unique_date_partition_directory(
        "/path/a/date_partition=2021-08-12-49-33/"
    )
)
```

...the above example prints:

```text
/path/to/date_partition=2021-08-12-49-34/
```

### S3 Parameters/Properties

In addition to the [common properties](#common-parametersproperties), S3 file
system clients also have additional public parameters/properties (each
initialization parameter corresponds to a public property). The
parameter/property list for `file_system_client.s3.S3` is as follows.

Required Parameters:

- bucket_name (str)

Typical Use Optional Parameters:

- root (str) = "": A root object prefix ("directory") to use in resolving
  relative paths. If not provided, this will default to the bucket root.

Less Typical Use Optional Parameters:

- profile_name (str): This is the profile name to use in retrieving
  stored credentials. If not provided, the profile will be inferred
  to be the first encountered which has access to the specified bucket.
- arn (str): An ARN to assume (optional).
- endpoint_url (str): The AWS endpoint URL to use (optional).
- config (botocore.config.Config): An (optional) botocore
  [configuration object](https://bit.ly/3cUHEwy).

### S3 Methods

In addition to methods defined by the abstract base class, and therefore
required to be included for all file systems, the S3 client adds the following
methods.

#### update_metadata

Update metadata for a pre-existing S3 object found at `path`.

Parameters:

- path (str): The path of a file relative to the root directory.
- metadata ({str: typing.Any}): A dictionary containing
  metadata which should be associated with the file. See
  [the AWS metadata documentation](https://go.aws/3Xm7CxM) for a list
  of system-defined metadata. Note: All keys which do not match
  system-defined metadata fields will be interpreted as user-defined
  metadata.
- clear (bool) = False: If `True`, all pre-existing metadata will
  be cleared prior to applying the new metadata.

Example:

```python
from file_system_client import s3

file_system: s3.S3 = s3.from_url("s3://my-bucket-name/my/root/prefix/")

# Update metadata for CSV file
# s3://my-bucket-name/my/root/prefix/path/to/file.csv.gz
file_system.update_metadata(
    "path/to/file.csv.gz",
    metadata={
        "Content-Encoding": "gzip",
        "Content-Type": "text/csv",
    }
)
```

Please note that it is more efficient to set metadata when
[putting a file](#put). When files are created through processes which
do not permit you to apply correct metadata, such as when writing from
Snowflake to S3, this method is an appropriate alternative means of
applying the correct metadata.

### Date Partition Examples

Typical use of the date partition functionality of this package would be to
timestamp extracts or intermediate steps in a data pipeline so that
subsequent tasks in the pipeline can identify the appropriate data sub-set
(usually the most recent) to use/ingest/process, then for those subsequent
tasks to identify the sub-directory housing the most recent data from the
upstream source or prior pipeline step without explicit input. This facilitates
replay of a pipeline, starting at any given stage, after having been
interrupted (purposely or on error).

Subsequent examples will reference the following source system
file structure:

```text
s3://source-bucket-name/source/root/prefix/
  └── raw
        └── full
              ├── date_partition=2021-07-22-09-55
              │     ├── file-01.parquet
              │     ├── file-02.parquet
              │     └── file-03.parquet
              ├── date_partition=2021-07-23-13-05
              │     ├── file-01.parquet
              │     ├── file-02.parquet
              │     └── file-03.parquet
              └── date_partition=2021-07-23-18-44
                    ├── file-01.parquet
                    ├── file-02.parquet
                    └── file-03.parquet
```

The following example identifies and prints the s3 prefix (analogous to a
directory), where the latest extract resides:

```python
from file_system_client import s3

source_file_system: s3.S3 = s3.from_url(
    "s3://source-bucket-name/source/root/prefix/"
)
print(source_file_system.get_latest_directory("/raw/full/"))
```

The above example would print the following:

```text
/raw/full/date_partition=2021-07-23-18-44/
```

The following example identifies the s3 prefix where the latest extract
resides, and prints the path to all files under that directory:

```python
from collections import deque
from file_system_client import s3, base

source_file_system: base.FileSystem = s3.from_url(
    "s3://source-bucket-name/source/root/prefix/"
)
deque(
    map(print, source_file_system.iter_latest_files("/raw/full/")),
    maxlen=0,
)
```

The above example would print the following:

```text
/raw/full/date_partition=2021-07-23-18-44/file-01.parquet
/raw/full/date_partition=2021-07-23-18-44/file-02.parquet
/raw/full/date_partition=2021-07-23-18-44/file-03.parquet
```

The following example identifies the s3 prefix where the latest extract
resides, and prints both the source directory path, and each
file path under that directory:

```python
from typing import Iterable
from file_system_client import s3, base

source_file_system: base.FileSystem = s3.from_url(
    "s3://source-bucket-name/source/root/prefix/"
)
directory: str
files: Iterable[str]
directory, files = source_file_system.iter_latest_directory_files(
    "/raw/full/"
)
print(f"Directory: {directory}")
print("Files:\n- {}".format("\n- ".join(files)))
```

The above example would print the following:

```text
Directory: /raw/full/date_partition=2021-07-23-18-44/
Files:
- /raw/full/date_partition=2021-07-23-18-44/file-01.parquet
- /raw/full/date_partition=2021-07-23-18-44/file-02.parquet
- /raw/full/date_partition=2021-07-23-18-44/file-03.parquet
```

The following example sources data from the most recent in a series of
exports, creates a data frame with only one record for each primary key
combination (PRIMARY_KEY_COLUMN_A, PRIMARY_KEY_COLUMN_B, and
PRIMARY_KEY_COLUMN_C), then writes the result to a time-stamped directory
in the target file system:

```python
from pyspark import sql as pyspark_sql  # type: ignore
from pyspark.sql.dataframe import DataFrame  # type: ignore
from pyspark.sql import (  # type: ignore
    SparkSession,
    functions as pyspark_sql_functions,
)
from file_system_client import s3
from file_system_client.utilities import get_path_datetime_and_index

# In this example the source and target file systems are in different buckets
source_file_system: s3.S3 = s3.from_url(
    "s3://source-bucket-name/source/root/prefix/"
)
target_file_system: s3.S3 = s3.from_url(
    "s3://target-bucket-name/target/root/prefix/"
)
# Find the latest full extract
source_directory: str = source_file_system.get_latest_directory("/raw/full/")
# Read the latest extract into a data frame
source_url_pattern: str = (
    f"{source_file_system.get_url(source_directory)}*.parquet"
)
spark_session: SparkSession = (
    SparkSession.builder.enableHiveSupport().getOrCreate()
)
data_frame: DataFrame = spark_session.read.parquet(source_url_pattern)
# Eliminate duplicate primary keys
window: pyspark_sql.WindowSpec = pyspark_sql.Window.partitionBy(
    "PRIMARY_KEY_COLUMN_A", "PRIMARY_KEY_COLUMN_B", "PRIMARY_KEY_COLUMN_C"
).orderBy("COLUMN_D", "COLUMN_E", "COLUMN_F")
ranked_data_frame: DataFrame = data_frame.withColumn(
    "rank", pyspark_sql_functions.rank().over(window)
)
consolidated_data_frame: DataFrame = ranked_data_frame.filter(
    ranked_data_frame.rank == 1
).drop("rank")
# Write to a time-stamped directory in the target file system, using the
# time-stamp from the source file system
target_url: str = target_file_system.get_date_partition_directory(
    "/consolidated/full/",
    get_path_datetime_and_index(source_directory).datetime,
)
consolidated_data_frame.write.mode("overwrite").parquet(
    target_url, partitionBy=None
)
# Alternately, write to a time-stamped directory in the target file system,
# using the current date and time, offset as needed to ensure we don't
# overwrite existing files
target_url = target_file_system.get_unique_date_partition_directory(
    target_file_system.get_date_partition_directory("/consolidated/full/")
)
consolidated_data_frame.write.mode("overwrite").parquet(
    target_url, partitionBy=None
)
```

