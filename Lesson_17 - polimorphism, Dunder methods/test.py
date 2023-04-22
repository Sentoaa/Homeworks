# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def activity(self):
#         raise NotImplementedError ('onnely for subclasses ')
#
#     def activity_and_title(self):
#         return f'{self.name}: {self.activity()}'
#
# class PresUkraine(Person):
#
#     def activity(self):
#         return 'зараз – красавчег'
#
#     def activity_and_title(self):
#         return f'{self.name}: {self.activity()}'
#
# class HolovnokomUkraine(Person):
#
#     def activity(self):
#         return 'фахівець по створенню котлів'
#
#     def activity_and_title(self):
#         return f'{self.name}: {self.activity()}'
#
# class Gandon(Person):
#
#     def activity(self):
#         return 'Politico: невдаха року'
#
#     def activity_and_title(self):
#         return f'{self.name}: {self.activity()}'
#
# my_list =[PresUkraine('Zelensky'), HolovnokomUkraine('Zaluzhny'), Gandon('putin')]
#
# for i in my_list:
#     print(i.activity_and_title())


# import turtle as t
#
# class MyPolygon:
#
#     def __init__(self, n):
#         self.n = n
#
#     def draw(self):
#         for _ in range(self.n):
#             t.forward(100)
#             t.right(360 / self.n)
#         t.done()
#
#
# a = MyPolygon(10)
#
# a.draw()
#
# class Detail:
#     def __init__(self, name, cost):
#         self.name = name
#         self.cost = cost
#
#     def __add__(self, other):
#         if not isinstance(other, Detail):
#             raise TypeError('the instances should be the same class')
#         return Detail(self.name, self.cost + other.cost)
#     def __str__(self):
#         return f"{self.name} {self.cost}"
#
# a = Detail('Wheel', 100)
#
# b = Detail('Wheel', 250)
#
# c = a + b
#
# print(c.name, c.cost)
# print(a)
class Client:

    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def client_info(self):
        return f'{self.name}, {self.date_of_birth}'

    def __str__(self):
        return f'{self.name}, {self.date_of_birth}'


class __Account:

    __account = 0

    def __init__(self, client, balance):
        # self.instance = instance
        self.client = client
        self.__balance = balance
    def __str__(self):
        return f'{self.client}, account: {self.__account}'

    def __change_count(self, amount):
        self.amount = amount
        self.__account += self.amount
        return self.__account

    def show_count(self):
        return self.__account

class GoldAccount(__Account):

    __account = 0

    def _change_count(self, amount):
        self.amount = amount
        self.__account = self.__account + self.amount
        return self.__account

    def _show_count(self):
        return self.__account



a = Client('Oleksii', '30.04.1991')

b = __Account(a, 100)

c = GoldAccount(a, 200)


b._Account__account = 10
print(b._Account__account)

b._Account__change_count(500)

# print(a.client_info())
# b._Account__change_count(+100)
# print(b)
# print(c._show_count())
# c._change_count(1000)
# print(c._show_count())
# print(b.client)





