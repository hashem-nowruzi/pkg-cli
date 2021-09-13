from .commands import BaseCommand
from setuptools import setup


if __name__ == '__main__':
    config = BaseCommand.get_user_config()
    setup(**config)
