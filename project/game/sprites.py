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
        _sprite = None
        _image_source = ""

    def set_sprite(self, sprite):
        """ Class setter, sets the Sprites sprite attribute.

        Args:
            self (Sprites): an instance of Sprites.
            sprite (Sprite): an instance of the arcade sprite object.
        """
        self._sprite = sprite

    def get_sprite(self):
        """ Class getter, retrieves the self._sprite attribute.

        Args:
            self (Sprites): an instance of Sprites.
        """
        return self._sprite

    def set_image_source(self, source):
        """ Class setter, sets the self._image_source attribute.

        Args:
            self (Sprites): an instance of Sprites.
            sours (str): the string path to the image source.
        """
        self._image_source = source

    def get_image_source(self):
        """ Class getter, retrieves the self._image_source attribute.

        Args:
            self (Sprites): an instance of Sprites.
        """
        return self._image_source