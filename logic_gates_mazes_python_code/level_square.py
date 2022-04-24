# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:17:23 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def level_square():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')

    T0 = Tree(tree_list=Tree.tree_list_from_str('TFTT'),
              empty=True,
              name='T0',
              switches=[S0, S1, S2, S3])
    T1 = Tree(tree_list=Tree.tree_list_from_str('TFFT'),
              empty=True,
              name='T1',
              switches=[S0, S1, S2, S3])
    T2 = Tree(tree_list=Tree.tree_list_from_str('TFFF'),
              empty=True,
              name='T2',
              switches=[S0, S1, S2, S3])
    T3 = Tree(tree_list=Tree.tree_list_from_str('TTTT'),
              empty=True,
              name='T3',
              switches=[S0, S1, S2, S3])
    T4 = Tree(tree_list=Tree.tree_list_from_str('TTTT'),
              empty=True,
              name='T4',
              switches=[S0, S1, S2, S3])

    position_R0 = [2, 0, 3, 2]
    position_R1 = [0, 3, 5, 2]
    position_RE = [0, 0, 1.25, 2]

    R0 = Room(name='R0',
              position=position_R0,
              switches_list=[S0, S2])
    R1 = Room(name='R1',
              position=position_R1,
              switches_list=[S1, S3])
    RE = Room(name='RE',
              position=position_RE,
              is_exit=True)  # E pour exit ou end

    relative_departure_coordinates_D0 = [0, 1]
    relative_arrival_coordinates_D0 = [0, 0]
    relative_departure_coordinates_D1 = [1/3, 0]
    relative_arrival_coordinates_D1 = [1/3, 1]
    relative_departure_coordinates_D2 = [2/3, 1]
    relative_arrival_coordinates_D2 = [2/3, 0]
    relative_departure_coordinates_D3 = [0.98, 0.02]
    relative_arrival_coordinates_D3 = [0.98, 0.98]
    relative_departure_coordinates_D4 = [0, 1/2]
    relative_arrival_coordinates_D4 = [1, 1/2]

    D0 = Door(two_way=False,
              tree=T0,
              name='D0',
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=relative_departure_coordinates_D0,
              relative_arrival_coordinates=relative_arrival_coordinates_D0)
    D1 = Door(two_way=False,
              tree=T1,
              name='D1',
              room_departure=R1,
              room_arrival=R0,
              relative_departure_coordinates=relative_departure_coordinates_D1,
              relative_arrival_coordinates=relative_arrival_coordinates_D1)
    D2 = Door(two_way=False,
              tree=T2,
              name='D2',
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=relative_departure_coordinates_D2,
              relative_arrival_coordinates=relative_arrival_coordinates_D2)
    D3 = Door(two_way=False,
              tree=T3,
              name='D3',
              room_departure=R1,
              room_arrival=R0,
              relative_departure_coordinates=relative_departure_coordinates_D3,
              relative_arrival_coordinates=relative_arrival_coordinates_D3)
    D4 = Door(two_way=False,
              tree=T4,
              name='D4',
              room_departure=R0,
              room_arrival=RE,
              relative_departure_coordinates=relative_departure_coordinates_D4,
              relative_arrival_coordinates=relative_arrival_coordinates_D4)

    l_help_txt = ["""Instead of writing actions one by one, one can write several at a time, separated by spaces.
For instance, you can write :
    S0 S1 D0
if you want to turn on S0, S1 and then use the door D0.
"""]

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, RE],
                 doors_list=[D0, D1, D2, D3, D4],
                 fastest_solution="S0 D2 S3 D1 S2 D0 S1 D3 D4",
                 level_color=Levels_colors_list.DARK_RED,
                 name='Square',
                 help_txt=l_help_txt,
                 door_window_size=500,
                 border=60,
                 keep_proportions=True)

    return level
