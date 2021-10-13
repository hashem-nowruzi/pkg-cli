[![pypi version]](https://pypi.org/project/pkg-cli/)
[![pypi license]](https://github.com/githashem/pkg-cli/blob/main/LICENSE)

## What is pkg-cli?
>pkg-cli is a command-line tool for Making a Python package that is configured with the standard **'package.json'** file.

## Installation
Windows
```shell
py -m venv venv
venv\Scripts\activate
py -m pip install pkg-cli
```

Linux/unix/macOS
```shell
python3 -m venv venv
source venv/bin/activate
python3 -m pip install pkg-cli
```

## Usage
Create a 'setup.cfg' file
```shell
pkg init
```

Publish package to PyPi
```shell
pkg publish
```

<!-- MarkDown Links -->
[pypi version]: https://img.shields.io/pypi/v/pkg-cli?color=blue&style=flat-square
[pypi license]: https://img.shields.io/pypi/l/pkg-cli?color=blue&style=flat-square
