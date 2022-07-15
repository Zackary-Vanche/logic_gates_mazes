#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 15:33:35 2022

@author: blanc-sablon
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_magic_square():
    
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
    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')
    S15 = Switch(name='S15')
    S16 = Switch(name='S16')
    S17 = Switch(name='S17')
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')
    S20 = Switch(name='S20')
    S21 = Switch(name='S21')
    S22 = Switch(name='S22')
    S23 = Switch(name='S23')

    SN8 = Switch(value=8, name='8')
    
    tree_list_SUM = ['SUM',
                     Tree.tree_list_BIN(3),
                     Tree.tree_list_BIN(3),
                     Tree.tree_list_BIN(3)]
    
#    tree_list_EQU = ['EQU'] + [tree_list_SUM]*8

    T0 = Tree(tree_list=['EQU',
                         tree_list_SUM,
                         tree_list_SUM,
                         ['SUM',
                          Tree.tree_list_BIN(3),
                          [None],
                          Tree.tree_list_BIN(3)],
                         tree_list_SUM,
                         ['SUM',
                          Tree.tree_list_BIN(3),
                          Tree.tree_list_BIN(3),
                          [None]],
                         tree_list_SUM,
                         tree_list_SUM,
                         tree_list_SUM
                         ],
              empty=True,
              name='T0',
              switches = [
                          S0, S1, S2,
                          S3, S4, S5,
                          S6, S7, S8,

                          S9, S10, S11,
                          S12, S13, S14,
                          S15, S16, S17,
                          
                          S18, S19, S20,
                          SN8,
                          S21, S22, S23,
                          
                          S0, S1, S2,
                          S9, S10, S11,
                          S18, S19, S20,
                          
                          S3, S4, S5,
                          S12, S13, S14,
                          SN8,
                          
                          S6, S7, S8,
                          S15, S16, S17,
                          S21, S22, S23,
                          
                          S0, S1, S2,
                          S12, S13, S14,
                          S21, S22, S23,
                          
                          S6, S7, S8,
                          S12, S13, S14,
                          S18, S19, S20
                          ],
        cut_expression=True,
        cut_expression_separator=')')
    R0 = Room(name='R0',
              position = [0, 0, 3, 8],
              switches_list = [S0, S1, S2,
                               S3, S4, S5,
                               S6, S7, S8,
                               S9, S10, S11,
                               S12, S13, S14,
                               S15, S16, S17,
                               S18, S19, S20,
                               S21, S22, S23])
    RE = Room(name='RE',
              position=[4, 3, 1, 2],
              is_exit=True)   # E pour exit ou end
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=RE,
              relative_departure_coordinates=[5/6, 1/2])
    
    level = Maze(start_room_index=0, 
             exit_room_index=-1, 
             rooms_list=[R0, RE], 
             doors_list = [D0], 
             fastest_solution=None,
             level_color=Levels_colors_list.GREY,
             name='Magic_square',
             door_window_size = 500,
             keep_proportions = True)
    
    return level