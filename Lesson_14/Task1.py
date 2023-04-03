from functools import wraps

def logger(func):
    @wraps(func)
    def wrap(*args):
        arguments =''
        for a in args:
            arguments = arguments + str(a) + ', '
        arguments = arguments[:-2]
        print(f"{func.__name__} called with {arguments}")
        value = func(*args)
        return value
    return wrap

@logger
def add(x, y):
    return x + y

add(4, 5)

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

square_all(7, 5)



