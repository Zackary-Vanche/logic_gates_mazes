from Game import Game
from pyautogui import size as pyautogui_size
from Color import Color
from Levels_colors_list import Levels_colors_list

if __name__ == "__main__":

    TOTAL_SIZE = pyautogui_size()
    # You need that line.
    # If you don't put it, the pixel of the game
    # will be too big after compilation
    
    # 128 129
    # 130 138 139
    # 140 141 142 143 144 145 146 147 

    Game(show_help=1,
         index_current_level=0, 
         is_fullscreen=0,
         # WINDOW_SIZE=None,
         # SMALLEST_WINDOW_SIZE=None,
         # game_color=Levels_colors_list.FROM_HUE(hu=0.1, sa=0, li=0.35)
         ).play()

    # import cProfile
    # cProfile.run("Game(show_help=1, index_current_level=0).play()")