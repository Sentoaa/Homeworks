# class Person:
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#
#
#     @property
#     def ful_name(self):
#         return self.first_name.title() + ' ' + self.last_name.title()
#
#     @property
#     def get_initials(self):
#         return self.first_name[0].upper() + ' ' + self.last_name[0].upper()
#
#     @ful_name.setter
#     def ful_name(self, new_ful_name):
#         first_name, last_name = new_ful_name.split(' ')
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#
#     @ful_name.deleter
#     def ful_name(self):
#         self.first_name = 0
#         self.last_name = 0
#         print('Del')
#
#
# a = Person('alex', 'marks')
# a.first_name = 'bro'
# a.last_name = 'dro'
# a.ful_name = 'kjh kjh'
# print(a.ful_name)
#
# a.first_name = 'mack'
#
# print(a.ful_name)
# print(a.first_name)
#
# a.ful_name = 'dereck doe'
# print(a.first_name)
# print(a.last_name)


# print(a.ful_name)
# del a.ful_name
# print(a.first_name, a.last_name)
#
# print(a.__dict__)
#
# print(a.__class__)

# from datetime import date
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # a class method to create a Person object by birth year.
#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)
#
#     # a static method to check if a Person is adult or not.
#     @staticmethod
#     def isAdult(age):
#         return age >= 18
#
#
# person1 = Person('mayank', 18)
# person2 = Person.fromBirthYear('mayank', 2020)
#
# print(person1.age)
# print(person2.age)
#
# # print the result
# print(Person.isAdult(18))

# Дана функція send_secure_information, яка приймає словник user, вона повідомляє користувачу
# деяку секретну інформацію.
# Напиши декоратор admin_required, який перевіряє атрибут user'a 'is_admin' і якщо він False -
# виводить повідомлення з забороною, як показано у прикладі.
# Приклад:
# @admin_required
# def send_secure_information(user: dict) -> None:
#     print(f"{user['name']}, site's secure code is 'SecUR43Esit78Eco90DE'")
#     send_secure_information({'name': 'Administrator', 'is_admin': True})
# # Administrator, site's secure code is 'SecUR43Esit78Eco90DE'
#     send_secure_information({'name': 'User1234', 'is_admin': False})
# # You are not allowed to see this information!

# from typing import Callable
#
# def admin_required(func: Callable):
#     # write your code here
#     def wrapper(user):
#        if user['is_admin'] == True:
#             return func((user))
#        print('You are not allowed to see this information!')
#     return wrapper
#
# @admin_required
# def send_secure_information(user: dict) -> None:
#     print(f"{user['name']}, site's secure code is 'SecUR43Esit78Eco90DE'")
#
# send_secure_information({'name': 'Administrator', 'is_admin': False})


# Створити клас клієнта банку, який приймає атрибути:
# ПІБ
# баланс рахунку (захищений атрибут)
# Реалізувати методи (звичайні, не property), які б дозволили:
# отримувати баланс
# присвоювати баланс
# видаляти атрибут баланс
# Створити екземпляр класу, відпрацювати всі методи.

# class Client:
#
#     def __init__(self, pib, balance):
#         self.pib = pib
#         self.__balance = balance
#
#     def get_balance(self):
#         print('getter')
#         return self.__balance
#
#     def set_balance(self, new_balance):
#         print('setter')
#         self.__balance = new_balance
#
#     def del_balance(self):
#         print('del')
#         del self.__balance
#
# a = Client('Alex', 1000)
#
# print(a.get_balance())
# a.set_balance(1500)
# print(a.get_balance())
# a.del_balance()
# print(a.get_balance())

#  Створити клас Авто, приймає атрибути:
# Марка авто
# Модель авто
# Пробіг
# Вартість (приватний атрибут)
# Реалізувати методи (для атрибуту „вартість“) через синтаксис (my_property = property(getx, setx, delx, "I'm the 'x' property.")
# Створити екземпляр класу,
# відпрацювати всі методи,
# викликати стрічку документації.

# class Auto:
#
#     def __init__(self, brand, model, miliage, cost):
#
#         self.brand = brand
#         self.model = model
#         self.miliage = miliage
#         self._cost = cost
#
#     def get_cost(self):
#         print('getter')
#         return self._cost
#
#     def set_cost(self, new_cost):
#         print('setter')
#         self._cost = new_cost
#
#     def del_cost(self):
#         print('del')
#         del self._cost
#
#     cost = property(get_cost, set_cost, del_cost, "I'm OK")
#
# a = Auto('BMW', 'X5', 50000, 15000)
#
# print(a.cost)
# a.cost = 12000
# print(Auto.cost.__doc__)

# Скопіювати рішення для задачі 2, переробити таким чином, щоб для
# геттера, сеттера та делітера використовувалось одне і те ж ім“я.

# class Auto:
#
#     def __init__(self, brand, model, miliage, cost):
#
#         self.brand = brand
#         self.model = model
#         self.miliage = miliage
#         self._cost = cost
#
#     @property
#     def get_cost(self):
#         print('getter')
#         return self._cost
#
#     @get_cost.setter
#     def get_cost(self, new_cost):
#         print('setter')
#         self._cost = new_cost
#
#     @get_cost.deleter
#     def get_cost(self):
#         print('del')
#         del self._cost
#
# a = Auto('BMW', 'X5', 50000, 15000)
#
# print(a.get_cost)
# a.get_cost = 11000
# print(a.get_cost)
# del a.get_cost
# print(a.get_cost)

# Задача 4.
# Ваш клас з задачі 1 почав використовуватись програмістами, що працюють в банку.
# В процесі роботи виявилось, що в ПІБ записуються не коректні дані. Прогнозувалось,
# що ПІБ – це стрінг, в якому знаходяться 3 слова, розділені пробілами, кожне - з великої букви.
# На практиці – туди інколи скидається різна «каша», типу «Петренко В.В», «кум Петро»,
# «Бульба С. – голова колгоспу» і т.д. і т.п.
# Ваша задача – зробити з ПІБ властивість (property), з відповідними операціями (гетер, сетер, делітер),
# для сетера виконати необхідні перевірки, інакше – викидати виключення з описом помилки.

# class Client:
#
#     def __init__(self, pib, balance):
#         self._pib = ''
#         self.pib = pib
#         self.__balance = balance
#
#     @property
#     def pib(self):
#         print('getter')
#         return self._pib
#
#     @pib.setter
#     def pib(self, new_pib):
#         tmp = new_pib.split(' ')
#         if len(tmp) != 3:
#             raise ValueError('wrong PIB format')
#         for i in tmp:
#             if i != i.capitalize():
#                 raise ValueError(f'wrong PIB format also, {i}')
#         print('setter')
#         self._pib = new_pib
#
#     @pib.deleter
#     def pib(self):
#         print('del')
#         del self._pib
#
# a = Client('Alex Fon World', 1000)
#
# print(a.pib)
#
# a.pib = 'Alex fon World'
#
# print(a.pib)

# Задача 5.
# Реалізувати додавання декількох чисел (к-сть від 1 до 10), як статичний метод.
# Принтити результат: перелік доданків, і суму

# class MyMath:
#
#     @staticmethod
#     def my_sum(*args):
#         if 10 > len(args) > 0:
#             print(f'{args}, {sum(args)}')
#         else:
#             raise ValueError
#
#
# MyMath.my_sum(1, 2, 3, 4, 5, 1, 5)

# Задача 6.
# Для задачі 1 додати атрибут класу number=0, і інкрементувати
# його при створенні кожного екземпляра клієнта.
# Реалізувати вивід (прінт) даного атрибуту , як метод класу.

class Client:
    number = 0

    def __init__(self, pib, balance):
        self._pib = ''
        self.pib = pib
        self.__balance = balance
        Client.number += 1

    @property
    def pib(self):
        print('getter')
        return self._pib

    @pib.setter
    def pib(self, new_pib):
        tmp = new_pib.split(' ')
        if len(tmp) != 3:
            raise ValueError('wrong PIB format')
        for i in tmp:
            if i != i.capitalize():
                raise ValueError(f'wrong PIB format also, {i}')
        print('setter')
        self._pib = new_pib

    @pib.deleter
    def pib(self):
        print('del')
        del self._pib

    @classmethod
    def get_number(cls):
        print(cls.number)

a = Client('Alex Fon World', 1000)
b = Client('Alex Fon World', 1000)
c = Client('Alex Fon World', 1000)
d = Client('Alex Fon World', 1000)

Client.get_number()
