import arcade
from game.action import Action
from game import constants

class HandleTrapCollisionAction(Action):
    """A code template for handling death collisions. The responsibility of this class of objects is to update the game state when actors dies.

    Stereotype:
        Controller
    Attributes:
        scene (Scene): An instance of the Scene object.
        cast (dict): The game actors {key: tag, value: list}.
        props (dict): The game interface objects {key: tag, value: Arcade Object}
        script (dict): The game Actions {key: tag, value: Action}
    """

    def execute(self, scene, cast, props, script, delta_time):

        """Executes the action using the given actors.

        Args:
            self (HandleTrapCollisionAction): An instance of the HandleTrapCollisionAction object.
            scene (Scene): An instance of the Scene object.
            cast (dict): The game actors {key: tag, value: list}.
            props (dict): The game interface objects {key: tag, value: Arcade Object}
            script (dict): The game Actions {key: tag, value: Action}
            delta_time (Time): Used for determining game time.
        """
        self.scene = scene
        self.props = props
        self.cast = cast
        self.script = script
        self._handle_trap_collisions(scene["Traps"], scene["Player"][0], cast["lives"], cast["score"])



    def _handle_trap_collisions(self, traps, player_location, lives, score):
        """This function checks the players location to see if they have landed on a trap. 
            If True the lives is reduced by one and the game resets.

        Args:
            self (HandleTrapCollisionAction): An instance of Handle_Collisions_Action.
            traps (Sprite): An instance of the arcade Sprite class.
            Player (Sprite): An instance of the arcade Sprite class.
            lives (Actor): An instance of the Actor class.
        """

        traps_sound = arcade.load_sound(constants.DEATH_SOUND)

        if arcade.check_for_collision_with_list(player_location, traps):
            arcade.play_sound(traps_sound)
            lives.subtract_number()
            score.subtract_points(constants.DEATH_COST)
            lives_left = lives.get_text()
            if lives_left < 1:
                self.script["view"].execute(self.scene, self.cast, self.props, self.script, "game_over")
            else:
                player_location.center_x = constants.START_LOCATION_X
                player_location.center_y = constants.START_LOCATION_Y



