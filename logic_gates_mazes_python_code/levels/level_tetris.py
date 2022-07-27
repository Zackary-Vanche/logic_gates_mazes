# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 11:44:05 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_tetris():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    
    SN0 = Switch(name='0', value=0)
    SN1 = Switch(name='1', value=1)
    SN2 = Switch(name='2', value=2)
    SN3 = Switch(name='3', value=3)
    SN4 = Switch(name='4', value=4)
    SN5 = Switch(name='5', value=5)
    SN6 = Switch(name='6', value=6)
    SN7 = Switch(name='7', value=7)
    SN8 = Switch(name='8', value=8)
    SN9 = Switch(name='9', value=9)
    SN10 = Switch(name='10', value=10)
    SN11 = Switch(name='11', value=11)

    T0 = Tree(tree_list=['EQUSET',
                         Tree.tree_list_BIN(4),
                         ['SUM', Tree.tree_list_BIN(4), [None]],
                         ['SUM', Tree.tree_list_BIN(4), [None]],
                         ['SUM', Tree.tree_list_BIN(4), [None]],
                         Tree.tree_list_BIN(4),
                         ['SUM', Tree.tree_list_BIN(4), [None]],
                         ['SUM', Tree.tree_list_BIN(4), [None]],
                         ['SUM', Tree.tree_list_BIN(4), [None]],
                         ['SUM', Tree.tree_list_BIN(4), [None]],
                         ['SUM', Tree.tree_list_BIN(4), [None]],
                         ['SUM', Tree.tree_list_BIN(4), [None]],
                         ['SUM', Tree.tree_list_BIN(4), [None]]] + [[None]]*12,
              empty=True,
              name='T0',
              switches = [S0, S1, S2, S3,
                          S0, S1, S2, S3, SN1,
                          S0, S1, S2, S3, SN2,
                          S0, S1, S2, S3, SN5,
                          S4, S5, S6, S7,
                          S4, S5, S6, S7, SN4,
                          S4, S5, S6, S7, SN5,
                          S4, S5, S6, S7, SN8,
                          S8, S9, S10, S11, SN2,
                          S8, S9, S10, S11, SN4,
                          S8, S9, S10, S11, SN5,
                          S8, S9, S10, S11, SN6,
                          SN0, SN1, SN2, SN3, SN4, SN5, SN6, SN7, SN8, SN9, SN10, SN11
                          ],
              cut_expression=True)

    R0 = Room(name='R0',
              position = [0, 0, 4, 3],
              switches_list = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11])
    RE = Room(name='RE',
              position=[1, 4, 2, 1],
              is_exit=True) # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=RE,
              relative_departure_coordinates=[1/2, 1],
              relative_arrival_coordinates=[1/2, 0])
    
    level = Maze(start_room_index=0, 
                 exit_room_index=-1, 
                 rooms_list=[R0, RE], 
                 doors_list=[D0], 
                 fastest_solution='S0 S8 S10 D0',
                 level_color=Levels_colors_list.FROM_HUE(0.2, sa=1, li=0.59),
                 name='Tetris',
                 door_window_size=800,
                 keep_proportions=True)

    return level