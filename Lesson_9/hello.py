
'''def hello():
    print('Hello my friend')'''

'''def count_lines(file):
    with open(file) as file:
        lines = len(file.readlines())
        print(lines)

count_lines('legend.txt')

def count_chars(file):
    with open(file) as file:
        chars = file.read()
        print(count_chars(chars))
count_chars("legend.txt")'''

def count_lines(file):
    with open(file) as file:
        lines = len(file.readlines())
        print(lines)
# count_lines("My_text.txt")

def count_chars(file):
    with open(file) as file:
        chars = file.read()
        print(len(chars))
# count_chars("My_text.txt")

def test(file):
    with open(file) as f:
        count_lines(file)
        count_chars(file)
test("My_text.txt")
