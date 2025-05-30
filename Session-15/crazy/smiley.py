from sense_hat import SenseHat

class Smiley:
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLANK = (0, 0, 0)
    BLUE = (0, 0, 255)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)

    def __init__(self, complexion = YELLOW, background = BLANK):
        """

        GeeksforGeeks. (2024, August). Primitive Data Types vs Non Primitive
        Data Types in Python. GeeksforGeeks; GeeksforGeeks.
        https://www.geeksforgeeks.org/primitive-data-types-vs-non-primitive-data-types-in-python/
        """
        # We have encapsulated the SenseHat object
        self.sense_hat = SenseHat()

        c = complexion
        b = background

        self.pixels = [
            b, c, c, c, c, c, c, b,
            c, c, c, c, c, c, c, c,
            c, c, c, c, c, c, c, c,
            c, c, c, c, c, c, c, c,
            c, c, c, c, c, c, c, c,
            c, c, c, c, c, c, c, c,
            c, c, c, c, c, c, c, c,
            b, c, c, c, c, c, c, b,
        ]


    def dim_display(self, dimmed=True):
        """
        Set the SenseHat's light intensity to low (True) or high (False)
        :param dimmed: Dim the display if True, otherwise don't dim
        """
        self.sense_hat.low_light = dimmed

    def show(self):
        """
        Show the smiley on the screen.
        """
        self.sense_hat.set_pixels(self.pixels)
