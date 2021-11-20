import arcade
from game import constants

class Game_Window(arcade.Window):
    """Creates our game screen and sets up the elements on screen. Uses the Window functions built into
    arcade to track movement and camera setup.

    Sterotype:
        Service Provider

    Attributes:
        scene (Scene): An instance of the arcade Scene object.
        camera (Camera): An instance of the Camera object.
        physics_engine (PhysicsEnginePlatformer): An instance of the PhysicsEnginePlatformer object.
        gui_camera (Camera): An instance of the Camera object.
    """

    def __init__(self, scene, collision_engine):
        """The class constructor

        Args:
            scene (Scene): An instance of the Scene object
        """

        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.TITLE)
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        self.scene = scene
        self.collision_engine = collision_engine
        self.camera = None
        self.physics_engine = None
        self.gui_camera = None
        self._setup()

    def on_draw(self):
        """Renders the screen.
        Args:
            self (Game_Window): An instance of the Game_Window object
        """

        arcade.start_render()
        # Code to draw the screen goes here

        # Activate our Camera
        self.camera.use()

        self.scene.draw()

        # Activate the GUI camera before drawing GUI elements
        self.gui_camera.use()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. Handles the movement of the player_sprite
        Args:
            self (Game_Window): An instance of the Game_Window object
        """

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.scene["Player"][0].change_y = constants.PLAYER_JUMP_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.scene["Player"][0].change_y = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.scene["Player"][0].change_x = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.scene["Player"][0].change_x = constants.PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.scene["Player"][0].change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.scene["Player"][0].change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.scene["Player"][0].change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.scene["Player"][0].change_x = 0

    def center_camera_to_player(self):
        screen_center_x = self.scene["Player"][0].center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.scene["Player"][0].center_y - (
            self.camera.viewport_height / 2
        )

        # Don't let camera travel past 0
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)

    def _setup(self):

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.scene["Player"][0], gravity_constant=constants.GRAVITY, walls=self.scene["Platform"]
        )

        self.camera = arcade.Camera(self.width, self.height)

        # Setup the GUI Camera
        self.gui_camera = arcade.Camera(self.width, self.height)
    
    def on_update(self, delta_time):
        """Movement and game logic"""
        self.collision_engine.execute(self.scene)
        # Move the player with the physics engine
        self.physics_engine.update()
