import random
import string


class NumberPlates:
    """
    Number Plates

    a class to generate random number plates of the form LLL-NNN
    where LLL are letters A-Z and NNN are numbers 0-9

    """

    def __init__(self):
        self.plate = ""

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

        for count in range(3):
            characters.append(random.choice(list(letter_list)))
        characters.append("-")
        for count in range(3):
            characters.append(random.choice(list(number_list)))

        return ("".join(characters)).upper()


if __name__ == "__main__":
    number_plate = NumberPlates()
    plate = number_plate.create()
    print(plate)
    print()

    # create number plate instance
    number_plate = NumberPlates()
    # set up empty list of number plates
    plates = []
    # generate random starter number plate
    new_plate = number_plate.create()

    # generate a list of 100 random number plates
    for count in range(100):
        while new_plate in plates:
            new_plate = number_plate.create()
        plates.append(new_plate)

    # Show the number plates
    for counter in range(len(plates)):
        print(f"{plates[counter]:10s}", end="")

        # start new line every 10 number plates
        if ((counter + 1) % 10) == 0:
            print()
