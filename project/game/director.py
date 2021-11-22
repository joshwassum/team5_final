import arcade
from game.game_view import Game_View
from game.sprites import Sprites
from game.handle_collisions_action import HandleCollisionsAction
from game.move_sprites_action import Move_Sprites_Action

class Director:
    """A code template for a person who directs the game. The responsibility of
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller   

    Attributes:
        scene (Scene): an instance of the Scene object.
        collision_engine (Handle_Collisions_Action): an instance off the Handle_Collisions_Action object.
    """
    def __init__(self, window):
        """The class constructor
        
        Args:
            self (Director): an instance of the Director object.
        """

        self.window = window

        # self.scene = None
        self.collision_engine = None
        # self.movement_engine = None

    def start_game(self, scene):
        """Runs the game logic.
        
        Args:
            self (Director): An instance of the Director object.
        """

        self.collision_engine = HandleCollisionsAction()
        start_view = Game_View(scene, self.collision_engine)
        self.window.show_view(start_view)
        arcade.run()