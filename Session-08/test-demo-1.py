# --------------------------------------------------------
#
# ADD PROGRAM TITLE HERE
#
# ADD SUMMARY OF PROGRAM HERE
#
# Folder:    Session-08
# Filename:  test-demo-1.py
# Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Version:   0.0
# 
# --------------------------------------------------------

def maximum(first_value, second_value):
    """
    This function returns the maximum of two values

    Parameters
    ----------
    first_value: the first number to compare
    second_value: the second number to compare

    Returns
    ----------
    maximum: number

    Examples
    ----------
    >>> maximum(1, 2)
    2
    >>> maximum(-7, -11)
    -7
    >>> maximum(101, 101)
    101
    """
    if first_value < second_value:
        return second_value
    if first_value> second_value:
        return first_value
    return first_value




import doctest
doctest.testmod()

print(maximum(1,2))