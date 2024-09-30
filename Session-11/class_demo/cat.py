# Add a coat color attribute to the Cat class.
# Instantiate a Cat instance and print the name,
# age, and coat_color attributes.
#
# Add a purr method to the Cat class that
# prints <name> purrs. Call the purr method on
# the Cat instance.
#
# Define a class Dog that has a name and an age attribute.
# Instantiate a Dog instance and print the name
# and age attributes.
#
# Add a bark method to the Dog class that prints
# <name> barks.
# Call the bark method on the Dog instance.
# The dog instance's name will be "Woof", and aged 4


class Cat:
    def __init__(self, name, age):
        # constructor (initializer)
        self.name = name
        self.age = age

    def meow(self):
        print(f"{self.name} says 'Meow!'")


tabby = Cat("Whiskers", 2)
black = Cat("Dark", 7)

print(tabby.name)
print(black.age)

tabby.meow()
