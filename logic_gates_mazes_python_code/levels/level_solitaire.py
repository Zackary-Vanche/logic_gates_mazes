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
    
    S30 = Switch(name='S30')
    S31 = Switch(name='S31')
    S32 = Switch(name='S32', value=1)
    S33 = Switch(name='S33', value=1)
    S34 = Switch(name='S34', value=1)

    SN1 = Switch(value=1)
    
    tree_list_JUMPS = ['XOR',
                        Tree.tree_list_JUMP(5*2),
                        Tree.tree_list_JUMP(4*2),
                        Tree.tree_list_JUMP(3*2)]
    
    tree_list_0 = ['EQU',
                            ['SUM',
                                 ['SUM'] + [[None]]*15,
                                 ['SUM'] + [[None]]*15],
                            Tree.tree_list_BIN(5)]
    
    tree_list_2 = ['EQU',
                            ['SUM',
                                 ['SUM'] + [[None]]*15,
                                 ['SUM'] + [[None]]*15,
                                 [None]],
                            Tree.tree_list_BIN(5)]
    
    Slist0 = [S0, S1, S2, S3, S4,
              S5, S6, S7, S8,
              S9, S10, S11,
              S12, S13, 
              S14,
              S15, S16, S17, S18, S19,
              S20, S21, S22, S23,
              S24, S25, S26,
              S27, S28,
              S29,
              S30, S31, S32, S33, S34]
    
    Slist2 = [S0, S1, S2, S3, S4,
              S5, S6, S7, S8,
              S9, S10, S11,
              S12, S13, 
              S14,
              S15, S16, S17, S18, S19,
              S20, S21, S22, S23,
              S24, S25, S26,
              S27, S28,
              S29,
              SN1,
              S30, S31, S32, S33, S34]

    T0 = Tree(tree_list=tree_list_0,
              empty=True,
              name='T0',
              switches=Slist0,
              cut_expression=True,
              cut_expression_separator=')')
    T1 = Tree(tree_list=tree_list_0,
              empty=True,
              name='T1',
              switches=Slist0,
              cut_expression=True,
              cut_expression_separator=')')
    T2 = Tree(tree_list=tree_list_2,
              empty=True,
              name='T2',
              switches=Slist2,
              cut_expression=True,
              cut_expression_separator=')')
    T3 = Tree(tree_list=tree_list_2,
              empty=True,
              name='T3',
              switches=Slist2,
              cut_expression=True,
              cut_expression_separator=')')

    T4 = Tree(tree_list=['EQU', Tree.tree_list_BIN(15), Tree.tree_list_BIN(15)],
              empty=True,
              name='T4',
              switches = [S0, S1, S2, S3, S4,
                          S5, S6, S7, S8,
                          S9, S10, S11,
                          S12, S13, 
                          S14,
                          S15, S16, S17, S18, S19,
                          S20, S21, S22, S23,
                          S24, S25, S26,
                          S27, S28,
                          S29],
              cut_expression=True,
              cut_expression_separator=')')
    T5 = Tree(tree_list=tree_list_JUMPS,
              empty=True,
              name='T5',
              switches = [S0, S15,
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
                          ],
              cut_expression=True,
              cut_expression_separator=')')
    T6 = Tree(tree_list=tree_list_JUMPS,
              empty=True,
              name='T6',
              switches = [S0, S15,
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
                          ],
              cut_expression=True,
              cut_expression_separator=')')
    T7 = Tree(tree_list=tree_list_JUMPS,
              empty=True,
              name='T7',
              switches = [S4, S19,
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
                          S9, S24,
                          ],
              cut_expression=True,
              cut_expression_separator=')')

    T8 = Tree(tree_list=['AND',
                          ['EQU', [None], Tree.tree_list_BIN(15)],
                          ['EQU', [None], Tree.tree_list_BIN(15)]],
              empty=True,
              name='T8',
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
              position = [2, 2.5, 3, 0.5],
              switches_list = [])
    R1 = Room(name='R1',
              position = [0, 4, 3, 5],
              switches_list = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14],
              possible_switches_values=possible_switches_values)
    R2 = Room(name='R2',
              position = [4, 4, 3, 5],
              switches_list = [S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29],
              possible_switches_values=possible_switches_values)
    R3 = Room(name='R3',
              position = [1, 10, 5, 0.5],
              switches_list = [S30, S31, S32, S33, S34])
    RE = Room(name='RE',
              position=[2.5, 0.5, 2, 0.7],
              is_exit=True)   # E pour exit ou end
    
    p = 1/4.75

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[0, 0])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R0,
              room_arrival=R2,
              relative_departure_coordinates=[1, 1],
              relative_arrival_coordinates=[1, 0])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R1,
              room_arrival=R3,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[0, 0],
              relative_position=0.65)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=[1, 1],
              relative_arrival_coordinates=[1, 0],
              relative_position=0.65)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R3,
              room_arrival=R0,
              relative_position=p)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R3,
              room_arrival=R0,
              relative_position=2*p)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R3,
              room_arrival=R0,
              relative_position=3*p)
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R3,
              room_arrival=R0,
              relative_position=4*p)
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R0,
              room_arrival=RE)
#    [R0, R1, R2, R3]
#    [D0, D1, D2, D3, D4, D5, D6, D7, D8]
#    [, ]

    level = Maze(start_room_index=0, 
                 exit_room_index=-1, 
                 rooms_list=[R0, R1, R2, R3, RE], 
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8], 
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(0, sa=0.35, li=0.49),
                 name='Solitaire',
                 door_window_size=777,
                 keep_proportions=True)

    return level