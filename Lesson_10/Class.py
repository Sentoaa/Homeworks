'''v = [0,1,2]
def test():
    try:
        v[5]
    except ZeroDivisionError:
        return print('/0 not work')
    finally:
        print('All is Ok')

test()'''