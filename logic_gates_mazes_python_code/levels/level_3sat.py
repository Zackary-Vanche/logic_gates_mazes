# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 20:30:42 2022

@author: utilisateur
"""

# Problème 3-SAT

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import randint as rd_randint
from random import shuffle as rd_shuffle

def level_3sat():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')

    Slist = [S0, S1, S2, S3, S4, S5]

    # m = 20
    # n = 3
    # CNF_expression = ''
    # for i in range(m):
    #     for j in range(n):
    #         CNF_expression += rd_choice(['T', 'F'])
    #     CNF_expression += ' '
    # CNF_expression = CNF_expression[:-1]
    # print(CNF_expression)
    # Slist_T0 = []
    # for i in range(m):
    #     rd.shuffle(Slist)
    #     Slist_T0.extend(Slist[:n])
    # print([S.name for S in Slist_T0])

    CNF_expression = "TTT FFF FFT TFT FFF FTF FTT FFT TFF FTT TTT FFT FFF FTF TFF FTT TTT FFT FTT TTF"
    Slist_T0 = [S1, S2, S5, S5, S1, S0, S0, S4, S3, S0, S2, S3, S3, S1, S5, S1, S2, S0, S3, S5, S4, S5, S1, S2, S5, S4,
                S2, S2, S4, S5, S3, S0, S2, S5, S2, S0, S3, S2, S0, S2, S5, S4, S1, S0, S5, S2, S4, S1, S4, S1, S3, S5,
                S3, S0, S2, S4, S5, S0, S5, S2]

    T0 = Tree(tree_list=Tree.tree_list_from_str(CNF_expression, CNF=True),
              empty=True,
              name='T0',
              switches=Slist_T0,
              cut_expression=True)

    R0 = Room(name='R0',
              position=[0, 0, 2, 3],
              switches_list=Slist)
    RE = Room(name='RE',
              position=[0, 4, 2, 1],
              is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=RE,
              relative_departure_coordinates=[1 / 2, 1],
              relative_arrival_coordinates=[1 / 2, 0])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution='S1 S3 S4 D0',
                 level_color=Levels_colors_list.WHITE_AND_BLACK,
                 name='3 SAT',
                 door_window_size=530,
                 keep_proportions=True)

    return level