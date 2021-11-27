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
            cast (dict): The game sprites {key: tag, value: list}.
        """
        jump_sound = arcade.load_sound(constants.PLAYER_JUMP_SOUND)

        if press:
            self._handle_movement(scene, key, physics_engine, jump_sound)
        else:
            self._handle_stop(scene, key)

        

    def _handle_movement(self, scene, key, physics_engine, jump_sound):
        if key == arcade.key.UP or key == arcade.key.W:
            if physics_engine.can_jump():
                scene["Player"][0].change_y = constants.PLAYER_JUMP_SPEED
                arcade.play_sound(jump_sound)
        elif key == arcade.key.DOWN or key == arcade.key.S:
            scene["Player"][0].change_y = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            scene["Player"][0].change_x = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            scene["Player"][0].change_x = constants.PLAYER_MOVEMENT_SPEED

    def _handle_stop(self, scene, key):
        if key == arcade.key.UP or key == arcade.key.W:
            scene["Player"][0].change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            scene["Player"][0].change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            scene["Player"][0].change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            scene["Player"][0].change_x = 0

