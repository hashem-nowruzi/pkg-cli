from .commands import BaseCommand
from setuptools import setup

config = BaseCommand.get_user_config()

setup(**config)
