# Напишіть програму, яка зчитує послідовність символів і визначає,
# чи є дужки, фігурні дужки та дужки "збалансованими".

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

    def is_balanced_brackets(self):
        res = []
        for i in self._items:
            if i == '(' or i == '{' or i == '[':
                res.append(i)
            if i == ')' or i == '}' or i == ']':
                if not res:
                    return False
                elif i == ')' and res[-1] == '(':
                    res.pop()
                elif i == '}' and res[-1] == '{':
                    res.pop()
                elif i == ']' and res[-1] == '[':
                    res.pop()
                else:
                    return False
        return not res

    def __str__(self):
        return str(self._items)

a = Stack()
a.push('(')
a.push(')')
a.push('1')
a.push('1')
a.push('1')
print(a)
print(a.is_balanced_brackets())