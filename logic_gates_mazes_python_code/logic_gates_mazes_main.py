# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 16:02:21 2022

@author: utilisateur
"""

from Game import Game
from pyautogui import size as pyautogui_size

if __name__ == "__main__":

    TOTAL_SIZE = pyautogui_size()
    Game().play()
