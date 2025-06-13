import random
import string


class NumberPlates:
    """
    Number Plates

    a class to generate random number plates of the form LLL-NNN
    where LLL are letters A-Z and NNN are numbers 0-9

    """

    def __init__(self, letter_count=3, number_count=3, separator="-"):
        """
        Instantiate the NumberPlate class

        Parameters
        ----------
        letter_count : int : number of letters on plate
        number_count : int : number of numbers on plate
        separator : string : character to place between letters and numbers

        """
        self.letter_count = letter_count
        self.number_count = number_count
        self.separator = separator

    def create(self):
        """
        Create a number plate from the letters of the alphabet and numbers 0-9

        Returns
        -------
        string: string of form LLL-NNN - e.g. ABC-098

        Example Usage
        -------------
        number_plate = NumberPlates()
        plate = number_plate.create()

        """
        characters = []
        letter_list = list(string.ascii_lowercase)
        number_list = list(string.digits)

        for count in range(self.letter_count):
            characters.append(random.choice(list(letter_list)))
        characters.append(self.separator)
        for count in range(self.number_count):
            characters.append(random.choice(list(number_list)))

        return ("".join(characters)).upper()
