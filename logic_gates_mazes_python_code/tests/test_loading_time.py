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
from Logic_Gate import Logic_Gate
lt.append(time.time())
from Maze import Maze
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