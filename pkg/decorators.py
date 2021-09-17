from . import PROJECT_DIR
import functools


def package_json_required(_func=None, *, required=True):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            package_file = PROJECT_DIR / 'package.json'
            if package_file.exists() and package_file.is_file():
                if required:
                    return func(*args, **kwargs)
                else:
                    print('Warning: The "package.json" file exists!!')
            else:
                if required:
                    print('Error: The "package.json" file is required!!')
                else:
                    return func(*args, **kwargs)

        return wrapper

    if _func is None:
        return decorator
    else:
        return decorator(_func)
