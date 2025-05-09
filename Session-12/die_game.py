"""
Die Rolling

Demonstrates the Die class

Author: Adrian Gould <adrian.gould@nmtafe.wa.edu.au>

"""

# Imports
from die import Die

# Constants
TIME_TO_ROLL = 2

# Global variables
dice_colours = [
    ("black", "white"),
    ("dark_grey", "black"),
    ("light_grey", "black"),
    ("light_red", "black"),
    ("red", "black"),
    ("light_magenta", "black"),
    ("magenta", "black"),
    ("blue", "black"),
    ("light_blue", "black"),
    ("cyan", "black"),
    ("light_cyan", "black"),
    ("light_green", "black"),
    ("green", "black"),
    ("yellow", "black"),
    ("light_yellow", "black"),
    ("white", "black"),
]
total_dice = len(dice_colours)
number_dice = total_dice

dice = []
for dice_number in range(number_dice):
    body, face = dice_colours[dice_number]
    dice.append(Die(6, body, face))

# Main program


def main():

    print(f"Rolling {number_dice} dice, 5 times...")
    print()
    for roll in range(1, 5):
        for die in dice:
            die.roll()

        for die in dice:
            print(die, end=" ")
        print()


if __name__ == "__main__":
    main()
