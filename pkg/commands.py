from abc import ABC, abstractmethod
from . import PROJECT_DIR


class BaseCommand(ABC):
    def __init__(self, argv):
        self.argv = argv

    @abstractmethod
    def execute(self) -> None:
        pass


class InitCommand(BaseCommand):
    def execute(self) -> None:
        (PROJECT_DIR / 'package.py').touch(exist_ok=True)
