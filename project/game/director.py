import arcade
from game.game_window import Game_Window
from game.sprites import Sprites
from game.handle_collisions_action import HandleCollisionsAction

class Director:    
    
    def __init__(self):
        """Person who directs the game. The responsibility of
            this class of objects is to control the sequence of play.

        Sterotype:
            Controller

        Attributes:
            scene (Scene): An instance of the arcade Scene object.
            collision_engine (Action): An instance of the Action Class.
        """
        self.scene = None
        self.collision_engine = None

    def start_game(self):
        """Starts the game."""

        sprites = Sprites()
        self.scene = sprites.scene
        self.collision_engine = HandleCollisionsAction()
        Game_Window(self.scene, self.collision_engine)
        arcade.run()