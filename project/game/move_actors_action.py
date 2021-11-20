"""THIS IS A TEST CLASS, DOES NOT CURRENTLY WORK"""

import arcade
from game import constants
from game.action import Action

class Move_Sprites_Action(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.

    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self.scene = cast

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
        """Called whenever a key is released. Handles the movement of the player_sprite
        Args:
            self (Game_Window): An instance of the Game_Window object
        """
        if key == arcade.key.UP or key == arcade.key.W:
            self.scene["Player"][0].change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.scene["Player"][0].change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.scene["Player"][0].change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.scene["Player"][0].change_x = 0