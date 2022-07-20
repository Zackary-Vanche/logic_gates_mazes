#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 15:35:30 2022

@author: blanc-sablon
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_pancake_sorting():
    
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
    S16 = Switch(name='S16')
    S17 = Switch(name='S17')
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')
    S20 = Switch(name='S20')
    S21 = Switch(name='S21')
    S22 = Switch(name='S22')
    S23 = Switch(name='S23')
    S24 = Switch(name='S24')
    S25 = Switch(name='S25')
    S26 = Switch(name='S26')
    S27 = Switch(name='S27')
    S28 = Switch(name='S28')
    S29 = Switch(name='S29')
    S30 = Switch(name='S30')
    S31 = Switch(name='S31')
    S32 = Switch(name='S32')
    S33 = Switch(name='S33')
    S34 = Switch(name='S34')
    S35 = Switch(name='S35')

    T0 = Tree(tree_list=[None],
                empty=True,
                name='T0',
                switches = [S0])
    T1 = Tree(tree_list=[None],
                empty=True,
                name='T1',
                switches = [S0])
    T2 = Tree(tree_list=[None],
                empty=True,
                name='T2',
                switches = [S0])
    T3 = Tree(tree_list=[None],
                empty=True,
                name='T3',
                switches = [S0])
    T4 = Tree(tree_list=[None],
                empty=True,
                name='T4',
                switches = [S0])
    T5 = Tree(tree_list=[None],
                empty=True,
                name='T5',
                switches = [S0])
    T6 = Tree(tree_list=[None],
                empty=True,
                name='T6',
                switches = [S0])
    T7 = Tree(tree_list=[None],
                empty=True,
                name='T7',
                switches = [S0])

    R0 = Room(name='R0',
              position = [0, 3, 3, 6],
              switches_list = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17])
    R1 = Room(name='R1',
              position = [4, 1, 8*2/9, 8],
              switches_list = [S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, S34, S35])
    R2 = Room(name='R2',
              position = [2, 1.5, 1, 1],
              switches_list = [])
    RE = Room(name='RE',
              position=[0, 1.5, 1, 1],
              is_exit=True)   # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1, 5.5/6],
              relative_arrival_coordinates=[0, 7.5/8])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1, 4.5/6],
              relative_arrival_coordinates=[0, 6.5/8])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1, 3.5/6],
              relative_arrival_coordinates=[0, 5.5/8])
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1, 2.5/6],
              relative_arrival_coordinates=[0, 4.5/8])
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1, 1.5/6],
              relative_arrival_coordinates=[0, 3.5/8])
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R1,
              room_arrival=R0,
              relative_departure_coordinates=[0, 2.5/8],
              relative_arrival_coordinates=[1, 0.5/6])
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=[0.5/2, 1/8])
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R2,
              room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7],
                 fastest_solution=None,
                 level_color=Levels_colors_list.YELLOW_AND_BLACK,
                 name='Pancake sorting',
                 door_window_size=850,
                 keep_proportions=True)

    return level