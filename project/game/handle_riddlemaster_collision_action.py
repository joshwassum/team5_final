import arcade
from game.action import Action
from game import constants

class HandleRiddlemasterCollisionAction(Action):
    """A code template for handling death collisions. The responsibility of this class of objects is to update the game state when actors dies.

    Stereotype:
        Controller
    """
    def execute(self, scene, cast, props):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self.scene = scene
        self.props = props
        self.cast = cast

        riddlemaster_sound = arcade.load_sound(constants.RIDDLEMASTER_SOUND)
        crystal_count = cast["crystals"].get_text()

        # if crystal_count == 5:
        if arcade.check_for_collision_with_list(scene["Player"][0], scene["Riddlemaster"]):
                
            arcade.play_sound(riddlemaster_sound)
            return True



