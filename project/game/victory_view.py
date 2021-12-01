import arcade

class VictoryView(arcade.View):
    """Creates our victory view and sets up the elements on screen. 

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


    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text("Congratulations", self.window.width / 2, self.window.height / 2,
                        arcade.color.WHITE, font_size=50, anchor_x="center")
        # arcade.draw_text("CLICK IF YOU DARE PLAY AGAIN!", self.window.width / 2, self.window.height / 2-75,
        #                 arcade.color.SEA_GREEN, font_size=20, anchor_x="center")

    # def on_mouse_press(self, _x, _y, _button, _modifiers):
    #     """ If the user presses the mouse button, start the game. """

    #     next_view = Game_View(self.scene, self.cast, self.script, self.props)
    #     self.window.show_view(next_view)