import arcade
from game.action import Action
from game import constants
import sys

class HandleDeathCollisionAction(Action):
    """A code template for handling death collisions. The responsibility of this class of objects is to update the game state when actors dies.

    Stereotype:
        Controller
    """
    def execute(self, scene, cast, props):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """


        # marquee = cast["marquee"][0]
        self._handle_death_collisions(scene["Player"][0], cast["lives"])



    def _handle_death_collisions(self, player_location, lives):
        """This function checks the players location to see if they have fallen. If True the lives is reduced by one and the game resets.

        Args:
            self (Handle_Death_Collisions): An instance of Handle_Collisions_Action
            lives (cast): is an instance of the marquee class
            Player (Sprite): An instance of the Sprites class.
        """
        death_sound = arcade.load_sound(constants.DEATH_SOUND)

        if player_location.center_y < -10:
            arcade.play_sound(death_sound)
            lives.subtract_number()
            if lives == 0:
                sys.exit()
            else:
                player_location.center_x = constants.START_LOCATION_X
                player_location.center_y = constants.START_LOCATION_Y

