import arcade
from game import constants
from game.move_sprites_action import Move_Sprites_Action

class Game_View(arcade.View):
    """Creates our game screen and sets up the elements on screen. Uses the Window functions built into
    arcade to track movement and camera setup.

    Sterotype:
        Service Provider

    Attributes:
        scene (Scene): An instance of the arcade Scene object.
        collision_engine (Handle_Collisions_Action): An instance of the Handle_Collisions_Action object.
        camera (Camera): An instance of the Camera object.
        physics_engine (PhysicsEnginePlatformer): An instance of the PhysicsEnginePlatformer object.
        gui_camera (Camera): An instance of the Camera object.
    """

    def __init__(self, scene, collision_engine):
        """The class constructor

        Args:
            scene (Scene): An instance of the Scene object
            collision_engine (Handle_Collisions_Action): An instance of the Handle_Collisions_Action object.
        """

        super().__init__()
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        self.movement_engine = Move_Sprites_Action()
        self.window.set_mouse_visible(False)
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

        self.camera.use()

        self.scene.draw()

        self.gui_camera.use()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. Handles the movement of the player_sprite
        Args:
            self (Game_Window): An instance of the Game_Window object
        """
        press = True
        self.movement_engine.execute(self.scene, key, self.physics_engine,press)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""
        press = False
        self.movement_engine.execute(self.scene,key, self.physics_engine, press)


    def center_camera_to_player(self):
        """Keeps the camera centered on the player character.
        
        Args:
            self (Game_Window): An instance of the Game_Window object.
        """
        screen_center_x = self.scene["Player"][0].center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.scene["Player"][0].center_y - (
            self.camera.viewport_height / 2
        )
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)

    def _setup(self):
        """Handles the stup of our needed attributes and functions.
        
        Args:
            self (Game_Window): An instance of the Game_Window object.
        """

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.scene["Player"][0], gravity_constant=constants.GRAVITY, walls=self.scene["Platform"]
        )
        self.camera = arcade.Camera(self.window.width, self.window.height)
        self.gui_camera = arcade.Camera(self.window.width, self.window.height)
    
    def on_update(self, delta_time):
        """Movement and game logic
        
        Args:
            self (Game_Window): An instance of the Game_Window object.
            delta_time (Time): An instance of time.
        """
        self.collision_engine.execute(self.scene)
        self.physics_engine.update()
