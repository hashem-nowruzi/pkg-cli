from .commands import get_user_config
from setuptools import setup


if __name__ == '__main__':
    config = get_user_config()
    if config is not None:
        setup(**config)
