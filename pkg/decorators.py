from . import PROJECT_DIR
import functools


def setup_file_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        file = PROJECT_DIR / 'setup.cfg'
        if file.exists() and file.is_file():
            return func(*args, **kwargs)
        else:
            print('Error: The "setup.cfg" file is required!!')
    return wrapper
