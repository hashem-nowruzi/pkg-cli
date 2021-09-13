from importlib.machinery import SourceFileLoader
from abc import ABC, abstractmethod
from argparse import ArgumentParser
from . import PROJECT_DIR, HERE
import subprocess
import sys


class BaseCommand(ABC):
    @abstractmethod
    def __init__(self, parser):
        self.parser: ArgumentParser = parser
        self.parser.set_defaults(func=self.execute)

    @abstractmethod
    def execute(self, args) -> None:
        pass

    @staticmethod
    def get_user_config():
        try:
            return SourceFileLoader('package', str(PROJECT_DIR / 'package.py')).load_module().config
        except FileNotFoundError:
            raise FileNotFoundError('The "package.py" file is not found!!')
        except AttributeError:
            raise AttributeError('The "package.py" file does not have a variable called "config"!!')

    @staticmethod
    def python(*args):
        command = [sys.executable]
        command.extend(args)
        subprocess.run(command)


class InitCommand(BaseCommand):
    def __init__(self, parser):
        super().__init__(parser)

    def execute(self, args) -> None:
        package_file = PROJECT_DIR / 'package.py'
        if package_file.exists() and package_file.is_file():
            print('Warning: This command could not be executed because the "package.py" file exists.')
        else:
            with open(f'{HERE}/templates/package.py', 'r') as file:
                package_file.write_text(file.read())


class PublishCommand(BaseCommand):
    def __init__(self, parser):
        super().__init__(parser)

    def execute(self, args) -> None:
        self.python('-m', 'pkg.setup', 'sdist')
        self.python('-m', 'twine', 'upload', 'dist/*')
