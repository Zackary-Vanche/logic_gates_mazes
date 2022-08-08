#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 14:33:42 2022

@author: blanc-sablon
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_compact():

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

    T0 = Tree(tree_list=[None],
                empty=True,
                name='T0',
                switches = [S0])
    T1 = Tree(tree_list=[None],
                empty=True,
                name='T1',
                switches = [S0])
    T2 = Tree(tree_list=[None],
                empty=True,
                name='T2',
                switches = [S0])
    T3 = Tree(tree_list=[None],
                empty=True,
                name='T3',
                switches = [S0])
    T4 = Tree(tree_list=[None],
                empty=True,
                name='T4',
                switches = [S0])
    T5 = Tree(tree_list=[None],
                empty=True,
                name='T5',
                switches = [S0])
    T6 = Tree(tree_list=[None],
                empty=True,
                name='T6',
                switches = [S0])
    T7 = Tree(tree_list=[None],
                empty=True,
                name='T7',
                switches = [S0])
    T8 = Tree(tree_list=[None],
                empty=True,
                name='T8',
                switches = [S0])
    T9 = Tree(tree_list=[None],
                empty=True,
                name='T9',
                switches = [S0])
    T10 = Tree(tree_list=[None],
                empty=True,
                name='T10',
                switches = [S0])
    T11 = Tree(tree_list=[None],
                empty=True,
                name='T11',
                switches = [S0])
    T12 = Tree(tree_list=[None],
                empty=True,
                name='T12',
                switches = [S0])
    T13 = Tree(tree_list=[None],
                empty=True,
                name='T13',
                switches = [S0])
    T14 = Tree(tree_list=[None],
                empty=True,
                name='T14',
                switches = [S0])
    T15 = Tree(tree_list=[None],
                empty=True,
                name='T15',
                switches = [S0])
    T16 = Tree(tree_list=[None],
                empty=True,
                name='T16',
                switches = [S0])
    T17 = Tree(tree_list=[None],
                empty=True,
                name='T17',
                switches = [S0])
    T18 = Tree(tree_list=[None],
                empty=True,
                name='T18',
                switches = [S0])
    T19 = Tree(tree_list=[None],
                empty=True,
                name='T19',
                switches = [S0])
    T20 = Tree(tree_list=[None],
                empty=True,
                name='T20',
                switches = [S0])
    T21 = Tree(tree_list=[None],
                empty=True,
                name='T21',
                switches = [S0])
    T22 = Tree(tree_list=[None],
                empty=True,
                name='T22',
                switches = [S0])
    T23 = Tree(tree_list=[None],
                empty=True,
                name='T23',
                switches = [S0])
    T24 = Tree(tree_list=[None],
                empty=True,
                name='T24',
                switches = [S0])
    T25 = Tree(tree_list=[None],
                empty=True,
                name='T25',
                switches = [S0])
    T26 = Tree(tree_list=[None],
                empty=True,
                name='T26',
                switches = [S0])
    T27 = Tree(tree_list=[None],
                empty=True,
                name='T27',
                switches = [S0])
    T28 = Tree(tree_list=[None],
                empty=True,
                name='T28',
                switches = [S0])
    T29 = Tree(tree_list=[None],
                empty=True,
                name='T29',
                switches = [S0])
    
    a = 1.005

    R0 = Room(name='R0',
                position = [0, 0, 5, a],
                switches_list = [S0, S1, S2])
    R1 = Room(name='R1',
                position = [0, 2, a, a],
                switches_list = [S3])
    R2 = Room(name='R2',
                position = [1, 3, a, a],
                switches_list = [S4])
    R3 = Room(name='R3',
                position = [2, 2, a, a],
                switches_list = [S5])
    R4 = Room(name='R4',
                position = [3, 3, a, a],
                switches_list = [S6])
    R5 = Room(name='R5',
                position = [0, 4, a, a],
                switches_list = [S7])
    R6 = Room(name='R6',
                position = [1, 5, a, a],
                switches_list = [S8])
    R7 = Room(name='R7',
                position = [2, 4, a, a],
                switches_list = [S9])
    R8 = Room(name='R8',
                position = [3, 5, a, a],
                switches_list = [S10])
    R9 = Room(name='R9',
                position = [0, 7, 5, a],
                switches_list = [S11, S12, S13])
    RE = Room(name='RE',
              position=[4.5, 5, 1, 1],
              is_exit=True)   # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[0.5/5, 1],
              relative_arrival_coordinates=[1/2, 0])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R0,
              room_arrival=R2,
              relative_departure_coordinates=[1.5/5, 1],
              relative_arrival_coordinates=[1/2, 0])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R0,
              room_arrival=R3,
              relative_departure_coordinates=[2.5/5, 1],
              relative_arrival_coordinates=[1/2, 0])
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R0,
              room_arrival=R4,
              relative_departure_coordinates=[3.5/5, 1],
              relative_arrival_coordinates=[1/2, 0])
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R1,
              room_arrival=R5)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R2,
              room_arrival=R6)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R3,
              room_arrival=R7)
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R4,
              room_arrival=R8)
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R5,
              room_arrival=R9,
              relative_departure_coordinates=[1/2, 1],
              relative_arrival_coordinates=[0.5/5, 0])
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R6,
              room_arrival=R9,
              relative_departure_coordinates=[1/2, 1],
              relative_arrival_coordinates=[1.5/5, 0])
    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R7,
               room_arrival=R9,
               relative_departure_coordinates=[1/2, 1],
               relative_arrival_coordinates=[2.5/5, 0])
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R8,
               room_arrival=R9,
               relative_departure_coordinates=[1/2, 1],
               relative_arrival_coordinates=[3.5/5, 0])

    d = 4.4/5
    p = 0.14
    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R9,
               room_arrival=R0,
               relative_departure_coordinates=[d, 1/2],
               relative_arrival_coordinates=[d, 1/2],
               relative_position=1-4*p)
    D13 = Door(two_way=False,
               tree=T13,
               room_departure=R9,
               room_arrival=R0,
               relative_departure_coordinates=[d, 1/2],
               relative_arrival_coordinates=[d, 1/2],
               relative_position=1-3*p)
    D14 = Door(two_way=False,
               tree=T14,
               room_departure=R9,
               room_arrival=R0,
               relative_departure_coordinates=[d, 1/2],
               relative_arrival_coordinates=[d, 1/2],
               relative_position=1-2*p)
    D15 = Door(two_way=False,
               tree=T15,
               room_departure=R9,
               room_arrival=R0,
               relative_departure_coordinates=[d, 1/2],
               relative_arrival_coordinates=[d, 1/2],
               relative_position=1-p)

    D16 = Door(two_way=False,
               tree=T16,
               room_departure=R9,
               room_arrival=RE,
               relative_departure_coordinates=[1, 0],
               relative_arrival_coordinates=[1/2, 1])

#    D17 = Door(two_way=False,
#                tree=T17,
#                room_departure=R17,
#                room_arrival=R18)
#    D18 = Door(two_way=False,
#                tree=T18,
#                room_departure=R18,
#                room_arrival=R19)
#    D19 = Door(two_way=False,
#                tree=T19,
#                room_departure=R19,
#                room_arrival=R20)
#    D20 = Door(two_way=False,
#                tree=T20,
#                room_departure=R20,
#                room_arrival=R21)
#    D21 = Door(two_way=False,
#                tree=T21,
#                room_departure=R21,
#                room_arrival=R22)
#    D22 = Door(two_way=False,
#                tree=T22,
#                room_departure=R22,
#                room_arrival=R23)
#    D23 = Door(two_way=False,
#                tree=T23,
#                room_departure=R23,
#                room_arrival=R24)
#    D24 = Door(two_way=False,
#                tree=T24,
#                room_departure=R24,
#                room_arrival=R25)
#    D25 = Door(two_way=False,
#                tree=T25,
#                room_departure=R25,
#                room_arrival=R26)
#    D26 = Door(two_way=False,
#                tree=T26,
#                room_departure=R26,
#                room_arrival=R27)
#    D27 = Door(two_way=False,
#                tree=T27,
#                room_departure=R27,
#                room_arrival=R28)
#    D28 = Door(two_way=False,
#                tree=T28,
#                room_departure=R28,
#                room_arrival=R29)
#    D29 = Door(two_way=False,
#                tree=T29,
#                room_departure=R29,
#                room_arrival=R30)

#    [R0, R1, R2, R3, R4, R5, R6, R7, R8, R9]
#    [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28, D29]
#    [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29]
        
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16],
                 fastest_solution=None,
                 level_color=Levels_colors_list.BLUE_GREEN,
                 name='Compact',
                 door_window_size=900,
                 keep_proportions=True)

    return level