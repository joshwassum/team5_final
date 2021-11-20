# from PIL.Image import Image # I'm not sure what this does so I commented it out and we can uncomment it out if needed.
import arcade
from game import constants

class Sprites():

    """This class is where the Sprites and the SpriteLists are created and stored.

        Attributes:
            scene (Scene): An instance of the arcade Scene object.
    """

    def __init__(self):
        """The class constructor

        Args:
            scene (Scene): An instance of the Scene object
            player_sprite (Sprites): An isntance of the Sprites object
        """

        self.scene = None

        self.player_sprite = None
        self.setup()


    def setup(self):
        """The setup function is used to set up all the pieces in the game. 

        Args:
            
            scene (Scene): An instance of the Scene object
            player_sprite (Sprites): An instance of the Sprites object
            platform (Sprite): An instance of the Sprite object
            coin (Sprite): An instance of the Sprite object
        """
        self.points = 0

        self.scene = arcade.Scene()

        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Platform", use_spatial_hash=True)

        self.player_sprite = arcade.Sprite(constants.PLAYER_IMAGE_SOURCE, constants.CHARACTER_SCALE)
        self.player_sprite.center_x = constants.START_LOCATION_X
        self.player_sprite.center_y = constants.START_LOCATION_Y
        self.scene.add_sprite("Player", self.player_sprite)

        for x in range(0, constants.SCREEN_WIDTH + 20, 64):
            platform = arcade.Sprite(constants.PLATFORM_IMAGE_SOURCE, constants.TILE_SCALE)
            platform.center_x = x
            platform.center_y = 32
            self.scene.add_sprite("Platform", platform)

        coin_list_location = [[300, 96], [500, 96], [700, 96]]
        for coordinate in coin_list_location:
            coin = arcade.Sprite(constants.COIN_IMAGE_SOURCE, constants.COIN_SCALE)
            coin.position = coordinate
            self.scene.add_sprite("Coin", coin)