import arcade
from game import constants
from game.player_sprite_animation import PlayerSpriteAnimation

class VictoryView(arcade.View):
    """Creates our victory view and sets up the elements on screen. 

    Stereotype:
        Controller
    """
    def __init__(self, cast, props, script):
        """The class constructor
        Args:
            scene (Scene): An instance of the Scene object
            collision_engine (Handle_Collisions_Action): An instance of the Handle_Collisions_Action object.
        """
        super().__init__()
        self.scene = None
        self.cast = cast
        self.props = props
        self.script = script


    def on_show(self):
        """ This is run once when we switch to this view 
        Args:
            scene (Scene): An instance of the Scene object
            """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view
        Args:
            scene (Scene): An instance of the Scene object
             """
        arcade.start_render()
        arcade.draw_text("Congratulations", self.window.width / 2, self.window.height / 2,
                        arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("CLICK IF YOU DARE PLAY AGAIN!", self.window.width / 2, self.window.height / 2-75,
                        arcade.color.SEA_GREEN, font_size=20, anchor_x="center")

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