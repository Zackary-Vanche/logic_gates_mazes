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
    # will be too big after compiling

    Game(show_help=0, index_current_level=64, sleep_time=10**(-2)).play()

    # import cProfile
    # cProfile.run("Game(show_help=1, index_current_level=0).play()")