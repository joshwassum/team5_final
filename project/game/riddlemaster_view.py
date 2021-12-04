import arcade
import arcade.gui
from game import constants


class RiddlemasterView(arcade.View):
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

    def __init__(self, scene, cast, props, script):
        """The class constructor.
        Args:
            scene (Scene): An instance of the Scene object
            cast (dict): The game actors {key: tag, value: list}.
        """
        super().__init__()
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        self.scene = scene
        self.cast = cast
        self.props = props
        self.script = script
        self.riddle = ""
        self.answer = ""
        self.level = self.cast["level"].get_text()
        self.iter = 0
        for key,value in constants.RIDDLE_MASTER_SCRIPT[self.level - 1][self.iter].items():
            self.riddle = key
            self.answer = value


        #######################GUI elements#######################
        self.manager = arcade.gui.UIManager(auto_enable=True)
        bg_tex = arcade.load_texture(":resources:gui_basic_assets/window/grey_panel.png")
        self.text_area = arcade.gui.UITextArea(x=100,
                            y=200,
                            width=200,
                            height=300,
                            text=self.riddle,
                            text_color=(0, 0, 0, 255))
        self.manager.add(
            arcade.gui.UITexturePane(
                self.text_area.with_space_around(right=20),
                tex=bg_tex,
                padding=(10, 10, 10, 10)
            )
        )
        self.text = arcade.gui.UIInputText(x=500, y=400, width=200, height=50, text=" ", text_color=(0,0,0,255))
        self.manager.add(
            arcade.gui.UITexturePane(
                self.text,
                tex=bg_tex,
                padding=(10, 10, 10, 10)
            ))
        self.v_box = arcade.gui.UIBoxLayout()
        test_answer = arcade.gui.UIFlatButton(text="OK", width=200)
        self.v_box.add(test_answer)
        test_answer.on_click = self.on_click_open
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                x=540,
                y=200,
                child=self.v_box)
        )

    def on_draw(self):
        """ In charge of drawing the elements on screen.
        Args:
        self (riddlemaster_view): An instance of the riddlemaster_view 
        """
        arcade.start_render()
        self.manager.draw()
        for action in self.script['draw']:
            action.execute(self.cast)

    def on_click_open(self, event):
        """Built in arcade function that allows us to perform some action when called.
        Args:
        self (riddlemaster_view): An instance of the riddlemaster_view
        """
        if self.iter < len(constants.RIDDLE_MASTER_SCRIPT[self.level - 1]) + 1:
            if self.answer == self.text.text.upper().strip():
                self.iter += 1
                for key,value in constants.RIDDLE_MASTER_SCRIPT[self.level - 1][self.iter].items():
                    self.riddle = key
                    self.answer = value
                self.text_area.text = self.riddle
                self.text.text = ""
            elif self.cast["lives"].get_text() > 0:
                self.cast["lives"].subtract_number()
                self.text.text = "Try again!"
            if self.cast["lives"].get_text() < 1:
                self.script["view"].execute(self.scene, self.cast, self.props, self.script, "game_over")
        else:
            self.script["view"].execute(self.scene, self.cast, self.props, self.script, "victory")




