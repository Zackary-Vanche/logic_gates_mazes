# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 18:10:17 2024

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def f(): 

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
    
    Slist_0 = [S0, S1, S2, S3]
    Slist_1 = [S4, S5, S6, S7]
    Slist_2 = [S8, S9, S10, S11]
    Slist = Slist_0 + Slist_1 + Slist_2
    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_0)),
          name='V0',
          switches=Slist_0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_1)),
          name='V1',
          switches=Slist_1)
    V2 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_2)),
          name='V2',
          switches=Slist_2)
    V3 = Tree(tree_list=["SUM", [None], Tree.tree_list_PROD(2), Tree.tree_list_PROD(2)],
          name='V3',
          switches=[V0, 10, V1, 100, V2])
    V4 = Tree(tree_list=["SUM", [None], Tree.tree_list_PROD(2), Tree.tree_list_PROD(2)],
          name='V4',
          switches=[V0, 10, V0, 100, V0])

    T0 = Tree(tree_list=["EQU", Tree.tree_list_PROD(2), [None]],
                name='T0',
                switches=[3, V3, V4])
    T1 = Tree(tree_list=["AND"] + [Tree.tree_list_INF(2)]*3 + [Tree.tree_list_DIFF(2)],
                name='T1',
                switches=[V0, 10, V1, 10, V2, 10, V3, V4],
                cut_expression_depth_1=True)

    dx = 1
    dy = 1
    ex = 1
    ey = 1

    R0 = Room(name='R0',
                position=[2*dx, 1*dy, 4*ex, 3*ey],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[1*dx, 0*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1/8, 5/6])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, RE],
                 doors_list=[D0, D1],
                 fastest_solution="S0 S2 S7 S8 D0 D1",
                 level_color=Levels_colors_list.FROM_HUE(hu=0.01, sa=0.4, li=0.5),
                 name='One third',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level