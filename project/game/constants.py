"""Holds all of the game constants."""

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
TITLE = "The Heroic V"
START_LOCATION_X = 64
START_LOCATION_Y = 128
MAX_LIVES = 5
CHARACTER_SCALE = .85
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


RIDDLE_MASTER_SCRIPT_LEVEL_1 = [{"In order to advance to the next level you must answer my riddle, click OK": "",
"I am not alive, but I grow; I don’t have lungs, but I need air; I don’t have a mouth, but water kills me. What am I? \n\nfire\n\nice\n\nwater\n\nearth": "FIRE"}]

RIDDLE_MASTER_SCRIPT_LEVEL_2 = [{"You've come for round two eh? Think you can handle it?, click OK": "", "What has to be broken before you can use it?\n\nballoon\n\nwindow\n\negg\n\nclock": "EGG"}]

RIDDLE_MASTER_SCRIPT_LEVEL_3 = [{"You've come for round two eh? Think you can handle it?, click OK": ""},
{"I’m tall when I’m young, and I’m short when I’m old. What am I?\n\nchild\n\ncandle\n\nbear\n\nbattery": "CANDLE"}]

RIDDLE_MASTER_SCRIPT_LEVEL_4 = [{"You've come for round two eh? Think you can handle it?, click OK": ""},
{"What is full of holes but still holds water?\n\nbucket\n\nbody\n\nearth\n\nsponge": "SPONGE"}]

RIDDLE_MASTER_SCRIPT_LEVEL_5 = [{"You've made it to the final level, answer me this one last riddle, click OK": ""},
{"What is always in front of you but can’t be seen?\n\nglasses\n\ntraffic\n\nfuture\n\nphone": "FUTURE"}]