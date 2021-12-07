import arcade
from game.action import Action
from game import constants

class HandleCrystalCollisionAction(Action):
    """Handle the players collisions with the Crystal cast member.
        When a collision occurs the crystal is removed from the scene
        and the crystal cast member is incremented by 1.

    Stereotype:
        Controller
    """

    def execute(self, scene, cast, props, script, delta_time):

        """Executes the action using the given actors.

        Args:
            self (HandleCrystalCollisionAction): An instance of the HandleCrystalCollisionAction object.
            scene (Scene): An instance of the Scene object.
            cast (dict): The game actors {key: tag, value: list}.
            props (dict): The game interface objects {key: tag, value: Arcade Object}
            script (dict): The game Actions {key: tag, value: Action}
            delta_time (Time): Used for determining game time.
        """
        self._handle_crystal_collisions(scene["Crystals"], scene["Player"][0], cast["crystals"], cast["score"])

    def _handle_crystal_collisions(self, crystals, player_location, crystal_score, score):
        """This function loops through the crystal locations and the players location to see if they are the same. 
            If True the crystal is removed and point value is added to Crystals.

        Args:
            self (HandleCrystalCollisionAction): An instance of HandleCrystalCollisionAction
            crystals (Sprite): is an instance of the arcade Sprite class.
            Player (Sprite): An instance of the arcade Sprite class.
            crystal_score (Actor): An instance of the Actor object.
            score (Actor): An instance of the Actor object.
        """

        # Creates a collision list and loads a collision sound.
        crystal_collision_list = arcade.check_for_collision_with_list(player_location, crystals)
        crystal_collect_sound = arcade.load_sound(constants.COIN_COLLISION_SOUND)

        # Loops through the collision list and removes the crystals from the scene.
        for crystal in crystal_collision_list:
            points = crystal.properties["Points"]
            score.add_points(points)
            crystal.remove_from_sprite_lists()
            arcade.play_sound(crystal_collect_sound)
            crystal_score.add_number()