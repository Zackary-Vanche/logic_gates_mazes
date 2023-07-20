# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 14:01:24 2023

@author: zackary.vanche
"""
    
from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from numpy import pi, cos, sin
from Color import Color

def level_wind_rose():
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    
    tree_list_1 = Tree.tree_list_from_str('TF')

    T0 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T0',
                switches=[S0, S1])
    T1 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T1',
                switches=[S1, S0])
    T2 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T2',
                switches=[S1, S2])
    T3 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T3',
                switches=[S2, S1])
    T4 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T4',
                switches=[S2, S3])
    T5 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T5',
                switches=[S3, S2])
    T6 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T6',
                switches=[S3, S4])
    T7 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T7',
                switches=[S4, S3])
    T8 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T8',
                switches=[S4, S5])
    T9 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T9',
                switches=[S5, S4])
    T10 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T10',
                switches=[S5, S6])
    T11 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T11',
                switches=[S6, S5])
    T12 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T12',
                switches=[S6, S7])
    T13 = Tree(tree_list=Tree.tree_list_from_str('FTF'),
                empty=True,
                name='T13',
                switches=[S1, S7, S6])
    T14 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T14',
                switches=[S7, S0])
    T15 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T15',
                switches=[S0, S7])
    T16 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T16',
                switches=[S0, S8])
    T17 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T17',
                switches=[S8, S0])
    T18 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T18',
                switches=[S1, S8])
    T19 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T19',
                switches=[S8, S1])
    T20 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T20',
                switches=[S2, S8])
    T21 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T21',
                switches=[S8, S2])
    T22 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T22',
                switches=[S3, S8])
    T23 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T23',
                switches=[S8, S3])
    T24 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T24',
                switches=[S4, S8])
    T25 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T25',
                switches=[S8, S4])
    T26 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T26',
                switches=[S5, S8])
    T27 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T27',
                switches=[S8, S5])
    T28 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T28',
                switches=[S6, S8])
    T29 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T29',
                switches=[S8, S6])
    T30 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T30',
                switches=[S7, S8])
    T31 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T31',
                switches=[S8, S7])
    T32 = Tree(tree_list=Tree.tree_list_AND(9),
                empty=True,
                name='T32',
                switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8])
    
    ex = 0.2
    ey = 0.2

    position_R = []
    
    for i in range(8):
        alpha = i*pi/4 + 3*pi/2
        position_R.append([cos(alpha), -sin(alpha), ex, ey])
        
    position_R.append([0, 0, ex, ey])

    position_RE = [0, -1.5, ex, ey]

    R0 = Room(name='R0',
              position=position_R[0],
              switches_list=[S0])
    R1 = Room(name='R1',
              position=position_R[1],
              switches_list=[S1])
    R2 = Room(name='R2',
              position=position_R[2],
              switches_list=[S2])
    R3 = Room(name='R3',
              position=position_R[3],
              switches_list=[S3])
    R4 = Room(name='R4',
              position=position_R[4],
              switches_list=[S4])
    R5 = Room(name='R5',
              position=position_R[5],
              switches_list=[S5])
    R6 = Room(name='R6',
              position=position_R[6],
              switches_list=[S6])
    R7 = Room(name='R7',
              position=position_R[7],
              switches_list=[S7])
    R8 = Room(name='R8',
              position=position_R[8],
              switches_list=[S8])
    RE = Room(name='RE', position=position_RE, is_exit=True)  # E pour exit ou end

    rp = 0.65

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_position=rp)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R0,
                relative_position=rp)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R2,
                relative_position=rp)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R1,
                relative_position=rp)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R3,
                relative_position=rp)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R2,
                relative_position=rp)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R3,
                room_arrival=R4,
                relative_position=rp)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R4,
                room_arrival=R3,
                relative_position=rp)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R4,
                room_arrival=R5,
                relative_position=rp)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R5,
                room_arrival=R4,
                relative_position=rp)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R5,
                room_arrival=R6,
                relative_position=rp)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R6,
                room_arrival=R5,
                relative_position=rp)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R6,
                room_arrival=R7,
                relative_position=rp)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R7,
                room_arrival=R6,
                relative_position=rp)
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R7,
                room_arrival=R0,
                relative_position=rp)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R0,
                room_arrival=R7,
                relative_position=rp)
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R0,
                room_arrival=R8,
                relative_position=rp)
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R8,
                room_arrival=R0,
                relative_position=rp)
    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=R1,
                room_arrival=R8,
                relative_position=rp)
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R8,
                room_arrival=R1,
                relative_position=rp)
    D20 = Door(two_way=False,
                tree=T20,
                name='D20',
                room_departure=R2,
                room_arrival=R8,
                relative_position=rp)
    D21 = Door(two_way=False,
                tree=T21,
                name='D21',
                room_departure=R8,
                room_arrival=R2,
                relative_position=rp)
    D22 = Door(two_way=False,
                tree=T22,
                name='D22',
                room_departure=R3,
                room_arrival=R8,
                relative_position=rp)
    D23 = Door(two_way=False,
                tree=T23,
                name='D23',
                room_departure=R8,
                room_arrival=R3,
                relative_position=rp)
    D24 = Door(two_way=False,
                tree=T24,
                name='D24',
                room_departure=R4,
                room_arrival=R8,
                relative_position=rp)
    D25 = Door(two_way=False,
                tree=T25,
                name='D25',
                room_departure=R8,
                room_arrival=R4,
                relative_position=rp)
    D26 = Door(two_way=False,
                tree=T26,
                name='D26',
                room_departure=R5,
                room_arrival=R8,
                relative_position=rp)
    D27 = Door(two_way=False,
                tree=T27,
                name='D27',
                room_departure=R8,
                room_arrival=R5,
                relative_position=rp)
    D28 = Door(two_way=False,
                tree=T28,
                name='D28',
                room_departure=R6,
                room_arrival=R8,
                relative_position=rp)
    D29 = Door(two_way=False,
                tree=T29,
                name='D29',
                room_departure=R8,
                room_arrival=R6,
                relative_position=rp)
    D30 = Door(two_way=False,
                tree=T30,
                name='D30',
                room_departure=R7,
                room_arrival=R8,
                relative_position=rp)
    D31 = Door(two_way=False,
                tree=T31,
                name='D31',
                room_departure=R8,
                room_arrival=R7,
                relative_position=rp)
    D32 = Door(two_way=False,
                tree=T32,
                name='D32',
                room_departure=R4,
                room_arrival=RE)

    lcolor = Levels_colors_list.FROM_HUE(hu=0.6, sa=0.2, li=0.9)
    lcolor.contour_color = Color.RED
    lcolor.surrounding_color = Color.RED

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7,
                             R8,
                             RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30, D31, D32],
                 fastest_solution="S0 D15 S7 D13 S6 D11 S5 D26 S8 D19 S1 D2 S2 D4 S3 D6 S4 D32",
                 level_color=lcolor,
                 name='Wind rose',
                 door_window_size=600,
                 y_separation=50,
                 border=30,
                 keep_proportions=True,
                 group='pure maze')

    return level