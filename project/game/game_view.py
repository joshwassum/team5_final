import arcade
from arcade.key import ASTERISK
from game.riddlemaster_view import RiddleMasterView
from game.game_over_view import GameOverView
from game import constants


class Game_View(arcade.View):
    """Creates our game screen and sets up the elements on screen. Uses the Window functions built into
    arcade to track movement and camera setup.

    Stereotype:
        Controller

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
        self.props = props
        self.camera = props["camera"]
        self.physics_engine = props["physics_engine"]
        self.gui_camera = props["gui_camera"]
        self.end_of_map = 0
        self.level = 1

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

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
        if key == arcade.key.LEFT and key == arcade.key.RIGHT:
            press = False
        self.script["movement"][0].execute(self.scene, key, self.physics_engine, press)

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key.
        Args:
            self (Game_View): An instance of Game_View.
        """
        press = False
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            press = True
        self.script["movement"][0].execute(self.scene, key, self.physics_engine, press)

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False


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

            game_action = action.execute(self.scene, self.cast, self.props, self.script, delta_time)

            if game_action:
                if self.cast["lives"].get_text() > 0:
                    next_view = RiddleMasterView(self.scene, self.cast, self.props, self.script)
                    self.window.show_view(next_view)

            self.scene["Player"][0].change_x = 0

            if self.up_pressed and not self.down_pressed:
                self.script["movement"][0].execute(self.scene, arcade.key.UP, self.physics_engine, self.up_pressed)
            elif self.down_pressed and not self.up_pressed:
                self.script["movement"][0].execute(self.scene, arcade.key.DOWN, self.physics_engine, self.down_pressed)
            if self.left_pressed and not self.right_pressed:
                self.script["movement"][0].execute(self.scene, arcade.key.LEFT, self.physics_engine, self.left_pressed)
            elif self.right_pressed and not self.left_pressed:
                self.script["movement"][0].execute(self.scene, arcade.key.RIGHT, self.physics_engine, self.right_pressed)

        self.physics_engine.update()
        self.center_camera_to_player()