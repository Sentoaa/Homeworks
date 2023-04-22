# Створіть власну реалізацію вбудованої функції range, назвавши її in_range(),
# яка приймає три параметри: `start`, `end` і необов'язковий крок. Підказки:
# Зверніться до документації до функції `range`.

def in_range(start, end, step = 1):
     if start < end:
        while start < end:
            yield start
            start += step
     else:
         while start > end:
            yield start
            start -= step



for i in in_range(10,1):
    print(i, end=' ')

print()

for i in in_range(1,10):
    print(i, end=' ')


