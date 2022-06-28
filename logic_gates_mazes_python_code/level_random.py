# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 20:41:06 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def level_random():
    
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
    T8 = Tree(tree_list=[None],
              empty=True,
              name='T8',
              switches = [S0])
    T9 = Tree(tree_list=[None],
              empty=True,
              name='T9',
              switches = [S0])
    T10 = Tree(tree_list=[None],
              empty=True,
              name='T10',
              switches = [S0])
    T11 = Tree(tree_list=[None],
              empty=True,
              name='T11',
              switches = [S0])
    T12 = Tree(tree_list=[None],
              empty=True,
              name='T12',
              switches = [S0])
    T13 = Tree(tree_list=[None],
              empty=True,
              name='T13',
              switches = [S0])
    T14 = Tree(tree_list=[None],
              empty=True,
              name='T14',
              switches = [S0])
    T15 = Tree(tree_list=[None],
              empty=True,
              name='T15',
              switches = [S0])
    T16 = Tree(tree_list=[None],
              empty=True,
              name='T16',
              switches = [S0])
    T17 = Tree(tree_list=[None],
              empty=True,
              name='T17',
              switches = [S0])
    
    position_R0 = [7.25, 0, 2, 2]
    position_R1 = [3.75, 0, 2, 2]
    position_R2 = [-0.5, 4, 2, 2]
    position_R3 = [3.75, 8, 2, 2]
    position_R4 = [0.25, 0, 2, 2]
    position_R5 = [4.5, 4, 2, 2]
    position_R6 = [0.25, 8, 2, 2]
    position_R7 = [7.25, 8, 2, 2]
    position_RE = [8.75, 4.5, 1, 1]
    
    R0 = Room(name='R0',
              position=position_R0,
              switches_list=[S12, S13])
    R1 = Room(name='R1',
              position=position_R1,
              switches_list=[S0, S6])
    R2 = Room(name='R2',
              position=position_R2,
              switches_list=[S1, S7])
    R3 = Room(name='R3',
              position=position_R3,
              switches_list=[S2, S8])
    R4 = Room(name='R4',
              position=position_R4,
              switches_list=[S3, S9])
    R5 = Room(name='R5',
              position=position_R5,
              switches_list=[S4, S10])
    R6 = Room(name='R6',
              position=position_R6,
              switches_list=[S5, S11])
    
    R7 = Room(name='R7',
              position=position_R7,
              switches_list=[S14, S15])
    RE = Room(name='RE',
              position=position_RE,
              is_exit=True)   # E pour exit ou end
    
    D0 = Door(two_way=True,
              tree=T0,
              room_departure=R1,
              room_arrival=R4)
    D1 = Door(two_way=True,
              tree=T1,
              room_departure=R1,
              room_arrival=R5)
    D2 = Door(two_way=True,
              tree=T2,
              room_departure=R1,
              room_arrival=R6,
              relative_position=2/3)
    D3 = Door(two_way=True,
              tree=T3,
              room_departure=R2,
              room_arrival=R4)
    D4 = Door(two_way=True,
              tree=T4,
              room_departure=R2,
              room_arrival=R5,
              relative_position=2/3)
    D5 = Door(two_way=True,
              tree=T5,
              room_departure=R2,
              room_arrival=R6)
    D6 = Door(two_way=True,
              tree=T6,
              room_departure=R3,
              room_arrival=R4,
              relative_position=2/3)
    D7 = Door(two_way=True,
              tree=T7,
              room_departure=R3,
              room_arrival=R5)
    D8 = Door(two_way=True,
              tree=T8,
              room_departure=R3,
              room_arrival=R6)
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R0,
              room_arrival=R1)
    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R0,
               room_arrival=R5,
               relative_departure_coordinates = [0, 1],
               relative_position = 0.4)
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R5,
               room_arrival=R7,
               relative_arrival_coordinates = [0, 0],
               relative_position = 0.6)
    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R3,
               room_arrival=R7)
    D13 = Door(two_way=False,
               tree=T13,
               room_departure=R7,
               room_arrival=R0,
               relative_departure_coordinates = [0.1, 0],
               relative_arrival_coordinates = [0.1, 1],
               relative_position = 0.3)
    D14 = Door(two_way=False,
               tree=T14,
               room_departure=R7,
               room_arrival=R0,
               relative_departure_coordinates = [0.4, 0],
               relative_arrival_coordinates = [0.4, 1])
    D15 = Door(two_way=False,
               tree=T15,
               room_departure=R7,
               room_arrival=R0,
               relative_departure_coordinates = [0.7, 0],
               relative_arrival_coordinates = [0.7, 1],
               relative_position = 0.7)
    D16 = Door(two_way=False,
               tree=T16,
               room_departure=R0,
               room_arrival=RE,
               relative_departure_coordinates = [1, 1])
    D17 = Door(two_way=False,
               tree=T17,
               room_departure=R7,
               room_arrival=RE,
               relative_departure_coordinates = [1, 0])
    
    l_help_txt = ["""This level has several solutions.
"""]

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17],
                 fastest_solution=None,#"S0 D0 S1 D1 S4 D4 S8 D4 D7 S3 D8 S11 D2 D3 S12 D3 S1 S7 D1 S4 S10 D7 S3 S9 D10 D11",
                 level_color=Levels_colors_list.RANDOM(),
                 uniform_surrounding_colors=False,
                 name='Random',
                 help_txt=l_help_txt,
                 door_window_size=450,
                 border=100,
                 keep_proportions=False)

    return level