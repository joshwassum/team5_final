import arcade
from game import constants

class GameView(arcade.View):
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

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.jump_needs_reset = False

        self.jump_sound = arcade.load_sound(constants.PLAYER_JUMP_SOUND)

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

    def process_keychange(self):
        """
        Called when we change a key up/down or we move on/off a ladder.
        """
        # Process up/down
        if self.up_pressed and not self.down_pressed:
            if self.physics_engine.is_on_ladder():
                self.scene["Player"][0].change_y = constants.PLAYER_MOVEMENT_SPEED
            elif (
                self.physics_engine.can_jump(y_distance=10)
                and not self.jump_needs_reset
            ):
                self.scene["Player"][0].change_y = constants.PLAYER_JUMP_SPEED
                self.jump_needs_reset = True
                arcade.play_sound(self.jump_sound)
        elif self.down_pressed and not self.up_pressed:
            if self.physics_engine.is_on_ladder():
                self.scene["Player"][0].change_y = -constants.PLAYER_MOVEMENT_SPEED

        # Process up/down when on a ladder and no movement
        if self.physics_engine.is_on_ladder():
            if not self.up_pressed and not self.down_pressed:
                self.scene["Player"][0].change_y = 0
            elif self.up_pressed and self.down_pressed:
                self.scene["Player"][0].change_y = 0

        # Process left/right
        if self.right_pressed and not self.left_pressed:
            self.scene["Player"][0].change_x = constants.PLAYER_MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.scene["Player"][0].change_x = -constants.PLAYER_MOVEMENT_SPEED
        else:
            self.scene["Player"][0].change_x = 0

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True

        self.process_keychange()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = False
            self.jump_needs_reset = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False

        self.process_keychange()


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
                    self.script["view"].execute(self.scene, self.cast, self.props, self.script, "riddle")

            self.scene["Player"][0].change_x = 0

            if self.up_pressed and not self.down_pressed:
                self.script["movement"][0].execute(self.scene, arcade.key.UP, self.physics_engine, self.up_pressed)
                if not self.physics_engine.is_on_ladder():
                    self.up_pressed = False
            elif self.down_pressed and not self.up_pressed:
                self.script["movement"][0].execute(self.scene, arcade.key.DOWN, self.physics_engine, self.down_pressed)
            if self.left_pressed and not self.right_pressed:
                self.script["movement"][0].execute(self.scene, arcade.key.LEFT, self.physics_engine, self.left_pressed)
            elif self.right_pressed and not self.left_pressed:
                self.script["movement"][0].execute(self.scene, arcade.key.RIGHT, self.physics_engine, self.right_pressed)

        self.physics_engine.update()

        if self.physics_engine.can_jump():
            self.scene["Player"][0].can_jump = False
        else:
            self.scene["Player"][0].can_jump = True

        if self.physics_engine.is_on_ladder() and not self.physics_engine.can_jump():
            self.scene["Player"][0].is_on_ladder = True
            self.process_keychange()
        else:
            self.scene["Player"][0].is_on_ladder = False
            self.process_keychange()
        self.center_camera_to_player()