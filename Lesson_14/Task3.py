from functools import wraps

def arg_rules(type_: type, max_length: int, contains: list):
    def decorating_func(func):
        @wraps(func)
        def wrap(name):
            j = 0
            for i in contains:
                if i in name:
                    j += 1
            if type(name) != type_:
                print('The type of name is not str!')
                return False
            elif len(name) > max_length:
                print(f'The length of the name is more than max_length - {max_length}!')
                return False
            elif j != len(contains):
                print(f'The contains: {contains}, should be in the name!')
                return False
            else:
                return func(name)
        return wrap
    return decorating_func


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('S@SH05'))

assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

