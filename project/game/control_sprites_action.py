import arcade
from game import constants
from game.action import Action

class ControlSpritesAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.

    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, scene, key, physics_engine, press):
        """Executes the action using the given sprites.

        Args:
            scene (Scene): An instance of the Scene arcade object.
            key (int): The key pressed by the user.
            physics_engine (PhysicsEnginePlatformer): An instance of the PhysicsEnginePlatformer arcade object.
            press (bool): A true or false value that indicates whether a button was pressed or released.
        """
        jump_sound = arcade.load_sound(constants.PLAYER_JUMP_SOUND)

        if press:
            self._handle_movement(scene, key, physics_engine, jump_sound)
        else:
            self._handle_stop(scene, key)

    def _handle_movement(self, scene, key, physics_engine, jump_sound):
        """Handles the movements of the player character.

        Args:
            self (ControlSpritesAction): An instance of ControlSpritesAction.
            scene (Scene): An instance of the Scene object.
            key (int): The key pressed by the user.
            physics_engine (PhysicsEnginePlatformer): An instance of the PhysicsEnginePlatformer arcade object.
            jump_sound (string): A string path that leads to the sound resource.
        """

        # scene["Player"][0].change_x = 0

        if key == arcade.key.UP or key == arcade.key.W:
            if physics_engine.is_on_ladder():
                scene["Player"][0].change_y = constants.PLAYER_MOVEMENT_SPEED
            elif physics_engine.can_jump():
                scene["Player"][0].change_y = constants.PLAYER_JUMP_SPEED
                arcade.play_sound(jump_sound)
        elif key == arcade.key.DOWN or key == arcade.key.S:
            if physics_engine.is_on_ladder():
                scene["Player"][0].change_y = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            scene["Player"][0].change_x = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            scene["Player"][0].change_x = constants.PLAYER_MOVEMENT_SPEED

    def _handle_stop(self, scene, key):
        """Handles the stopping of the player character.
        
        Args:
            self (ControlSpritesAction): An instance of ControlSpritesAction.
            scene (Scene): An instance of the Scene object.
            key (int): The key pressed by the user.
        """
        if key == arcade.key.UP or key == arcade.key.W:
            scene["Player"][0].change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            scene["Player"][0].change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            scene["Player"][0].change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            scene["Player"][0].change_x = 0