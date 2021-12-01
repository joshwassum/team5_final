from typing import cast
import arcade
import arcade.gui
from game.victory_view import VictoryView
from game.game_over_view import GameOverView
from game import constants


class RiddleMasterView(arcade.View):
    """Creates our riddle master screen and sets up the elements on screen. Uses the the Arcade gui to accept
    and output user information.

    Stereotype:
        Controller

    Attributes:
        scene (Scene): An instance of the arcade Scene object.
        cast (dict): The game actors {key: tag, value: list}.
        manager (UIManager): An instance of the arcade gui UIManager object.
        text (UIInputText): An instance of the arcade gui UIInputText object.
        v_box (UIBoxLayout): An instance of the arcade gui UIBoxLayout object
    """

    def __init__(self, scene, cast):
        """The class constructor
        Args:
            scene (Scene): An instance of the Scene object
            cast (dict): The game actors {key: tag, value: list}.
        """
        super().__init__()
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        self.scene = scene
        self.cast = cast

        #######################GUI elements#######################
        self.manager = arcade.gui.UIManager(auto_enable=True)
        bg_tex = arcade.load_texture(":resources:gui_basic_assets/window/grey_panel.png")
        text_area = arcade.gui.UITextArea(x=100,
                            y=200,
                            width=200,
                            height=300,
                            text=constants.RIDDLE,
                            text_color=(0, 0, 0, 255))
        self.manager.add(
            arcade.gui.UITexturePane(
                text_area.with_space_around(right=20),
                tex=bg_tex,
                padding=(10, 10, 10, 10)
            )
        )
        self.text = arcade.gui.UIInputText(x=500, y=400, width=200, height=50, text="Type Here", text_color=(0,0,0,255))
        self.manager.add(
            arcade.gui.UITexturePane(
                self.text,
                tex=bg_tex,
                padding=(10, 10, 10, 10)
            ))
        self.v_box = arcade.gui.UIBoxLayout()
        test_answer = arcade.gui.UIFlatButton(text="Submit", width=200)
        self.v_box.add(test_answer)
        test_answer.on_click = self.on_click_open
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                x=540,
                y=200,
                child=self.v_box)
        )

    def on_draw(self):
        """ In charge of drawing the elements on screen. """
        arcade.start_render()
        self.manager.draw()
        for action in self.script["draw"]:
            action.execute(self.cast)

    def on_click_open(self, event):
        """Built in arcade function that allows us to perform some action when called."""
        if self.text.text.upper() == "FIRE":
            next_view = VictoryView(self.scene, self.cast,self.script, self.props)
            self.window.show_view(next_view)
        elif self.cast["lives"].get_text() > 0:
            self.cast["lives"].subtract_number()
            self.text.text = "Try again!"
        elif self.cast["lives"].get_text() < 1:
            next_view = GameOverView(self.scene, self.cast,self.script, self.props)
            self.window.show_view(next_view)




