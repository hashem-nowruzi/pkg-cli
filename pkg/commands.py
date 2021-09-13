from abc import ABC, abstractmethod
from argparse import ArgumentParser
from . import PROJECT_DIR


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
        (PROJECT_DIR / 'package.py').touch(exist_ok=True)
