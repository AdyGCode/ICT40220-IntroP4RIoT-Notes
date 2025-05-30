import time

from smiley import Smiley
from blinkable import Blinkable

class Crazy(Smiley, Blinkable):
    """
    Crazy (Blue) Smiley

    Extends the Smiley Class
    Implements the Blinkable Class
    Adds Wink feature

    """
    def __init__(self):
        self.complexion = Smiley.BLUE
        self.background = Smiley.BLANK

        super().__init__(complexion=self.complexion,
                         background=self.background)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        mouth = [17, 10, 11, 12, 13, 22]
        for pixel in mouth:
            self.pixels[pixel] = self.background

    def draw_left_eye(self, wide_open=True):
        """
        Draws open or closed left eye on a smiley
        :param wide_open: Render eyes wide open or shut
        """
        eyes = [42, 50]
        for pixel in eyes:
            if wide_open:
                eyes = self.background
            else:
                eyes = self.complexion
            self.pixels[pixel] = eyes

    def draw_right_eye(self, wide_open=True):
        """
        Draws open or closed right eye on a smiley
        :param wide_open: Render eyes wide open or shut
        """
        eyes = [45, 53]
        for pixel in eyes:
            if wide_open:
                eyes = self.background
            else:
                eyes = self.complexion
            self.pixels[pixel] = eyes

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on a smiley
        :param wide_open: Render eyes wide open or shut
        """
        self.draw_right_eye(wide_open)
        self.draw_left_eye(wide_open)

    def blink(self, delay=0.25):
        """
        Blinks the smiley's eyes once

         :param delay: Delay between blinks (in seconds)
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()

    def wink(self, delay=0.25):
        """
        Winks using the smiley's left eye once

         :param delay: Delay between blinks (in seconds)
        """
        for wink in [False, True]:
            self.draw_left_eye(wide_open=wink)
            self.show()
            time.sleep(delay)
