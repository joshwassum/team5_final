from typing import DefaultDict
from arcade.key import L


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
TITLE = "The Heroic V"
START_LOCATION_X = 64
START_LOCATION_Y = 128
MAX_LIVES = 5
# File path to riddle folder
CHARACTER_SCALE = 1
TILE_SCALE = .5
COIN_SCALE = 1
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

COIN_COLLISION_SOUND = ":resources:sounds/coin1.wav"
PLAYER_JUMP_SOUND = ":resources:sounds/phasejump1.wav"
DEATH_SOUND = ":resources:sounds/gameover1.wav"
RIDDLEMASTER_SOUND = ":resources:sounds/upgrade3.wav"

MAIN_FILE = ":resources:images/animated_characters/female_adventurer/femaleAdventurer"

LEVEL = 1
MAP_NAME = f"project/game/assets/map_{LEVEL}.json"

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

RIDDLE_MASTER_SCRIPT = [[{"You've made it to the Riddle Master, click OK": ""}, 
{"Try to make it through my Riddles by typing the correct answer, click OK": ""},
{"I am not alive, but I grow; I don’t have lungs, but I need air; I don’t have a mouth, but water kills me. What am I? \n\nfire\n\nice\n\nwater\n\nearth": "FIRE"}, 
{"What has to be broken before you can use it?\n\nballoon\n\nwindow\n\negg\n\nclock": "EGG"},  
{"I’m tall when I’m young, and I’m short when I’m old. What am I?\n\nchild\n\ncandle\n\nbear\n\nbattery": "CANDLE"},
{"What is full of holes but still holds water?\n\nbucket\n\nbody\n\nearth\n\nsponge": "SPONGE"},
{"What is always in front of you but can’t be seen?\n\nglasses\n\ntraffic\n\nfuture\n\nphone": "FUTURE"}]]