import arcade
from game.action import Action
from game import constants


class SpriteAnimation(Action):
    """The responsibility of this class of objects is to update the animation of the sprite lists 
        in the tile map.

    Stereotype:
        Controller
    """


    def execute(self, scene, cast, props, script, delta_time):
        """Executes the action using the given actors.

        Args:
            self (SpriteAnimation): An instance of the SpriteAnimation object.
            scene (Scene): An instance of the Scene object.
            delta_time (Clock): Schedule a function to be called every interval seconds.
        """

        self.scene = scene
        arcade.Scene.update_animation(self.scene, delta_time)