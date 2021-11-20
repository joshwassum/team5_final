from game import constants
from game.director import Director
from game.game_window import Game_Window

def main():
    """Calls the game Director Class the start the game."""
    director = Director()
    director.start_game()

if __name__ == "__main__":
    main()