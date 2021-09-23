from .decorators import package_json_file_required
from .utils import python
from . import PROJECT_DIR
import json


def init(args):
    config = {"name": "<package_name>", "version": "0.1.0", "packages": []}
    package_file = PROJECT_DIR / 'package.json'
    if package_file.exists() and package_file.is_file():
        print('Warning: The "package.json" file exists!!')
    else:
        with open(str(package_file), 'w') as outfile:
            json.dump(config, outfile, indent=4)


@package_json_file_required
def publish(args):
    python('-m', 'pkg.setup', 'sdist')
    python('-m', 'twine', 'upload', 'dist/*')
