# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 22:14:16 2023

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_seven(EQU_list = [None, None, None, None, None, None, None,
                            None, None, None, None, None, None, None]):

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
    S28 = Switch(name='S28')
    S29 = Switch(name='S29')
    S30 = Switch(name='S30')
    S31 = Switch(name='S31')
    S32 = Switch(name='S32')
    S33 = Switch(name='S33')
    S34 = Switch(name='S34')
    S35 = Switch(name='S35')
    S36 = Switch(name='S36')
    S37 = Switch(name='S37')
    S38 = Switch(name='S38')
    S39 = Switch(name='S39')
    S40 = Switch(name='S40')
    S41 = Switch(name='S41')
    S42 = Switch(name='S42')
    S43 = Switch(name='S43')
    S44 = Switch(name='S44')
    S45 = Switch(name='S45')
    S46 = Switch(name='S46')
    S47 = Switch(name='S47')
    S48 = Switch(name='S48')
    
    MOD_list = [7 for i in range(14)]
    
    Slist0 = [S0, S1, S2, S3, S4, S5, S6]
    Slist1 = [S7, S8, S9, S10, S11, S12, S13]
    Slist2 = [S14, S15, S16, S17, S18, S19, S20]
    Slist3 = [S21, S22, S23, S24, S25, S26, S27]
    Slist4 = [S28, S29, S30, S31, S32, S33, S34]
    Slist5 = [S35, S36, S37, S38, S39, S40, S41]
    Slist6 = [S42, S43, S44, S45, S46, S47, S48]
    
    Slist = [[S0, S7, S14, S21, S28, S35, S42],
             [S1, S8, S15, S22, S29, S36, S43],
             [S2, S9, S16, S23, S30, S37, S44],
             [S3, S10, S17, S24, S31, S38, S45],
             [S4, S11, S18, S25, S32, S39, S46],
             [S5, S12, S19, S26, S33, S40, S47],
             [S6, S13, S20, S27, S34, S41, S48]]
    
    Slist7 = []
    for i in range(7):
        Slist7.append(EQU_list[i+7])
        Slist7.extend(Slist[i])
        Slist7.append(MOD_list[i+7])
    
    tree_list = ['EQU', [None], ['MOD', Tree.tree_list_BIN(7), [None]]]
    
    T0 = Tree(tree_list=tree_list,
              empty=True,
              name='T0',
              switches = [EQU_list[0]] + Slist0 + [MOD_list[0]])
    T1 = Tree(tree_list=tree_list,
              empty=True,
              name='T1',
              switches = [EQU_list[1]] + Slist1 + [MOD_list[1]])
    T2 = Tree(tree_list=tree_list,
              empty=True,
              name='T2',
              switches = [EQU_list[2]] + Slist2 + [MOD_list[2]])
    T3 = Tree(tree_list=tree_list,
              empty=True,
              name='T3',
              switches = [EQU_list[3]] + Slist3 + [MOD_list[3]])
    T4 = Tree(tree_list=tree_list,
              empty=True,
              name='T4',
              switches = [EQU_list[4]] + Slist4 + [MOD_list[4]])
    T5 = Tree(tree_list=tree_list,
              empty=True,
              name='T5',
              switches = [EQU_list[5]] + Slist5 + [MOD_list[5]])
    T6 = Tree(tree_list=tree_list,
              empty=True,
              name='T6',
              switches = [EQU_list[6]] + Slist6 + [MOD_list[6]])
    T7 = Tree(tree_list=['AND'] + [tree_list]*7,
              empty=True,
              name='T7',
              switches = Slist7,
              cut_expression=True,
              cut_expression_separator=' 7')
    
    ex = 7
    exe = 1
    ey = 0.35
    
    R0 = Room(name='R0',
              position = [0, 8, ex, ey],
              switches_list = Slist0)
    R1 = Room(name='R1',
              position = [0, 7, ex, ey],
              switches_list = Slist1)
    R2 = Room(name='R2',
              position = [0, 6, ex, ey],
              switches_list = Slist2)
    R3 = Room(name='R3',
              position = [0, 5, ex, ey],
              switches_list = Slist3)
    R4 = Room(name='R4',
              position = [0, 4, ex, ey],
              switches_list = Slist4)
    R5 = Room(name='R5',
              position = [0, 3, ex, ey],
              switches_list = Slist5)
    R6 = Room(name='R6',
              position = [0, 2, ex, ey],
              switches_list = Slist6)
    R7 = Room(name='R7',
              position = [ex/2-exe/2, 1, exe, ey],
              switches_list = [])
    RE = Room(name='RE',
              position=[ex/2-exe/2, 0, exe, ey],
              is_exit=True)   # E pour exit ou end
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1/2, 1/2],
              relative_arrival_coordinates=[1/2, 1/2])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=R4)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R4,
              room_arrival=R5)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R5,
              room_arrival=R6)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R6,
              room_arrival=R7)
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R7,
              room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0.925, sa=1, li=0.2),
                 name='Seven',
                 door_window_size=800,
                 keep_proportions=True,
                 y_separation=40,
                 border=40)

    return level