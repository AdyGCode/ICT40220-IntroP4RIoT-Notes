# Write a function that calculates the sum of two numbers
# Call it add or add2, not sum (that is a built-in function)
# Include a docstring!
class Calculations:
    def add(self, first_number, second_number):
        """
        Adds two numbers together

        Parameters
        ----------
        first_number : int | float | complex
        second_number : int | float | complex

        Returns
        -------
        int | float | complex
        """

        if type(first_number) not in [int, float, complex]:
            raise ValueError("First argument must be an integer or float")

        if type(second_number) not in [int, float, complex]:
            raise ValueError("Second argument must be an integer or float")

        return first_number + second_number


# Write the unit tests that check:
# that correct values are calculated for integer, floating point, and complex numbers (e.g., 2 - 1j is complex)
# that a TypeError is raised if any of the arguments is not a valid type
#
# Question:
# do you need to test for a ValueError like in the Socratica video?
