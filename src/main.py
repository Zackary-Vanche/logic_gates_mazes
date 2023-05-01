from Game import Game
from pyautogui import size as pyautogui_size
from Color import Color
from Levels_colors_list import Levels_colors_list 

if __name__ == "__main__":

    TOTAL_SIZE = pyautogui_size()
    # You need that line.
    # If you don't put it, the pixel of the game
    # will be too big after compilation
    
    game_color = Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.4)
    game_color = None

    Game(show_help=1,
         index_current_level=0,
         sleep_time=10**(-2),
         print_click_rects=1,
         is_fullscreen=0,
         time_between_actions=0.15,
         time_between_deletings=0.05,
         time_between_level_changing=0.25,
         game_color=game_color).play()

    # import cProfile
    # cProfile.run("Game(show_help=1, index_current_level=0).play()")