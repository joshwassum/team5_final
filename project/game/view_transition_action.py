from game.action import Action
from game.start_view import StartView
from game.game_view import GameView
from game.riddlemaster_view import RiddlemasterView

class ViewTransitionAction(Action):
    """A code template for a thing done in a game. The responsibility of
    this class of objects is to interact with actors to change the state of the game.

    Stereotype:
        Controller

    Attributes:
        _tag (string): The action tag (input, update or output).
    """

    def execute(self, scene, cast, props, script, view):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        if view == 'start':
            self.start_view(scene, cast, props, script)
        elif view == 'game':
            self.game_view(scene, cast, props, script)
        elif view == 'riddle':
            self.riddlemaster_view(scene, cast, props, script)

    def start_view(self, scene, cast, props, script):
        view = StartView(scene, cast, script, props)
        props["window"].show_view(view)

    def game_view(self, scene, cast, props, script):
        view = GameView(scene, cast, script, props)
        props["window"].show_view(view)

    def riddlemaster_view(self, scene, cast, props, script):
        view = RiddlemasterView(scene, cast, props, script)
        props["window"].show_view(view)