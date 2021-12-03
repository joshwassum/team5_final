import arcade
from game.action import Action
from game import constants
from game.game_over_view import GameOverView

class HandleDeathCollisionAction(Action):
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
        self.scene = scene
        self.cast = cast
        self.props = props
        self.script = script
        self._handle_death_collisions(scene["Player"][0], cast["lives"])



    def _handle_death_collisions(self, player_location, lives):
        """This function checks the players location to see if they have fallen. If True the lives is reduced by one and the game resets.

        Args:
            self (Handle_Death_Collisions): An instance of Handle_Collisions_Action
            lives (cast): is an instance of the marquee class
            Player (Sprite): An instance of the Sprites class.
        """
        death_sound = arcade.load_sound(constants.DEATH_SOUND)

        death_count = lives.get_text()
        if player_location.center_y < -10:
            arcade.play_sound(death_sound)
            lives.subtract_number()
            if death_count < 2:
                next_view = GameOverView(self.scene, self.cast, self.props, self.script)
                self.props["window"].show_view(next_view)
            else:
                player_location.center_x = constants.START_LOCATION_X
                player_location.center_y = constants.START_LOCATION_Y

