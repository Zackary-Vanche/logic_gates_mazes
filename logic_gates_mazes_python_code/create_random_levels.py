# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 15:08:10 2023

@author: utilisateur
"""

from Maze import Maze
from levels.level_random_K2 import aux_level_random_K2
from levels.level_random_K5 import aux_level_random_K5
from levels.level_random_K33 import aux_level_random_K33
from levels.level_random_star import aux_level_random_star
from levels.level_random_loop import aux_level_random_loop

if __name__ == '__main__':
    # Maze.save_random_door_trees_list(aux_level_random_K2, n_files=100, i0=0)
    # Maze.save_random_door_trees_list(aux_level_random_K5, n_files=100, i0=0)
    # Maze.save_random_door_trees_list(aux_level_random_K33, n_files=100, i0=0)
    for aux_level in [#aux_level_random_K2,
                      #aux_level_random_K5,
                      #aux_level_random_K33,
                      aux_level_random_loop,
                      #aux_level_random_star,
                      ]:
        print(aux_level().name)
        Maze.save_random_door_trees_list(aux_level, n_files=100, i0=0)
    pass