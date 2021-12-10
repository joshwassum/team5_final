import arcade
import arcade.gui

class InstructionView(arcade.View):
    """Creates our start game view and sets up the elements on screen.

    Stereotype:
        Controller
    """

    def __init__(self, scene, cast, props, script):
        """The class constructor

        Args:
            scene (Scene): An instance of the Scene object
            collision_engine (Handle_Collisions_Action): An instance of the Handle_Collisions_Action object.
        """
        super().__init__()
        self.scene = scene
        self.cast = cast
        self.script = script
        self.props = props

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.BANGLADESH_GREEN)
        

        self.v_box = arcade.gui.UIBoxLayout()

        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))

        #instruction_button = arcade.gui.UIFlatButton(text="Instructions", width=200)
        #self.v_box.add(instruction_button.with_space_around(bottom=20))

        start_button.on_click = self.on_click_start

        #instruction_button.on_click = self.on_click_instruction

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )


    def on_click_start(self, event):
        """The on click to start the game view

        Args:
            self (instance): An instance of the instruction_view
        """
        print("you made it here.")
        self.script["view"].execute(self.scene, self.cast, self.props, self.script, "game")

    #def on_click_instruction(self, event):
        #print("Intruction:", event)

    def on_draw(self):
        """The on draw to get the text on the instructions view screen

        Args:
            self (instruction_view): An instance of the instruction_view
        """
        arcade.start_render()
        self.manager.draw()
        arcade.draw_text("The Heroic V(five)", self.window.width / 2, self.window.height / 2 + 150,
                        arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Instructions", self.window.width / 2, self.window.height / 2 + 85,
                        arcade.color.WHITE, font_size=50, anchor_x="center")

        arcade.draw_text("Play as the hero V. Take five crystals to the Riddle Master and he will ask a riddle before you can advance to the next dungeon. ", self.window.width / 2, self.window.height / 2-75,
                        arcade.color.WHITE, font_size=12, anchor_x="center")

        arcade.draw_text("Along the way collect coins to earn points. Bronze is worth one point, silver is worth three points, gold is worth five points, and gems are worth 15 points.", self.window.width / 2, self.window.height / 2-125,
                        arcade.color.WHITE, font_size=12, anchor_x="center")
        arcade.draw_text("If you think you have what it takes click start game to begin.", self.window.width / 2, self.window.height / 2-225,
                        arcade.color.WHITE, font_size=12, anchor_x="center")