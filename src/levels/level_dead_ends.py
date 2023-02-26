# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:13:00 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def level_dead_ends():

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
    # SN  = Switch(name='SN') # Switch Null

    tree_list_0 = ["AND", Tree.tree_list_not, [None], [None], [None], [None]]
    tree_list_1 = Tree.tree_list_from_str('TFF')
    tree_list_2 = Tree.tree_list_NOR(2)
    tree_list_3 = Tree.tree_list_from_str('TFF')
    tree_list_4 = Tree.tree_list_NOR(2)
    tree_list_5 = Tree.tree_list_NOR(2)
    tree_list_6 = Tree.tree_list_NOR(2)
    tree_list_7 = Tree.tree_list_NOR(2)
    tree_list_8 = Tree.tree_list_from_str('TT T')  # ['OR', Tree.tree_list_and_2, [None]]
    tree_list_9 = Tree.tree_list_from_str('TF')
    tree_list_10 = ['AND', Tree.tree_list_XOR(2), Tree.tree_list_XOR(2), Tree.tree_list_not]
    tree_list_11 = Tree.tree_list_from_str('TF')
    # tree_list_12 = ['NA', [None], [None]]
    tree_list_12 = ['NOT', [None]]
    tree_list_13 = Tree.tree_list_from_str('FFF')
    tree_list_14 = tree_list_10[:]

    T0 = Tree(tree_list=tree_list_0, empty=True, name='T0', switches=[S0, S5, S6, S7, S8])
    T1 = Tree(tree_list=tree_list_1, empty=True, name='T1', switches=[S0, S1, S2])
    T2 = Tree(tree_list=tree_list_2, empty=True, name='T2', switches=[S3, S4])
    T3 = Tree(tree_list=tree_list_3, empty=True, name='T3', switches=[S0, S3, S4])
    T4 = Tree(tree_list=tree_list_4, empty=True, name='T4', switches=[S2, S8])
    T5 = Tree(tree_list=tree_list_5, empty=True, name='T5', switches=[S0, S5])
    T6 = Tree(tree_list=tree_list_6, empty=True, name='T6', switches=[S7, S10])
    T7 = Tree(tree_list=tree_list_7, empty=True, name='T7', switches=[S0, S6])
    T8 = Tree(tree_list=tree_list_8, empty=True, name='T8', switches=[S9, S11, S10])
    T9 = Tree(tree_list=tree_list_9, empty=True, name='T9', switches=[S0, S7])
    T10 = Tree(tree_list=tree_list_10, empty=True, name='T10', switches=[S1, S2, S3, S4, S6])
    T11 = Tree(tree_list=tree_list_11, empty=True, name='T11', switches=[S0, S8])
    T12 = Tree(tree_list=tree_list_12, empty=True, name='T12', switches=[S9])
    T13 = Tree(tree_list=tree_list_13, empty=True, name='T13', switches=[S9, S10, S11])
    T14 = Tree(tree_list=tree_list_14, empty=True, name='T14', switches=[S1, S3, S2, S4, S5])

    position_R0 = [3, 4, 4, 2]
    position_R1 = [1, 1.5, 3, 1]
    position_R2 = [6, 1.5, 3, 1]
    position_R3 = [-0.5, 4, 1.5, 2]
    position_R4 = [9, 4, 1.5, 2]
    position_R5 = [1, 7, 2, 1]
    position_R6 = [7, 7, 2, 1]
    position_R7 = [3, 8.5, 4, 1.25]
    position_RE = [4, 0.1, 2, 1]

    R0 = Room(name='R0', position=position_R0, switches_list=[S0])
    R1 = Room(name='R1', position=position_R1, switches_list=[S1, S2])
    R2 = Room(name='R2', position=position_R2, switches_list=[S3, S4])
    R3 = Room(name='R3', position=position_R3, switches_list=[S5])
    R4 = Room(name='R4', position=position_R4, switches_list=[S6])
    R5 = Room(name='R5', position=position_R5, switches_list=[S7])
    R6 = Room(name='R6', position=position_R6, switches_list=[S8])
    R7 = Room(name='R7', position=position_R7, switches_list=[S9, S10, S11])
    RE = Room(name='RE', position=position_RE, is_exit=True)  # E pour exit ou end

    e = 0.1

    relative_departure_coordinates_D0 = [1 / 2, 1 / 2]
    relative_arrival_coordinates_D0 = [1 / 2, 1 / 2]
    relative_departure_coordinates_D1 = [0, 0]
    relative_arrival_coordinates_D1 = [2 / 3, 1]
    relative_departure_coordinates_D2 = [1, 1]
    relative_arrival_coordinates_D2 = [1 / 4, 0]
    relative_departure_coordinates_D3 = [3 / 4, 0]
    relative_arrival_coordinates_D3 = [0, 1]
    relative_departure_coordinates_D4 = [1 / 3, 1]
    relative_arrival_coordinates_D4 = [1, 0]
    relative_departure_coordinates_D5 = [0, 1 / 4]
    relative_arrival_coordinates_D5 = [1, 1 / 4]
    relative_departure_coordinates_D6 = [1, 3 / 4]
    relative_arrival_coordinates_D6 = [0, 3 / 4]
    relative_departure_coordinates_D7 = [1, 1 / 4]
    relative_arrival_coordinates_D7 = [0, 1 / 4]
    relative_departure_coordinates_D8 = [0, 3 / 4]
    relative_arrival_coordinates_D8 = [1, 3 / 4]
    relative_departure_coordinates_D9 = [0, 1]
    relative_arrival_coordinates_D9 = [1 / 2 - e, 0 + e]
    relative_departure_coordinates_D10 = [1, 0]
    relative_arrival_coordinates_D10 = [1 / 4 + e, 1 - e]
    relative_departure_coordinates_D12 = [0, 0]
    relative_arrival_coordinates_D12 = [3 / 4 - e, 1 - e]
    relative_departure_coordinates_D11 = [1, 1]
    relative_arrival_coordinates_D11 = [1 / 2 + e, 0 + e]
    relative_departure_coordinates_D13 = [3 / 8, 1]
    relative_arrival_coordinates_D13 = [3 / 8, 0]
    relative_departure_coordinates_D14 = [5 / 8, 0]
    relative_arrival_coordinates_D14 = [5 / 8, 1]

    D0 = Door(two_way=False,
              tree=T0, name='D0',
              room_departure=R0,
              room_arrival=RE,
              relative_departure_coordinates=relative_departure_coordinates_D0,
              relative_arrival_coordinates=relative_arrival_coordinates_D0)
    D1 = Door(two_way=False,
              tree=T1, name='D1',
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=relative_departure_coordinates_D1,
              relative_arrival_coordinates=relative_arrival_coordinates_D1)
    D2 = Door(two_way=False,
              tree=T2,
              name='D2',
              room_departure=R1,
              room_arrival=R0,
              relative_departure_coordinates=relative_departure_coordinates_D2,
              relative_arrival_coordinates=relative_arrival_coordinates_D2)
    D3 = Door(two_way=False,
              tree=T3,
              name='D3',
              room_departure=R0,
              room_arrival=R2,
              relative_departure_coordinates=relative_departure_coordinates_D3,
              relative_arrival_coordinates=relative_arrival_coordinates_D3)
    D4 = Door(two_way=False,
              tree=T4,
              name='D4',
              room_departure=R2,
              room_arrival=R0,
              relative_departure_coordinates=relative_departure_coordinates_D4,
              relative_arrival_coordinates=relative_arrival_coordinates_D4)
    D5 = Door(two_way=False,
              tree=T5,
              name='D5',
              room_departure=R0,
              room_arrival=R3,
              relative_departure_coordinates=relative_departure_coordinates_D5,
              relative_arrival_coordinates=relative_arrival_coordinates_D5)
    D6 = Door(two_way=False,
              tree=T6,
              name='D6',
              room_departure=R3,
              room_arrival=R0,
              relative_departure_coordinates=relative_departure_coordinates_D6,
              relative_arrival_coordinates=relative_arrival_coordinates_D6)
    D7 = Door(two_way=False,
              tree=T7,
              name='D7',
              room_departure=R0,
              room_arrival=R4,
              relative_departure_coordinates=relative_departure_coordinates_D7,
              relative_arrival_coordinates=relative_arrival_coordinates_D7)
    D8 = Door(two_way=False,
              tree=T8,
              name='D8',
              room_departure=R4,
              room_arrival=R0,
              relative_departure_coordinates=relative_departure_coordinates_D8,
              relative_arrival_coordinates=relative_arrival_coordinates_D8)
    D9 = Door(two_way=False,
              tree=T9,
              name='D9',
              room_departure=R0,
              room_arrival=R5,
              relative_departure_coordinates=relative_departure_coordinates_D9,
              relative_arrival_coordinates=relative_arrival_coordinates_D9)
    D10 = Door(two_way=False,
               tree=T10,
               name='D10',
               room_departure=R5,
               room_arrival=R0,
               relative_departure_coordinates=relative_departure_coordinates_D10,
               relative_arrival_coordinates=relative_arrival_coordinates_D10)
    D11 = Door(two_way=False,
               tree=T11,
               name='D11',
               room_departure=R0,
               room_arrival=R6,
               relative_departure_coordinates=relative_departure_coordinates_D11,
               relative_arrival_coordinates=relative_arrival_coordinates_D11)
    D12 = Door(two_way=False,
               tree=T12,
               name='D12',
               room_departure=R6,
               room_arrival=R0,
               relative_departure_coordinates=relative_departure_coordinates_D12,
               relative_arrival_coordinates=relative_arrival_coordinates_D12)
    D13 = Door(two_way=False,
               tree=T13,
               name='D13',
               room_departure=R0,
               room_arrival=R7,
               relative_departure_coordinates=relative_departure_coordinates_D13,
               relative_arrival_coordinates=relative_arrival_coordinates_D13)
    D14 = Door(two_way=False,
               tree=T14,
               name='D14',
               room_departure=R7,
               room_arrival=R0,
               relative_departure_coordinates=relative_departure_coordinates_D14,
               relative_arrival_coordinates=relative_arrival_coordinates_D14)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14],
                 fastest_solution="S0 D1 S1 D2 D3 S4 D4 D11 S8 D12 S0 D13 S9 S11 D14 D5 S5 D6 S0 D9 S7 D10 S0 D7 S6 D8 D0",
                 level_color=Levels_colors_list.DARK_GREEN,
                 name='Dead_ends',
                 door_window_size=500,
                 border=50)

    return level