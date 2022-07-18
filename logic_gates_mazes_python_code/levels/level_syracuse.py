#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:14:47 2022

@author: blanc-sablon
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_syracuse(test_solution=False):

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8', value=1)
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')
    S15 = Switch(name='S15')
    
    SN1 = Switch(name='1', value=1)
    SN2 = Switch(name='2', value=2)
    SN3 = Switch(name='3', value=3)
    SN228 = Switch(name='228', value=228)
    
    tree_list_0 = ['EQU',
                   Tree.tree_list_BIN(8),
                   Tree.tree_list_BIN(8)]
    
    tree_list_1 = ['EQU',
                       Tree.tree_list_BIN(8),
                       ['DIV',
                            Tree.tree_list_BIN(8),
                            [None]]]
    
    tree_list_prod = ['PROD', [None], Tree.tree_list_BIN(8)]
    tree_list_3plus1 = ['SUM', tree_list_prod, [None]]
    tree_list_equ_3plus1 = ['EQU', Tree.tree_list_BIN(8), tree_list_3plus1]
    tree_list_equ_mod = ['EQU', [None], [None]] 
    tree_list_2 = ['AND', tree_list_equ_mod, tree_list_equ_3plus1]

    tree_list_3 = ['EQU', Tree.tree_list_BIN(8), Tree.tree_list_BIN(8), [None]]

    T0 = Tree(tree_list=tree_list_0,
              empty=True,
              name='T0',
              switches = [S0, S1, S2, S3, S4, S5, S6, S7,
                          S8, S9, S10, S11, S12, S13, S14, S15])
    T1 = Tree(tree_list=tree_list_1,
              empty=True,
              name='T1',
              switches = [S0, S1, S2, S3, S4, S5, S6, S7,
                          S8, S9, S10, S11, S12, S13, S14, S15,
                          SN2])
    T2 = Tree(tree_list=tree_list_2,
              empty=True,
              name='T2',
              switches = [S8,
                          SN1,
                          S0, S1, S2, S3, S4, S5, S6, S7,
                          SN3,
                          S8, S9, S10, S11, S12, S13, S14, S15,
                          SN1],
              cut_expression=True,
              cut_expression_separator=']')
    T3 = Tree(tree_list=tree_list_3,
              empty=True,
              name='T3',
              switches = [S0, S1, S2, S3, S4, S5, S6, S7,
                          S8, S9, S10, S11, S12, S13, S14, S15,
                          SN228])

    R0 = Room(name='R0',
              position = [0, 0, 4, 2],
              switches_list = [S0, S1, S2, S3, S4, S5, S6, S7])
    R1 = Room(name='R1',
              position = [0, 4, 4, 2],
              switches_list = [S8, S9, S10, S11, S12, S13, S14, S15])
    RE = Room(name='RE',
              position=[0, 8, 4, 1],
              is_exit=True)   # E pour exit ou end

    p = 0.17

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[p, 1/2],
              relative_arrival_coordinates=[p, 1/2])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R0,
              relative_departure_coordinates=[1-p, 1/2],
              relative_arrival_coordinates=[1-p, 1/2])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R1,
              room_arrival=R0,
              relative_departure_coordinates=[1-2*p, 1/2],
              relative_arrival_coordinates=[1-2*p, 1/2])
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R1,
              room_arrival=RE)    

    level = Maze(start_room_index=0, 
                 exit_room_index=-1, 
                 rooms_list=[R0, R1, RE], 
                 doors_list = [D0, D1, D2, D3], 
                 fastest_solution='S0 D0 S8 S9 D1 S0 S1 D0 S9 S10 D1 S1 S2 D0 S10 S11 D1 S2 S3 D0 S11 S12 D1 S3 S4 D0 S8 S10 S12 D2 S0 S2 S4 D0 S8 S9 S10 S11 D1 S0 S1 S2 S3 D0 S9 S10 S11 S12 D1 S1 S2 S3 S4 D0 S10 S11 S12 S13 D1 S2 S3 S4 S5 D0 S8 S10 S13 D2 S0 S2 S5 D0 S8 S9 S10 S12 D1 S0 S1 S2 S4 D0 S9 S10 S11 S13 D1 S1 S2 S3 S5 D0 S8 S10 S13 D2 S0 S2 S5 D0 S8 S9 S12 S13 D1 S0 S1 S4 S5 D0 S8 S11 S13 D2 S0 S3 S5 D0 S8 S10 S11 S12 D1 S0 S2 S3 S4 D0 S8 S12 D2 S0 S4 D0 S8 S11 D1 S0 S3 D0 S9 S12 D1 S1 S4 D0 S10 S13 D1 S2 S5 D0 S11 S14 D1 S3 S6 D0 S8 S10 S12 S14 D2 S0 S2 S4 S6 D0 S8 S9 S10 S11 S13 S14 D1 S0 S1 S2 S3 S5 S6 D0 S9 S10 S11 S12 S14 S15 D1 S1 S2 S3 S4 S6 S7 D0 S8 S10 S13 S15 D2 S0 S2 S5 S7 D0 S8 S9 S12 S14 D1 S0 S1 S4 S6 D0 S9 S10 S13 S15 D1 S1 S2 S5 S7 D0 S8 S10 S15 D2 S0 S2 S7 D0 S8 S9 S14 S15 D1 S0 S1 S6 S7 D0 S8 S11 S13 S15 D2 S0 S3 S5 S7 D0 S8 S10 S11 S12 S13 S14 D1 S0 S2 S3 S4 S5 S6 D0 S9 S11 S12 S13 S14 S15 D1 S1 S3 S4 S5 S6 S7 D0 S8 S10 S12 S15 D2 S0 S2 S4 S7 D0 S8 S9 S11 S14 D1 S0 S1 S3 S6 D0 S9 S10 S12 S15 D1 S1 S2 S4 S7 D0 D3',
                 level_color=Levels_colors_list.BROWN_AND_BLUE,
                 name='Syracuse',
                 door_window_size = 800,
                 keep_proportions = True,
                 border=20)
    
    return level