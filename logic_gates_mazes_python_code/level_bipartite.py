# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 08:42:08 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_bipartite():
    
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    
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
    
    position_R0 = [10, 0, 3, 6]
    position_R1 = [6, 0, 2, 2]
    position_R2 = [0, 4, 2, 2]
    position_R3 = [6, 8, 2, 2]
    position_R4 = [0, 0, 2, 2]
    position_R5 = [6, 4, 2, 2]
    position_R6 = [0, 8, 2, 2]
    position_RE = [10, 8, 3, 2]
    
    R0 = Room(name='R0', position=position_R0, switches_list=[S0])
    R1 = Room(name='R1', position=position_R1, switches_list=[S1])
    R2 = Room(name='R2', position=position_R2, switches_list=[S2])
    R3 = Room(name='R3', position=position_R3, switches_list=[S3])
    R4 = Room(name='R4', position=position_R4, switches_list=[S4])
    R5 = Room(name='R5', position=position_R5, switches_list=[S5])
    R6 = Room(name='R6', position=position_R6, switches_list=[S6])
    RE = Room(name='RE', position=position_RE,
              is_exit=True)   # E pour exit ou end
    
    D0 = Door(two_way=False,
                tree=T0,
                room_departure=R0,
                room_arrival=R1,
                relative_position=0.6)
    
    D1 = Door(two_way=False,
                tree=T1,
                room_departure=R1,
                room_arrival=R4)
    D2 = Door(two_way=False,
                tree=T2,
                room_departure=R1,
                room_arrival=R5)
    D3 = Door(two_way=False,
                tree=T3,
                room_departure=R1,
                room_arrival=R6,
                relative_position=1/4)

    D4 = Door(two_way=False,
                tree=T4,
                room_departure=R2,
                room_arrival=R4)
    D5 = Door(two_way=False,
                tree=T5,
                room_departure=R2,
                room_arrival=R5,
                relative_position=1/3)
    D6 = Door(two_way=False,
                tree=T6,
                room_departure=R2,
                room_arrival=R6)

    D7 = Door(two_way=False,
                tree=T7,
                room_departure=R3,
                room_arrival=R4,
                relative_position=1/4)
    D8 = Door(two_way=False,
                tree=T8,
                room_departure=R3,
                room_arrival=R5)
    D9 = Door(two_way=False,
                tree=T9,
                room_departure=R3,
                room_arrival=R6)

    D10 = Door(two_way=False,
                tree=T10,
                room_departure=R3,
                room_arrival=RE)
    
    l_help_txt = ["""
"""] # TODO

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10],
                 fastest_solution=None,
                 level_color=Levels_colors_list.BLACK_AND_GREY_ORANGE_CONTOUR,
                 name='Bipartite',
                 help_txt=l_help_txt,
                 door_window_size=600,
                 keep_proportions=True)

    return level