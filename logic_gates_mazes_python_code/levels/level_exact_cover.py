# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 20:44:03 2022

@author: utilisateur
"""

# Problème de la couverture exacte d'un ensemble

# 0 2 5
# 1 4
# 3 6 7

# 3 1 2
# 0 1
# 3 4 6
# 3 4
# 4 5
# 7 5

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_exact_cover():

    level = Maze(start_room_index=0, 
                 exit_room_index=-1, 
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, RE], 
                 doors_list = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11], 
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(0.6, sa=0.12, li=0.45),
                 name='Knight',
                 border = 30,
                 door_window_size = 700,
                 keep_proportions=True)

    return level