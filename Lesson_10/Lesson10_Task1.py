#IndexError
def f():

    raise IndexError('Oops')


def f_f():
    try: f()
    except IndexError:
        print('IndexError - no longer exist')

f_f()

'''#KeyError
def f():

    raise KeyError('Oops')


def f_f():
    try: f()
    except IndexError:
        print('IndexError - no longer exist')

f_f()'''
