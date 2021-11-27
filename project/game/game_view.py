import arcade

class Game_View(arcade.View):
    """Creates our game screen and sets up the elements on screen. Uses the Window functions built into
    arcade to track movement and camera setup.

    Stereotype:
        Service Provider

    Attributes:
        script (dict): The game Actions {key: tag, value: Action}
        scene (Scene): An instance of the arcade Scene object.
        cast (dict): The game actors {key: tag, value: list}.
        camera (Camera): An instance of the Camera object.
        gui_camera (Camera): An instance of the Camera object.
        end_of_map (int): Sets the end of the map.
        level (int): Indicates which level the player is on.
    """

    def __init__(self, scene, cast, script, props):
        """The class constructor

        Args:
            script (dict): The game Actions {key: tag, value: Action}
            self (GameView): An instance of GameView.
            scene (Scene): An instance of the Scene object.
            cast (dict): The game actors {key: tag, value: list}.
            props (dict): The game interface objects {key: tag, value: Arcade Object}
        """

        super().__init__()
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        self.script = script
        self.scene = scene
        self.cast = cast
        self.camera = props["camera"]
        self.physics_engine = props["physics_engine"]
        self.gui_camera = props["gui_camera"]
        self.end_of_map = 0
        self.level = 1

    def on_draw(self):
        """Renders the screen.

        Args:
            self (Game_Window): An instance of the Game_Window object
        """

        arcade.start_render()

        self.camera.use()

        self.scene.draw()

        self.gui_camera.use()

        for action in self.script["draw"]:
            action.execute(self.cast)


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. Handles the movement of the player_sprite.
        Args:
            self (Game_Window): An instance of the Game_Window object.
        """
        press = True
        self.script["movement"][0].execute(self.scene, key, self.physics_engine, press)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key.
        Args:
            self (Game_View): An instance of Game_View.
        """
        press = False
        self.script["movement"][0].execute(self.scene, key, self.physics_engine, press)


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

    def on_update(self, delta_time):
        """Movement and game logic

        Args:
            self (Game_Window): An instance of the Game_Window object.
            delta_time (Time): An instance of time.
        """
        for action in self.script["update"]:
            action.execute(self.scene, self.cast)
        self.physics_engine.update()
        self.center_camera_to_player()