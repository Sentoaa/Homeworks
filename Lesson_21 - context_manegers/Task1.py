# Створіть власний клас, який може поводитися як вбудована функція `open`.
# Також потрібно розширити його функціональність лічильником та логуванням.
# Зверніть особливу увагу на реалізацію методу `__exit__`, який повинен
# задовольняти усі вимоги до менеджерів контексту, що були наведені тут:
import json


class MyCounter:
    counter = 0

    def __init__(self, file_name, mode):
        self.file = open(file_name, mode)

    @classmethod
    def get_num_of_usage(cls):
        return cls.counter

    def __enter__(self):
        print('starting the magic')
        MyCounter.counter += 1
        with open('logs.txt', 'a') as file:
            file.write(f'The context manager get started: {self.counter} time(s)\n')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'It was cool, was"nt it?) see you next time. Number of contexts is {self.counter}')
        self.file.close()
        return None


# with MyCounter('Phonebook.json', 'r+') as file:
#     t = file.read()
#     b = 'hello'
#     json.dump(b, file)
#     print(t)

# with MyCounter('Phonebook.json', 'r') as file:
#     t = file.read()
#     print(t)

