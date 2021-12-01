import arcade
from game.action import Action
from game import constants

class HandleCoinCollisionAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update 
    the game state when the player collides with a coin.

    Stereotype:
        Controller
    """

    def execute(self, scene, cast):

        """Executes the action using the given actors.

        Args:
            self (HandleRiddlemasterCollisionAction): An instance of the HandleRiddlemasterCollisionAction object.
            scene (Scene): An instance of the Scene object.
            cast (dict): The game actors {key: tag, value: list}.
        """

        self._handle_coin_collisions(scene["Coins"], scene["Player"][0], cast["score"])
        


    def _handle_coin_collisions(self, coins, player_location, score):
        """This function loops through the coin locations and the players location to see if they are the same. If True the coin is removed and point value is
            added to the score.

        Args:
            self (Handle_collisions_Action): An instance of Handle_Collisions_Action
            coins (Sprite): is an instance of the Sprites class
            Player (Sprite): An instance of the Sprites class.
        """

        coin_collision_list = arcade.check_for_collision_with_list(player_location, coins)
        coin_collect_sound = arcade.load_sound(constants.COIN_COLLISION_SOUND)

        for coin in coin_collision_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(coin_collect_sound)
            score.add_number()
