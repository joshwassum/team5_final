import arcade
from game.action import Action
from game import constants

class HandleDeathCollisionAction(Action):
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
            self (HandleDeathCollisionAction): An instance of the HandleDeathCollisionAction object.
            scene (Scene): An instance of the Scene object.
            cast (dict): The game actors {key: tag, value: list}.
            props (dict): The game interface objects {key: tag, value: Arcade Object}
            script (dict): The game Actions {key: tag, value: Action}
            delta_time (Time): Used for determining game time.
        """

        self.scene = scene
        self.cast = cast
        self.props = props
        self.script = script
        self._handle_death_collisions(scene["Player"][0], cast["lives"], cast["score"])

    def _handle_death_collisions(self, player_location, lives, score):
        """This function checks the players location to see if they have fallen. If True the lives is reduced by one and the game resets.

        Args:
            self (HandleDeathCollisionAction): An instance of HandleDeathCollisionAction.
            lives (cast): An instance of the Actor class.
            Player (Sprite): An instance of the arcade Sprite class.
        """

        death_sound = arcade.load_sound(constants.DEATH_SOUND)

        death_count = lives.get_text()
        if player_location.center_y < -10:
            arcade.play_sound(death_sound)
            lives.subtract_number()
            score.subtract_points(5)
            if death_count < 2:
                self.script["view"].execute(self.scene, self.cast, self.props, self.script, "game_over")
            else:
                player_location.center_x = constants.START_LOCATION_X
                player_location.center_y = constants.START_LOCATION_Y

