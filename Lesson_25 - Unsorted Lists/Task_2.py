from Task_1 import *


class Stack:
    def __init__(self):
        self._items = LinkedList()

    def push(self, data):
        self._items.append(data)

    def pop_(self):
        return  self._items.pop()

    def size(self):
        return  self._items.size()

    def __str__(self):
        return str(self._items)


a = Stack()

a.push(5)
a.push(20)
a.push(30)
print(a)
a.pop_()
print(a)