# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 15:08:10 2023

@author: utilisateur
"""

from Maze import Maze
from Levels import Levels

def create_random_levels(a, b):
    for aux_level in Levels.aux_level_function_list:
        print(aux_level().name)
        Maze.save_random_door_trees_list(aux_level, n_files=a+b, i0=a)

if __name__ == '__main__':
    for aux_level in Levels.aux_level_function_list:
        print(aux_level().name)
        Maze.save_random_door_trees_list(aux_level, n_files=128, i0=0)


















