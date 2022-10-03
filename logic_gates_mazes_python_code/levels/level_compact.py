# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:15:31 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def level_compact():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    
    SN1 = Switch(value=1)

    T0 = Tree(tree_list=[None],
              empty=True,
              name='T0',
              switches = [SN1])
    T1 = Tree(tree_list=[None],
              empty=True,
              name='T1',
              switches = [SN1])
    T2 = Tree(tree_list=[None],
              empty=True,
              name='T2',
              switches = [SN1])
    T3 = Tree(tree_list=[None],
              empty=True,
              name='T3',
              switches = [SN1])
    T4 = Tree(tree_list=[None],
              empty=True,
              name='T4',
              switches = [SN1])
    T5 = Tree(tree_list=[None],
              empty=True,
              name='T5',
              switches = [SN1])
    T6 = Tree(tree_list=[None],
              empty=True,
              name='T6',
              switches = [SN1])
    T7 = Tree(tree_list=[None],
              empty=True,
              name='T7',
              switches = [SN1])
    T8 = Tree(tree_list=[None],
              empty=True,
              name='T8',
              switches = [SN1])
    T9 = Tree(tree_list=[None],
              empty=True,
              name='T9',
              switches = [SN1])
    T10 = Tree(tree_list=[None],
              empty=True,
              name='T10',
              switches = [SN1])
    T11 = Tree(tree_list=[None],
              empty=True,
              name='T11',
              switches = [SN1])
    T12 = Tree(tree_list=[None],
              empty=True,
              name='T12',
              switches = [SN1])

    e = 1

    R0 = Room(name='R0',
              position = [[2, 0, e, e]]*2,
              switches_list = [S0],
              pages_list=[0])
    R1 = Room(name='R1',
              position = [[0, 0, e, e]]*2,
              switches_list = [S1],
              pages_list=[1])
    R2 = Room(name='R2',
              position = [[2, 2, e, e], [0, 2, e, e]],
              switches_list = [S2],
              pages_list=[0, 1])
    R3 = Room(name='R3',
              position = [[0, 2, e, e], [2, 2, e, e]],
              switches_list = [S3],
              pages_list=[0, 1])
    RE = Room(name='RE',
              position=[[2, -1.5, e, e]]*2,
              is_exit=True,
              pages_list=[0, 1])   # E pour exit ou end

    p1 = 0.65
    p2 = 0.40

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_position=p1)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R0,
              relative_position=p1)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R0,
              room_arrival=R2,
              relative_position=p1)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R2,
              room_arrival=R0,
              relative_position=p1)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R0,
              room_arrival=R3,
              relative_position=p2)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R3,
              room_arrival=R0,
              relative_position=p2)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R1,
              room_arrival=R2,
              relative_position=p2)
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R2,
              room_arrival=R1,
              relative_position=p2)
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R1,
              room_arrival=R3,
              relative_position=p1)
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R3,
              room_arrival=R1,
              relative_position=p1)
    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R2,
               room_arrival=R3,
               relative_position=p1)
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R3,
               room_arrival=R2,
               relative_position=p1)
    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R0,
               room_arrival=RE,
               relative_position=0.5)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12],
                 fastest_solution=None,
                 level_color=Levels_colors_list.BLACK_AND_GREY_WHITE_CONTOUR,
                 name='Compact',
                 door_window_size=1000,
                 border=100,
                 keep_proportions=True)

    return level