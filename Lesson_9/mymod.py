def count_lines(name):
    #for unlocking of using function by itself get rid of '#' in lines 3 - 5 also put the '#' in lines 6 and 7
    #q = open(name, 'r')
    #print('The number of lines in file: ', len(q.readlines()))
    #q.close()
    name.seek(0)
    print('The number of lines in file: ', len(name.readlines()))

#count_lines('legend.txt')

def count_chars(name):
    # for unlocking of using function by itself get rid of '#' in lines 13 - 15 also put the '#' in lines 16 and 17
    #w = open(name, 'r')
    #print('The number of characters in file: ', len(w.read()))
    #w.close()
    name.seek(0)
    print('The number of characters in file: ', len(name.read()))


def test(name):
    f = open(name, 'r')
    count_lines(f)
    count_chars(f)
    f.close()

test('mymod.py')