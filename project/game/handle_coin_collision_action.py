import arcade
from game.action import Action
from game import constants

class HandleCoinCollisionAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update 
    the game state when the player collides with a coin.

    Stereotype:
        Controller
    """

    def execute(self, scene, cast, props, script, delta_time):

        """Executes the action using the given actors.

        Args:
            self (HandleCoinCollisionAction): An instance of the HandleCoinCollisionAction object.
            scene (Scene): An instance of the Scene object.
            cast (dict): The game actors {key: tag, value: list}.
            props (dict): The game interface objects {key: tag, value: Arcade Object}
            script (dict): The game Actions {key: tag, value: Action}
            delta_time (Time): Used for determining game time.
        """

        self._handle_coin_collisions(scene["Coins"], scene["Player"][0], cast["score"])
        


    def _handle_coin_collisions(self, coins, player_location, score):
        """This function loops through the coin locations and the players location to see if they are the same. 
            If True the coin is removed and point value is added to the score.
        Args:
            self (HandleCoinCollisionAction): An instance of HandleCoinCollisionAction.
            coins (Sprite): is an instance of the arcade Sprite class.
            player_location (Sprite): An instance of the arcade Sprite class.
            score (Actor): An instance of the Actor class.
        """

        # Creates a collision list and loads a collision sound.
        coin_collision_list = arcade.check_for_collision_with_list(player_location, coins)
        coin_collect_sound = arcade.load_sound(constants.COIN_COLLISION_SOUND)

        # Loops through the collision list and removes the coins from the scene.
        for coin in coin_collision_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(coin_collect_sound)
            score.add_number()
