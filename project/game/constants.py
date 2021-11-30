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
COIN_SCALE = .5
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

COIN_COLLISION_SOUND = ":resources:sounds/coin1.wav"
PLAYER_JUMP_SOUND = ":resources:sounds/phasejump1.wav"
DEATH_SOUND = ":resources:sounds/gameover1.wav"
RIDDLEMASTER_SOUND = ":resources:sounds/upgrade3.wav"

MAP_NAME = "project/game/assets/map_sample.json"

LAYER_NAME_FOREGROUND = "Foreground"
LAYER_NAME_PLATFORMS = "Platforms"
LAYER_NAME_COINS = "Coins"
LAYER_NAME_BACKGROUND = "Background"
LAYER_NAME_LADDERS = "Ladders"
LAYER_NAME_PLAYER = "Player"
LAYER_NAME_CRYSTALS = "Crystals"
LAYER_NAME_TRAPS = "Traps"
LAYER_NAME_RIDDLEMASTER = "Riddlemaster"

RIDDLE = "You've made it to the riddle master, now answer my question to proceed: \nI am not alive, but I grow; I don’t have lungs, but I need air; I don’t have a mouth, but water kills me. What am I?"