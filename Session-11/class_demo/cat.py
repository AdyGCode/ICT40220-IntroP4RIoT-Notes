"""
It's raining Cats & Dogs

Demo of (Simple) Classes in Python
"""


class Cat:
    def __init__(self, name, age):
        # constructor (initializer)
        self.name = name
        self.age = age

    def meow(self):
        print(f"{self.name} says 'Meow!'")


class Dog:
    ...


tabby = Cat("Whiskers", 2)
black = Cat("Dark", 7)

print(tabby.name)
print(black.age)

tabby.meow()
