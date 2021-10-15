from .decorators import setup_file_required
from configparser import ConfigParser
from .utils import python
from . import PROJECT_DIR


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


@setup_file_required
def publish(args):
    python('-m', 'build')
    python('-m', 'twine', 'upload', 'dist/*')
