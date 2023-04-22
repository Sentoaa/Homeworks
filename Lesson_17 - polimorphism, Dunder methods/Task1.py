class Animal:

    def talk(self):
        raise NotImplementedError ('only for the sub classes')

class Dog(Animal):

    def talk(self):
        return 'Woof'

class Cat(Animal):

    def talk(self):
        return 'Meow'

def go_talk(obj):
    return obj.talk()

a = Cat()
b = Dog()

print(go_talk(a))
print(go_talk(b))