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

    # Game.play() 
    
    Game.play(save_image = True) 
    
    # Game.play(WINDOW_SIZE = TOTAL_SIZE, save_image = True)
    
    sys_exit()
    
    # À lancer dans le Anaconda powershell :
    # pyinstaller E:\Perso\games\logic_gates_maze_code_python\logic_gates_maze.py --distpath E:\Perso\games\logic_gates_maze_executable --icon=E:\Perso\games\logic_gates_maze_code_python\images\icone.ico
    
    # Si on ne veut qu'un seul fichier au lieu d'un dossier
    # on ajoute -F
    # En ne prenant qu'un seul fichier, l'application est beaucoup plus longue à se lancer
    
    








