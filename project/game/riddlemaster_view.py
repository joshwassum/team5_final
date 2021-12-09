import arcade
import arcade.gui
from game import constants


class RiddlemasterView(arcade.View):
    """Creates our riddle master screen and sets up the elements on screen. Uses the the Arcade gui to accept
    and output user information.

    Stereotype:
        View

    Attributes:
        scene (Scene): An instance of the arcade Scene object.
        cast (dict): The game actors {key: tag, value: list}.
        props (dict): The game interface objects {key: tag, value: Arcade Object}.
        script (dict): The game Actions {key: tag, value: Action}.
        riddle (str): Placeholder for the riddles that will be asked.
        answer (str): Placeholder for the correct answer.
        level (Actor): An instance of the Actor class.
        iter (int): Tracks how many questions have been asked.
        manager (UIManager): An instance of the arcade gui UIManager object.
        text (UIInputText): An instance of the arcade gui UIInputText object.
        v_box (UIBoxLayout): An instance of the arcade gui UIBoxLayout object
        text_area (UITextArea): An instance of the arcade gui UITextArea object
    """

    def __init__(self, scene, cast, props, script):
        """The class constructor.
        Args:
            self (RiddleMasterView): An instance of RiddleMasterView.
            scene (Scene): An instance of the Scene object.
            cast (dict): The game actors {key: tag, value: list}.
            props (dict): The game interface objects {key: tag, value: Arcade Object}
            script (dict): The game Actions {key: tag, value: Action}
        """
        
        super().__init__()
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        self.scene = scene
        self.cast = cast
        self.props = props
        self.script = script
        self.riddle = []
        self.answer = []
        self.level = self.cast["level"].get_text()
        self.iter = 0
        self.riddle_script = self._set_script()
        
        for key,value in self.riddle_script[0].items():
            self.riddle.append(key)
            self.answer.append(value)


        #######################GUI elements#######################
        self.manager = arcade.gui.UIManager(auto_enable=True)
        bg_tex = arcade.load_texture(":resources:gui_basic_assets/window/grey_panel.png")

        # Creates our text_area where questions will be asked.
        self.text_area = arcade.gui.UITextArea(x=100,
                            y=200,
                            width=200,
                            height=300,
                            text=self.riddle[self.iter],
                            text_color=(0, 0, 0, 255))
        self.manager.add(
            arcade.gui.UITexturePane(
                self.text_area.with_space_around(right=20),
                tex=bg_tex,
                padding=(10, 10, 10, 10)
            )
        )

        # Creates our input object where the user will submit answers.
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
            self (RiddleMasterView): An instance of RiddleMasterView.
        """

        arcade.start_render()
        self.manager.draw()
        for action in self.script['draw']:
            action.execute(self.cast)

    def on_click_open(self, event):
        """Allows us to perform some action when called.
            In this case we are handling questions and answers.
        Args:
            self (RiddleMasterView): An instance of RiddleMasterView.
            event (Event): The triggering arcade gui event.
        """

        if self.iter <= len(self.riddle) - 1:
            if self.answer[self.iter] == self.text.text.upper().strip():
                self.iter += 1
                if self.iter == len(self.riddle) and self.cast["level"].get_text() < 5:
                    self.script["view"].execute(self.scene, self.cast, self.props, self.script, "level_advance_view")
                elif self.iter == len(self.riddle) and self.cast["level"].get_text() == 5:
                    self.script["view"].execute(self.scene, self.cast, self.props, self.script, "victory")
                else:
                    self.text_area.text = self.riddle[self.iter]
                    self.text.text = ""
            elif self.cast["lives"].get_text() > 0:
                self.cast["lives"].subtract_number()
                self.text.text = "Try again!"
            if self.cast["lives"].get_text() < 1:
                self.script["view"].execute(self.scene, self.cast, self.props, self.script, "game_over")

    def _set_script(self):

        if self.level == 1:
            return constants.RIDDLE_MASTER_SCRIPT_LEVEL_1
        elif self.level == 2:
            return constants.RIDDLE_MASTER_SCRIPT_LEVEL_2
        elif self.level == 3: 
            return constants.RIDDLE_MASTER_SCRIPT_LEVEL_3
        elif self.level == 4: 
            return constants.RIDDLE_MASTER_SCRIPT_LEVEL_4
        elif self.level == 5: 
            return constants.RIDDLE_MASTER_SCRIPT_LEVEL_5




