# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:19:57 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_icone():
    
    # Only used to make the icone of the game
    
    S0 = Switch(name='S0')
    
    T0 = Tree(tree_list=[None], 
      empty=True, 
      name='T0', 
          switches = [S0])
    
    c = 1.5
    
    position_R0 = [0,0,c,c]
    position_RE = [2,0,c,c]
    
    R0 = Room(name='R0', position = position_R0, switches_list = [S0])
    RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
    
    D0 = Door(two_way = True, 
          tree = T0, 
          name='D0', 
          room_departure = R0, 
          room_arrival = RE)

    level = Maze(start_room_index=0, 
             exit_room_index=-1, 
             rooms_list=[R0, RE], 
             doors_list = [D0], 
             fastest_solution="S0 D0",
             level_color=Levels_colors_list.BLACK_AND_WHITE_2,
             name='Icone',
             door_window_size = 500,
             keep_proportions = True)
    
    return level