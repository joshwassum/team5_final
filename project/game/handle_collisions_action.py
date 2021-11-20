import arcade
from game.action import Action
from game import constants

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when sprites collide.

    Stereotype:
        Controller
    """
    def execute(self, cast):
        """Executes the action using the given sprites.

        Args:
            cast (dict): The game sprite {key: tag, value: list}.
        """


        coins = cast["Coin"]
        self._handle_coin_collisions(coins, cast["Player"][0])


    def _handle_coin_collisions(self, coins, player_location):
        """This function loops through the coin locations and the players sprite location to see if they are the same. If True the coin is removed.

        Args:
            self (Handle_collisions_Action): An instance of Handle_Collisions_Action
            coins (Sprites): is an instance of the Sprites object.
            Player (Sprites): An instance of the Sprites object.
        """

        coin_collision_list = arcade.check_for_collision_with_list(player_location, coins)
        collect_coin_sound = arcade.load_sound(constants.COIN_COLLISION_SOUND)

        for coin in coin_collision_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(collect_coin_sound)

    def _handle_riddlemaster_collision(self):
        pass


    def _handle_wall_constraints(self):
        pass


    def _handle_deathzone_constraints(self):
        pass


    def _end_of_world_collisions(self):
        pass


