
class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def intro(self):
        print(f'Hello, my name {self.name}, I am {self.age} years old.')

class Student(Person):

    def __init__(self, name, age, gender, stud_year, subject):
        super().__init__(name, age, gender)
        self.stud_year = stud_year
        self.subject = subject

    def intro(self):
        print(f'Hello, my name {self.name}, I am a {self.stud_year} cors student. My subject is {self.subject}')

    def __repr__(self):
        return self.name + ', ' + str(self.age) + ', ' + self.gender + ', ' + str(self.stud_year) + ', ' + self.subject

class Teacher(Person):

    def __init__(self, name, age, gender, category, salary):
        super().__init__(name, age, gender)
        self.category = category
        self.salary = salary

    def __repr__(self):
        return self.name + ', ' + str(self.age) + ', ' + self.gender + ', ' + str(self.category) + ', ' + str(self.salary)

sam = Teacher('Sam', 32, 'mail', 1, 3000)

print(sam.__repr__())
sam.intro()

alex = Student('Alex', 20, 'mail', 2, 'history')

alex.intro()

print(alex.__repr__())