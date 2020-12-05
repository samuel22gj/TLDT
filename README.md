TL;DT
=====

> Too Long; Didn't Type

Do you maintain a note to collect a bunch of commands? And copy/paste when you want to use it?

`tldt` can help you collect commands that are long and difficult to remember. You can view all of these on command-line and enter the key you define for each command. `tldt` will execute it and show the execution time information for you!

![screenshot](screenshot.png)

Prerequisite
------------

Create a `.tldt.json` file and place in wherever you would like to execute(e.g., root path of a project ).

You can follow the example [.tldt.json](.tldt.json) file to create your own one or run `tldt --init` to create a sample.

```json5
{
  "configuration": {
    "sortByKey": true // whether sort action by key in ascending before displaying
  },
  "actions": [
    {
      "key": "1", // Shortcut key for the command
      "description": "Support argument and pipeline", // Describe the command
      "command": "sleep 2; ls -l | grep app" // Actually executed command
    },
    // other actions
  ]
}
```

Usage
-----

Create a sample `.tldt.json` file in the current directory

```
$ tldt --init
```

View all of commands on command-line:

```
$ tldt
```

Execute specific command directly

```
$ tldt [key]
```

Command Argument
----------------

```
usage: tldt [-h] [--version] [--no-time] [--init] [key]

Too Long; Didn't Type.

positional arguments:
  key             a key of the action

optional arguments:
  -h, --help      show this help message and exit
  --version, -v   show program's version number and exit
  --init          create a sample .tldt.json file in the current directory
  --no-time, -nt  don't show execution time information
```

Dependency
----------

- python3

Install
-------

### macOS

```
$ brew install samuel22gj/repo/tldt
```

### Manually

1. Download `tldt.py` from [latest release](https://github.com/samuel22gj/TLDT/releases/latest)
1. Run `chmod +x tldt.py`
1. Place it on your `$PATH`
1. Rename to `tldt` (remove filename extension `.py`)

License
-------

```
Copyright 2020 Samuel Huang

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
