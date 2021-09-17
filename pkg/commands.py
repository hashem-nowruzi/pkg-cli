from abc import ABC, abstractmethod
from argparse import ArgumentParser
from . import PROJECT_DIR, HERE
import subprocess
import json
import sys


class BaseCommand(ABC):
    def __init__(self, parser):
        self.parser: ArgumentParser = parser
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
        package_file = PROJECT_DIR / 'package.json'
        if package_file.exists() and package_file.is_file():
            print('Warning: This command could not be executed because the "package.json" file exists.')
        else:
            with open(f'{HERE}/package.json', 'r') as file:
                config = json.load(file)

            with open(f'{PROJECT_DIR}/package.json', 'w') as outfile:
                json.dump(config, outfile, indent=4)


class PublishCommand(BaseCommand):
    def execute(self, args) -> None:
        if (PROJECT_DIR / 'package.json').exists() and (PROJECT_DIR / 'package.json').is_file():
            self.python('-m', 'pkg.setup', 'sdist')
            self.python('-m', 'twine', 'upload', 'dist/*')
