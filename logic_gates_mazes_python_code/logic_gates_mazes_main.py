# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 16:02:21 2022

@author: utilisateur
"""
# from numba import njit

from sys import exit as sys_exit
from Game import Game
from pyautogui import size as pyautogui_size
            
if __name__ == "__main__":

    TOTAL_SIZE = pyautogui_size()

    Game.play(index_current_level=0) 

    # Game.play(save_image = True) 

    # Game.play(WINDOW_SIZE = TOTAL_SIZE, save_image = True)

    sys_exit()

    # À lancer dans le Anaconda powershell :
    # pyinstaller C:\Users\utilisateur\Documents\github\logic_gates_mazes\logic_gates_mazes_python_code\logic_gates_mazes_main.py --distpath C:\Users\utilisateur\Documents\github\logic_gates_mazes\logic_gates_mazes_executable --icon=C:\Users\utilisateur\Documents\github\logic_gates_mazes\icone.ico

    # Si on ne veut qu'un seul fichier au lieu d'un dossier
    # on ajoute -F
    # En ne prenant qu'un seul fichier, l'application est beaucoup plus longue à se lancer
    
    








