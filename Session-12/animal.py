"""
Animal Class - the superclass for cat/dog

------------------------------------------------------------------------------
Project:   ICT40220-IntroP4RIoT-Notes
Folder:    Session-12
Filename:  animal.py
Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
Version:   0.0
------------------------------------------------------------------------------
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    def speak(self): ...
        # print(f"{self.name} speaks")


if __name__ == '__main__':
    raise NotImplementedError("This is a CLASS, no code executes")
