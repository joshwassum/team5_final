import arcade
from game.action import Action
from game import constants
from game.game_over_view import GameOverView

class HandleTrapCollisionAction(Action):
    """A code template for handling death collisions. The responsibility of this class of objects is to update the game state when actors dies.

    Stereotype:
        Controller
    """
    def execute(self, scene, cast, script, props):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self.scene = scene
        self.props = props
        self.cast = cast
        self.script = script
        self._handle_trap_collisions(scene["Traps"], scene["Player"][0], cast["lives"])



    def _handle_trap_collisions(self, traps, player_location, lives):
        """This function checks the players location to see if they have fallen. If True the lives is reduced by one and the game resets.

        Args:
            self (Handle_Death_Collisions): An instance of Handle_Collisions_Action
            lives (cast): is an instance of the marquee class
            Player (Sprite): An instance of the Sprites class.
        """
        traps_sound = arcade.load_sound(constants.DEATH_SOUND)

        if arcade.check_for_collision_with_list(player_location, traps):
                  
            arcade.play_sound(traps_sound)
            lives.subtract_number()
            lives_left = lives.get_text()
            if lives_left < 1:
                next_view = GameOverView(self.scene, self.cast, self.script, self.props)
                self.props["window"].show_view(next_view)
            else:
                player_location.center_x = constants.START_LOCATION_X
                player_location.center_y = constants.START_LOCATION_Y



