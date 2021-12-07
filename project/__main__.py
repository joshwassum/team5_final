import arcade
from game.actor import Actor
from game import constants
from game.handle_coin_collision_action import HandleCoinCollisionAction
from game.handle_death_collision_action import HandleDeathCollisionAction
from game.handle_crystal_collision_action import HandleCrystalCollisionAction
from game.handle_trap_collision_action import HandleTrapCollisionAction
from game.handle_riddlemaster_collision_action import HandleRiddlemasterCollisionAction
from game.view_transition_action import ViewTransitionAction
from game.draw_cast_action import DrawCastAction
from game.sprite_animation_action import SpriteAnimationAction
from game.player_sprite_animation import PlayerSpriteAnimation

def main():
    """main activates the game and its various functions by gathering the various componenets of the app.
    It then initializes these componenets and separates them into groups and sub groups. I then passes it to
    the start view object.
    """
#########################Cast Objects######################################

    # Initializing cast dictionary
    cast = {}

    # Initializing an Actor object and saves it as lives in cast
    lives = Actor()
    lives.set_text(constants.MAX_LIVES)
    cast["lives"] = lives

    # Initializing an Actor object and saves it as score in cast
    score = Actor()
    score.set_text(0)
    cast["score"] = score

    # Initializing an Actor object and saves it as crystals in cast
    crystals = Actor()
    crystals.set_text(0)
    cast["crystals"] = crystals


    # Initializing an Actor object and saves it as level in cast
    level = Actor()
    level.set_text(constants.LEVEL)
    cast["level"] = level



#########################Scene Objects######################################  

    # Initializes arcade Scene object
    scene = arcade.Scene()

    map_level = level.get_text()
    map_name = f"project/game/assets/map_{map_level}.json"

    # Saves the tilemap and stores in the Scene object
    tile_map = arcade.load_tilemap(map_name, constants.TILE_SCALE, constants.LAYER_OPTIONS)
    scene = arcade.Scene.from_tilemap(tile_map)

    # Initializes the player sprite and assigns attributes to it. Then stores it in the scene object
    player_sprite = PlayerSpriteAnimation()
    player_sprite.center_x = constants.START_LOCATION_X
    player_sprite.center_y = constants.START_LOCATION_Y
    
    scene.add_sprite(constants.LAYER_NAME_PLAYER, player_sprite)




#########################Script Objects######################################  

    # Initializing script dictionary
    script = {}

    # Initializing collision objects and storing them in script
    handle_death_collision_action = HandleDeathCollisionAction()
    handle_coin_collision_action = HandleCoinCollisionAction()
    handle_crystal_collision_action = HandleCrystalCollisionAction()
    handle_trap_collision_action = HandleTrapCollisionAction()
    handle_riddlemaster_collision_action = HandleRiddlemasterCollisionAction()
    sprite_animation_action = SpriteAnimationAction()
    script["update"] = [handle_coin_collision_action, 
                        handle_death_collision_action, 
                        handle_crystal_collision_action, 
                        handle_trap_collision_action,
                        handle_riddlemaster_collision_action,
                        sprite_animation_action
                        ]

    # Initializing draw objects and storing it in script
    draw_cast_action = DrawCastAction()
    script["draw"] = [draw_cast_action]

    # Initializing the view transition object and storing it in script
    view_transition_action = ViewTransitionAction()
    script["view"] = view_transition_action



#########################Prop Objects######################################

    # Initializing props Dictionary
    props = {}

    # Initializing game window
    props["window"] = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.TITLE)

    # Initializing physics engine and storing it in props
    physics_engine = arcade.PhysicsEnginePlatformer(
        scene["Player"][0], 
        gravity_constant=constants.GRAVITY, 
        walls=scene[constants.LAYER_NAME_PLATFORMS],
        ladders=scene[constants.LAYER_NAME_LADDERS],
    )
    props["physics_engine"] = physics_engine
    
    # Initializing camera and storing it in props
    camera = arcade.Camera(props["window"].width, props["window"].height)
    props["camera"] = camera
    
    # Initializing gui camera and storing it in props
    gui_camera = arcade.Camera(props["window"].width, props["window"].height)
    props["gui_camera"] = gui_camera

    # Starts the game and passes key values to the view
    script["view"].execute(scene, cast, props, script, "start")
    arcade.run()

if __name__ == "__main__":
    main()