# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:16:04 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def level_loop():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')

    tree_list_0 = [None]
    tree_list_1 = [None]
    tree_list_2 = [None]
    tree_list_3 = Tree.tree_list_bna

    T0 = Tree(tree_list=tree_list_0,
              empty=True,
              name='T0',
              switches=[S0])
    T1 = Tree(tree_list=tree_list_1,
              empty=True,
              name='T1',
              switches=[S1])
    T2 = Tree(tree_list=tree_list_2,
              empty=True,
              name='T2',
              switches=[S2])
    T3 = Tree(tree_list=tree_list_3,
              empty=True,
              name='T3',
              switches=[S0, S3])

    position_R0 = [1, 0, 2, 2]
    position_R1 = [4, 1, 2, 2]
    position_R2 = [3, 4, 2, 2]
    position_RE = [0, 3, 2, 2]

    R0 = Room(name='R0',
              position=position_R0,
              switches_list=[S0])
    R1 = Room(name='R1',
              position=position_R1,
              switches_list=[S1])
    R2 = Room(name='R2',
              position=position_R2,
              switches_list=[S2, S3])
    RE = Room(name='RE',
              position=position_RE,
              is_exit=True)  # E pour exit ou end

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
              room_arrival=R0)
    D3 = Door(two_way=False,
              tree=T3,
              name='D3',
              room_departure=R0,
              room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, RE],
                 doors_list=[D0, D1, D2, D3],
                 fastest_solution='S0 D0 S1 D1 S2 S3 D2 S0 D3',
                 level_color=Levels_colors_list.BRIGHT_RED,
                 name='Loop',
                 door_window_size=500,
                 border=60,
                 keep_proportions=True)

    return level
