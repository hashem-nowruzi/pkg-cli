from pathlib import Path
from pkg import __version__

HERE = Path(__file__).parent

config = {
    'name': 'pkg-cli',
    'version': __version__,
    'packages': ['pkg'],
    'url': 'https://github.com/githashem/pkg-cli',

    'license': 'MIT',
    'description': 'Create Packages and Publish them to PyPi',
    'keywords': ['pypi', 'package', 'pkg-cli', 'pkg'],

    'author': 'Hashem',
    'author_email': 'PersonalHashem@gmail.com',

    'long_description': (HERE / 'README.md').read_text(),
    'long_description_content_type': 'text/markdown',

    'python_requires': '>=3.7',
    'entry_points': {
        'console_scripts': [
            'pkg = pkg.__main__:main',
        ],
    },
}
