class Mathematician:

    def square_nums(self, some_list: list):
        return [i**2 for i in some_list]

    def remove_positives(self, some_list: list):
        return list(filter(lambda i: i < 0, some_list))

    def filter_leaps(self, some_list: list):
        return list(filter(lambda i: i % 4 ==0 or i % 100 ==0 or i % 400 ==0, some_list))

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]