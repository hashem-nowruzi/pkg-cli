from abc import ABC, abstractmethod
from argparse import ArgumentParser
from . import PROJECT_DIR, HERE


class BaseCommand(ABC):
    @abstractmethod
    def __init__(self, parser):
        self.parser: ArgumentParser = parser
        self.parser.set_defaults(func=self.execute)

    @abstractmethod
    def execute(self, args) -> None:
        pass


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
