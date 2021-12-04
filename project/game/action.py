class Action:
    """A code template for a thing done in a game. The responsibility of
    this class of objects is to interact with actors to change the state of the game.

    Stereotype:
        Controller
    """

    def execute(self, scene, cast, props, script, delta_time):
        """Executes the action using the given actors.

        Args:
            self (Action): An instance of Action.
            scene (Scene): An instance of the Scene object.
            cast (dict): The game actors {key: tag, value: list}.
            props (dict): The game interface objects {key: tag, value: Arcade Object}
            script (dict): The game Actions {key: tag, value: Action}
            delta_time (Time): Used for determining game time.
        """
        raise NotImplementedError("execute not implemented in superclass")