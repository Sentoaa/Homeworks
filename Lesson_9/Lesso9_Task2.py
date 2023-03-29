'''sys.path можна змінити, можна повністю очистити,
якщо не буде прописаний шлях до модуля - видається помилка,
додаємо шлях - модуль імпортується'''

import sys
print(sys.path)
sys.path.clear()

print(sys.path)
#from mymod import*
sys.path.append('C:\\Users\\User\\PycharmProjects\\pythonProject\\Tasks\\Lesson_9')

print(sys.path)

from mymod import*

test('legend.txt')