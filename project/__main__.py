import arcade
from game.start_view import StartView
from game.actor import Actor
from game import constants
from game.sprites import Sprites
from game.handle_coin_collision_action import HandleCoinCollisionAction
from game.handle_death_collision_action import HandleDeathCollisionAction
from game.control_sprites_action import ControlSpritesAction
from game.draw_cast_action import DrawCastAction

def main():
    """main activates the game and its various functions by gathering the various componenets of the app.
    It then initializes these componenets and seperates them into groups and sub groups. I then passes it to
    the start view object.
    """
    
#########################Scene Objects######################################  

    # Inilizes arcade Scene object
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

    # Saves the tilemap and stores in the Scene object
    tile_map = arcade.load_tilemap(constants.MAP_NAME, constants.TILE_SCALE, layer_options)
    scene = arcade.Scene.from_tilemap(tile_map)

    # Creates a sprite ;ist within the scene object
    scene.add_sprite_list("Player")

    # Initializes the player sprite and assigns attirbutes to it. Then stores it in the scene object
    player_sprite = Sprites()
    player_sprite.set_image_source(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png")
    player_sprite.set_sprite(arcade.Sprite(player_sprite.get_image_source(), constants.CHARACTER_SCALE))
    player_sprite.get_sprite().center_x = constants.START_LOCATION_X
    player_sprite.get_sprite().center_y = constants.START_LOCATION_Y
    scene.add_sprite("Player", player_sprite.get_sprite())


#########################Cast Objects######################################

    # Initializing cast dictionary
    cast = {}

    # Initializing an Actor object and saves it as lives in cast
    lives = Actor()
    lives.set_text(5)
    cast["lives"] = lives

    # Initializing an Actor object and saves it as score in cast
    score = Actor()
    score.set_text(0)
    cast["score"] = score

    # Initializing an Actor object and saves it as crystals in cast
    crystals = Actor()
    crystals.set_text(0)
    cast["crystals"] = crystals


#########################Script Objects######################################  

    # Initializing script dictionary
    script = {}

    # Initializing collision objects and storing them in script
    handle_death_collision_action = HandleDeathCollisionAction()
    handle_coin_collision_action = HandleCoinCollisionAction()
    script["update"] = [handle_coin_collision_action, handle_death_collision_action]

    # Initializing draw objects and storing it in script
    draw_cast_action = DrawCastAction()
    script["draw"] = [draw_cast_action]
    
    # Initializing movement objects and storing it in script
    control_sprites_action = ControlSpritesAction()
    script["movement"] = [control_sprites_action]


#########################Prop Objects######################################

    # Initializing props Dictionary
    props = {}

    # Initializing game window
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.TITLE)

    # Initializing physics engine and storing it in props
    physics_engine = arcade.PhysicsEnginePlatformer(
        scene["Player"][0], gravity_constant=constants.GRAVITY, walls=scene[constants.LAYER_NAME_PLATFORMS]
    )
    props["physics_engine"] = physics_engine
    
    # Initializing camera and storing it in props
    camera = arcade.Camera(window.width, window.height)
    props["camera"] = camera
    
    # Initializing gui camera and storing it in props
    gui_camera = arcade.Camera(window.width, window.height)
    props["gui_camera"] = gui_camera



    # Starts the game and passes key values to the view
    start_view = StartView(scene, cast, script, props)
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()