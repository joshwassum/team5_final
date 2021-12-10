import arcade
from game import constants
from game.player_sprite_animation import PlayerSpriteAnimation

class LevelAdvanceView(arcade.View):
    """Creates our level advance view and sets up the elements on screen. 

    Stereotype:
        View

    Attributes:
        scene (None): Awaits initialization by the _new_scene function.
        cast (dict): The game actors {key: tag, value: list}.
        props (dict): The game props {key: tag, value: list}.
        script (dict): The game actions {key: tag, value: list}.
    """

    def __init__(self, scene, cast, props, script):
        """The class constructor
        Args:
            self (LevelAdvanceView): An instance of LevelAdvanceView.
            scene (None): Awaits initialization by the _new_scene function.
            cast (dict): The game actors {key: tag, value: list}.
            props (dict): The game interface objects {key: tag, value: Arcade Object}.
            script (dict): The game Actions {key: tag, value: Action}.
        """

        super().__init__()
        self.scene = scene
        self.cast = cast
        self.props = props
        self.script = script
        

    def on_show(self):
        """ This is run once when we switch to this view 
        Args:
            self (LevelAdvanceView): An instance of LevelAdvanceView.
        """

        arcade.set_background_color(arcade.color.BANGLADESH_GREEN)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view
        Args:
            self (LevelAdvanceView): An instance of LevelAdvanceView.
        """

        arcade.start_render()
        arcade.draw_text(f"Level { self.cast['level'].get_text()} Complete!", self.window.width / 2, self.window.height / 2,
                        arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("When ready to move to the next dungeon CLICK to start!", self.window.width / 2, self.window.height / 2-75,
                        arcade.color.SEA_GREEN, font_size=16, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, restart the game.
        Handles the restting of important game logic.
        
        Args:
            self (LevelAdvanceView): An instance of LevelAdvanceView.
            _x (int): The mouses x coordinate.
            _y (int): The mouses y coordinate.
            _button (??): The mouse button clicked.
            _modifiers (??): Any effects effecting the clicking of the mouse.
        """
        self.cast['lives'].set_text(self.cast['lives'].get_text())
        self.cast['score'].set_text(self.cast['score'].get_text())
        self.cast['crystals'].set_text(0)
            #adds one to the current level
        self.cast['level'].add_number()
        self._new_scene()
        self._new_props()
        self.script["view"].execute(self.scene, self.cast, self.props, self.script, "game")

    def _new_scene(self):
        """Private function that recreates the first level for next game level.
        
        Args:
            self (LevelAdvanceView): An instance of LevelAdvanceView.
        """

        # Initializes arcade Scene object
        self.scene = arcade.Scene()


        map_name = f"project/game/assets/map_{self.cast['level'].get_text()}.json"

        # Saves the tilemap and stores in the Scene object
        tile_map = arcade.load_tilemap(map_name, constants.TILE_SCALE, constants.LAYER_OPTIONS)
        self.scene = arcade.Scene.from_tilemap(tile_map)


        # Initializes the player sprite and assigns attributes to it. Then stores it in the scene object
        player_sprite = PlayerSpriteAnimation()
        player_sprite.center_x = constants.START_LOCATION_X
        player_sprite.center_y = constants.START_LOCATION_Y
        
        self.scene.add_sprite(constants.LAYER_NAME_PLAYER, player_sprite)

    def _new_props(self):
        """Generates a new physics engine.
        Args:
            self(LevelAdvanceView): An instance of LevelAdvanceView.
        """
        
        # Initializing physics engine and storing it in props
        physics_engine = arcade.PhysicsEnginePlatformer(
            self.scene["Player"][0], 
            gravity_constant=constants.GRAVITY, 
            walls=self.scene[constants.LAYER_NAME_PLATFORMS],
            ladders=self.scene[constants.LAYER_NAME_LADDERS],
        )
        self.props["physics_engine"] = physics_engine