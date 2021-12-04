import arcade
from game.action import Action


class SpriteAnimationAction(Action):
    """The responsibility of this class of objects is to update the animation of the sprite lists 
        in the tile map.

    Stereotype:
        Controller

    Attributes:
        scene (Scene): An instance of the arcade Scene object.
    """


    def execute(self, scene, cast, props, script, delta_time):
        """Executes the action using the given actors.

        Args:
            self (SpriteAnimationAction): An instance of the SpriteAnimationAction object.
            scene (Scene): An instance of the Scene object.
            cast (dict): The game actors {key: tag, value: list}.
            props (dict): The game interface objects {key: tag, value: Arcade Object}
            script (dict): The game Actions {key: tag, value: Action}
            delta_time (Time): Used for determining game time.
        """

        self.scene = scene
        arcade.Scene.update_animation(self.scene, delta_time) 