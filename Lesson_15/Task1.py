
class Person:

    def __init__(self, name, s_name, age):
        self.name = name
        self.s_name = s_name
        self.age = age

    def talk(self):
        print(f'Hello, my name is {self.name} {self.s_name} and I am {self.age}')

some_person = Person('Karl', 'Johnson', 26)

some_person.talk()
