"""
Recap Session - OOP and Modules

------------------------------------------------------------------------------
Project:   ICT40220-IntroP4RIoT-Notes
Folder:    Session-12
Filename:  recap-example-1.py
Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
Version:   0.0
------------------------------------------------------------------------------
"""

from pen import Pen

def demo():
    my_first_pen = Pen("Staedtler Triplus 0.45mm", "blue")
    my_second_pen = Pen("Staedtler Triplus 0.45mm", "red")

    my_first_pen.write("Hello there, everyone")
    my_second_pen.write("Hope this makes sense")

    print(my_first_pen.name)
    print(my_second_pen.colour)


if __name__ == '__main__':
    demo()
