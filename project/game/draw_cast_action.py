from game.action import Action
from game import constants
import arcade

class DrawCastAction(Action):    
    
    
    def execute(self, cast):
        """Executes the drawing of Marquee elements.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        lives = cast["lives"]
        lives_text = f"Lives: {lives.get_text()}"
        arcade.draw_text(
            lives_text,
            400,
            constants.SCREEN_HEIGHT - 20,
            arcade.csscolor.WHITE,
            18
        )

        score = cast["score"]
        score_text = f"Score: {score.get_text()}"
        arcade.draw_text(
            score_text,
            200,
            constants.SCREEN_HEIGHT - 20,
            arcade.csscolor.WHITE,
            18
        )

        crystals = cast["crystals"]
        crystal_text = f"Crystals: {crystals.get_text()}"
        arcade.draw_text(
            crystal_text,
            10,
            constants.SCREEN_HEIGHT - 20,
            arcade.csscolor.WHITE,
            18
        )