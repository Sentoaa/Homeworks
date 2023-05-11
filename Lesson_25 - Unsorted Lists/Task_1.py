class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.index = -1

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.index += 1
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        self.index += 1

    def __str__(self):
        res = []
        current_node = self.head
        while current_node:
            res.append(current_node.data)
            current_node = current_node.next
        return str(res)

    def find(self, elem):
        current = self.head
        while current is not None:
            if current.data == elem:
                return True
            current = current.next
        return False

    def remove(self, elem):
        current = self.head
        previos = None
        while current is not None:
            if current.data == elem:
                previos.next = current.next
                print(elem, 'removed')
                return
            previos = current
            current = current.next
        print(elem, 'not removed')

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def pop(self, pos=None):
        if pos is None:
            pos = self.size() - 1
        if pos == 0:
            data = self.head.data
            self.head = self.head.next
            return data
        current = self.head
        previous = None
        i = 0
        while current is not None and i < pos:
            previous = current
            current = current.next
            i += 1
        if current is None:
            raise IndexError("pop index out of range")
        data = current.data
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        return data

    def find_ind(self, data):
        current = self.head
        index = 0
        while current is not None:
            if current.data == data:
                return index
            index += 1
            current = current.next
        return 'There is no such element'

    def insert(self, index, data):
        node = Node(data)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            if index > self.index:
                index = self.index
            i = 0
            current_node = self.head
            previous_node = None
            while current_node is not None and i < index:
                previous_node = current_node
                current_node = current_node.next
                i += 1
            node.next = current_node
            previous_node.next = node
            self.index += 1

    def slice(self, start, stop):
        if start < 0:
            start = self.size() + start
        if stop < 0:
            stop = self.size() + stop
        if start < 0 or start >= self.size():
            raise IndexError("slice start index out of range")
        if stop < start or stop > self.size():
            raise IndexError("slice stop index out of range")
        result = LinkedList()
        current = self.head
        i = 0
        while current is not None and i < stop:
            if i >= start:
                result.append(current.data)
            current = current.next
            i += 1
        return result


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append("2")
    linked_list.append("Stas")
    print(linked_list)
    linked_list.pop()
    print(linked_list)
    linked_list.insert(0, 5)
    print(linked_list)
    new_list = linked_list.slice(0,2)
    print(linked_list)
    new_list.add(1)
    print(linked_list)


