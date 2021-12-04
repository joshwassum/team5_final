import arcade

class GameOverView(arcade.View):
    """Creates our game over view and sets up the elements on screen. Uses the Window functions built into
    arcade to track movement and camera setup.

    Stereotype:
        Controller

    Attributes:
        scene (Scene): An instance of the Scene object
    """
    def __init__(self, scene, cast, props, script):
        """The class constructor
        Args:
            scene (Scene): An instance of the Scene object
        """
        super().__init__()
        self.scene = scene
        self.scene = props

    def on_show(self):
        """ This is run once when we switch to this view 
        Args:
        self (game_over_view): An instance of the game over view
        """ 
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view 
        Args:
        self (game_over_view): An instance of the game over view
        """
        arcade.start_render()
        arcade.draw_text("Game Over", self.window.width / 2, self.window.height / 2,
                        arcade.color.WHITE, font_size=50, anchor_x="center")
        # arcade.draw_text("Click to advance", self.window.width / 2, self.window.height / 2-75,
        #                 arcade.color.WHITE, font_size=20, anchor_x="center")
    def on_death(self):
        """ When lives are at zero this restarts the game over and closes the existing window
        Args:
        self (game_over_view): An instance of the game over view
        """
        
        arcade.start()
        arcade.window.close()
    # def on_mouse_press(self, _x, _y, _button, _modifiers):
    #     """ If the user presses the mouse button, start the game. """

    #     game_view = Game_View(self.scene)
    #     self.window.show_view(game_view)