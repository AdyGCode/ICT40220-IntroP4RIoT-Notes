"""
Cat Class used for demonstrating inheritance

------------------------------------------------------------------------------
Project:   ICT40220-IntroP4RIoT-Notes
Folder:    Session-12
Filename:  cat.py
Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
Version:   0.0
------------------------------------------------------------------------------
"""

from animal import Animal


class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")


class Cat(Animal):
    def __init__(self, name, colour):
        # Override the Animal.__init__
        # Use the super() method to execute the Animal.__init__
        # super().__init__(name)
        self._name = None
        self.set_name(name)
        self.colour = colour

    def speak(self):
        # Override the Animal.speak method
        print(f"{self.get_name()} meows")

    def purr(self):
        print(f"{self.get_name()} purrs")

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


if __name__ == '__main__':
    raise NotImplementedError("This is a CLASS, no code executes")
