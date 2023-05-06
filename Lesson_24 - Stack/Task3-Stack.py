# Розширити стек, додавши до нього метод get_from_stack, який шукає і повертає елемент e зі стеку.
# Всі інші елементи повинні залишатися у стеку з дотриманням їх порядку. Розглянемо випадок, коли
# елемент не знайдено - згенеруємо ValueError з відповідним інформаційним повідомленням Message

class Stack:
    def __init__(self):
        self._items = []

    def reversed_data(self):
        return self._items[::-1]

    def is_empty(self):
        return self._items == []

    def push(self, item):
        self._items.append(item)

    def pop_(self):
        return self._items.pop()

    def to_see_top(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def get_from_stack(self, e):
        if e not in self._items:
            raise ValueError('there is no such element')
        for i in self._items:
            if i == e:
                __ = []
                while i != self._items[-1]:
                    _ = self._items.pop()
                    __.append(_)
                res = self._items.pop()
                for j in __[::-1]:
                    self._items.append(j)
                return res



a = Stack()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
print(a)
print(a.get_from_stack(1))
print(a)