import arcade
from game.action import Action
from game import constants

class HandleRiddlemasterCollisionAction(Action):
    """A code template for handling death collisions. The responsibility of this class of objects is to update the game state when actors dies.

    Stereotype:
        Controller
    """

    def execute(self, scene, cast, props, script, delta_time):

        """Executes the action using the given actors.

        Args:
            self (HandleRiddlemasterCollisionAction): An instance of the HandleRiddlemasterCollisionAction object.
            scene (Scene): An instance of the Scene object.
            cast (dict): The game actors {key: tag, value: list}.
        """

        riddlemaster_sound = arcade.load_sound(constants.RIDDLEMASTER_SOUND)
        crystal_count = cast["crystals"].get_text()

        if crystal_count == 5:
            if arcade.check_for_collision_with_list(scene["Player"][0], scene["Riddlemaster"]):

                arcade.play_sound(riddlemaster_sound)
                return True



