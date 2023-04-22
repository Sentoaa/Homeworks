from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_res = func(*args, **kwargs)
            try:
                return int(func_res)
            except ValueError:
                return func_res
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_res = func(*args, **kwargs)
            try:
                return int(func_res)
            except ValueError:
                return func_res
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_res = func(*args, **kwargs)
            try:
                return float(func_res)
            except ValueError:
                return func_res
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_res = func(*args, **kwargs)
            return bool(func_res)
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True