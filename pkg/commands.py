from .decorators import package_json_required
from abc import ABC, abstractmethod
from argparse import ArgumentParser
from . import PROJECT_DIR
import subprocess
import json
import sys


class BaseCommand(ABC):
    def __init__(self, parser: ArgumentParser):
        self.parser = parser
        self.parser.set_defaults(func=self.execute)

    @abstractmethod
    def execute(self, args) -> None:
        pass

    @staticmethod
    def get_user_config():
        try:
            with open(f'{PROJECT_DIR}/package.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print('Error: The "package.json" file is not found!!')

    @staticmethod
    def python(*args):
        command = [sys.executable]
        command.extend(args)
        subprocess.run(command)


class InitCommand(BaseCommand):
    def execute(self, args) -> None:
        config = {"name": "<package_name>", "version": "0.1.0", "packages": []}

        package_file = PROJECT_DIR / 'package.json'
        if package_file.exists() and package_file.is_file():
            print('Warning: The "package.json" file exists!!')
        else:
            with open(str(package_file), 'w') as outfile:
                json.dump(config, outfile, indent=4)


class PublishCommand(BaseCommand):
    @package_json_required
    def execute(self, args) -> None:
        self.python('-m', 'pkg.setup', 'sdist')
        self.python('-m', 'twine', 'upload', 'dist/*')
