# Створіть власну реалізацію вбудованої функції enumerate з назвою
# `with_index`, яка приймає два параметри: `iterable` і `start`, за
# замовчуванням 0. Підказки: дивіться документацію до функції enumerate

def with_index(iterable, start=0):
    for i in range(len(iterable)):
        yield start, iterable[i]
        start += 1

d = [1, 2, 3, 4, 5]

for i, v in with_index(d, start=100):
    print(f'index - {i} : value - {v}')
