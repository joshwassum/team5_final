# from PIL.Image import Image # I'm not sure what this does so I commented it out and we can uncomment it out if needed.
import arcade
from game import constants

class Sprites():
    """This class is where the actors and their lists are created and stored.

    Stereotype:
        Information Holder.

    Attributes:
        scene (Scene): An instance of the Scene object.
        player_sprite(Sprite): An instance of the Sprite object.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Sprites): An instance of the Sprites object.

        """
        self.scene = None
        self.player_sprite = None


    def create_sprites(self):
        """The setup function is used to set up all the pieces in the game.

        Args:
            self (Sprites): An instance of the Sprites object.
        """

        self.scene = arcade.Scene()
        self._create_platform()
        self._create_player()
        self._create_coins()

    def _create_player(self):
        """Manages the creation of the player sprite.
        
        Args:
            self (Sprites): An instance of the Sprites object.
        """

        self.scene.add_sprite_list("Player")

        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, constants.CHARACTER_SCALE)
        self.player_sprite.center_x = constants.START_LOCATION_X
        self.player_sprite.center_y = constants.START_LOCATION_Y
        self.scene.add_sprite("Player", self.player_sprite)

    def _create_platform(self):
        """Manages the creation of the platform sprites.
        
        Args:
            self (Sprites): An instance of the Sprites object.
        """

        self.scene.add_sprite_list("Platform", use_spatial_hash=True)

        for x in range(0, constants.SCREEN_WIDTH + 20, 64):
            platform = arcade.Sprite(":resources:images/tiles/grassMid.png", constants.TILE_SCALE)
            platform.center_x = x
            platform.center_y = 32
            self.scene.add_sprite("Platform", platform)

    def _create_coins(self):
        """Manages the creation of the coin sprites.
        
        Args:
            self (Sprites): An instance of the Sprites object.
        """

        coin_list_location = [[300, 96], [500, 96], [700, 96]]

        for coordinate in coin_list_location:
            coin = arcade.Sprite(":resources:images/items/coinGold.png", constants.COIN_SCALE)
            coin.position = coordinate
            self.scene.add_sprite("Coin", coin)