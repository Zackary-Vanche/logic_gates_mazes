#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 10:59:30 2022

@author: blanc-sablon
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_solitaire(fast_solution_finding=False):

    S0 = Switch(name='S0')
    S1 = Switch(name='S1', value=1)
    S2 = Switch(name='S2', value=1)
    S3 = Switch(name='S3', value=1)
    S4 = Switch(name='S4', value=1)
    S5 = Switch(name='S5', value=1)
    S6 = Switch(name='S6', value=1)
    S7 = Switch(name='S7', value=1)
    S8 = Switch(name='S8', value=1)
    S9 = Switch(name='S9', value=1)
    S10 = Switch(name='S10', value=1)
    S11 = Switch(name='S11', value=1)
    S12 = Switch(name='S12', value=1)
    S13 = Switch(name='S13', value=1)
    S14 = Switch(name='S14', value=1)
    S15 = Switch(name='S15')
    S16 = Switch(name='S16', value=1)
    S17 = Switch(name='S17', value=1)
    S18 = Switch(name='S18', value=1)
    S19 = Switch(name='S19', value=1)
    S20 = Switch(name='S20', value=1)
    S21 = Switch(name='S21', value=1)
    S22 = Switch(name='S22', value=1)
    S23 = Switch(name='S23', value=1)
    S24 = Switch(name='S24', value=1)
    S25 = Switch(name='S25', value=1)
    S26 = Switch(name='S26', value=1)
    S27 = Switch(name='S27', value=1)
    S28 = Switch(name='S28', value=1)
    S29 = Switch(name='S29', value=1)

    SN1 = Switch(value=1)
    
    tree_list_SUM_5 = ['SUM'] + [Tree.tree_list_XOR(2)]*5
    
    tree_list_1 = ['EQU',
                   ['SUM',
                    tree_list_SUM_5,
                    tree_list_SUM_5,
                    tree_list_SUM_5],
                   [None]]
    
    Slist1 = [
              S0, S15,
              S1, S16,
              S2, S17,
              S3, S18,
              S4, S19,
              S5, S20,
              S6, S21,
              S7, S22,
              S8, S23,
              S9, S24,
              S10, S25,
              S11, S26,
              S12, S27,
              S13, S28,
              S14, S29,
              Switch(value=3)]
    
    # tree_list_1 = [None]
    # Slist1 = [SN1]

    T0 = Tree(tree_list=['AND',
                         tree_list_1,
                         ['XOR',
                          Tree.tree_list_JUMP(5*2),
                          Tree.tree_list_JUMP(4*2),
                          Tree.tree_list_JUMP(3*2),
                          Tree.tree_list_JUMP(5*2),
                          Tree.tree_list_JUMP(4*2),
                          Tree.tree_list_JUMP(3*2),
                          Tree.tree_list_JUMP(5*2),
                          Tree.tree_list_JUMP(4*2),
                          Tree.tree_list_JUMP(3*2)]],
              empty=True,
              name='T0',
              switches=Slist1 + [S0, S15,
                                 S1, S16,
                                 S2, S17,
                                 S3, S18,
                                 S4, S19,
                                 S5, S20,
                                 S6, S21,
                                 S7, S22,
                                 S8, S23,
                                 S9, S24,
                                 S10, S25,
                                 S11, S26,
                  
                                 S0, S15,
                                 S5, S20,
                                 S9, S24,
                                 S12, S27,
                                 S14, S29,
                                 S1, S16,
                                 S6, S21,
                                 S10, S25,
                                 S13, S28,
                                 S2, S17,
                                 S7, S22,
                                 S11, S26,
              
                                 S4, S19,
                                 S8, S23,
                                 S11, S26,
                                 S13, S28,
                                 S14, S29,
                                 S3, S18,
                                 S7, S22,
                                 S10, S25,
                                 S12, S27,
                                 S2, S17,
                                 S6, S21,
                                 S9, S24,],
              cut_expression=True,
              cut_expression_separator=')')
    T1 = Tree(tree_list=['EQU', Tree.tree_list_BIN(15), Tree.tree_list_BIN(15)],
              empty=True,
              name='T1',
              switches=[S0, S1, S2, S3, S4,
                        S5, S6, S7, S8,
                        S9, S10, S11,
                        S12, S13, 
                        S14,
                        S15, S16, S17, S18, S19,
                        S20, S21, S22, S23,
                        S24, S25, S26,
                        S27, S28,
                        S29,],
              cut_expression=True,
              cut_expression_separator=')')
    T2 = Tree(tree_list=['AND',
                          ['EQU', [None], Tree.tree_list_BIN(15)],
                          ['EQU', [None], Tree.tree_list_BIN(15)]],
              empty=True,
              name='T2',
              switches = [SN1,
                          S0, S1, S2, S3, S4,
                          S5, S6, S7, S8,
                          S9, S10, S11,
                          S12, S13, 
                          S14,
                          SN1,
                          S15, S16, S17, S18, S19,
                          S20, S21, S22, S23,
                          S24, S25, S26,
                          S27, S28,
                          S29],
              cut_expression=True,
              cut_expression_separator=')')
    
    # T2 = Tree(tree_list=['EQU', Tree.tree_list_BIN(15), Tree.tree_list_BIN(15)],
    #           empty=True,
    #           name='T2',
    #           switches=[S0, S1, S2, S3, S4,
    #                     S5, S6, S7, S8,
    #                     S9, S10, S11,
    #                     S12, S13, 
    #                     S14,
    #                     S15, S16, S17, S18, S19,
    #                     S20, S21, S22, S23,
    #                     S24, S25, S26,
    #                     S27, S28,
    #                     S29,],
    #           cut_expression=True,
    #           cut_expression_separator=')')
    
    if fast_solution_finding:
        possible_switches_values = [[1, 1, 1, 0, 0,
                                     0, 0, 0, 0,
                                     0, 0, 0,
                                     0, 0,
                                     0],
                                    [0, 1, 1, 1, 0,
                                     0, 0, 0, 0,
                                     0, 0, 0,
                                     0, 0,
                                     0],
                                    [0, 0, 1, 1, 1,
                                     0, 0, 0, 0,
                                     0, 0, 0,
                                     0, 0,
                                     0],
                                    [0, 0, 0, 0, 0,
                                     1, 1, 1, 0,
                                     0, 0, 0,
                                     0, 0,
                                     0],
                                    [0, 0, 0, 0, 0,
                                     0, 1, 1, 1,
                                     0, 0, 0,
                                     0, 0,
                                     0],
                                    [0, 0, 0, 0, 0,
                                     0, 0, 0, 0,
                                     1, 1, 1,
                                     0, 0,
                                     0],
                                    
                                    [1, 0, 0, 0, 0,
                                     1, 0, 0, 0,
                                     1, 0, 0,
                                     0, 0,
                                     0],
                                    [0, 0, 0, 0, 0,
                                     1, 0, 0, 0,
                                     1, 0, 0,
                                     1, 0,
                                     0],
                                    [0, 0, 0, 0, 0,
                                     0, 0, 0, 0,
                                     1, 0, 0,
                                     1, 0,
                                     1],
                                    [0, 1, 0, 0, 0,
                                     0, 1, 0, 0,
                                     0, 1, 0,
                                     0, 0,
                                     0],
                                    [0, 0, 0, 0, 0,
                                     0, 1, 0, 0,
                                     0, 1, 0,
                                     0, 1,
                                     0],
                                    [0, 0, 1, 0, 0,
                                     0, 0, 1, 0,
                                     0, 0, 1,
                                     0, 0,
                                     0],
                                    
                                    [0, 0, 0, 0, 1,
                                     0, 0, 0, 1,
                                     0, 0, 1,
                                     0, 0,
                                     0],
                                    [0, 0, 0, 0, 0,
                                     0, 0, 0, 1,
                                     0, 0, 1,
                                     0, 1,
                                     0],
                                    [0, 0, 0, 0, 0,
                                     0, 0, 0, 0,
                                     0, 0, 1,
                                     0, 1,
                                     1],
                                    [0, 0, 0, 1, 0,
                                     0, 0, 1, 0,
                                     0, 1, 0,
                                     0, 0,
                                     0],
                                    [0, 0, 0, 0, 0,
                                     0, 0, 1, 0,
                                     0, 1, 0,
                                     1, 0,
                                     0],
                                    [0, 0, 1, 0, 0,
                                     0, 1, 0, 0,
                                     1, 0, 0,
                                     0, 0,
                                     0],]
        for l in possible_switches_values:
            assert sum(l) == 3, l
        assert len(possible_switches_values) == 18
    else:
        possible_switches_values = None

    R0 = Room(name='R0',
              position = [0, 4, 3, 5],
              switches_list = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14],
              possible_switches_values=possible_switches_values)
    R1 = Room(name='R1',
              position = [4.15, 4, 3, 5],
              switches_list = [S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29],
              possible_switches_values=possible_switches_values)
    RE = Room(name='RE',
              position=[4.15, 2.2, 3, 0.75],
              is_exit=True)   # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1, 1],
              relative_arrival_coordinates=[0, 1])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R0,
              relative_departure_coordinates=[0, 0],
              relative_arrival_coordinates=[1, 0])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R1,
              room_arrival=RE,
              relative_departure_coordinates=[1/2, 0],
              relative_arrival_coordinates=[1/2, 1])

    level = Maze(start_room_index=0, 
                 exit_room_index=-1, 
                 rooms_list=[R0, R1, RE], 
                 doors_list=[D0, D1, D2], 
                 fastest_solution='''S0 S1 S2 D1
S15 S16 S17 D0
S2 S7 S11 D1
S17 S22 S26 D0
S1 S2 S3 D1
S16 S17 S18 D0
S0 S1 S2 D1
S15 S16 S17 D0
S5 S6 S7 D1
S20 S21 S22 D0
S5 S9 S12 D1
S20 S24 S27 D0
S4 S8 S11 D1
S19 S23 S26 D0
S8 S11 S13 D1
S23 S26 S28 D0
S2 S7 S11 D1
S17 S22 S26 D0
S8 S11 S13 D1
S23 S26 S28 D0
S11 S13 S14 D1
S26 S28 S29 D0
S9 S10 S11 D1
S24 S25 S26 D0
S0 S5 S9 D1
S15 S20 S24 D2'''.replace('\n', ''),
                 level_color=Levels_colors_list.FROM_HUE(0, sa=0.35, li=0.49),
                 name='Solitaire',
                 door_window_size=777,
                 keep_proportions=True)

    return level