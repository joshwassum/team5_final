import arcade
from arcade.color import WHITE
from game import constants


class Marquee():
    """Marquee is used to show inforation such as how many lives the player has, how many coins they have collected, and how many crystals they have collected.

    Args:
        player_lives (output): prints to the screen how many lives the player has

        count_score (output): prints to the screen how many points the player has

        count_crystals (output): print to the screen how many crystals the player has
    """

    def player_lives(lives):
        lives_text = f"Lives: {lives}"
        arcade.draw_text(
            lives_text,
            210,
            constants.SCREEN_HEIGHT - 10,
            arcade.csscolor,WHITE,
            18
        )

    def count_score(score):
        score_text = f"Score: {score}"
        arcade.draw_text(
            score_text,
            110,
            constants.SCREEN_HEIGHT - 10,
            arcade.csscolor,WHITE,
            18
        )

    def count_crystals(crystals):
        crystal_text = f"Crystals: {crystals}"
        arcade.draw_text(
            crystal_text,
            10,
            constants.SCREEN_HEIGHT - 10,
            arcade.csscolor,WHITE,
            18
        )