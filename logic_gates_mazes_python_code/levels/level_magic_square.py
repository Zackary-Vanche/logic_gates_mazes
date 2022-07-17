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
    S24 = Switch(name='S24')
    S25 = Switch(name='S25')
    S26 = Switch(name='S26')
    S27 = Switch(name='S27')

    SN12 = Switch(value=12, name='12')
    
    tree_list_SUM = ['SUM',
                      Tree.tree_list_BIN(3),
                      Tree.tree_list_BIN(3),
                      Tree.tree_list_BIN(3)]
    
    tree_list_EQU = ['EQU', tree_list_SUM, [None]]

    T0 = Tree(tree_list=tree_list_EQU,
              empty=True,
              name='T0',
              switches = [S0, S1, S2, S3, S4, S5, S6, S7, S8, SN12])
    T1 = Tree(tree_list=tree_list_EQU,
              empty=True,
              name='T1',
              switches = [S9, S10, S11, S12, S13, S14, S15, S16, S17, SN12])
    T2 = Tree(tree_list=['EQU',
                             ['SUM',
                                  Tree.tree_list_BIN(3),
                                  Tree.tree_list_BIN(4),
                                  Tree.tree_list_BIN(3)],
                             [None]],
              empty=True,
              name='T2',
              switches = [S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, SN12])
    T3 = Tree(tree_list=['EQU',
                         tree_list_SUM,
                         ['SUM',
                          Tree.tree_list_BIN(3),
                          Tree.tree_list_BIN(3),
                          Tree.tree_list_BIN(4)],
                         tree_list_SUM],
              empty=True,
              name='T3',
              switches = [S0, S1, S2,
                          S9, S10, S11,
                          S18, S19, S20,
                          
                          S3, S4, S5,
                          S12, S13, S14,
                          S21, S22, S23, S24,
                          
                          S6, S7, S8,
                          S15, S16, S17,
                          S25, S26, S27,
                          ],
              cut_expression=True,
              cut_expression_separator=']')
    T4 = Tree(tree_list=['EQU',
                         tree_list_SUM,
                         tree_list_SUM],
              empty=True,
              name='T4',
              switches = [S0, S1, S2,
                          S12, S13, S14,
                          S25, S26, S27,
                          
                          S6, S7, S8,
                          S12, S13, S14,
                          S18, S19, S20],
              cut_expression=True,
              cut_expression_separator=']')
    T5 = Tree(tree_list=['AND',
                            ['DIFF'] + [Tree.tree_list_BIN(3)]*7 + [Tree.tree_list_BIN(4)] + [Tree.tree_list_BIN(3)],
                            ['INF', Tree.tree_list_BIN(3), Tree.tree_list_BIN(3)]],
              empty=True,
              name='T5',
              switches = [S0, S1, S2,
                          S3, S4, S5,
                          S6, S7, S8,
                          S9, S10, S11,
                          S12, S13, S14,
                          S15, S16, S17,
                          S18, S19, S20,
                          S21, S22, S23, S24,
                          S25, S26, S27, 
                          S0, S1, S2, S6, S7, S8],
              cut_expression=True)

    R0 = Room(name='R0',
              position = [4, -0.1, 3, 3],
              switches_list = [S0, S1, S2, S3, S4, S5, S6, S7, S8])
    R1 = Room(name='R1',
              position = [4, 4, 4, 4],
              switches_list = [S9, S10, S11, S12, S13, S14, S15, S16, S17])
    R2 = Room(name='R2',
              position = [-0.2, 4.5, 3, 4],
              switches_list = [S18, S19, S20, S21, S22, S23, S24, S25, S26, S27])
    R3 = Room(name='R3',
              position = [-0.2, 2.7, 0.7, 0.7],
              switches_list = [])
    R4 = Room(name='R4',
              position = [2.2, 2.7, 1.5, 1.5],
              switches_list = [])
    R5 = Room(name='R5',
              position = [2.2, 0.6, 1, 1],
              switches_list = [])
    RE = Room(name='RE',
              position=[2.1, -1.5, 1.2, 1],
              is_exit=True)   # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1/3, 1],
              relative_arrival_coordinates=[1/4, 0])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=[0, 1/4],
              relative_arrival_coordinates=[1, 0.5/4])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=[1/6, 0],
              relative_arrival_coordinates=[0.5/0.7, 1])
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=R4,
              relative_departure_coordinates=[1, 0.5/0.7],
              relative_arrival_coordinates=[0, 1/3])
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R4,
              room_arrival=R5,
              relative_departure_coordinates=[1/3, 1/3])
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R5,
              room_arrival=RE)

    level = Maze(start_room_index=0, 
             exit_room_index=-1, 
             rooms_list=[R0, R1, R2, R3, R4, R5, RE], 
             doors_list = [D0, D1, D2, D3, D4, D5], 
             fastest_solution=None,
             level_color=Levels_colors_list.GREY,
             name='Magic_square',
             door_window_size = 650,
             keep_proportions = True)
    
    return level

"""
('S2', 'S5', 'S8', 'D0', 'S10', 'S11', 'S16', 'S17', 'D1', 'S19', 'S22', 'D2', 'D3', 'D4')
('S1', 'S2', 'S4', 'S8', 'D0', 'S9', 'S10', 'S13', 'S15', 'S16', 'S17', 'D1', 'S18', 'S19', 'S21', 'D2', 'D3', 'D4')
('S1', 'S2', 'S7', 'S8', 'D0', 'S11', 'S14', 'S17', 'D1', 'S19', 'S22', 'D2', 'D3', 'D4')
('S2', 'S4', 'S7', 'S8', 'D0', 'S9', 'S10', 'S11', 'S13', 'S15', 'S16', 'D1', 'S18', 'S21', 'S22', 'D2', 'D3', 'D4')
('S0', 'S1', 'S2', 'S6', 'S8', 'D0', 'S10', 'S14', 'S16', 'S17', 'D1', 'S18', 'S19', 'S21', 'D2', 'D3', 'D4')
('S0', 'S2', 'S4', 'S6', 'S8', 'D0', 'S9', 'S11', 'S13', 'S15', 'S17', 'D1', 'S19', 'S22', 'D2', 'D3', 'D4')
('S0', 'S2', 'S6', 'S7', 'S8', 'D0', 'S10', 'S11', 'S14', 'S16', 'D1', 'S18', 'S21', 'S22', 'D2', 'D3', 'D4')
"""