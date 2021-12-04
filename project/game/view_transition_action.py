from game.action import Action
from game.start_view import StartView
from game.game_view import GameView
from game.riddlemaster_view import RiddlemasterView
from game.victory_view import VictoryView
from game.game_over_view import GameOverView

class ViewTransitionAction(Action):
    """A code template for a thing done in a game. The responsibility of
    this class of objects is to change the games view when called.

    Stereotype:
        Controller
    """

    def execute(self, scene, cast, props, script, view):
        """Executes the action using the given dictionaries and objects.

        Args:
            self (ViewTransitionAction): An instance of ViewTransitionAction.
            scene (Scene): An instance of the Scene object.
            cast (dict): The game actors {key: tag, value: list}.
            props (dict): The game interface objects {key: tag, value: Arcade Object}
            script (dict): The game Actions {key: tag, value: Action}
            view (str): Used for determining the screen to show
        """

        if view == 'start':
            self._start_view(scene, cast, props, script)
        elif view == 'game':
            self._game_view(scene, cast, props, script)
        elif view == 'riddle':
            self._riddlemaster_view(scene, cast, props, script)
        elif view == 'game_over':
            self._game_over_view(cast, props, script)
        elif view == 'victory':
            self._victory_view(cast, props, script)

    def _start_view(self, scene, cast, props, script):
        """Handles the transition to the start screen.

        Args:
            self (ViewTransitionAction): An instance of ViewTransitionAction.
            scene (Scene): An instance of the Scene object.
            cast (dict): The game actors {key: tag, value: list}.
            props (dict): The game interface objects {key: tag, value: Arcade Object}
            script (dict): The game Actions {key: tag, value: Action}
        """

        view = StartView(scene, cast, props, script)
        props["window"].show_view(view)

    def _game_view(self, scene, cast, props, script):
        """Handles the transition to the game screen.

        Args:
            self (ViewTransitionAction): An instance of ViewTransitionAction.
            scene (Scene): An instance of the Scene object.
            cast (dict): The game actors {key: tag, value: list}.
            props (dict): The game interface objects {key: tag, value: Arcade Object}
            script (dict): The game Actions {key: tag, value: Action}
        """

        view = GameView(scene, cast, props, script)
        props["window"].show_view(view)

    def _riddlemaster_view(self, scene, cast, props, script):
        """Handles the transition to the riddlemaster screen.

        Args:
            self (ViewTransitionAction): An instance of ViewTransitionAction.
            scene (Scene): An instance of the Scene object.
            cast (dict): The game actors {key: tag, value: list}.
            props (dict): The game interface objects {key: tag, value: Arcade Object}
            script (dict): The game Actions {key: tag, value: Action}
        """

        view = RiddlemasterView(scene, cast, props, script)
        props["window"].show_view(view)

    def _game_over_view(self, cast, props, script):
        """Handles the transition to the game over screen.

        Args:
            self (ViewTransitionAction): An instance of ViewTransitionAction.
            scene (Scene): An instance of the Scene object.
            cast (dict): The game actors {key: tag, value: list}.
            props (dict): The game interface objects {key: tag, value: Arcade Object}
            script (dict): The game Actions {key: tag, value: Action}
        """

        view = GameOverView(cast, props, script)
        props["window"].show_view(view)

    def _victory_view(self, cast, props, script):
        """Handles the transition to the victory screen.

        Args:
            self (ViewTransitionAction): An instance of ViewTransitionAction.
            scene (Scene): An instance of the Scene object.
            cast (dict): The game actors {key: tag, value: list}.
            props (dict): The game interface objects {key: tag, value: Arcade Object}
            script (dict): The game Actions {key: tag, value: Action}
        """
        
        view = VictoryView(cast, props, script)
        props["window"].show_view(view)