# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 18:04:41 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_small():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    
    Slist = [S0, S1, S2, S3]
    
    SN1 = Switch(value=1)
    
    T0 = Tree(Tree.tree_list_from_str('T'),
              empty=True,
              name='T0',
              switches = [SN1],
              cut_expression=True)
    T1 = Tree(Tree.tree_list_from_str('T'),
              empty=True,
              name='T1',
              switches = [SN1],
              cut_expression=True)
    T2 = Tree(Tree.tree_list_from_str('T'),
              empty=True,
              name='T2',
              switches = [SN1],
              cut_expression=True)
    T3 = Tree(Tree.tree_list_from_str('T'),
              empty=True,
              name='T3',
              switches = [SN1],
              cut_expression=True)
    T4 = Tree(Tree.tree_list_from_str('T'),
              empty=True,
              name='T4',
              switches = [SN1],
              cut_expression=True)
    T5 = Tree(Tree.tree_list_from_str('T'),
              empty=True,
              name='T5',
              switches = [SN1],
              cut_expression=True)
    T6 = Tree(Tree.tree_list_from_str('T'),
              empty=True,
              name='T6',
              switches = [SN1],
              cut_expression=True)
    T7 = Tree(Tree.tree_list_from_str('T'),
              empty=True,
              name='T7',
              switches = [SN1],
              cut_expression=True)
    T8 = Tree(Tree.tree_list_from_str('T'),
              empty=True,
              name='T8',
              switches = [SN1],
              cut_expression=True)
    T9 = Tree(Tree.tree_list_from_str('T'),
              empty=True,
              name='T9',
              switches = [SN1],
              cut_expression=True)
    T10 = Tree(Tree.tree_list_from_str('T'),
              empty=True,
              name='T10',
              switches = [SN1],
              cut_expression=True)
    T11 = Tree(Tree.tree_list_from_str('T'),
              empty=True,
              name='T11',
              switches = [SN1],
              cut_expression=True)
    T12 = Tree(Tree.tree_list_from_str('T'),
              empty=True,
              name='T12',
              switches = [SN1],
              cut_expression=True)
    
    R0 = Room(name='R0',
              position = [0, 0, 1, 1],
              switches_list = [S0])
    R1 = Room(name='R1',
              position = [0, 2, 1, 1],
              switches_list = [S1])
    R2 = Room(name='R2',
              position = [2, 0, 1, 1],
              switches_list = [S2])
    R3 = Room(name='R3',
              position = [2, 2, 1, 1],
              switches_list = [S3])
    RE = Room(name='RE',
              position=[-0.7, -0.7, 0.4, 0.4],
              is_exit=True)   # E pour exit ou end
    
    rp = 0.4
    
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R0,
              relative_position=rp)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R0,
              room_arrival=R2,
              relative_position=rp)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R2,
              room_arrival=R0,
              relative_position=rp)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R0,
              room_arrival=R3,
              relative_position=rp)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R3,
              room_arrival=R0,
              relative_position=rp)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R1,
              room_arrival=R2,
              relative_position=rp)
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R2,
              room_arrival=R1,
              relative_position=rp)
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R1,
              room_arrival=R3,
              relative_position=rp)
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R3,
              room_arrival=R1,
              relative_position=rp)
    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R2,
               room_arrival=R3,
               relative_position=rp)
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R3,
               room_arrival=R2,
               relative_position=rp)
    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R0,
               room_arrival=RE,
               relative_departure_coordinates=[0, 0],
               relative_arrival_coordinates=[0.707, 0.707],
               relative_position=0.45)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0.15, sa=1, li=0.9),
                 name='Small',
                 door_window_size=600,
                 keep_proportions=False,
                 y_separation=40,
                 border=40)
    
    return level