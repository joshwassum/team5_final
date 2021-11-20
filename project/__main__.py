from game import constants
from game.director import Director
from game.game_window import Game_Window

def main():
    director = Director()
    director.start_game()

if __name__ == "__main__":
    main()