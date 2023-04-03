from functools import wraps


def stop_words(words: list):
    def decorating_func(func):
        @wraps(func)
        def wrap(name):
            text = func(name)
            for i in words:
                text = text.replace(i, '*')
            return text
        return wrap
    return decorating_func



@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("Steve"))


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"