# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 21:09:59 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_longest_path():
    
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    
    SN1 = Switch(name='1', value=1)
    SN2 = Switch(name='2', value=2)
    SN3 = Switch(name='3', value=3)
    SN4 = Switch(name='4', value=4)
    SN5 = Switch(name='5', value=5)
    
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
                switches = [S1])
    T3 = Tree(tree_list=[None],
                empty=True,
                name='T3',
                switches = [S1])
    T4 = Tree(tree_list=[None],
                empty=True,
                name='T4',
                switches = [S2])
    T5 = Tree(tree_list=[None],
                empty=True,
                name='T5',
                switches = [S2])
    T6 = Tree(tree_list=[None],
                empty=True,
                name='T6',
                switches = [S3])
    T7 = Tree(tree_list=[None],
                empty=True,
                name='T7',
                switches = [S4])
    T8 = Tree(tree_list=[None],
                empty=True,
                name='T8',
                switches = [S4])
    T9 = Tree(tree_list=[None],
                empty=True,
                name='T9',
                switches = [S5])
    T10 = Tree(tree_list=[None],
                empty=True,
                name='T10',
                switches = [S6])
    T11 = Tree(tree_list=[None],
                empty=True,
                name='T11',
                switches = [S7])
    T12 = Tree(tree_list=['SUP',
                              ['SUM'] + [['PROD', [None], [None]]]*9,
                              [None]],
                empty=True,
                name='T12',
                switches = [
                            SN1, S0,

                            SN2, S1,
                            SN3, S2,

                            SN4, S3,
                            SN3, S4,
                            SN5, S5,

                            SN2, S6,
                            SN1, S7,

                            SN1, S8,

                            Switch(name='5', value=10)])
    
    a = 1.5

    R0 = Room(name='R0',
                position = [0, 2*a, 1, 1],
                switches_list = [S0])
    R1 = Room(name='R1',
                position = [2, 1*a, 1, 1],
                switches_list = [S1])
    R2 = Room(name='R2',
                position = [2, 3*a, 1, 1],
                switches_list = [S2])
    R3 = Room(name='R3',
                position = [4, 0, 1, 1],
                switches_list = [S3])
    R4 = Room(name='R4',
                position = [4, 2*a, 1, 1],
                switches_list = [S4])
    R5 = Room(name='R5',
                position = [4, 4*a, 1, 1],
                switches_list = [S5])
    R6 = Room(name='R6',
                position = [6, 1*a, 1, 1],
                switches_list = [S6])
    R7 = Room(name='R7',
                position = [6, 3*a, 1, 1],
                switches_list = [S7])
    R8 = Room(name='R8',
                position = [8, 2*a, 1, 1],
                switches_list = [S8])
    RE = Room(name='RE',
              position=[8, 4*a, 1, 1],
              is_exit=True)   # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R0,
              room_arrival=R2)

    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R1,
              room_arrival=R3)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R1,
              room_arrival=R4)

    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R2,
              room_arrival=R4)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R2,
              room_arrival=R5)

    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R3,
              room_arrival=R6)

    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R4,
              room_arrival=R6)
    D8 = Door(two_way=False,
               tree=T8,
               room_departure=R4,
               room_arrival=R7)

    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R5,
              room_arrival=R7)

    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R6,
               room_arrival=R8)

    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R7,
               room_arrival=R8)
    
    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R8,
               room_arrival=RE)

    level = Maze(start_room_index=0, 
                 exit_room_index=-1, 
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, RE], 
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12], 
                 fastest_solution='S0 D1 S2 D5 S5 D9 S7 D11 S8 D12',
                 level_color=Levels_colors_list.WHITE,
                 name='Longest path',
                 door_window_size = 550,
                 keep_proportions = True)

    return level