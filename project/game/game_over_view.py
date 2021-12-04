import arcade
from game import constants
from game.player_sprite_animation import PlayerSpriteAnimation

class GameOverView(arcade.View):
    """Creates our game over view and sets up the elements on screen. Uses the Window functions built into
    arcade to track movement and camera setup.

    Stereotype:
        Controller

    Attributes:
        scene (Scene): An instance of the Scene object
    """
    def __init__(self, cast, props, script):
        """The class constructor
        Args:
            scene (Scene): An instance of the Scene object
        """
        super().__init__()
        self.scene = None
        self.props = props
        self.cast = cast
        self.script = script
        self._new_scene()

    def on_show(self):
        """ This is run once when we switch to this view 
        Args:
        self (game_over_view): An instance of the game over view
        """ 
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view 
        Args:
        self (game_over_view): An instance of the game over view
        """
        arcade.start_render()
        arcade.draw_text("Game Over", self.window.width / 2, self.window.height / 2,
                        arcade.color.WHITE, font_size=50, anchor_x="center")

        arcade.draw_text("Click to advance", self.window.width / 2, self.window.height / 2-75,
                        arcade.color.WHITE, font_size=20, anchor_x="center")

        arcade.draw_text("Click to advance", self.window.width / 2, self.window.height / 2-75,
                        arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        self.cast['lives'].set_text(5)
        self.cast['score'].set_text(0)
        self.cast['crystals'].set_text(0)
        self.cast['level'].set_text(1)
        self.script["view"].execute(self.scene, self.cast, self.props, self.script, "game")

    def _new_scene(self):
        #########################Scene Objects######################################  

        # Inilizes arcade Scene object
        self.scene = arcade.Scene()

        # Layer Specific Options for the Tilemap
        layer_options = {
            constants.LAYER_NAME_PLATFORMS: {
                "use_spatial_hash": True,
            },
            constants.LAYER_NAME_FOREGROUND: {
                "use_spatial_hash": True,
                },
            constants.LAYER_NAME_LADDERS: {
                "use_spatial_hash": True,
                },
            constants.LAYER_NAME_COINS: {
                "use_spatial_hash": True,
                },
            constants.LAYER_NAME_PLAYER: {
                "use_spatial_hash": False,
                },
            constants.LAYER_NAME_TRAPS: {
                "use_spatial_hash": True,
                },        
            constants.LAYER_NAME_CRYSTALS: {
                "use_spatial_hash": True,
                },
            constants.LAYER_NAME_BACKGROUND: {
                "use_spatial_hash": True,
                },
            constants.LAYER_NAME_RIDDLEMASTER: {
                "use_spatial_hash": True,
                },
        }

        # Saves the tilemap and stores in the Scene object
        tile_map = arcade.load_tilemap(constants.MAP_NAME, constants.TILE_SCALE, layer_options)
        self.scene = arcade.Scene.from_tilemap(tile_map)

        self.scene.add_sprite_list_before("Player", constants.LAYER_NAME_FOREGROUND)
        # Initializes the player sprite and assigns attirbutes to it. Then stores it in the scene object
        player_sprite = PlayerSpriteAnimation()
        player_sprite.center_x = constants.START_LOCATION_X
        player_sprite.center_y = constants.START_LOCATION_Y
        
        self.scene.add_sprite(constants.LAYER_NAME_PLAYER, player_sprite)