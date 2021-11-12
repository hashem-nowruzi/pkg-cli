from .decorators import setup_file_required
from configparser import ConfigParser
from .utils import python
from . import PROJECT_DIR
import pkg_resources


def init(args):
    config = ConfigParser()
    config['metadata'] = {
        'name': '<package_name>',
        'version': '0.1.0',
    }
    config['options'] = {
        'packages': 'find:'
    }

    file = PROJECT_DIR / 'setup.cfg'
    if file.exists() and file.is_file():
        print('Warning: The "setup.cfg" file exists!!')
        return

    with open(str(file), 'w') as outfile:
        config.write(outfile)

    if not (PROJECT_DIR / 'setup.py').exists():
        (PROJECT_DIR / 'setup.py').touch()
        (PROJECT_DIR / 'setup.py').write_text('from setuptools import setup\n\nsetup()\n')


@setup_file_required
def build(args):
    python('-m', 'build')


@setup_file_required
def publish(args):
    python('-m', 'build')
    python('-m', 'twine', 'upload', 'dist/*')


def freeze(args):
    packages_set = set()
    requires_set = set()
    for package in pkg_resources.working_set:
        packages_set.add(package.key)
        for require in package.requires():
            requires_set.add(require.key)

    packages_output = sorted(packages_set - requires_set)
    for i, package_name in enumerate(packages_output):
        package_version = pkg_resources.get_distribution(package_name).version
        packages_output[i] = f"{package_name}=={package_version}"

    print("\n".join(packages_output))
