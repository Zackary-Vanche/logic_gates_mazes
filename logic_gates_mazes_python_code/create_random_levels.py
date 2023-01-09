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
from levels.level_random_starting_point import aux_level_random_starting_point
from levels.level_random_loop import aux_level_random_loop
from levels.level_random_line import aux_level_random_line
from levels.level_random_binary_tree import aux_level_random_binary_tree
from levels.level_random_wheel import aux_level_random_wheel
from levels.level_random_bull import aux_level_random_bull
from levels.level_random_butterfly import aux_level_random_butterfly
from levels.level_random_come_back import aux_level_random_come_back


if __name__ == '__main__':
    # Maze.save_random_door_trees_list(aux_level_random_K2, n_files=100, i0=0)
    # Maze.save_random_door_trees_list(aux_level_random_K5, n_files=100, i0=0)
    # Maze.save_random_door_trees_list(aux_level_random_K33, n_files=100, i0=0)
    aux_level_list = [aux_level_random_K2,
                      aux_level_random_K5,
                      aux_level_random_K33,
                      aux_level_random_line,
                      aux_level_random_loop,
                      aux_level_random_star,
                      aux_level_random_starting_point,
                      aux_level_random_binary_tree,
                      aux_level_random_wheel,
                      aux_level_random_bull,
                      aux_level_random_butterfly,
                      aux_level_random_come_back
                      ]
    # for aux_level in aux_level_list:
    #     print(aux_level().name)
    #     Maze.save_random_door_trees_list(aux_level, n_files=1, i0=0)
    for aux_level in aux_level_list:
        print(aux_level().name)
        Maze.save_random_door_trees_list(aux_level, n_files=64, i0=0)
    pass
    # Maze.save_random_door_trees_list(aux_level_random_starting_point, n_files=64, i0=0)