from . import PROJECT_DIR
import functools


def package_json_file_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        package_file = PROJECT_DIR / 'package.json'
        if package_file.exists() and package_file.is_file():
            return func(*args, **kwargs)
        else:
            print('Error: The "package.json" file is required!!')
    return wrapper
