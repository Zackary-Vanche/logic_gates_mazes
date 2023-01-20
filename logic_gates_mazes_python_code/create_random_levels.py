# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 15:08:10 2023

@author: utilisateur
"""

from Maze import Maze
from Levels import Levels
import threading

if __name__ == '__main__':
    # for aux_level in aux_level_list:
    #     print(aux_level().name)
    #     Maze.save_random_door_trees_list(aux_level, n_files=1, i0=0)
    # for aux_level in Levels.aux_level_function_list:
    #     print(aux_level().name)
    #     Maze.save_random_door_trees_list(aux_level, n_files=1, i0=0)
    
    # Levels.aux_level_function_list.reverse()
    # for aux_level in Levels.aux_level_function_list:
    #     print(aux_level().name)
    #     Maze.save_random_door_trees_list(aux_level, n_files=1, i0=0)
    
    # Levels.aux_level_function_list.reverse()
        
    # for p in range(1):
    for aux_level in Levels.aux_level_function_list:
        print(aux_level().name)
        Maze.save_random_door_trees_list(aux_level, n_files=128, i0=0)

    #Maze.save_random_door_trees_list(aux_level, n_files=64, i0=0)

    # threading_list = []
    # for aux_level in Levels.aux_level_function_list:
    #     t = threading.Thread(target=lambda : print(aux_level.name))
    #     threading_list.append(t)
    # for t in threading_list:
    #     t.start()
    # for t in threading_list:
    #     t.join()
    # Maze.save_random_door_trees_list(aux_level_random_starting_point, n_files=64, i0=0)


















