import arcade
from game.game_window import Game_Window
from game.sprites import Sprites
from game.handle_collisions_action import HandleCollisionsAction

class Director:
    """A code template for a person who directs the game. The responsibility of
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller   

    Attributes:
        scene (Scene): an instance of the Scene object.
        collision_engine (Handle_Collisions_Action): an instance off the Handle_Collisions_Action object.
    """
    def __init__(self):
        """The class constructor
        
        Args:
            self (Director): an instance of the Director object.
        """

        self.scene = None
        self.collision_engine = None
        # self.movement_engine = None

    def start_game(self):
        """Runs the game logic.
        
        Args:
            self (Director): An instance of the Director object.
        """

        sprites = Sprites()
        sprites.create_sprites()
        self.scene = sprites.scene
        self.collision_engine = HandleCollisionsAction()
        Game_Window(self.scene, self.collision_engine)
        arcade.run()