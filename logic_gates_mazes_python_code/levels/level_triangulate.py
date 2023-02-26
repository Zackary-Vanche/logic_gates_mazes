# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 10:03:01 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def level_triangulate():
    v = 0

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3', value=v)
    S4 = Switch(name='S4')
    S5 = Switch(name='S5', value=v)
    S6 = Switch(name='S6')
    S7 = Switch(name='S7', value=v)
    S8 = Switch(name='S8', value=v)
    S9 = Switch(name='S9')

    SN1 = Switch(value=1)

    tree_list_BIN_5 = Tree.tree_list_BIN(5)

    T0 = Tree(tree_list=['AND',
                         ['SUPOREQU', [None], ['DIST', tree_list_BIN_5, tree_list_BIN_5, [None], [None]]],
                         ['SUPOREQU', [None], ['DIST', tree_list_BIN_5, tree_list_BIN_5, [None], [None]]],
                         ['SUP', [None], ['DIST', tree_list_BIN_5, tree_list_BIN_5, [None], [None]]]],
              empty=True,
              name='T0',
              switches=[Switch(value=2),
                        S0, S1, S2, S3, S4,
                        S5, S6, S7, S8, S9,
                        Switch(value=7), Switch(value=12),

                        Switch(value=3),
                        S0, S1, S2, S3, S4,
                        S5, S6, S7, S8, S9,
                        Switch(value=7), Switch(value=10),

                        Switch(value=4),
                        S0, S1, S2, S3, S4,
                        S5, S6, S7, S8, S9,
                        Switch(value=9), Switch(value=16),
                        ],
              cut_expression=True,
              cut_expression_separator=']')

    R0 = Room(name='R0',
              position=[0, 0, 5, 2],
              switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9])
    RE = Room(name='RE',
              position=[2, 2.5, 1, 1 / 2],
              is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=RE,
              relative_position=1 / 2,
              relative_departure_coordinates=[1 / 2, 1],
              relative_arrival_coordinates=[1 / 2, 0])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution='S0 S1 S2 S5 S7 S8 D0',
                 level_color=Levels_colors_list.FROM_HUE(hu=0, sa=0.3, li=0.7),
                 name='Triangulate',
                 door_window_size=700,
                 keep_proportions=True,
                 y_separation=40,
                 border=70)

    return level