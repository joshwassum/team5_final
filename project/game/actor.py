# from PIL.Image import Image # I'm not sure what this does so I commented it out and we can uncomment it out if needed.
import arcade
from game import constants

class Actor():

    """This class is where the actors and their lists are created and stored
    """

    def __init__(self):

        # Creating the scene Object
        self.scene = None

        # Variable that holds teh player sprite
        self.player_sprite = None


    def setup(self):
        """The setup function is used to set up all the pieces in the game.
        """

        # Variable to keep track of the score
        self.points = 0

        # Initialize the scene
        self.scene = arcade.Scene()

        # Create the sprite lists
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Platform", use_spatial_hash=True)

        # Create the playing character
        image_source = ":resources:images/animated_characters?robot/robot_walk0.png"
        self.player_sprite = arcade.Sprite(image_source, constants.CHARACTER_SCALE)
        self.player_sprite.center_x = constants.START_LOCATION_X
        self.player_sprite.center_y = constants.START_LOCATION_Y
        self.scene.add_sprite("Player", self.player_sprite)

        # Create the ground by using a loop.
        for x in range(0, constants.SCREEN_WIDTH + 20, 64):
            platform = arcade.Sprite(":resources:images/tiles/grassMid.png", constants.TILE_SCALE)
            platform.center_x = x
            platform.center_y = 32
            self.scene.add_sprite("Platform", platform)

        # Using a coordinate list to add some coins
        coin_list_location = [[300, 96], [500, 96], [700, 96]]
        for coordinate in coin_list_location:
            coin = arcade.Sprite(":resources:images/items/coinGold.png", constants.COIN_SCALE)
            coin.position = coordinate
            self.scene.add_sprite("Coin", coin)