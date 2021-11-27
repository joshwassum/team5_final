import arcade
from game.action import Action
from game import constants

class HandleCrystalCollisionAction(Action):
    """Handle the players collisions with the Crystal cast member.

    Stereotype:
        Controller

    Attributes:
        _tag (string): The action tag (input, update or output).
    """

    def execute(self, cast, scene):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
            scene (Scene): An instance of the Scene object.
        """
        self._handle_crystal_collisions(scene["Crystals"], scene["Player"][0], cast["crystals"])

    def _handle_crystal_collisions(self, crystals, player_location, score):
        """This function loops through the crystal locations and the players location to see if they are the same. 
            If True the crystal is removed and point value is added to Crystals.

        Args:
            self (Handle_collisions_Action): An instance of Handle_Collisions_Action
            crystals (Sprite): is an instance of the Sprites class
            Player (Sprite): An instance of the Sprites class.
            scroe (Actor): An instance of the Actor object.
        """

        crystal_collision_list = arcade.check_for_collision_with_list(player_location, crystals)
        crystal_collect_sound = arcade.load_sound(constants.CRYSTAL_COLLISION_SOUND)

        for crystal in crystal_collision_list:
            crystal.remove_from_sprite_lists()
            arcade.play_sound(crystal_collect_sound)
            score.add_number()