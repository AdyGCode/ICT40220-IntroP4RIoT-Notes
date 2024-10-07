"""
Demonstration of Inheritance II

Uses the Contact and Enhanced Contact classes to
demonstrate the OO Principle of Inheritance

------------------------------------------------------------------------------
Project:   ICT40220-IntroP4RIoT-Notes
Folder:    Session-12
Filename:  inheritance-demo-1.py
Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
Version:   0.0
------------------------------------------------------------------------------
"""

from cat import Cat, Dog
from animal import Animal

def demo():
    cat = Cat('Whiskers', 'black')
    cat.speak()  # speaks
    cat.purr()  # purrs

    dog = Dog("Rover")
    dog.speak()

    print(type(cat) is Cat)
    print(type(cat) is Animal)

    print(isinstance(cat, Cat))
    print(isinstance(cat, Animal))



def talk_to_the_animals(animal):
    print("hello, Animal")
    animal.speak()


if __name__ == '__main__':
    demo()
    cat2 = Cat("Raf", "green")
    dog2 = Dog("Woof")
    talk_to_the_animals(cat2)
    talk_to_the_animals(dog2)
