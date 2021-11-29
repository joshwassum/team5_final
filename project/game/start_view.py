import arcade
from game.game_view import Game_View

class StartView(arcade.View):

    def __init__(self, scene, cast, script, props):
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

    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text("The Heroic V", self.window.width / 2, self.window.height / 2 + 75, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Collect as many coins as possible while searching for the crystals. Present the crystals to the questioner and test your knowledge.", 
                        self.window.width / 2, self.window.height / 2, arcade.color.WHITE, font_size=12, anchor_x="center")
        arcade.draw_text("Click to advance", self.window.width / 2, self.window.height / 2-75,
                        arcade.color.WHITE, font_size=20, anchor_x="center")
    
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        
        game_view = Game_View(self.scene, self.cast, self.script, self.props)
        self.window.show_view(game_view)
