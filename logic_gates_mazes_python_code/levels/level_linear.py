# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:15:58 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def level_linear():
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')

    tree_list_0 = Tree.tree_list_AND(2)
    tree_list_1 = Tree.tree_list_from_str('TF')
    tree_list_2 = Tree.tree_list_from_str('FT')
    tree_list_3 = Tree.tree_list_NOR(2)

    T0 = Tree(tree_list=tree_list_0, empty=True, name='T0',
              switches=[S0, S1])  # , easy_logical_expression_PN = 'AND S0 S1\n= & S0 S1')
    T1 = Tree(tree_list=tree_list_1, empty=True, name='T1',
              switches=[S2, S3])  # , easy_logical_expression_PN = 'AND S2 NOT S3\n= & S2 ¬ S3')
    T2 = Tree(tree_list=tree_list_2, empty=True, name='T2',
              switches=[S4, S5])  # , easy_logical_expression_PN = 'AND NOT S4 S5\n= & ¬ S2 S3')
    T3 = Tree(tree_list=tree_list_3, empty=True, name='T3',
              switches=[S6, S7])  # , easy_logical_expression_PN = 'NOR S6 S7\n= & ¬ S6 ¬ S7\n= ¬| S6 S7')

    position_R0 = [1, 16, 12, 2]
    position_R1 = [2, 12, 10, 2]
    position_R2 = [3, 8, 8, 2]
    position_R3 = [4, 4, 6, 2]
    position_RE = [5, 0, 4, 2]

    R0 = Room(name='R0', position=position_R0, switches_list=[S0, S1])
    R1 = Room(name='R1', position=position_R1, switches_list=[S2, S3])
    R2 = Room(name='R2', position=position_R2, switches_list=[S4, S5])
    R3 = Room(name='R3', position=position_R3, switches_list=[S6, S7])
    RE = Room(name='RE', position=position_RE, is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=True,
              tree=T0,
              name='D0',
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=True,
              tree=T1,
              name='D1',
              room_departure=R1,
              room_arrival=R2)
    D2 = Door(two_way=True,
              tree=T2,
              name='D2',
              room_departure=R2,
              room_arrival=R3)
    D3 = Door(two_way=True,
              tree=T3,
              name='D3',
              room_departure=R3,
              room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, RE],
                 doors_list=[D0, D1, D2, D3],
                 fastest_solution='S0 S1 D0 S2 D1 S5 D2 D3',
                 level_color=Levels_colors_list.BRIGHT_GREEN,
                 name='Linear',
                 door_window_size=550,
                 keep_proportions=True)

    return level