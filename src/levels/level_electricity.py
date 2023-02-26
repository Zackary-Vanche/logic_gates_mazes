# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:13:36 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def level_electricity():
    v = 0
    w = 0

    S0 = Switch(name='S0', value=v)
    S1 = Switch(name='S1')
    S2 = Switch(name='S2', value=v)
    S3 = Switch(name='S3')
    S4 = Switch(name='S4', value=v)
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7', value=v)
    S8 = Switch(name='S8', value=v)
    S9 = Switch(name='S9', value=v)

    S10 = Switch(name='S10')
    S11 = Switch(name='S11', value=w)
    S12 = Switch(name='S12', value=w)
    S13 = Switch(name='S13')
    S14 = Switch(name='S14', value=w)
    S15 = Switch(name='S15')
    S16 = Switch(name='S16', value=w)
    S17 = Switch(name='S17', value=w)

    tree_list_0 = ['AND', [None], ['NAND', Tree.tree_list_from_str('FFT'), Tree.tree_list_from_str('TFF'),
                                   Tree.tree_list_from_str('FFT')]]

    T0 = Tree(tree_list=tree_list_0,
              empty=True,
              name='T0',
              switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9],
              easy_logical_expression_PN="& S0 ¬& [ & ( ¬S1 ¬S2 S3 ) & ( S4 ¬S5 ¬S6 ) & ( ¬S7 ¬S8 S9 ) ]")
    T1 = Tree(tree_list=Tree.tree_list_from_str('FFTTT'),
              empty=True,
              name='T1',
              switches=[S1, S2, S3, S10, S11])
    T2 = Tree(tree_list=Tree.tree_list_from_str('FTFTF'),
              empty=True, name='T2',
              switches=[S1, S2, S3, S10, S11])
    T3 = Tree(tree_list=Tree.tree_list_from_str('TFFFT'),
              empty=True, name='T3',
              switches=[S1, S2, S3, S10, S11])
    T4 = Tree(tree_list=['AND', Tree.tree_list_from_str('FFTTT'), Tree.tree_list_from_str('F T')],
              empty=True, name='T4',
              switches=[S4, S5, S6, S12, S13, S10, S11])
    T5 = Tree(tree_list=['AND', Tree.tree_list_from_str('FTFTF'), Tree.tree_list_NAND(2)],
              empty=True, name='T5',
              switches=[S4, S5, S6, S12, S13, S10, S11])
    T6 = Tree(tree_list=['AND', Tree.tree_list_from_str('TFFFT'), Tree.tree_list_from_str('T F')],
              empty=True, name='T6',
              switches=[S4, S5, S6, S12, S13, S10, S11])
    T7 = Tree(tree_list=['AND', Tree.tree_list_from_str('FFTTT'), Tree.tree_list_from_str('F T')],
              empty=True, name='T7',
              switches=[S7, S8, S9, S14, S15, S12, S13])
    T8 = Tree(tree_list=['AND', Tree.tree_list_from_str('FTFTF'), Tree.tree_list_from_str('T F')],
              empty=True, name='T8',
              switches=[S7, S8, S9, S14, S15, S12, S13])
    T9 = Tree(tree_list=['AND', Tree.tree_list_from_str('TFFFT'), Tree.tree_list_NAND(2)],
              empty=True, name='T9',
              switches=[S7, S8, S9, S14, S15, S12, S13])
    T10 = Tree(tree_list=['AND', Tree.tree_list_from_str('F T'), Tree.tree_list_NAND(2), Tree.tree_list_from_str('T F'),
                          [None], [None]],
               empty=True, name='T10',
               switches=[S10, S11, S12, S13, S14, S15, S16, S17])

    d = 0

    position_R0 = [5.25, 0 - d, 6, 4 + d]
    position_R1 = [9.75, 5.5 - d, 1, 4 + d]
    position_R2 = [6.75, 5 - d, 1, 4.5 + d]
    position_R3 = [3.75, 4.5 - d, 1, 5 + d]
    position_R4 = [0.75, 4 - d, 1, 5.5 + d]
    position_RE = [0.75, 0 - d, 2, 2 + d]

    R0 = Room(name='R0', position=position_R0, switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9])
    R1 = Room(name='R1', position=position_R1, switches_list=[S10, S11])
    R2 = Room(name='R2', position=position_R2, switches_list=[S12, S13])
    R3 = Room(name='R3', position=position_R3, switches_list=[S14, S15])
    R4 = Room(name='R4', position=position_R4, switches_list=[S16, S17])
    RE = Room(name='RE', position=position_RE, is_exit=True)  # E pour exit ou end

    e = 0.02

    relative_departure_coordinates_D0 = [11 / 12, 1]
    relative_arrival_coordinates_D0 = [1 / 2, 0]
    relative_departure_coordinates_D1 = [0, e]
    relative_arrival_coordinates_D1 = [1, e]
    relative_departure_coordinates_D2 = [0, 1 / 2]
    relative_arrival_coordinates_D2 = [1, 1 / 2]
    relative_departure_coordinates_D3 = [0.1, 1 - e]
    relative_arrival_coordinates_D3 = [1, 1 - e]
    relative_departure_coordinates_D4 = [0, e]
    relative_arrival_coordinates_D4 = [1, e]
    relative_departure_coordinates_D5 = [0, 1 / 2]
    relative_arrival_coordinates_D5 = [1, 1 / 2]
    relative_departure_coordinates_D6 = [0.1, 1 - e]
    relative_arrival_coordinates_D6 = [1, 1 - e]
    relative_departure_coordinates_D7 = [0, e]
    relative_arrival_coordinates_D7 = [1, e]
    relative_departure_coordinates_D8 = [0, 1 / 2]
    relative_arrival_coordinates_D8 = [1, 1 / 2]
    relative_departure_coordinates_D9 = [0.1, 1 - e]
    relative_arrival_coordinates_D9 = [1, 1 - e]
    relative_departure_coordinates_D10 = [1 / 2, 1 / 4]
    relative_arrival_coordinates_D10 = [1 / 2, 1 / 2]

    D0 = Door(two_way=False,
              tree=T0, name='D0',
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=relative_departure_coordinates_D0,
              relative_arrival_coordinates=relative_arrival_coordinates_D0)
    D1 = Door(two_way=False,
              tree=T1, name='D1',
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=relative_departure_coordinates_D1,
              relative_arrival_coordinates=relative_arrival_coordinates_D1)
    D2 = Door(two_way=False,
              tree=T2,
              name='D2',
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=relative_departure_coordinates_D2,
              relative_arrival_coordinates=relative_arrival_coordinates_D2)
    D3 = Door(two_way=False,
              tree=T3,
              name='D3',
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=relative_departure_coordinates_D3,
              relative_arrival_coordinates=relative_arrival_coordinates_D3)
    D4 = Door(two_way=False,
              tree=T4,
              name='D4',
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=relative_departure_coordinates_D4,
              relative_arrival_coordinates=relative_arrival_coordinates_D4)
    D5 = Door(two_way=False,
              tree=T5,
              name='D5',
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=relative_departure_coordinates_D5,
              relative_arrival_coordinates=relative_arrival_coordinates_D5)
    D6 = Door(two_way=False,
              tree=T6,
              name='D6',
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=relative_departure_coordinates_D6,
              relative_arrival_coordinates=relative_arrival_coordinates_D6)
    D7 = Door(two_way=False,
              tree=T7,
              name='D7',
              room_departure=R3,
              room_arrival=R4,
              relative_departure_coordinates=relative_departure_coordinates_D7,
              relative_arrival_coordinates=relative_arrival_coordinates_D7)
    D8 = Door(two_way=False,
              tree=T8,
              name='D8',
              room_departure=R3,
              room_arrival=R4,
              relative_departure_coordinates=relative_departure_coordinates_D8,
              relative_arrival_coordinates=relative_arrival_coordinates_D8)
    D9 = Door(two_way=False,
              tree=T9,
              name='D9',
              room_departure=R3,
              room_arrival=R4,
              relative_departure_coordinates=relative_departure_coordinates_D9,
              relative_arrival_coordinates=relative_arrival_coordinates_D9)
    D10 = Door(two_way=False,
               tree=T10,
               name='D10',
               room_departure=R4,
               room_arrival=RE,
               relative_departure_coordinates=relative_departure_coordinates_D10,
               relative_arrival_coordinates=relative_arrival_coordinates_D10)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10],
                 fastest_solution='S0 S1 S5 S8 D0 S11 D3 S12 D5 S14 D8 S16 S17 D10',
                 level_color=Levels_colors_list.GOLD_AND_SILVER,
                 name='Electricity',
                 border=70,
                 door_window_size=575)

    return level