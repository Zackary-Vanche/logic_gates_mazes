#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 15:40:05 2022

@author: blanc-sablon
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_water_pouring():
    
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6', value=1)
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
    
    SN0 = Switch(value=0)
    SN1 = Switch(value=1)
    SN4 = Switch(value=4)
    SN7 = Switch(value=7)
    SN8 = Switch(value=8)
    
    tree_list_EQU_plus1_BIN3 = ['EQU', Tree.tree_list_BIN(3), ['SUM', Tree.tree_list_BIN(3), [None]]]
    
    # 17 18 3 4 5 6 S0
    # 11 12 13 3 4 5 6 S1
    T0 = Tree(tree_list=['AND',
                             ['OR',
                              Tree.tree_list_NOT,
                              Tree.tree_list_from_str('TT TTTT FF FFFF')],
                             ['OR',
                              Tree.tree_list_NOT,
                              Tree.tree_list_from_str('TFT TTTT FFF FFFF')],
                             Tree.tree_list_OR(2),],
                empty=True,
                name='T0',
                switches = [
                            S0,
                            S17, S18,
                            S3, S4, S5, S6,
                            S17, S18,
                            S3, S4, S5, S6,
                            S1,
                            S11, S12, S13,
                            S3, S4, S5, S6,
                            S11, S12, S13,
                            S3, S4, S5, S6,
                            S0, S1,
                            ],
                cut_expression=True,
                cut_expression_separator=')')

    T1 = Tree(tree_list=['AND',
                             [None],
                             Tree.tree_list_from_str('TT TFT FF FFF')],
                empty=True,
                name='T1',
                switches = [S2,
                            S17, S18,
                            S11, S12, S13,
                            S17, S18,
                            S11, S12, S13],
                cut_expression=False)
    T2 = Tree(tree_list=[None],
                empty=True,
                name='T2',
                switches = [S1])

    T3 = Tree(tree_list=[None],
                empty=True,
                name='T3',
                switches = [S0])

    T4 = Tree(tree_list=['AND', [None], tree_list_EQU_plus1_BIN3],
                empty=True,
                name='T4',
                switches = [S1, S21, S22, S23, S24, S25, S26, SN1])

    T5 = Tree(tree_list=[None],
                empty=True,
                name='T5',
                switches = [S2])

    T6 = Tree(tree_list=['AND', Tree.tree_list_OR(2), tree_list_EQU_plus1_BIN3],
                empty=True,
                name='T6',
                switches = [S0, S2, S21, S22, S23, S24, S25, S26, SN1])
    
    T7 = Tree(tree_list=['AND',
                             ['EQU', ['SUM', Tree.tree_list_BIN(4), Tree.tree_list_BIN(3), Tree.tree_list_BIN(2)], [None]],
                             ['EQU', Tree.tree_list_BIN(9), Tree.tree_list_BIN(9)]],
              empty=True,
              name='T7',
              switches = [S7, S8, S9, S10,
                          S14, S15, S16,
                          S19, S20,
                          SN8,
                          S17, S18,
                          S11, S12, S13,
                          S3, S4, S5, S6,
                          S19, S20,
                          S14, S15, S16,
                          S7, S8, S9, S10],
              cut_expression=True,
              cut_expression_separator=')')
    T8 = Tree(tree_list=['EQU', ['SUM', Tree.tree_list_BIN(4), Tree.tree_list_BIN(3), Tree.tree_list_BIN(2)], [None]],
              empty=True,
              name='T8',
              switches = [S3, S4, S5, S6,
                          S11, S12, S13,
                          S17, S18,
                          SN8],
              cut_expression=False,
              cut_expression_separator=')')
    T9 = Tree(tree_list=['EQU',
                         Tree.tree_list_BIN(3),
                         Tree.tree_list_BIN(3)],
                empty=True,
                name='T9',
                switches = [S21, S22, S23,
                            S24, S25, S26],
                cut_expression=False)
    T10 = Tree(tree_list=['EQU',
                         Tree.tree_list_BIN(2),
                         Tree.tree_list_BIN(2)],
               empty=True,
               name='T10',
               switches = [S17, S18,
                           S19, S20],
               cut_expression=False)
    T11 = Tree(tree_list=['EQU',
                         Tree.tree_list_BIN(3),
                         Tree.tree_list_BIN(3)],
               empty=True,
               name='T11',
               switches = [S11, S12, S13,
                           S14, S15, S16],
               cut_expression=False)
    T12 = Tree(tree_list=['EQU',
                         Tree.tree_list_BIN(4),
                         Tree.tree_list_BIN(4)],
               empty=True,
               name='T12',
               switches = [S3, S4, S5, S6,
                           S7, S8, S9, S10],
               cut_expression=False)
    T13 = Tree(tree_list=['AND'] + [['AND',
                                       ['EQU', Tree.tree_list_BIN(2), [None]],
                                       ['EQU', Tree.tree_list_BIN(3), [None]],
                                       ['EQU', Tree.tree_list_BIN(4), [None]]]]*2 + [['EQU', Tree.tree_list_BIN(3), [None]]]*3,
                empty=True,
                name='T13',
                switches = [S17, S18,
                            SN0,
                            S11, S12, S13,
                            SN4,
                            S3, S4, S5, S6,
                            SN4,
                            
                            S19, S20,
                            SN0,
                            S14, S15, S16,
                            SN4,
                            S7, S8, S9, S10,
                            SN4,
                            
                            S0, S1, S2,
                            SN0,
                            
                            S21, S22, S23,
                            SN7,
                            S24, S25, S26,
                            SN7,
                            ],
                cut_expression=True,
                cut_expression_separator=']')

    ex = 0.9
    ey = 1.5
    dy = 2.8
    a = 0.3
    
    symetric = 0
    if symetric:
        d3 = 3
    else:
        d3 = 3.2
        
    epsilonx = 0.1

    R0 = Room(name='R0',
              position = [5+a-epsilonx, 2*dy, ex, 2*dy+ey],
              switches_list = [S0, S1, S2])
    R1 = Room(name='R1',
              position = [0, 4*dy, 4, ey],
              switches_list = [S3, S4, S5, S6])
    R2 = Room(name='R2',
              position = [symetric, 3*dy, d3, ey],
              switches_list = [S11, S12, S13])
    R3 = Room(name='R3',
              position = [1-symetric, 2*dy, d3, ey],
              switches_list = [S17, S18])
    R4 = Room(name='R4',
              position = [symetric, 1*dy, d3, ey],
              switches_list = [S21, S22, S23])
    # if fast_solution_finding:
    #     psv5 = lambda : [[S.value for S in [S3, S4, S5, S6,
    #                                         S11, S12, S13,
    #                                         S17, S18,
    #                                         S21, S22, S23]]]
    # else:
    #     psv5 = None
    R5 = Room(name='R5',
              position = [7.1+a+ex, 1*dy, 3*ex, ey],
              switches_list = [S24, S25, S26])
    R6 = Room(name='R6',
              position = [7.1+a+ex, 2*dy, 3*ex, ey],
              switches_list = [S19, S20])
    R7 = Room(name='R7',
              position = [7.1+a+ex, 3*dy, 3*ex, ey],
              switches_list = [S14, S15, S16])
    R8 = Room(name='R8',
              position = [7.1+a, 4*dy, 4*ex, ey],
              switches_list = [S7, S8, S9, S10])
    le = 1
    position_RE = [5+a-epsilonx-le/2, 1*dy, ex+le, ey]
    RE = Room(name='RE',
              position=position_RE,
              is_exit=True)   # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R1,
              room_arrival=R0,
              relative_departure_coordinates=[1, 1/2],
              relative_arrival_coordinates=[0, (2*dy+ey/2)/(2*dy+ey)])
    if symetric:
        rp2 = 1/2
    else:
        rp2 = 0.725
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R2,
              room_arrival=R0,
              relative_departure_coordinates=[1, 1/2],
              relative_arrival_coordinates=[0, (1*dy+ey/2)/(2*dy+ey)],
              relative_position=rp2)
    if symetric:
        rdc4 = [(d3-1.5)/d3, 1/2]
        rac4 = [(4-1.5)/4, 1/2]
    else:
        rdc4 = [1.5/d3, 1/2]
        rac4 = [1.5/4, 1/2]
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R1,
              relative_departure_coordinates=rdc4,
              relative_arrival_coordinates=rac4)
    if symetric:
        rdc6 = [(d3-2.75)/d3, 1/2]
        rac6 = [(4-3.75)/4, 1/2]
    else:
        rdc6 = [2.7/d3, 1/2]
        rac6 = [3.7/4, 1/2]
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=R1,
              relative_departure_coordinates=rdc6,
              relative_arrival_coordinates=rac6)
    if symetric:
        rdc8 = [(d3-0.5)/d3, 1/2]
        rac8 = [(d3-0.5)/d3, 1/2]
    else:
        rdc8 = [0.5/d3, 1/2]
        rac8 = [0.5/d3, 1/2]
    D4 = Door(two_way=False,
               tree=T4,
               room_departure=R4,
               room_arrival=R2,
               relative_departure_coordinates=rdc8,
               relative_arrival_coordinates=rac8)
    if symetric:
        rdc10 = [(d3-1)/d3, 1/2]
        rac10 = [(d3-2)/d3, 1/2]
    else:
        rdc10 = [1/d3, 1/2]
        rac10 = [2/d3, 1/2]
    D5 = Door(two_way=False,
               tree=T5,
               room_departure=R3,
               room_arrival=R2,
               relative_departure_coordinates=rdc10,
               relative_arrival_coordinates=rac10)
    if symetric:
        rdc12 = [(d3-2.5)/d3, 1/2]
        rac12 = [(d3-1.5)/d3, 1/2]
    else:
        rdc12 = [2.5/d3, 1/2]
        rac12 = [1.5/d3, 1/2]
    D6 = Door(two_way=False,
               tree=T6,
               room_departure=R4,
               room_arrival=R3,
               relative_departure_coordinates=rdc12,
               relative_arrival_coordinates=rac12)
    D7 = Door(two_way=False,
               tree=T7,
               room_departure=R0,
               room_arrival=R4,
               relative_departure_coordinates=[0, 0],
               relative_arrival_coordinates=[1, 1])
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R0,
              room_arrival=R5,
              relative_departure_coordinates=[1, 0],
              relative_arrival_coordinates=[0, 1])
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R5,
              room_arrival=R6,
              relative_departure_coordinates=[1/2, 1/2],
              relative_arrival_coordinates=[1/2, 1/2])
    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R6,
               room_arrival=R7)
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R7,
               room_arrival=R8,
               relative_arrival_coordinates=[2.5/4, 1/2])
    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R8,
               room_arrival=R0,
               relative_departure_coordinates=[0, 1/2],
               relative_arrival_coordinates=[1, (2*dy+ey/2)/(2*dy+ey)])
    D13 = Door(two_way=False,
               tree=T13,
               room_departure=R0,
               room_arrival=RE,
               relative_departure_coordinates=[1/2, 0],
               relative_arrival_coordinates=[1/2, 1],
               relative_position=1/2)
    
    solution = """D8
D9
D10
D11
S10 D12
S1 D7
S21 D4
S11 S13 D2
S3 S4 S6 D0
D8
S24 D9
D10
S14 S16 D11
S7 S8 S10 D12
S1 S2 D7
S22 S21 D6
S17 S18 D5
S11 S12 S13 D1
D8
S24 S25 D9
S19 S20 D10
S14 S15 S16 D11
D12
S0 S2 D7
S21 D6
S17 S18 D3
S3 S5 D0
D8
S24 D9
S19 S20 D10
D11
S7 S9 D12
S0 S2 D7
S23 S21 S22 D6
S18 D5
S12 D1
D8
S24 S25 S26 D9
S20 D10
S15 D11
D12
S1 S2 D7
S21 D4
S11 S13 D2
S3 S4 S5 D0
D8
S24 D9
D10
S14 S16 D11
S7 S8 S9 D12
S1 S2 D7
S21 S22 D6
S17 D5
S11 D1
D8
S24 S25 D9
S19 D10
S14 D11
D12
S0 S2 D7
S21 D6
S17 S18 D3
S3 S5 D0
S0 D8
S24 D9
S19 S20 D10
D11
S7 S9 D12
D13
""".replace('\n', ' ')

    solution = '''D8
D9
D10
D11
S10 D12
S1 S2 D7
S21 D4
D1
D8
S24 D9
D10
D11
D12
D7
S21 S22 D4
D1
D8
S24 S25 D9
D10
D11
D12
D7
S21 D4
D1
D8
S24 D9
D10
D11
D12
D7
S21 S22 S23 D4
D1
D8
S24 S25 S26 D9
D10
D11
D12
D7
S21 D6
S18 D5
S11 S13 D2
S3 S6 D0
D8
S24 D9
S20
D10
S14 S16 D11
S7 S10 D12
D7
S21 S22 D6
S17 D5
S11 D1
D8
S24 S25 D9
S19 D10
S14 D11
D12
S0 S1 D7
S21 D6
S17 S18
D3
S3 S5 D0
D8
S24 D9
S19 S20 D10
D11
S7 S9 D12
S0 S2 D13'''.replace('\n', ' ')

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13],
                 fastest_solution='S1 S2 D8 D9 D10 D11 S10 D12 D7 S21 D4 D1 D8 S24 D9 D10 D11 D12 D7 S21 S22 D4 D1 D8 S24 S25 D9 D10 D11 D12 D7 S21 D4 D1 D8 S24 D9 D10 D11 D12 D7 S21 S22 S23 D4 D1 D8 S24 S25 S26 D9 D10 D11 D12 D7 S21 D6 S18 D5 S11 S13 D2 S3 S6 D0 S0 S1 D8 S24 D9 S20 D10 S14 S16 D11 S7 S10 D12 D7 S21 S22 D6 S17 D5 S11 D1 D8 S24 S25 D9 S19 D10 S14 D11 D12 D7 S21 D6 S17 S18 D3 S3 S5 D0 S0 S2 D8 S24 D9 S19 S20 D10 D11 S7 S9 D12 D13',
                 level_color=Levels_colors_list.FROM_HUE(0.58, sa=0.8, li=0.49),
                 name='Water pouring',
                 door_window_size=640,
                 keep_proportions=True)

    return level

# D8 D9 D10 D11 S10 D12 S1 S2 D7 S21 D6 S18 D5 S11 S13 D2 S3 S6 D0 D8 S24 D9 S20 D10 S14 S16 D11 S7 S10 D12 D7 S21 S22 D6 S17 D5 S11 D1 D8 S24 S25 D9 S19 D10 S14 D11 D12 S0 S1 D7 S21 D6 S17 S18 D3 S3 S5 D0 D8 S24 D9 S19 S20 D10 D11 S7 S9 D12 S0 S2 D13
# D8 D9 D10 D11 S10 D12 S1 S2 D7 S21 D6 S18 D5 S11 S13 D2 S3 S6 D0 D8 S24 D9 S20 D10 S14 S16 D11 S7 S10 D12 D7 S21 S22 D6 S17 D5 S11 D1 D8 S24 S25 D9 S19 D10 S14 D11 D12 S0 S1 D7 S21 D6 S17 S18 D3 S3 S5 D0 D8 S24 D9 S19 S20 D10 D11 S7 S9 D12 D7 S21 S22 S23 D6 D3 D0 S0 S2 D13
# D8 D9 D10 D11 S10 D12 S1 S2 D7 S21 D4 D1 D8 S24 D9 D10 D11 D12 D7 S21 S22 D6 S18 D5 S11 S13 D2 S3 S6 D0 D8 S24 S25 D9 S20 D10 S14 S16 D11 S7 S10 D12 D7 S21 D6 S17 D5 S11 D1 D8 S24 D9 S19 D10 S14 D11 D12 S0 S1 D7 S21 S22 S23 D6 S17 S18 D3 S3 S5 D0 D8 S24 S25 S26 D9 S19 S20 D10 D11 S7 S9 D12 S0 S2 D13
# D8 D9 D10 D11 S10 D12 S1 S2 D7 S21 D4 D1 D8 S24 D9 D10 D11 D12 D7 S21 S22 D6 S18 D5 S11 S13 D2 S3 S6 D0 D8 S24 S25 D9 S20 D10 S14 S16 D11 S7 S10 D12 D7 S21 D6 S17 D5 S11 D1 D8 S24 D9 S19 D10 S14 D11 D12 S0 S1 D7 S21 S22 S23 D6 S17 S18 D3 S3 S5 D0 D8 S24 S25 S26 D9 S19 S20 D10 D11 S7 S9 D12 D7 S21 D6 D3 D0 S0 S2 D13
# D8 D9 D10 D11 S10 D12 S1 S2 D7 S21 D4 D1 D8 S24 D9 D10 D11 D12 D7 S21 S22 D4 D1 D8 S24 S25 D9 D10 D11 D12 D7 S21 D6 S18 D5 S11 S13 D2 S3 S6 D0 D8 S24 D9 S20 D10 S14 S16 D11 S7 S10 D12 D7 S21 S22 S23 D6 S17 D5 S11 D1 D8 S24 S25 S26 D9 S19 D10 S14 D11 D12 S0 S1 D7 S21 D6 S17 S18 D3 S3 S5 D0 D8 S24 D9 S19 S20 D10 D11 S7 S9 D12 S0 S2 D13
# D8 D9 D10 D11 S10 D12 S1 S2 D7 S21 D4 D1 D8 S24 D9 D10 D11 D12 D7 S21 S22 D4 D1 D8 S24 S25 D9 D10 D11 D12 D7 S21 D6 S18 D5 S11 S13 D2 S3 S6 D0 D8 S24 D9 S20 D10 S14 S16 D11 S7 S10 D12 D7 S21 S22 S23 D6 S17 D5 S11 D1 D8 S24 S25 S26 D9 S19 D10 S14 D11 D12 S0 S1 D7 S21 D6 S17 S18 D3 S3 S5 D0 D8 S24 D9 S19 S20 D10 D11 S7 S9 D12 D7 S21 S22 D6 D3 D0 S0 S2 D13
# D8 D9 D10 D11 S10 D12 S1 S2 D7 S21 D4 D1 D8 S24 D9 D10 D11 D12 D7 S21 S22 D4 D1 D8 S24 S25 D9 D10 D11 D12 D7 S21 D4 D1 D8 S24 D9 D10 D11 D12 D7 S21 S22 S23 D6 S18 D5 S11 S13 D2 S3 S6 D0 D8 S24 S25 S26 D9 S20 D10 S14 S16 D11 S7 S10 D12 D7 S21 D6 S17 D5 S11 D1 D8 S24 D9 S19 D10 S14 D11 D12 S0 S1 D7 S21 S22 D6 S17 S18 D3 S3 S5 D0 D8 S24 S25 D9 S19 S20 D10 D11 S7 S9 D12 S0 S2 D13
# D8 D9 D10 D11 S10 D12 S1 S2 D7 S21 D4 D1 D8 S24 D9 D10 D11 D12 D7 S21 S22 D4 D1 D8 S24 S25 D9 D10 D11 D12 D7 S21 D4 D1 D8 S24 D9 D10 D11 D12 D7 S21 S22 S23 D6 S18 D5 S11 S13 D2 S3 S6 D0 D8 S24 S25 S26 D9 S20 D10 S14 S16 D11 S7 S10 D12 D7 S21 D6 S17 D5 S11 D1 D8 S24 D9 S19 D10 S14 D11 D12 S0 S1 D7 S21 S22 D6 S17 S18 D3 S3 S5 D0 D8 S24 S25 D9 S19 S20 D10 D11 S7 S9 D12 D7 S21 D6 D3 D0 S0 S2 D13
# D8 D9 D10 D11 S10 D12 S1 S2 D7 S21 D4 D1 D8 S24 D9 D10 D11 D12 D7 S21 S22 D4 D1 D8 S24 S25 D9 D10 D11 D12 D7 S21 D4 D1 D8 S24 D9 D10 D11 D12 D7 S21 S22 S23 D4 D1 D8 S24 S25 S26 D9 D10 D11 D12 D7 S21 D6 S18 D5 S11 S13 D2 S3 S6 D0 D8 S24 D9 S20 D10 S14 S16 D11 S7 S10 D12 D7 S21 S22 D6 S17 D5 S11 D1 D8 S24 S25 D9 S19 D10 S14 D11 D12 S0 S1 D7 S21 D6 S17 S18 D3 S3 S5 D0 D8 S24 D9 S19 S20 D10 D11 S7 S9 D12 S0 S2 D13