#import inspect

my_list = [1, 2, 3, 4, 5]

def my_f(some_list):
    a = 1
    b = 2
    d = sum(some_list)+a+b
    return d

def count_values(func):
    vel = func.__code__.co_nlocals - func.__code__.co_argcount
    print(f'The number of the local values of the function - {func.__name__}: {vel}')

count_values(my_f)


