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


class Cat(Animal):
    def purr(self):
        print(f"{self.name} purrs")


if __name__ == '__main__':
    raise NotImplementedError("This is a CLASS, no code executes")
