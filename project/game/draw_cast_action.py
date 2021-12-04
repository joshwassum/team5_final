from game.action import Action
from game import constants
import arcade

class DrawCastAction(Action):    
    """This is a polymorphism of the action class. This particular class deals with the drawing of the 
    various cast elements

    Stereotype:
        Controller
    """
    
    def execute(self, cast):
        """Executes the drawing of cast elements.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        
        # Draws the life cast element
        lives = cast["lives"]
        lives_text = f"Lives: {lives.get_text()}"
        arcade.draw_text(
            lives_text,
            400,
            constants.SCREEN_HEIGHT - 20,
            arcade.csscolor.WHITE,
            18
        )

        # Draws the score cast element
        score = cast["score"]
        score_text = f"Score: {score.get_text()}"
        arcade.draw_text(
            score_text,
            200,
            constants.SCREEN_HEIGHT - 20,
            arcade.csscolor.WHITE,
            18
        )

        # Draws the crystal cast element
        crystals = cast["crystals"]
        crystal_text = f"Crystals: {crystals.get_text()}"
        arcade.draw_text(
            crystal_text,
            10,
            constants.SCREEN_HEIGHT - 20,
            arcade.csscolor.WHITE,
            18
        )

        # Draws the level cast element
        level = cast["level"]
        level_text = f"Level: {level.get_text()}"
        arcade.draw_text(
            level_text,
            600,
            constants.SCREEN_HEIGHT - 20,
            arcade.csscolor.WHITE,
            18
        )