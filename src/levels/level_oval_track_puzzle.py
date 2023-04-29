# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 12:16:18 2023

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from os.path import exists as os_path_exists

def level_oval_track_puzzle(): 
    
    v = 1

    S0 = Switch(name='S0')

    S1 = Switch(name='S1')
    S2 = Switch(name='S2')

    S3 = Switch(name='S3')
    S4 = Switch(name='S4')

    S5 = Switch(name='S5', value=v)
    S6 = Switch(name='S6')

    S7 = Switch(name='S7', value=v)
    S8 = Switch(name='S8')

    S9 = Switch(name='S9')
    S10 = Switch(name='S10', value=v)

    S11 = Switch(name='S11')
    S12 = Switch(name='S12', value=v)

    S13 = Switch(name='S13', value=v)
    S14 = Switch(name='S14', value=v)

    S15 = Switch(name='S15', value=v)
    S16 = Switch(name='S16', value=v)
    
    tree_list_1 = ['EQU', Tree.tree_list_BIN(2), Tree.tree_list_BIN(2)]
    tree_list_2 = ['AND', [None], tree_list_1]
    tree_list_8 = ['EQUSET'] + [Tree.tree_list_BIN(2)]*8 + [[None]]*8

    T0 = Tree(tree_list=[None],
                empty=True,
                name='T0',
                switches=[S0])
    T1 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T1',
                switches=[S1, S2, S3, S4])
    T2 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T2',
                switches=[S0, S3, S4, S5, S6])
    T3 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T3',
                switches=[S0, S5, S6, S7, S8])
    T4 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T4',
                switches=[S0, S7, S8, S9, S10])
    T5 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T5',
                switches=[S0, S9, S10, S11, S12])
    T6 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T6',
                switches=[S0, S11, S12, S13, S14])
    T7 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T7',
                switches=[S13, S14, S15, S16])
    T8 = Tree(tree_list=tree_list_8,
                empty=True,
                name='T8',
                switches=[S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16,
                          0, 0, 1, 1, 2, 2, 3, 3])
    T9 = Tree(tree_list=Tree.tree_list_not,
                empty=True,
                name='T9',
                switches=[S0])
    T10 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T10',
                switches=[S0, S15, S16, S1, S2])
    T11 = Tree(tree_list=tree_list_8,
                empty=True,
                name='T11',
                switches=[S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16,
                          0, 0, 1, 1, 2, 2, 3, 3])
    filename = 'levels/Oval_track_puzzle_random_exits.txt'
    if os_path_exists(filename):
        with open(filename, 'r') as fr:
            lines = fr.readlines()
            l = rd_choice(lines)
        T12 = Tree(tree_list=Tree.tree_list_from_str(l),
                    empty=True,
                    name='T12',
                    switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16])
    else:
        T12 = Tree(tree_list=[None],
                    empty=True,
                    name='T12',
                    switches=[S0])
    
    ey = 1/3
    e = 0.95+2*ey

    R0 = Room(name='R0',
                position=[2, 2, 2.5, ey],
                switches_list=[S0])
    R1 = Room(name='R1',
                position=[2-1/16, 4, 1, ey],
                switches_list=[S1, S2])
    R2 = Room(name='R2',
                position=[1.5, 3, 1, ey],
                switches_list=[S3, S4])
    R3 = Room(name='R3',
                position=[1.75, 7-e, 1, ey],
                switches_list=[S5, S6])
    R4 = Room(name='R4',
                position=[2+1/16, 6-e, 1, ey],
                switches_list=[S7, S8])
    R5 = Room(name='R5',
                position=[3.5-1/16, 6-e, 1, ey],
                switches_list=[S9, S10])
    R6 = Room(name='R6',
                position=[3.75, 7-e, 1, ey],
                switches_list=[S11, S12])
    R7 = Room(name='R7',
                position=[4, 3, 1, ey],
                switches_list=[S13, S14])
    R8 = Room(name='R8',
                position=[3.5+1/16, 4, 1, ey],
                switches_list=[S15, S16])
    RE = Room(name='RE',
              position=[2.75, 2+e, 1, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_arrival_coordinates=[0.5/2, 1/2])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=[0.5/2, 1/2])
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3,
                relative_departure_coordinates=[0.25/2, 1/2],
                relative_arrival_coordinates=[0.25/2, 1/2])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R5)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R5,
                room_arrival=R6)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R6,
                room_arrival=R7,
                relative_departure_coordinates=[1.75/2, 1/2],
                relative_arrival_coordinates=[1.75/2, 1/2])
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R7,
                room_arrival=R8,
                relative_arrival_coordinates=[1.5/2, 1/2])
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R8,
                room_arrival=R0,
                relative_departure_coordinates=[1.5/2, 1/2])
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R0,
                room_arrival=R7,
                relative_departure_coordinates=[2.5/3, 1/2])
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R8,
                room_arrival=R1)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R2,
                room_arrival=R0,
                relative_arrival_coordinates=[0.5/3, 1/2])
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R0,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=-0.075, sa=0.6, li=0.3),
                 name='Oval_track_puzzle',
                 keep_proportions=True,
                 door_window_size=900)
    
    return level