# class Reverse:
#
#     def __init__(self, iter_obj):
#         self.iter_obj = iter_obj
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == len(self.iter_obj):
#             raise StopIteration
#         else:
#             self.index += 1
#             return self.iter_obj[self.index-1]
#
# a = 'qwerty'
#
# b = Reverse(a)
# print(type(b))
# for i in b:
#     print(i, end=' ')

a = 'qwerty'

def rev(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i]



