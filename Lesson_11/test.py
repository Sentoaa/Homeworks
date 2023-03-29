'''with open('info.txt', 'w') as a:
    a.write('Hello Hello')
    a.close()

with open('info.txt') as b:
    b1 = b.read()
    print('Whot can you say to me? ' + b1)'''
'''import json
d ={}
d['car'] = 'Beep'
d['heir'] = 'white'

with open ('', 'w') as file:
    json.dump(d, file)
with open('') as file_1:
    q = json.load(file_1)
    print(q)'''

''''with open('info.txt', 'a') as f:
        f.write(' Hello friend')
        f.seek(0)
        print(b)'''

with open("foo.txt", "w+") as file:
    file.write('qwerty\nqwerty')
    print(file.tell())
    file.seek(0)
    b = file.read(1000)
    print(b)



