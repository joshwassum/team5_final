# from PIL.Image import Image # I'm not sure what this does so I commented it out and we can uncomment it out if needed.
import arcade
from game import constants

class Sprites():
    """This class is where the actors and their lists are created and stored.

    Stereotype:
        Information Holder.

    Attributes:
        sprite (Sprite): An instance of the Sprite object.
        image_path (str): A path to the sprites image file.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Sprites): An instance of the Sprites object.

        """
        sprite = None
        image_source = ""

    def set_sprite(self, sprite):

        self.sprite = sprite

    def get_sprite(self):

        return self.sprite

    def set_image_source(self, source):

        self.image_source = source

    def get_image_source(self):

        return self.image_source