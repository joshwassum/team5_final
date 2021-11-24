import arcade
from game.action import Action
from game import constants
from game import game_view

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.

    Stereotype:
        Controller
    """
    def execute(self, cast, coin_sound):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        lives = 0
        if cast["Player"][0].center_y < -10:
            self._handle_deathzone_constraints(lives)
        coins = cast["Coins"]

        # marquee = cast["marquee"][0]
        self._handle_coin_collisions(coins, cast["Player"][0])
        self.coin_collect_sound = coin_sound
        


    def _handle_coin_collisions(self, coins, player_location):
        """This function loops through the coin locations and the players location to see if they are the same. If True the coin is removed and point value is
            added to the score.

        Args:
            self (Handle_collisions_Action): An instance of Handle_Collisions_Action

            coins (Sprite): is an instance of the Sprites class
            Player (Sprite): An instance of the Sprites class.
        """

        coin_collision_list = arcade.check_for_collision_with_list(player_location, coins)


        for coin in coin_collision_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.coin_collect_sound)

    # TO DO
    def _handle_riddlemaster_collision(self):
        pass

    # TO DO
    def _handle_wall_constraints(self):
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.scene.get_sprite_list("Walls"))

    # TO DO
    def _handle_deathzone_constraints(self, lives):
        if lives == 0:
            quit()
        # else:
        #   lives -= 1
        #   reset the player


    # TO DO
    def _end_of_world_collisions(self):
        pass

######## FUTURE UPDATE ###########
    # def _update_score(self, coin, marquee):
    #     """This function gets the point value from the brick and adds it to the score. Then sets value of points
    #         to the marquee.

    #         Args:
    #             marquee (Actor): marquee is an instance of Actor
    #             coin (Actor): brick is an instance of Actor
    #             points (integer): point value from Actor
    #             lives (integer): how many lives left
    #     """
    #     points = coin.get_points()
    #     lives = 3
    #     marquee.add_points(points)
    #     marquee.set_text(marquee.get_lives())
    #     marquee.set_text(marquee.get_points())
