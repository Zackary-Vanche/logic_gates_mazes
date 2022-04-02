# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 17:21:23 2022

@author: utilisateur
"""

import os
import time
import numpy as np

lt = []
lt.append(time.time())
from Color import Color
lt.append(time.time())
from Door import Door
lt.append(time.time())
from fonction_affine import fonction_affine
lt.append(time.time())
from Game import Game
lt.append(time.time())
from Levels import Levels
lt.append(time.time())
from Levels_colors_list import Levels_colors_list
lt.append(time.time())
from level_backward import level_backward
lt.append(time.time())
from level_binary import level_binary
lt.append(time.time())
from level_cartesian import level_cartesian
lt.append(time.time())
from Level_color import Level_color
lt.append(time.time())
from level_crossroad import level_crossroad
lt.append(time.time())
from level_crystal import level_crystal
lt.append(time.time())
from level_dead_ends import level_dead_ends
lt.append(time.time())
from level_electricity import level_electricity
lt.append(time.time())
from level_fluid import level_fluid
lt.append(time.time())
from level_graph import level_graph
lt.append(time.time())
from level_hello_world import level_hello_world
lt.append(time.time())
from level_icone import level_icone
lt.append(time.time())
from level_infinity import level_infinity
lt.append(time.time())
from level_linear import level_linear
lt.append(time.time())
from level_loop import level_loop
lt.append(time.time())
from level_manhattan_distance import level_manhattan_distance
lt.append(time.time())
from level_odd import level_odd
lt.append(time.time())
from level_parallel import level_parallel
lt.append(time.time())
from level_point_of_no_return import level_point_of_no_return
lt.append(time.time())
from level_recurrence import level_recurrence
lt.append(time.time())
from level_sinusoidal import level_sinusoidal
lt.append(time.time())
from level_square import level_square
lt.append(time.time())
from level_tetrahedron import level_tetrahedron
lt.append(time.time())
from level_xor import level_xor
lt.append(time.time())
from Logic_Gate import Logic_Gate
lt.append(time.time())
from Maze import Maze
lt.append(time.time())
from moindres_carres import moindres_carres
lt.append(time.time())
from Room import Room
lt.append(time.time())
from Switch import Switch
lt.append(time.time())
from Tree import Tree
lt.append(time.time())

if __name__ == "__main__":
    
    # racine = __file__
    # racine = racine.split('\\')
    # del racine[-1]
    # racine = '/'.join(racine)
    # n_lines = 0
    # l = []
    # for file in os.listdir(racine):
    #     # file = '/'.join([racine,file])
    #     if file.split('.')[-1] == 'py':
    #         print('from {0} import {0}'.format(file.split('.')[0]))
    
    for i in range(len(lt)-1):
        print(lt[i+1]-lt[i])