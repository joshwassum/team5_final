import arcade
from game.director import Director
from game.sprites import Sprites
from game import constants
from game.marquee import Marquee


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

    cast = {}

    lives = Marquee()
    lives.set_text(5)
    cast["lives"] = lives

    score = Marquee()
    score.set_text(0)
    cast["score"] = score

    crystals = Marquee()
    crystals.set_text(0)
    cast["crystals"] = crystals




    
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.TITLE)

    # Starts the game
    director = Director(scene, cast, window)
    director.start_game()

if __name__ == "__main__":
    main()