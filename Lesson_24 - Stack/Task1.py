# Напишіть програму, яка зчитує послідовність символів і виводить
# їх у зворотному порядку, використовуючи вашу реалізацію стеку.

class Stack:
    def __init__(self):
        self._items = []

    def reversed_data(self):
        return self._items[::-1]

    def is_empty(self):
        return self._items == []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def to_see_top(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)



a = Stack()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
print(a)
print(a.reversed_data())