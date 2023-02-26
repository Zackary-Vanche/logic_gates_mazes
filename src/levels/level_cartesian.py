# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:04:36 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_cartesian():

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
              switches=[S0])
    T1 = Tree(tree_list=[None],
              empty=True,
              name='T1',
              switches=[S0])
    T2 = Tree(tree_list=[None],
              empty=True,
              name='T2',
              switches=[S7])
    T3 = Tree(tree_list=Tree.tree_list_from_str('TF'),
              empty=True,
              name='T3',
              switches=[S1, S2])
    T4 = Tree(tree_list=Tree.tree_list_from_str('FT'),
              empty=True,
              name='T4',
              switches=[S4, S8])
    T5 = Tree(tree_list=Tree.tree_list_XNOR(2),
              empty=True,
              name='T5',
              switches=[S5, S6])
    T6 = Tree(tree_list=["AND", Tree.tree_list_XOR(2), [None]],
              empty=True,
              name='T6',
              switches=[S0, S1, S2])
    T7 = Tree(tree_list=["AND", Tree.tree_list_XOR(2), [None]],
              empty=True,
              name='T7',
              switches=[S1, S2, S4])
    T8 = Tree(tree_list=Tree.tree_list_XOR(2),
              empty=True,
              name='T8',
              switches=[S5, S6])
    T9 = Tree(tree_list=Tree.tree_list_XNOR(2),
              empty=True,
              name='T9',
              switches=[S3, S8])
    T10 = Tree(tree_list=Tree.tree_list_from_str('FTTTTTT'),
               empty=True,
               name='T10',
               switches=[S0, S2, S3, S4, S5, S7, S8])

    c = 1.2

    position_R0 = [0, 2, c, c]
    position_R1 = [0, 0, c, c]
    position_R2 = [2, 0, c, c]
    position_R3 = [4, 0, c, c]
    position_R4 = [4, 2, c, c]
    position_R5 = [4, 4, c, c]
    position_R6 = [2, 4, c, c]
    position_R7 = [2, 2, c, c]
    position_RE = [0, 4, c, c]

    R0 = Room(name='R0', position=position_R0, switches_list=[S0])
    R1 = Room(name='R1', position=position_R1, switches_list=[S1])
    R2 = Room(name='R2', position=position_R2, switches_list=[S2])
    R3 = Room(name='R3', position=position_R3, switches_list=[S3])
    R4 = Room(name='R4', position=position_R4, switches_list=[S4])
    R5 = Room(name='R5', position=position_R5, switches_list=[S5])
    R6 = Room(name='R6', position=position_R6, switches_list=[S6])
    R7 = Room(name='R7', position=position_R7, switches_list=[S7, S8])
    RE = Room(name='RE', position=position_RE,
              is_exit=True)   # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              name='D0',
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=False,
              tree=T1,
              name='D1',
              room_departure=R1,
              room_arrival=R2)
    D2 = Door(two_way=False,
              tree=T2,
              name='D2',
              room_departure=R2,
              room_arrival=R3)
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
              room_departure=R2,
              room_arrival=R7)
    D7 = Door(two_way=False,
              tree=T7,
              name='D7',
              room_departure=R4,
              room_arrival=R7)
    D8 = Door(two_way=False,
              tree=T8,
              name='D8',
              room_departure=R6,
              room_arrival=R7)
    D9 = Door(two_way=False,
              tree=T9,
              name='D9',
              room_departure=R7,
              room_arrival=R0)
    D10 = Door(two_way=False,
               tree=T10,
               name='D10',
               room_departure=R0,
               room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10],
                 fastest_solution="S0 D0 D1 S2 D6 S7 D9 D0 S1 D1 S2 D2 S3 D3 S4 D7 S8 D9 D0 D1 D2 D3 S4 D4 D5 S6 D8 D9 D0 D1 D2 D3 D4 S5 D5 S6 D8 D9 D0 D1 D2 D3 S4 D7 D9 D0 S1 D1 S2 D6 D9 S0 D10",
                 level_color=Levels_colors_list.GREEN_GREY,
                 name='Cartesian',
                 door_window_size=550,
                 keep_proportions=True)

    return level