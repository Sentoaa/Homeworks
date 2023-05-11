from Task_1 import *

class Quequ:
    def __init__(self):
        self._items = LinkedList()

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return self._items.size()

    def __str__(self):
        return str(self._items)


a = Quequ()

a.enqueue(2)
a.enqueue(4)
a.enqueue(10)
print(a)
a.dequeue()
print(a)
