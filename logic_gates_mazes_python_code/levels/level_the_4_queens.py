#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 14:47:27 2022

@author: blanc-sablon
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def level_the_4_queens(fast_solution_finding=False):
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
    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')
    S15 = Switch(name='S15')

    SN2 = Switch(name='2', value=2)
    SN3 = Switch(name='3', value=3)
    SN4 = Switch(name='4', value=4)

    tree_list_sum2 = ['SUM'] + [[None]] * 2
    tree_list_sum3 = ['SUM'] + [[None]] * 3
    tree_list_sum4 = ['SUM'] + [[None]] * 4

    tree_list_2 = ['INF', tree_list_sum2, [None]]
    tree_list_3 = ['INF', tree_list_sum3, [None]]
    tree_list_4 = ['INF', tree_list_sum4, [None]]

    tree_list_line = ['AND'] + [tree_list_4] * 4
    tree_list_diag = ['AND',
                      tree_list_2,
                      tree_list_3,
                      tree_list_4,
                      tree_list_3,
                      tree_list_2]

    if fast_solution_finding:
        T0 = Tree(tree_list=['AND',
                             ['SUP', ["SUM"] + [[None]] * 16, [None]],
                             tree_list_line,
                             tree_list_line,
                             tree_list_diag,
                             tree_list_diag,
                             ['INF', ["SUM"] + [[None]] * 4, [None]]],
                  empty=True,
                  name='T0',
                  switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15,
                            SN3,

                            S0, S1, S2, S3, SN2,
                            S4, S5, S6, S7, SN2,
                            S8, S9, S10, S11, SN2,
                            S12, S13, S14, S15, SN2,

                            S0, S4, S8, S12, SN2,
                            S1, S5, S9, S13, SN2,
                            S2, S6, S10, S14, SN2,
                            S3, S7, S11, S15, SN2,

                            S8, S13, SN2,
                            S4, S9, S14, SN2,
                            S0, S5, S10, S15, SN2,
                            S1, S6, S11, SN2,
                            S2, S7, SN2,

                            S4, S1, SN2,
                            S8, S5, S2, SN2,
                            S12, S9, S6, S3, SN2,
                            S13, S10, S7, SN2,
                            S14, S11, SN2,

                            S1, S7, S8, S14, SN4
                            ],
                  cut_expression=True,
                  cut_expression_separator=')')

        R0 = Room(name='R0',
                  position=[0, 8, 9, 9],
                  switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15])
        RE = Room(name='RE',
                  position=[-1 / 2, -1 / 2, 2, 2],
                  is_exit=True)  # E pour exit ou end

        D0 = Door(two_way=False,
                  tree=T0,
                  room_departure=R0,
                  room_arrival=RE,
                  relative_departure_coordinates=[1 / 20, 1 / 20])

        level = Maze(start_room_index=0,
                     exit_room_index=-1,
                     rooms_list=[R0, RE],
                     doors_list=[D0],
                     fastest_solution='S2 S4 S11 S13 D0',
                     level_color=Levels_colors_list.FROM_HUE(0),
                     name='The 4 queens',
                     door_window_size=800,
                     keep_proportions=True)

        return level
    else:
        T0 = Tree(tree_list=['SUP', ["SUM"] + [[None]] * 16, [None]],
                  empty=True,
                  name='T0',
                  switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15,
                            SN3])
        T1 = Tree(tree_list=tree_list_line,
                  empty=True,
                  name='T1',
                  switches=[S0, S1, S2, S3, SN2,
                            S4, S5, S6, S7, SN2,
                            S8, S9, S10, S11, SN2,
                            S12, S13, S14, S15, SN2])
        T2 = Tree(tree_list=tree_list_line,
                  empty=True,
                  name='T2',
                  switches=[S0, S4, S8, S12, SN2,
                            S1, S5, S9, S13, SN2,
                            S2, S6, S10, S14, SN2,
                            S3, S7, S11, S15, SN2])
        T3 = Tree(tree_list=tree_list_diag,
                  empty=True,
                  name='T3',
                  switches=[S8, S13, SN2,
                            S4, S9, S14, SN2,
                            S0, S5, S10, S15, SN2,
                            S1, S6, S11, SN2,
                            S2, S7, SN2])
        T4 = Tree(tree_list=tree_list_diag,
                  empty=True,
                  name='T4',
                  switches=[S4, S1, SN2,
                            S8, S5, S2, SN2,
                            S12, S9, S6, S3, SN2,
                            S13, S10, S7, SN2,
                            S14, S11, SN2])
        T5 = Tree(tree_list=['INF', ["SUM"] + [[None]] * 4, [None]],
                  empty=True,
                  name='T5',
                  switches=[S1, S7, S8, S14, SN4])

        R0 = Room(name='R0',
                  position=[0, 8, 9, 9],
                  switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15])
        R1 = Room(name='R1',
                  position=[0, 4, 1, 1],
                  switches_list=[])
        R2 = Room(name='R2',
                  position=[4, 4, 1, 1],
                  switches_list=[])
        R3 = Room(name='R3',
                  position=[8, 4, 1, 1],
                  switches_list=[])
        R4 = Room(name='R4',
                  position=[8, 0, 1, 1],
                  switches_list=[])
        R5 = Room(name='R5',
                  position=[4, 0, 1, 1],
                  switches_list=[])
        RE = Room(name='RE',
                  position=[-1 / 2, -1 / 2, 2, 2],
                  is_exit=True)  # E pour exit ou end

        D0 = Door(two_way=False,
                  tree=T0,
                  room_departure=R0,
                  room_arrival=R1,
                  relative_departure_coordinates=[1 / 20, 1 / 20])
        D1 = Door(two_way=False,
                  tree=T1,
                  room_departure=R1,
                  room_arrival=R2)
        D2 = Door(two_way=False,
                  tree=T2,
                  room_departure=R2,
                  room_arrival=R3)
        D3 = Door(two_way=False,
                  tree=T3,
                  room_departure=R3,
                  room_arrival=R4)
        D4 = Door(two_way=False,
                  tree=T4,
                  room_departure=R4,
                  room_arrival=R5)
        D5 = Door(two_way=False,
                  tree=T5,
                  room_departure=R5,
                  room_arrival=RE)

        level = Maze(start_room_index=0,
                     exit_room_index=-1,
                     rooms_list=[R0, R1, R2, R3, R4, R5, RE],
                     doors_list=[D0, D1, D2, D3, D4, D5],
                     fastest_solution='S2 S4 S11 S13 D0 D1 D2 D3 D4 D5',
                     level_color=Levels_colors_list.FROM_HUE(0),
                     name='The 4 queens',
                     door_window_size=800,
                     keep_proportions=True)

        return level