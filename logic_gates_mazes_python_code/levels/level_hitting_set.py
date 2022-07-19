# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 20:15:12 2022

@author: utilisateur
"""

# Ensemble intersectant minimum

# (2 4 5)

# 0 2 6
# 1 4
# 2 5
# 2 7
# 3 4
# 3 5 6
# 4 5
# 5 7

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_hitting_set():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    
    SN3 = Switch(value=3, name='3')

    tree_list_0 = ["AND",
                   Tree.tree_list_OR(3),
                   Tree.tree_list_OR(2),
                   Tree.tree_list_OR(2),
                   Tree.tree_list_OR(2),
                   Tree.tree_list_OR(2),
                   Tree.tree_list_OR(3),
                   Tree.tree_list_OR(2),
                   Tree.tree_list_OR(2)]

    tree_list_1 = ["INFOREQU", Tree.tree_list_SUM(8), [None]]

    T0 = Tree(tree_list=tree_list_0,
              empty=True,
              name='T0',
              switches = [S0, S2, S6,
                          S1, S4,
                          S2, S5,
                          S2, S7,
                          S3, S4,
                          S3, S5, S6,
                          S4, S5,
                          S5, S7])
    T1 = Tree(tree_list=tree_list_1,
            empty=True,
            name='T1',
            switches = [S0, S1, S2, S3, S4, S5, S6, S7, SN3])
    
    R0 = Room(name='R0',
              position = [0, 0, 4, 2],
              switches_list = [S0, S1, S2, S3, S4, S5, S6, S7])
    R1 = Room(name='R1',
              position = [1, -2, 1, 1],
              switches_list = [])
    RE = Room(name='RE',
              position=[6, -2, 1, 1],
              is_exit=True)   # E pour exit ou end
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[3/8, 1/4])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=RE)

    level = Maze(start_room_index=0, 
                 exit_room_index=-1, 
                 rooms_list=[R0, R1, RE], 
                 doors_list = [D0, D1], 
                 fastest_solution='S2 S4 S5 D0 D1',
                 level_color=Levels_colors_list.FROM_HUE(0, sa=0.3, li=0.5),
                 name='Hitting set',
                 border = 30,
                 door_window_size = 700,
                 keep_proportions=True)

    return level