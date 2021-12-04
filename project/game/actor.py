class Actor():
    """Actor is used to show information such as how many lives the player has, 
    how many coins they have collected, and how many crystals they have collected.
    """

    def __init__(self):

        """The class constructor
        
        Args:
            self (Actor): an instance of the Actor object.
        """

        self._number = None


    def set_text(self, number):
        """Class setter, in charge of setting the text.

        Args:
            self (Actor): An instance of Actor
            text (String): String to set self._text to
        """

        self._number = number

    def get_text(self): 
        """Class Getter, returns the self._text element.

        Args:
            self (Actor): an instance of Actor.
        """
        return self._number
    
    def add_number(self):
        """ Increases self._number by 1.

        Args:
            self (Actor): An instance of Actor.
        """
        self._number += 1

    def subtract_number(self):
        """ Decreases self._number by 1.

        Args:
            self (Actor): An instance of Actor.
        """
        self._number -= 1