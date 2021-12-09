import arcade
from game import constants
from game.player_sprite_animation import PlayerSpriteAnimation
from game import actor

class GameOverView(arcade.View):
    """Creates our game over view and sets up the elements on screen. Uses the arcade.View functions built into
    arcade.

    Stereotype:
        View

    Attributes:
        scene (None): Awaits initialization by the _new_scene function.
        cast (dict): The game actors {key: tag, value: list}.
        props (dict): The game props {key: tag, value: list}.
        script (dict): The game actions {key: tag, value: list}.
    """

    def __init__(self, cast, props, script):
        """The class constructor.
        Args:
            self(GameOverView): An instance of GameOverView.
            cast (dict): The game actors {key: tag, value: list}.
            props (dict): The game interface objects {key: tag, value: Arcade Object}
            script (dict): The game Actions {key: tag, value: Action}
        """

        super().__init__()
        self.scene = None
        self.props = props
        self.cast = cast
        self.script = script
        self._new_scene()
        self._new_props()

    def on_show(self):
        """ This is run once when we switch to this view 
        Args:
            self (game_over_view): An instance of the game over view
        """ 

        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view 
        Args:
            self (game_over_view): An instance of GameOverView
        """

        arcade.start_render()
# Final Score: {self.cast['score'].get_text()}
        # Draws the test on the screen.
        arcade.draw_text("Game Over", self.window.width / 2, self.window.height / 2,
                        arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text(f"Final Score: {self.cast['score'].get_text()}", self.window.width / 2, self.window.height / 2-40,
                        arcade.color.WHITE, font_size=25, anchor_x="center")
        arcade.draw_text("Click to restart", self.window.width / 2, self.window.height / 2-75,
                        arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, restart the game.
        Handles the restting of important game logic.
        
        Args:
            self (game_over_view): An instance of GameOverView.
            _x (int): The mouses x coordinate.
            _y (int): The mouses y coordinate.
            _button (??): The mouse button clicked.
            _modifiers (??): Any effects effecting the clicking of the mouse.
        """

        self.cast['lives'].set_text(constants.MAX_LIVES)
        self.cast['score'].set_text(0)
        self.cast['crystals'].set_text(0)
        self.cast['level'].set_text(constants.LEVEL)
        self.script["view"].execute(self.scene, self.cast, self.props, self.script, "game")
        

    def _new_scene(self):
        """Private function that recreates the first level for game restart.
        
        Args:
            self (GameOverView): An instance of GameOverView.
        """

        # Initializes arcade Scene object
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
        map_name = f"project/game/assets/map_{constants.LEVEL}.json"
        tile_map = arcade.load_tilemap(map_name, constants.TILE_SCALE, layer_options)
        self.scene = arcade.Scene.from_tilemap(tile_map)
        self.scene.add_sprite_list_before("Player", constants.LAYER_NAME_FOREGROUND)

        # Initializes the player sprite and assigns attributes to it. Then stores it in the scene object
        player_sprite = PlayerSpriteAnimation()
        player_sprite.center_x = constants.START_LOCATION_X
        player_sprite.center_y = constants.START_LOCATION_Y
        
        self.scene.add_sprite(constants.LAYER_NAME_PLAYER, player_sprite)

    def _new_props(self):
        """Generates a new physics engine.
        Args:
            self(GameOverView): An instance of GameOverView.
        """

        # Initializing physics engine and storing it in props
        physics_engine = arcade.PhysicsEnginePlatformer(
            self.scene["Player"][0], 
            gravity_constant=constants.GRAVITY, 
            walls=self.scene[constants.LAYER_NAME_PLATFORMS],
            ladders=self.scene[constants.LAYER_NAME_LADDERS],
        )
        self.props["physics_engine"] = physics_engine
        