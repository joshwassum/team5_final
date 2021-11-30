import arcade
from game.action import Action
from game import constants
import sys

class HandleRiddlemasterCollisionAction(Action):
    """A code template for handling death collisions. The responsibility of this class of objects is to update the game state when actors dies.

    Stereotype:
        Controller
    """
    def execute(self, scene, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        self._handle_riddlemaster_collisions(scene["Riddlemaster"], scene["Player"][0], cast["lives"], cast["crystals"])



    def _handle_riddlemaster_collisions(self, riddlemaster, player_location, lives, crystals):
        """This function checks the players location to see if they have fallen. If True the lives is reduced by one and the game resets.

        Args:
            self (Handle_Death_Collisions): An instance of Handle_Collisions_Action
            lives (cast): is an instance of the marquee class
            Player (Sprite): An instance of the Sprites class.
        """
        riddlemaster_sound = arcade.load_sound(constants.RIDDLEMASTER_SOUND)
        crystal_count = crystals.get_text()

        if crystal_count == 5:
            if arcade.check_for_collision_with_list(player_location, riddlemaster):
                  
                arcade.play_sound(riddlemaster_sound)
            



