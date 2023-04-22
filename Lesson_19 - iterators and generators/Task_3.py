class Iter_obj:

    def __init__(self, data):
        self.data = data
        self.ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind < len(self.data):
            self.ind += 1
            return self.data[self.ind - 1]
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        count = 0
        for _ in self.data:
            count += 1
        return count


a = [1, 2, 3, 4, 5]

for i in Iter_obj(a):
    print(i, end='')

print()
b = Iter_obj(a)
print(b[4])
print(len(b))