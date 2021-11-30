import arcade
import arcade.gui
from game.victory_view import VictoryView
from game import constants


class RiddleMasterView(arcade.View):

    def __init__(self, scene, cast, script, props):
        """The class constructor
        Args:
            scene (Scene): An instance of the Scene object
            collision_engine (Handle_Collisions_Action): An instance of the Handle_Collisions_Action object.
        """
        super().__init__()
        self.manager = arcade.gui.UIManager(auto_enable=True)
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        self.scene = scene
        self.cast = cast
        self.props = props
        self.script = script

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
        self.text = arcade.gui.UIInputText(x=340, y=200, width=200, height=50, text="Type answer here")
        self.manager.add(
            arcade.gui.UITexturePane(
                self.text,
                tex=bg_tex,
                padding=(10, 10, 10, 10)
            ))

        self.v_box = arcade.gui.UIBoxLayout()

        # Create a button. We'll click on this to open our window.
        # Add it v_box for positioning.
        test_answer = arcade.gui.UIFlatButton(text="Open", width=200)
        self.v_box.add(test_answer)

        # Add a hook to run when we click on the button.
        test_answer.on_click = self.on_click_open
        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_draw(self):
        arcade.start_render()
        self.manager.draw()

    def on_click_open(self, event):
        if self.text.text == "A":
            victory_view = VictoryView(self.scene, self.cast,self.script, self.props)
            self.window.show_view(victory_view)

