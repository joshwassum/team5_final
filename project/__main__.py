from game.director import Director
import arcade
from game.game_view import Game_View
from game.sprites import Sprites
from game.handle_collisions_action import HandleCollisionsAction
from game import constants

def main():
    """Initializes the game functionality.
    """
    scene = arcade.Scene()

    scene.add_sprite_list("Player")
    player_sprite = Sprites()
    player_sprite.set_image_source(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png")
    player_sprite.set_sprite(arcade.Sprite(player_sprite.get_image_source(), constants.CHARACTER_SCALE))
    player_sprite.get_sprite().center_x = constants.START_LOCATION_X
    player_sprite.get_sprite().center_y = constants.START_LOCATION_Y
    scene.add_sprite("Player", player_sprite.get_sprite())

    scene.add_sprite_list("Platform", use_spatial_hash=True)
    for x in range(0, constants.SCREEN_WIDTH + 20, 64):
        platform_sprite = Sprites()
        platform_sprite.set_image_source(":resources:images/tiles/grassMid.png")
        platform_sprite.set_sprite(arcade.Sprite(platform_sprite.get_image_source(), constants.TILE_SCALE))
        platform_sprite.get_sprite().center_x = x
        platform_sprite.get_sprite().center_y = 32
        scene.add_sprite("Platform", platform_sprite.get_sprite())

    scene.add_sprite_list("Coin", use_spatial_hash=True)
    coin_list_location = [[300, 96], [500, 96], [700, 96]]
    for coordinate in coin_list_location:
        coin_sprite = Sprites()
        coin_sprite.set_image_source(":resources:images/items/coinGold.png")
        coin_sprite.set_sprite(arcade.Sprite(coin_sprite.get_image_source(), constants.COIN_SCALE))
        coin_sprite.get_sprite().position = coordinate
        scene.add_sprite("Coin", coin_sprite.get_sprite())
    
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.TITLE)
    director = Director(window)
    director.start_game(scene)

if __name__ == "__main__":
    main()