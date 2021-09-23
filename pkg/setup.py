from setuptools import setup
from . import CONFIG


if __name__ == '__main__':
    if CONFIG is not None:
        setup(**CONFIG)
