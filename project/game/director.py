import arcade
from game.game_view import Game_View
from game.control_sprites_action import ControlSpritesAction
from game.handle_collisions_action import HandleCollisionsAction
from game.start_view import StartView


class Director:
    """A code template for a person who directs the game. The responsibility of
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller   

    Attributes:
        scene (Scene): an instance of the Scene object.
        collision_engine (Handle_Collisions_Action): an instance off the Handle_Collisions_Action object.
    """
    def __init__(self, scene, window):
        """The class constructor
        
        Args:
            self (Director): an instance of the Director object.
        """
        self.scene = scene
        self.window = window

    def start_game(self):
        """Runs the game logic.
        
        Args:
            self (Director): An instance of the Director object.
        """
        start_view = StartView(self.scene)
        self.window.show_view(start_view)
        arcade.run()

