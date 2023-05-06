# Розширити чергу, додавши до неї метод get_from_stack, який шукає і повертає елемент e з черги.
# Всі інші елементи повинні залишатися у черзі з дотриманням їх порядку. Розглянемо випадок, коли
# елемент не знайдено - згенеруємо ValueError з відповідним інформаційним повідомленням Message

class Quequ:
    def __init__(self):
        self._items = []

    def reversed_data(self):
        return self._items[::-1]

    def is_empty(self):
        return self._items == []

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def get_from_quequ(self, e):
        if e not in self._items:
            raise ValueError('there is no such element')
        for i in self._items:
            if i == e:
                __ = []
                while i != self._items[-1]:
                    _ = self._items.pop()
                    __.insert(0, _)
                res = self._items.pop()
                for j in __:
                    self._items.append(j)
                return res



a = Quequ()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
a.enqueue(5)
print(a)
print(a.get_from_quequ(5))
print(a)