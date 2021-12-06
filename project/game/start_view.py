import arcade
import arcade.gui

class StartView(arcade.View):
    """Creates our start game view and sets up the elements on screen.

    Stereotype:
        View

    Attributes:
        scene (Scene): An instance of the arcade Scene object.
        cast (dict): The game actors {key: tag, value: list}.
        props (dict): The game interface objects {key: tag, value: Arcade Object}.
        script (dict): The game Actions {key: tag, value: Action}.
        manager (UIManager): An instance of the arcade gui UIManager object.
        v_box (UIBoxLayout): An instance of the arcade gui UIBoxLayout object
    """

    def __init__(self, scene, cast, props, script):
        """The class constructor.

        Args:
            self (StartView): An instance of StartView.
            scene (Scene): An instance of the Scene object.
            cast (dict): The game actors {key: tag, value: list}.
            props (dict): The game interface objects {key: tag, value: Arcade Object}.
            script (dict): The game Actions {key: tag, value: Action}.
        """

        super().__init__()
        self.scene = scene
        self.cast = cast
        self.script = script
        self.props = props

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        self.v_box = arcade.gui.UIBoxLayout()

        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))

        instruction_button = arcade.gui.UIFlatButton(text="Instructions", width=200)
        self.v_box.add(instruction_button.with_space_around(bottom=20))

        start_button.on_click = self.on_click_start

        instruction_button.on_click = self.on_click_instruction

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )


    def on_click_start(self, event):
        """Allows us to perform some action when called.
            In this case we are Starting the game.
        Args:
            self (StartView): An instance of StartView.
            event (Event): The triggering arcade gui event.
        """

        self.script["view"].execute(self.scene, self.cast, self.props, self.script, "game")


    def on_click_instruction(self, event):
        """Allows us to perform some action when called.
            In this case we are Sending the view to the instructions view.
        Args:
            self (StartView): An instance of StartView.
            event (Event): The triggering arcade gui event.
        """

        # Placeholder until the intructions screen is created.
        self.script["view"].execute(self.scene, self.cast, self.props, self.script, "instruction")


    def on_draw(self):
        """ Draw this view 
        Args:
            self (game_over_view): An instance of GameOverView
        """

        arcade.start_render()
        self.manager.draw()
        arcade.draw_text("The Heroic V", self.window.width / 2, self.window.height / 2 + 150,
                        arcade.color.WHITE, font_size=50, anchor_x="center")