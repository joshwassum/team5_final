"""Holds all of the game constants."""

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
TITLE = "The Heroic V"
START_LOCATION_X = 64
START_LOCATION_Y = 128
MAX_LIVES = 5
CHARACTER_SCALE = 1
TILE_SCALE = .5
COIN_SCALE = 1
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20
DEATH_COST = 5

COIN_COLLISION_SOUND = ":resources:sounds/coin1.wav"
PLAYER_JUMP_SOUND = ":resources:sounds/phasejump1.wav"
DEATH_SOUND = ":resources:sounds/gameover1.wav"
RIDDLEMASTER_SOUND = ":resources:sounds/upgrade3.wav"

MAIN_FILE = ":resources:images/animated_characters/female_adventurer/femaleAdventurer"

LEVEL = 1

RIGHT_FACING = 0
LEFT_FACING = 1

LAYER_NAME_FOREGROUND = "Foreground"
LAYER_NAME_PLATFORMS = "Platforms"
LAYER_NAME_COINS = "Coins"
LAYER_NAME_BACKGROUND = "Background"
LAYER_NAME_LADDERS = "Ladders"
LAYER_NAME_PLAYER = "Player"
LAYER_NAME_CRYSTALS = "Crystals"
LAYER_NAME_TRAPS = "Traps"
LAYER_NAME_RIDDLEMASTER = "Riddlemaster"

# Layer Specific Options for the Tilemap
LAYER_OPTIONS = {
    LAYER_NAME_PLATFORMS: {
            "use_spatial_hash": True,
        },
    LAYER_NAME_LADDERS: {
            "use_spatial_hash": True,
            },
    LAYER_NAME_COINS: {
            "use_spatial_hash": True,
            },
    LAYER_NAME_PLAYER: {
            "use_spatial_hash": False,
            },
    LAYER_NAME_TRAPS: {
            "use_spatial_hash": True,
            },        
    LAYER_NAME_CRYSTALS: {
            "use_spatial_hash": True,
            },
    LAYER_NAME_BACKGROUND: {
            "use_spatial_hash": True,
            },
    LAYER_NAME_RIDDLEMASTER: {
            "use_spatial_hash": True,
            },
    LAYER_NAME_FOREGROUND: {
            "use_spatial_hash": True,
            },
    }


from game import riddle_list
RIDDLE_MASTER_SCRIPT = riddle_list.riddles