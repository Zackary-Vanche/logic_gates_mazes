# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 17:18:30 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def level_wheel_graph():
    
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

    SN0 = Switch(value=0)
    SN1 = Switch(value=1)
    SN2 = Switch(value=2)

    tree_list_0 = ['AND', ['EQU', ['SUM'] + [[None]]*4, [None]], Tree.tree_list_NAND(2)]
    
    tree_list_2 = ['NOT', Tree.tree_list_OR(8)]
    
    tree_list_12 = ['EQU', ['SUM'] + [[None]]*8, [None]]
    
    tree_list_14 = ['AND',
                    Tree.tree_list_XOR(2),
                    Tree.tree_list_XOR(2),]

    T0 = Tree(tree_list=tree_list_0,
              empty=True,
              name='T0',
              switches = [S0, S1, S2, S3, SN2, S0, S1])
    T1 = Tree(tree_list=[None],
              empty=True,
              name='T1',
              switches = [SN1])
    T2 = Tree(tree_list=tree_list_2,
              empty=True,
              name='T2',
              switches = [S4, S5, S6, S7, S8, S9, S10, S11])
    T3 = Tree(tree_list=tree_list_0,
              empty=True,
              name='T3',
              switches = [S0, S1, S2, S3, SN2, S0, S2])
    T4 = Tree(tree_list=[None],
              empty=True,
              name='T4',
              switches = [SN1])
    T5 = Tree(tree_list=tree_list_2,
              empty=True,
              name='T5',
              switches = [S4, S5, S6, S7, S8, S9, S10, S11])
    T6 = Tree(tree_list=tree_list_0,
              empty=True,
              name='T6',
              switches = [S0, S1, S2, S3, SN2, S2, S3])
    T7 = Tree(tree_list=[None],
              empty=True,
              name='T7',
              switches = [SN1])
    T8 = Tree(tree_list=tree_list_2,
              empty=True,
              name='T8',
              switches = [S4, S5, S6, S7, S8, S9, S10, S11])
    T9 = Tree(tree_list=tree_list_0,
              empty=True,
              name='T9',
              switches = [S0, S1, S2, S3, SN2, S1, S3])
    T10 = Tree(tree_list=[None],
               empty=True,
               name='T10',
               switches = [SN1])
    T11 = Tree(tree_list=tree_list_2,
               empty=True,
               name='T11',
               switches = [S4, S5, S6, S7, S8, S9, S10, S11])
    T12 = Tree(tree_list=tree_list_12,
               empty=True,
               name='T12',
               switches = [S4, S5, S6, S7, S8, S9, S10, S11, Switch(value=4)])
    T13 = Tree(tree_list=[None],
               empty=True,
               name='T13',
               switches = [S0])
    T14 = Tree(tree_list=tree_list_14,
               empty=True,
               name='T14',
               switches = [S0, S3,
                           S1, S2])
    T15 = Tree(tree_list=tree_list_12,
               empty=True,
               name='T15',
               switches = [S4, S5, S6, S7, S8, S9, S10, S11, Switch(value=6)])
    T16 = Tree(tree_list=[None],
               empty=True,
               name='T16',
               switches = [S2])
    T17 = Tree(tree_list=tree_list_14,
               empty=True,
               name='T17',
               switches = [S0, S3,
                           S1, S2])
    T18 = Tree(tree_list=tree_list_12,
               empty=True,
               name='T18',
               switches = [S4, S5, S6, S7, S8, S9, S10, S11, Switch(value=12)])
    T19 = Tree(tree_list=[None],
               empty=True,
               name='T19',
               switches = [S3])
    T20 = Tree(tree_list=tree_list_14,
               empty=True,
               name='T20',
               switches = [S0, S3,
                           S1, S2])
    T21 = Tree(tree_list=tree_list_12,
               empty=True,
               name='T21',
               switches = [S4, S5, S6, S7, S8, S9, S10, S11, Switch(value=8)])
    T22 = Tree(tree_list=[None],
               empty=True,
               name='T22',
               switches = [S1])
    T23 = Tree(tree_list=tree_list_14,
               empty=True,
               name='T23',
               switches = [S0, S3,
                           S1, S2])
    T24 = Tree(tree_list=Tree.tree_list_AND(4),
               empty=True,
               name='T24',
               switches = [S0, S1, S2, S3])

    e = 0.19
    Color1 = Color.WHITE
    Color2 = Color.TOTAL_YELLOW
    Color3 = Color.REALLY_BRIGHT_ORANGE
    Color4 = Color.TOTAL_RED

    R0 = Room(name='R0',
              position = [4, 4, 3, 3],
              switches_list = [S0, S1, S2, S3],
              surrounding_color=Color1)
    R1 = Room(name='R1',
              position = [9, 4.5, 2, 2],
              switches_list = [S4, S8],
              surrounding_color=Color3)
    R2 = Room(name='R2',
              position = [9.5, 2.5-e, 1, 1],
              switches_list = [],
              surrounding_color=Color3)
    R3 = Room(name='R3',
              position = [7.5+e, 0.5, 1, 1],
              switches_list = [],
              surrounding_color=Color3)
    R4 = Room(name='R4',
              position = [4.5, 0, 2, 2],
              switches_list = [S5, S9],
              surrounding_color=Color3)
    R5 = Room(name='R5',
              position = [2.5-e, 0.5, 1, 1],
              switches_list = [],
              surrounding_color=Color3)
    R6 = Room(name='R6',
              position = [0.5, 2.5-e, 1, 1],
              switches_list = [],
              surrounding_color=Color3)
    R7 = Room(name='R7',
              position = [0, 4.5, 2, 2],
              switches_list = [S6, S10],
              surrounding_color=Color3)
    R8 = Room(name='R8',
              position = [0.5, 7.5+e, 1, 1],
              switches_list = [],
              surrounding_color=Color3)
    R9 = Room(name='R9',
              position = [2.5-e, 9.5, 1, 1],
              switches_list = [],
              surrounding_color=Color3)
    R10 = Room(name='R10',
               position = [4.5, 9, 2, 2],
               switches_list = [S7, S11],
               surrounding_color=Color3)
    R11 = Room(name='R11',
               position = [7.5+e, 9.5, 1, 1],
               switches_list = [],
               surrounding_color=Color3)
    R12 = Room(name='R12',
               position = [9.5, 7.5+e, 1, 1],
               switches_list = [],
               surrounding_color=Color3)
    RE = Room(name='RE',
              position=[10, 0, 1, 1],
              is_exit=True,
              surrounding_color=Color4)   # E pour exit ou end

    d1 = 4.5
    d2 = (4.5**2+(3-e)**2)**(1/2)
    p = 0.4
    p1 = 1-0.4
    p2 = p*d2/d1
    a = 0.35

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R1,
              room_arrival=R0,
              relative_position=p2,
              surrounding_color=Color2)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R0,
              room_arrival=R2,
              relative_position=p1,
              surrounding_color=Color2)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R0,
              room_arrival=R3,
              relative_position=p1,
              surrounding_color=Color2)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R4,
              room_arrival=R0,
              relative_position=p2,
              surrounding_color=Color2)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R0,
              room_arrival=R5,
              relative_position=p1,
              surrounding_color=Color2)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R0,
              room_arrival=R6,
              relative_position=p1,
              surrounding_color=Color2)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R7,
              room_arrival=R0,
              relative_position=p2,
              surrounding_color=Color2)
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R0,
              room_arrival=R8,
              relative_position=p1,
              surrounding_color=Color2)
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R0,
              room_arrival=R9,
              relative_position=p1,
              surrounding_color=Color2)
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R10,
              room_arrival=R0,
              relative_position=p2,
              surrounding_color=Color2)
    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R0,
               room_arrival=R11,
               relative_position=p1,
               surrounding_color=Color2)
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R0,
               room_arrival=R12,
               relative_position=p1,
               surrounding_color=Color2)
    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R1,
               room_arrival=R2,
               relative_departure_coordinates=[1/2, 0],
               relative_arrival_coordinates=[1/2, 1],
               surrounding_color=Color3)
    D13 = Door(two_way=False,
               tree=T13,
               room_departure=R2,
               room_arrival=R3,
               relative_departure_coordinates=[1-a, a],
               relative_arrival_coordinates=[1-a, a],
               surrounding_color=Color3)
    D14 = Door(two_way=False,
               tree=T14,
               room_departure=R3,
               room_arrival=R4,
               relative_departure_coordinates=[0, 1/2],
               relative_arrival_coordinates=[1, 1/2],
               surrounding_color=Color3)
    D15 = Door(two_way=False,
               tree=T15,
               room_departure=R4,
               room_arrival=R5,
               relative_departure_coordinates=[0, 1/2],
               relative_arrival_coordinates=[1, 1/2],
               surrounding_color=Color3)
    D16 = Door(two_way=False,
               tree=T16,
               room_departure=R5,
               room_arrival=R6,
               relative_departure_coordinates=[a, a],
               relative_arrival_coordinates=[a, a],
               surrounding_color=Color3)
    D17 = Door(two_way=False,
               tree=T17,
               room_departure=R6,
               room_arrival=R7,
               relative_departure_coordinates=[1/2, 1],
               relative_arrival_coordinates=[1/2, 0],
               surrounding_color=Color3)
    D18 = Door(two_way=False,
               tree=T18,
               room_departure=R7,
               room_arrival=R8,
               relative_departure_coordinates=[1/2, 1],
               relative_arrival_coordinates=[1/2, 0],
               surrounding_color=Color3)
    D19 = Door(two_way=False,
               tree=T19,
               room_departure=R8,
               room_arrival=R9,
               relative_departure_coordinates=[a, 1-a],
               relative_arrival_coordinates=[a, 1-a],
               surrounding_color=Color3)
    D20 = Door(two_way=False,
               tree=T20,
               room_departure=R9,
               room_arrival=R10,
               relative_departure_coordinates=[1, 1/2],
               relative_arrival_coordinates=[0, 1/2],
               surrounding_color=Color3)
    D21 = Door(two_way=False,
               tree=T21,
               room_departure=R10,
               room_arrival=R11,
               relative_departure_coordinates=[1, 1/2],
               relative_arrival_coordinates=[0, 1/2],
               surrounding_color=Color3)
    D22 = Door(two_way=False,
               tree=T22,
               room_departure=R11,
               room_arrival=R12,
               relative_departure_coordinates=[1-a, 1-a],
               relative_arrival_coordinates=[1-a, 1-a],
               surrounding_color=Color3)
    D23 = Door(two_way=False,
               tree=T23,
               room_departure=R12,
               room_arrival=R1,
               relative_departure_coordinates=[1/2, 0],
               relative_arrival_coordinates=[1/2, 1],
               surrounding_color=Color3)
    D24 = Door(two_way=False,
               tree=T24,
               room_departure=R0,
               room_arrival=RE,
               relative_position=0.55,
               surrounding_color=Color4)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24],
                 fastest_solution=None,
                 level_color=Levels_colors_list.BLACK,
                 name='Wheel graph',
                 door_window_size=650,
                 keep_proportions=True,
                 uniform_surrounding_colors=False,
                 uniform_inside_room_color=False)

    return level