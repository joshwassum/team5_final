import arcade
from game.game_window import Game_Window
from game.sprites import Sprites
from game.handle_collisions_action import HandleCollisionsAction
from game import constants

class Director:    
    
    def __init__(self):

        self.scene = None
        self.collision_engine = None
        self.movement_engine = None

    def start_game(self):

        sprites = Sprites()
        self.scene = sprites.scene
        self.collision_engine = HandleCollisionsAction()
        Game_Window(self.scene, self.collision_engine)
        arcade.run()