"""
Die Class

Provides the core functionality for a die used in board games and D&D.

Author: Adrian Gould <adrian.gould@nmtafe.wa.edu.au>
"""

import random
from termcolor import colored



class Die:
    def __init__(self, sides=6,body_colour="black",text_colour="white"):
        """

        """
        self.sides = 6
        self.body_colour = body_colour.lower().strip()
        self.text_colour = text_colour.lower().strip()
        self.last_roll = None

    def get_colour(self) -> tuple:
        """

        Returns
        -------
        tuple: body_colour, text_colour
        """
        return self.body_colour, self.text_colour

    def roll(self):
        """

        Returns
        -------
        int:
        """
        sides = range(1, self.sides + 1)
        self.last_roll = random.choice(sides)

    def get_roll(self):
        return self.last_roll

    def __str__(self):
        body = "on_"+self.body_colour
        text = self.text_colour
        die = colored(f"{self.last_roll}",text, body)
        return die

if __name__ == "__main__":
    print("You are running the Die Class.")
    print("Please `import die` to use this class.")
