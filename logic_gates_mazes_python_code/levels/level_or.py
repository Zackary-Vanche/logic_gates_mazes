#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 14:36:20 2022

@author: blanc-sablon
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_or():
    
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    
    T0 = Tree(tree_list=Tree.tree_list_OR(2), 
              empty=True, 
              name='T0', 
              switches = [S0, S1])
    T1 = Tree(tree_list=Tree.tree_list_OR(2), 
              empty=True, 
              name='T1', 
              switches = [S1, S2])
    T2 = Tree(tree_list=Tree.tree_list_from_str('FFF'), 
              empty=True, 
              name='T2', 
              switches = [S0, S1, S2])
    
    position_R0 = [0,0,1,1]
    position_R1 = [3,0,1,1]
    position_R2 = [6,0,1,1]
    position_RE = [9,0,1,1]
    
    R0 = Room(name='R0', position = position_R0, switches_list = [S0])
    R1 = Room(name='R1', position = position_R1, switches_list = [S1])
    R2 = Room(name='R2', position = position_R2, switches_list = [S2])
    RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
    
    D0 = Door(two_way = True, 
          tree = T0, 
          name='D0', 
          room_departure = R0, 
          room_arrival = R1)
    D1 = Door(two_way = True, 
          tree = T1, 
          name='D1', 
          room_departure = R1, 
          room_arrival = R2)
    D2 = Door(two_way = False, 
          tree = T2, 
          name='D2', 
          room_departure = R2, 
          room_arrival = RE)
    
    level = Maze(start_room_index=0, 
             exit_room_index=-1, 
             rooms_list=[R0, R1, R2, RE], 
             doors_list = [D0, D1, D2], 
             fastest_solution="S0 D0 S1 D0 S0 D0 D1 S2 D1 S1 D1 S2 D2",
             level_color=Levels_colors_list.FROM_HUE(0.9),
             name='OR',
             door_window_size = 500,
             keep_proportions = True)
    
    return level