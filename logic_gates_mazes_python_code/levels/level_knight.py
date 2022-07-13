#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 15:46:06 2022

@author: blanc-sablon
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_knight():
    
    v = 0
    
    S0 = Switch(name='S0')
    S1 = Switch(name='S1', value=v)
    S2 = Switch(name='S2', value=v)
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7', value=v)
    S8 = Switch(name='S8', value=v)
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    S12 = Switch(name='S12', value=v)
    S13 = Switch(name='S13', value=v)
    S14 = Switch(name='S14', value=v)
    S15 = Switch(name='S15')
    S16 = Switch(name='S16', value=v)
    S17 = Switch(name='S17')
    S18 = Switch(name='S18')
    S19 = Switch(name='S19', value=v)
    S20 = Switch(name='S20')
    S21 = Switch(name='S21', value=v)
    S22 = Switch(name='S22')
    S23 = Switch(name='S23')
    S24 = Switch(name='S24', value=v)
    S25 = Switch(name='S25', value=v)
    S26 = Switch(name='S26')
    S27 = Switch(name='S27', value=v)
    S28 = Switch(name='S28', value=v)
    S29 = Switch(name='S29')
    S30 = Switch(name='S30', value=v)
    S31 = Switch(name='S31')
    S32 = Switch(name='S32', value=v)
    S33 = Switch(name='S33', value=v)
    S34 = Switch(name='S34')
    S35 = Switch(name='S35')
    S36 = Switch(name='S36')
    S37 = Switch(name='S37', value=v)
    S38 = Switch(name='S38')
    S39 = Switch(name='S39', value=v)
    S40 = Switch(name='S40')
    S41 = Switch(name='S41')
    S42 = Switch(name='S42', value=v)
    S43 = Switch(name='S43')

    SN0 = Switch(value=0, name='0')
    SN1 = Switch(value=1, name='1')
    SN2 = Switch(value=2, name='2')
    SN3 = Switch(value=3, name='3')
    
    tree_list_bin = ['BIN', [None], [None]] # 2
    tree_list_inf = ['INF', tree_list_bin, [None]] # 3
    tree_list_minus = ['MINUS', tree_list_bin] # 2
    tree_list_diff = ['SUM', tree_list_bin, tree_list_minus] # 4
    tree_list_abs = ['ABS', tree_list_diff] # 4
    tree_list_equ = ['EQUSET', tree_list_abs, tree_list_abs, [None], [None]] # 10
    tree_list_tot = ['AND', tree_list_inf, tree_list_equ] # 23

    T0 = Tree(tree_list=tree_list_tot,
              empty=True,
              name='T0',
              switches = [S2, S3, SN3,
                          SN0, SN0, S0, S1, 
                          SN0, SN0, S2, S3,
                          SN1,
                          SN2],
              cut_expression=False)
    T1 = Tree(tree_list=tree_list_tot,
              empty=True,
              name='T1',
              switches = [S6, S7, SN3,
                          S0, S1, S4, S5,
                          S2, S3, S6, S7,
                          SN1,
                          SN2])
    T2 = Tree(tree_list=tree_list_tot,
              empty=True,
              name='T2',
              switches = [S10, S11, SN3,
                          S4, S5, S8, S9,
                          S6, S7, S10, S11,
                          SN1,
                          SN2])
    T3 = Tree(tree_list=tree_list_tot,
              empty=True,
              name='T3',
              switches = [S14, S15, SN3,
                          S8, S9, S12, S13,
                          S10, S11, S14, S15,
                          SN1,
                          SN2])
    T4 = Tree(tree_list=tree_list_tot,
              empty=True,
              name='T4',
              switches = [S18, S19, SN3,
                          S12, S13, S16, S17,
                          S14, S15, S18, S19,
                          SN1,
                          SN2])
    T5 = Tree(tree_list=tree_list_tot,
              empty=True,
              name='T5',
              switches = [S22, S23, SN3,
                          S16, S17, S20, S21,
                          S18, S19, S22, S23,
                          SN1,
                          SN2])
    T6 = Tree(tree_list=tree_list_tot,
              empty=True,
              name='T6',
              switches = [S26, S27, SN3,
                          S20, S21, S24, S25,
                          S22, S23, S26, S27,
                          SN1,
                          SN2])
    T7 = Tree(tree_list=tree_list_tot,
              empty=True,
              name='T7',
              switches = [S30, S31, SN3,
                          S24, S25, S28, S29,
                          S26, S27, S30, S31,
                          SN1,
                          SN2])
    T8 = Tree(tree_list=tree_list_tot,
              empty=True,
              name='T8',
              switches = [S34, S35, SN3,
                          S28, S29, S32, S33,
                          S30, S31, S34, S35,
                          SN1,
                          SN2])
    T9 = Tree(tree_list=tree_list_tot,
              empty=True,
              name='T9',
              switches = [S38, S39, SN3,
                          S32, S33, S36, S37,
                          S34, S35, S38, S39,
                          SN1,
                          SN2])
    T10 = Tree(tree_list=tree_list_tot,
               empty=True,
               name='T10',
               switches = [S42, S43, SN3,
                          S36, S37, S40, S41,
                          S38, S39, S42, S43,
                          SN1,
                          SN2])
    T11 = Tree(tree_list=['DIFF'] + [['BIN', [None], [None], [None], [None]]]*11,
               empty=True,
               name='T11',
               switches = [S0, S1, S2, S3,
                           S4, S5, S6, S7,
                           S8, S9, S10, S11,
                           S12, S13, S14, S15,
                           S16, S17, S18, S19,
                           S20, S21, S22, S23,
                           S24, S25, S26, S27,
                           S28, S29, S30, S31,
                           S32, S33, S34, S35,
                           S36, S37, S38, S39,
                           S40, S41, S42, S43],
                cut_expression=True)

    l = 1
    L = 4
    a = L + 1.5
    d = 1.55
    e = d/2

    R0 = Room(name='R0',
              position = [0, 0, L, l],
              switches_list = [S0, S1, S2, S3])
    R1 = Room(name='R1',
              position = [a, e, L, l],
              switches_list = [S4, S5, S6, S7])
    R2 = Room(name='R2',
              position = [0, d, L, l],
              switches_list = [S8, S9, S10, S11])
    R3 = Room(name='R3',
              position = [a, d+e, L, l],
              switches_list = [S12, S13, S14, S15])
    R4 = Room(name='R4',
              position = [0, 2*d, L, l],
              switches_list = [S16, S17, S18, S19])
    R5 = Room(name='R5',
              position = [a, 2*d+e, L, l],
              switches_list = [S20, S21, S22, S23])
    R6 = Room(name='R6',
              position = [0, 3*d, L, l],
              switches_list = [S24, S25, S26, S27])
    R7 = Room(name='R7',
              position = [a, 3*d+e, L, l],
              switches_list = [S28, S29, S30, S31])
    R8 = Room(name='R8',
              position = [0, 4*d, L, l],
              switches_list = [S32, S33, S34, S35])
    R9 = Room(name='R9',
              position = [a, 4*d+e, L, l],
              switches_list = [S36, S37, S38, S39])
    R10 = Room(name='R10',
               position = [0, 5*d, L, l],
               switches_list = [S40, S41, S42, S43])
    R11 = Room(name='R11',
               position = [a, 5*d+e, l, l],
               switches_list = [])
    RE = Room(name='RE',
              position=[a+L-l, 5*d+e, l, l],
              is_exit=True)   # E pour exit ou end
    
    rp = 0.5
    rc1 = [3/4, 1/2]
    rc2 = [1/4, 1/2]

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp,
              relative_departure_coordinates=rc1,
              relative_arrival_coordinates=rc2)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2,
              relative_position=rp,
              relative_departure_coordinates=rc2,
              relative_arrival_coordinates=rc1)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3,
              relative_position=rp,
              relative_departure_coordinates=rc1,
              relative_arrival_coordinates=rc2)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=R4,
              relative_position=rp,
              relative_departure_coordinates=rc2,
              relative_arrival_coordinates=rc1)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R4,
              room_arrival=R5,
              relative_position=rp,
              relative_departure_coordinates=rc1,
              relative_arrival_coordinates=rc2)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R5,
              room_arrival=R6,
              relative_position=rp,
              relative_departure_coordinates=rc2,
              relative_arrival_coordinates=rc1)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R6,
              room_arrival=R7,
              relative_position=rp,
              relative_departure_coordinates=rc1,
              relative_arrival_coordinates=rc2)
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R7,
              room_arrival=R8,
              relative_position=rp,
              relative_departure_coordinates=rc2,
              relative_arrival_coordinates=rc1)
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R8,
              room_arrival=R9,
              relative_position=rp,
              relative_departure_coordinates=rc1,
              relative_arrival_coordinates=rc2)
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R9,
              room_arrival=R10,
              relative_position=rp,
              relative_departure_coordinates=rc2,
              relative_arrival_coordinates=rc1)
    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R10,
               room_arrival=R11,
               relative_position=rp,
               relative_departure_coordinates=rc1,
               relative_arrival_coordinates=[1, 1/2])
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R11,
               room_arrival=RE,
               relative_position=rp)

    level = Maze(start_room_index=0, 
                 exit_room_index=-1, 
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, RE], 
                 doors_list = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11], 
                 fastest_solution="S1 S2 D0 S7 D1 S8 D2 S12 S13 S14 D3 S16 S19 D4 S21 D5 S24 S25 S27 D6 S28 S30 D7 S32 S33 D8 S37 S39 D9 S42 D10 D11",
                 level_color=Levels_colors_list.FROM_HUE(0.6, sa=0.12, li=0.45),
                 name='Knight',
                 border = 30,
                 door_window_size = 700,
                 keep_proportions=True)

    return level