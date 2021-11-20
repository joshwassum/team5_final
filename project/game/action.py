class Action:
    """A code template for a thing done in a game. The responsibility of
    this class of objects is to interact with sprites to change the state of the game.

    Stereotype:
        Controller

    Attributes:
        _tag (string): The action tag (input, update or output).
    """

    def execute(self, cast):
        """Executes the action using the given sprites.

        Args:
            cast (dict): The game sprites {key: tag, value: list}.
        """
        raise NotImplementedError("execute not implemented in superclass")