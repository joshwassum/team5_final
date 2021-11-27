import arcade

from game import constants


class Marquee():
    """Marquee is used to show information such as how many lives the player has, how many coins they have collected, and how many crystals they have collected.
    """

    def __init__(self):

        """The class constructor
        
        Args:
            self (Marquee): an instance of the Marquee object.
        """

        self._text = None


    def set_text(self, text):
        """Class setter, in charge of setting the text.

        Args:
            self (Marquee): An instance of Marquee
            text (String): String to set self._text to
        """

        self._text = text

    def get_text(self): 
        """Class Getter, returns the self._text element.

        Args:
            self (Marquee): an instance of Marquee.
        """
        return self._text