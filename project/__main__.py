import arcade
from game.director import Director
from game.sprites import Sprites
from game import constants


def main():
    """main activates the game and its various functions by gathering the various componenets of the app.
    It then groups them in to various sub groups and creates a scene for the director to use
    """
    scene = arcade.Scene()


    # Layer Specific Options for the Tilemap
    layer_options = {
        constants.LAYER_NAME_PLATFORMS: {
            "use_spatial_hash": True,
        },
        constants.LAYER_NAME_MOVING_PLATFORMS: {
                "use_spatial_hash": False,
            },
        constants.LAYER_NAME_LADDERS: {
            "use_spatial_hash": True,
            },
        constants.LAYER_NAME_COINS: {
            "use_spatial_hash": True,
            },
        constants.LAYER_NAME_PLAYER: {
            "use_spatial_hash": True,
            },
    }

    tile_map = arcade.load_tilemap(constants.MAP_NAME, constants.TILE_SCALE, layer_options)
    scene = arcade.Scene.from_tilemap(tile_map)




    scene.add_sprite_list("Player")
    player_sprite = Sprites()
    player_sprite.set_image_source(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png")
    player_sprite.set_sprite(arcade.Sprite(player_sprite.get_image_source(), constants.CHARACTER_SCALE))
    player_sprite.get_sprite().center_x = constants.START_LOCATION_X
    player_sprite.get_sprite().center_y = constants.START_LOCATION_Y
    scene.add_sprite("Player", player_sprite.get_sprite())




    # scene.add_sprite_list("Coin", use_spatial_hash=True)
    # coin_list_location = [[300, 96], [500, 96], [700, 96]]
    # for coordinate in coin_list_location:
    #     coin_sprite = Sprites()
    #     coin_sprite.set_image_source(":resources:images/items/coinGold.png")
    #     coin_sprite.set_sprite(arcade.Sprite(coin_sprite.get_image_source(), constants.COIN_SCALE))
    #     coin_sprite.get_sprite().position = coordinate
    #     scene.add_sprite("Coin", coin_sprite.get_sprite())



    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.TITLE)

    # Starts the game
    director = Director(scene, window)
    director.start_game()

if __name__ == "__main__":
    main()