
class Dog:

    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        dog_to_human_age = self.age_factor * self.dog_age
        return f'The dog’s age in human equivalent: {dog_to_human_age}'

bard = Dog(2)

print(bard.human_age())


