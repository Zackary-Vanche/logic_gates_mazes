# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 16:02:21 2022

@author: utilisateur
"""

from Game import Game
from pyautogui import size as pyautogui_size

if __name__ == "__main__":

    TOTAL_SIZE = pyautogui_size()
    # You need that line.
    # If you don't put it, the pixel of the game
    # will be too big after compilation

    Game(show_help=1,
         index_current_level=0,
         sleep_time=10**(-2),
         print_click_rects=True,
         is_fullscreen=True,
         time_between_actions=0.15,
         time_between_deletings=0.05,
         time_between_level_changing=0.25).play()

    # import cProfile
    # cProfile.run("Game(show_help=1, index_current_level=0).play()")