class Dog:
    # Class attribute
    species = 'Canis familiaris'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def speak(self, sound):
        return f'{self.name} says {sound}'

    # Special instance method
    def __str__(self):
        return f'{self.name} is {self.age} years old'

# self is an instance that this class creates
# self.name and self.age are instance attributes

billy = Dog('Billy', 4)
jimmy = Dog('Jimmy', 9)

billy.name
# 'Billy'

jimmy.age
# 9

billy.species
# 'Canis familiaris'
# access to the class attribute

billy.age = 6
jimmy.species = 'Husky'
# change the attributes

print(jimmy.speak('woof-woof'))

print(billy)
# run the __str__ method
# Billy is 6 years old


# Inheritance

class Dachshund(Dog):
    def speak(self, sound="Arf-arf"):
        return super().speak(sound)
# super() is an access to the parent class

class Bulldog(Dog):
    def speak(self, sound="Arf"):
        return f'{self.name} says {sound}'

chappy = Bulldog('Chappy', 8)

isinstance(chappy, Dog)
# True
# checks the inheritance from the class

isinstance(chappy, Dachshund)
# False

print(chappy.speak())
print(chappy.speak('afafaafafafafaf'))
