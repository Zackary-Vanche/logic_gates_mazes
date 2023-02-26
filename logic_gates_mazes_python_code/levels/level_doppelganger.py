# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 21:41:11 2023

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle

def level_doppelganger():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')

    Slist = [S0, S1, S2, S3]
    lint = [i for i in range(1, 4)]
    rd_shuffle(lint)
    lint = [0] + lint

    Slist0 = []
    for i in range(4):
        for j in range(i+1):
            Slist0.extend([lint[j] + lint[i] * 4])
    # Slist0 = sorted(Slist0)

    T0 = Tree(tree_list=['IN', Tree.tree_list_BIN(4)] + [[None]]*len(Slist0),
              empty=True,
              name='T0',
              switches = Slist + Slist0,
              cut_expression=True)
    T1 = Tree(tree_list=['EQU', Tree.tree_list_BIN(4), [None]],
              empty=True,
              name='T1',
              switches = Slist + [Slist0[-1]])

    ex = 0.25
    ey = 0.75

    R0 = Room(name='R0',
              position = [0, 0, ex, ey],
              switches_list = [S0, S1])
    R1 = Room(name='R1',
              position = [0, 1, ex, ey],
              switches_list = [S2, S3])
    RE = Room(name='RE',
              position=[0, 2, ex, ey],
              is_exit=True)   # E pour exit ou end

    D0 = Door(two_way=True,
              tree=T0,
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1] + [RE],
                 doors_list=[D0, D1],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.3),
                 name='Doppelganger',
                 door_window_size=800,
                 keep_proportions=True,
                 y_separation=40,
                 border=40,
                 random=True)

    return level