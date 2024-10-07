"""
Pen Class

------------------------------------------------------------------------------
Project:   ICT40220-IntroP4RIoT-Notes
Folder:    Session-12
Filename:  pen.py
Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
Version:   0.0
------------------------------------------------------------------------------
"""


class Pen:

    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def write(self, message):
        print(f"{self.name} writes in {self.colour}: {message}")


if __name__ == '__main__':
    print("This is the Pen Class... nothing to execute here")
