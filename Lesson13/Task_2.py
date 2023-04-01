def f_1(x):
    def f_2():
        return x**3
    return f_2()

print(f_1(10))