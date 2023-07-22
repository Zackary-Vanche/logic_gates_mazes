# -*- coding: utf-8 -*-
"""
Created on Thu May  4 21:53:03 2023

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from os.path import exists as os_path_exists
from random import choice as rd_choice

def level_the_4th_dimension(): 
    
    v = 1

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')

    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')

    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')

    S9 = Switch(name='S9', value=v)
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')

    S12 = Switch(name='S12')
    S13 = Switch(name='S13', value=v)
    S14 = Switch(name='S14')
    
    S15 = Switch(name='S15', value=v)
    S16 = Switch(name='S16', value=v)
    S17 = Switch(name='S17')
    
    Slist0 = [S0, S1, S2]
    Slist1 = [S3, S4, S5]
    Slist2 = [S6, S7, S8]
    Slist3 = [S9, S10, S11]
    Slist4 = [S12, S13, S14]
    Slist5 = [S15, S16, S17]
    
    Slist = Slist0 + Slist1 + Slist2 + Slist3 + Slist4 + Slist5
    
    
    # tree_list_0 = ['IN'] + [Tree.tree_list_BIN(3)]*4
    tree_list_1 = ['EQU'] + [Tree.tree_list_BIN(3)]*2
    tree_list_4 = ['EQU'] + [Tree.tree_list_BIN(3)]*3
    tree_list_10 = ['EQU', ['BIN', [None], [None], Tree.tree_list_not], Tree.tree_list_BIN(3)]

    T0 = Tree(tree_list=[None],
                empty=True,
                name='T0',
                switches=[1]) # Slist0 + Slist2 + Slist3 + Slist4)
    T1 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T1',
                switches=Slist0 + Slist2)
    T2 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T2',
                switches=Slist0 + Slist3)
    T3 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T3',
                switches=Slist0 + Slist4)
    T4 = Tree(tree_list=tree_list_4,
                empty=True,
                name='T4',
                switches=Slist1 + Slist2 + Slist3)
    T5 = Tree(tree_list=tree_list_4,
                empty=True,
                name='T5',
                switches=Slist1 + Slist2 + Slist4)
    T6 = Tree(tree_list=tree_list_4,
                empty=True,
                name='T6',
                switches=Slist1 + Slist2 + Slist5)
    T7 = Tree(tree_list=tree_list_4,
                empty=True,
                name='T7',
                switches=Slist1 + Slist3 + Slist4)
    T8 = Tree(tree_list=tree_list_4,
                empty=True,
                name='T8',
                switches=Slist1 + Slist3 + Slist5)
    T9 = Tree(tree_list=tree_list_4,
                empty=True,
                name='T9',
                switches=Slist1 + Slist4 + Slist5)
    T10 = Tree(tree_list=tree_list_10,
                empty=True,
                name='T10',
                switches=Slist0 + Slist3)
    T11 = Tree(tree_list=tree_list_10,
                empty=True,
                name='T11',
                switches=Slist0 + Slist4)
    T12 = Tree(tree_list=tree_list_10,
                empty=True,
                name='T12',
                switches=Slist0 + Slist5)
    filename = 'levels/The_4th_dimension_random_exits.txt'
    if os_path_exists(filename):
        with open(filename, 'r') as fr:
            lines = fr.readlines()
            l = rd_choice(lines)
        T13 = Tree(tree_list=Tree.tree_list_from_str(l),
                    empty=True,
                    name='T13',
                    switches=Slist)
    else:
        T13 = Tree(tree_list=Tree.tree_list_from_str('FFFFFF'),
                    empty=True,
                    name='T13',
                    switches=[S0, S1, S2, S3, S4, S5])
    
    y0 = 1/4

    R0 = Room(name='R0',
                position=[0, 10, 7, 0.5],
                switches_list=Slist0)
    R1 = Room(name='R1',
                position=[0, y0+0.25, 5, 0.5],
                switches_list=Slist1)
    R2 = Room(name='R2',
                position=[1, 4, 1, 3],
                switches_list=Slist2)
    R3 = Room(name='R3',
                position=[3, 2, 1, 3],
                switches_list=Slist3)
    R4 = Room(name='R4',
                position=[4, 6, 1, 3],
                switches_list=Slist4)
    R5 = Room(name='R5',
                position=[6, 4, 1, 3],
                switches_list=Slist5)
    RE = Room(name='RE',
              position=[6, y0, 1, 2],
              is_exit=True)

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[0, 0],
                relative_arrival_coordinates=[0, 1])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=[1.5/5, 1],
                relative_arrival_coordinates=[1/2, 0])
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R3,
                relative_departure_coordinates=[3.5/5, 1],
                relative_arrival_coordinates=[1/2, 0])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R4,
                relative_departure_coordinates=[4.5/5, 1],
                relative_arrival_coordinates=[1/2, 0])
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R3)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R2,
                room_arrival=R4)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R2,
                room_arrival=R5,
                relative_position=0.3)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R3,
                room_arrival=R4)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R3,
                room_arrival=R5)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R4,
                room_arrival=R5)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R3,
                room_arrival=R0,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[3.5/7, 0])
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R4,
                room_arrival=R0,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[4.5/7, 0])
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R5,
                room_arrival=R0,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[6.5/7, 0])
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R1,
                room_arrival=RE,
                relative_departure_coordinates=[4.5/5, 1/2],
                relative_arrival_coordinates=[1/2, 1/4])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0.6, sa=0.4, li=0.5),
                 name='The_4th_dimension',
                 keep_proportions=True,
                 door_window_size=1000,
                 random=True)
    
    return level