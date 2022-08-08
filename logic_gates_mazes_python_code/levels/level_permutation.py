# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 13:11:42 2022

@author: utilisateur
"""

# 15 puzzle

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_permutation():
    
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')

    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')

    S7 = Switch(name='S7', value=1)
    S8 = Switch(name='S8')
    S9 = Switch(name='S9')

    S10 = Switch(name='S10')
    S11 = Switch(name='S11', value=1)
    S12 = Switch(name='S12')

    S13 = Switch(name='S13', value=1)
    S14 = Switch(name='S14', value=1)
    S15 = Switch(name='S15')

    S16 = Switch(name='S16')
    S17 = Switch(name='S17')
    S18 = Switch(name='S18', value=1)

    SN0 = Switch(value=0)
    SN1 = Switch(value=1)
    SN2 = Switch(value=2)
    SN3 = Switch(value=3)
    SN4 = Switch(value=4)
    SN5 = Switch(value=5)
    SN6 = Switch(value=6)
    SN7 = Switch(value=7)
    SN8 = Switch(value=8)
    SN9 = Switch(value=9)

    tree_list_OR_BIN4 = ['OR'] + [['EQU', Tree.tree_list_BIN(4), [None]]]*4

    T0 = Tree(tree_list=tree_list_OR_BIN4,
              empty=True,
              name='T0',
              switches = [S0, S1, S2, S3, SN0,
                          S0, S1, S2, S3, SN1,
                          S0, S1, S2, S3, SN2,
                          S0, S1, S2, S3, SN3],
              cut_expression=True,
              cut_expression_separator=']')
    T1 = Tree(tree_list=tree_list_OR_BIN4,
              empty=True,
              name='T1',
              switches = [S0, S1, S2, S3, SN0,
                          S0, S1, S2, S3, SN4,
                          S0, S1, S2, S3, SN5,
                          S0, S1, S2, S3, SN6],
              cut_expression=True,
              cut_expression_separator=']')
    T2 = Tree(tree_list=tree_list_OR_BIN4,
              empty=True,
              name='T2',
              switches = [S0, S1, S2, S3, SN1,
                          S0, S1, S2, S3, SN4,
                          S0, S1, S2, S3, SN7,
                          S0, S1, S2, S3, SN8])
    T3 = Tree(tree_list=tree_list_OR_BIN4,
              empty=True,
              name='T3',
              switches = [S0, S1, S2, S3, SN2,
                          S0, S1, S2, S3, SN5,
                          S0, S1, S2, S3, SN7,
                          S0, S1, S2, S3, SN9])
    T4 = Tree(tree_list=tree_list_OR_BIN4,
              empty=True,
              name='T4',
              switches = [S0, S1, S2, S3, SN3,
                          S0, S1, S2, S3, SN6,
                          S0, S1, S2, S3, SN8,
                          S0, S1, S2, S3, SN9])


    T5 = Tree(tree_list=tree_list_OR_BIN4,
              empty=True,
              name='T5',
              switches = [S0, S1, S2, S3, SN0,
                          S0, S1, S2, S3, SN1,
                          S0, S1, S2, S3, SN2,
                          S0, S1, S2, S3, SN3])
    T6 = Tree(tree_list=tree_list_OR_BIN4,
              empty=True,
              name='T6',
              switches = [S0, S1, S2, S3, SN0,
                          S0, S1, S2, S3, SN4,
                          S0, S1, S2, S3, SN5,
                          S0, S1, S2, S3, SN6])
    T7 = Tree(tree_list=tree_list_OR_BIN4,
              empty=True,
              name='T7',
              switches = [S0, S1, S2, S3, SN1,
                          S0, S1, S2, S3, SN4,
                          S0, S1, S2, S3, SN7,
                          S0, S1, S2, S3, SN8])
    T8 = Tree(tree_list=tree_list_OR_BIN4,
              empty=True,
              name='T8',
              switches = [S0, S1, S2, S3, SN2,
                          S0, S1, S2, S3, SN5,
                          S0, S1, S2, S3, SN7,
                          S0, S1, S2, S3, SN9])
    T9 = Tree(tree_list=tree_list_OR_BIN4,
              empty=True,
              name='T9',
              switches = [S0, S1, S2, S3, SN3,
                          S0, S1, S2, S3, SN6,
                          S0, S1, S2, S3, SN8,
                          S0, S1, S2, S3, SN9])


    T10 = Tree(tree_list=tree_list_OR_BIN4,
               empty=True,
               name='T10',
               switches = [S0, S1, S2, S3, SN0,
                           S0, S1, S2, S3, SN1,
                           S0, S1, S2, S3, SN2,
                           S0, S1, S2, S3, SN3])
    T11 = Tree(tree_list=tree_list_OR_BIN4,
               empty=True,
               name='T11',
               switches = [S0, S1, S2, S3, SN0,
                           S0, S1, S2, S3, SN4,
                           S0, S1, S2, S3, SN5,
                           S0, S1, S2, S3, SN6])
    T12 = Tree(tree_list=tree_list_OR_BIN4,
               empty=True,
               name='T12',
               switches = [S0, S1, S2, S3, SN1,
                           S0, S1, S2, S3, SN4,
                           S0, S1, S2, S3, SN7,
                           S0, S1, S2, S3, SN8])
    T13 = Tree(tree_list=tree_list_OR_BIN4,
               empty=True,
               name='T13',
               switches = [S0, S1, S2, S3, SN2,
                           S0, S1, S2, S3, SN5,
                           S0, S1, S2, S3, SN7,
                           S0, S1, S2, S3, SN9])
    T14 = Tree(tree_list=tree_list_OR_BIN4,
               empty=True,
               name='T14',
               switches = [S0, S1, S2, S3, SN3,
                           S0, S1, S2, S3, SN6,
                           S0, S1, S2, S3, SN8,
                           S0, S1, S2, S3, SN9])
    T15 = Tree(tree_list=['EQUSET'] + [Tree.tree_list_BIN(3)]*5 + [[None]]*5,
               empty=True,
               name='T15',
               switches = [S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18,
                           SN0, SN1, SN2, SN3, SN4],
               cut_expression=True,
               cut_expression_separator=']')
    # ['AND',
    #                       Tree.tree_list_from_str('FFFF'),
    #                       Tree.tree_list_from_str('FTF'),
    #                       Tree.tree_list_from_str('FFF'),
    #                       Tree.tree_list_from_str('FFT'),
    #                       Tree.tree_list_from_str('TFF'),
    #                       Tree.tree_list_from_str('TTF'),],
    T16 = Tree(tree_list=['AND', ['EQU', [None], Tree.tree_list_BIN(4)]] + [['EQU', [None], Tree.tree_list_BIN(3)]]*5,
               empty=True,
               name='T16',
               switches = [SN0, S0, S1, S2, S3,
                           SN2, S4, S5, S6,
                           SN4, S7, S8, S9,
                           SN0, S10, S11, S12,
                           SN1, S13, S14, S15,
                           SN3, S16, S17, S18,],
               cut_expression=True)

    ex = 0.925
    dy = 4.1
    dx = 1
    
    lx = 2.1

    R0 = Room(name='R0',
              position = [5*dx+lx, dy, ex, dy],
              switches_list = [S0, S1, S2, S3])
    R1 = Room(name='R1',
              position = [5*dx, 0, ex, dy],
              switches_list = [S4, S5, S6])
    R2 = Room(name='R2',
              position = [4*dx, dy/4, ex, dy],
              switches_list = [S7, S8, S9])
    R3 = Room(name='R3',
              position = [3*dx, dy/2, ex, dy],
              switches_list = [S10, S11, S12])
    R4 = Room(name='R4',
              position = [2*dx, 3*dy/4, ex, dy],
              switches_list = [S13, S14, S15])
    R5 = Room(name='R5',
              position = [dx, dy, ex, dy],
              switches_list = [S16, S17, S18])
    R6 = Room(name='R6',
              position = [-0.5*dx-0.4, 0, 2/3, dy],
              switches_list = [])
    R7 = Room(name='R7',
              position = [dx, 2.3*dy, 4*dx+ex, 2/3],
              switches_list = [])
    RE = Room(name='RE',
              position=[5*dx+lx, 0.35*dy, ex, dy/3],
              is_exit=True)   # E pour exit ou end

    a = 0.6

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[0, 0],
              relative_arrival_coordinates=[1, 1],
              relative_position=a*dx/(lx-ex))
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R0,
              room_arrival=R2,
              relative_departure_coordinates=[0, 1/4],
              relative_arrival_coordinates=[1, 1],
              relative_position=a*dx/(lx+dx-ex))
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R0,
              room_arrival=R3,
              relative_departure_coordinates=[0, 1/2],
              relative_arrival_coordinates=[1, 1],
              relative_position=a*dx/(lx+2*dx-ex))
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R0,
              room_arrival=R4,
              relative_departure_coordinates=[0, 3/4],
              relative_arrival_coordinates=[1, 1],
              relative_position=a*dx/(lx+3*dx-ex))
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R0,
              room_arrival=R5,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[1, 1],
              relative_position=a*dx/(lx+4*dx-ex))
    D5 = Door(two_way=True,
              tree=T5,
              room_departure=R1,
              room_arrival=R6,
              relative_departure_coordinates=[0, 0],
              relative_arrival_coordinates=[1, 0])
    D6 = Door(two_way=True,
              tree=T6,
              room_departure=R2,
              room_arrival=R6,
              relative_departure_coordinates=[0, 0],
              relative_arrival_coordinates=[1, 1/4])
    D7 = Door(two_way=True,
              tree=T7,
              room_departure=R3,
              room_arrival=R6,
              relative_departure_coordinates=[0, 0],
              relative_arrival_coordinates=[1, 1/2])
    D8 = Door(two_way=True,
              tree=T8,
              room_departure=R4,
              room_arrival=R6,
              relative_departure_coordinates=[0, 0],
              relative_arrival_coordinates=[1, 3/4])
    D9 = Door(two_way=True,
              tree=T9,
              room_departure=R5,
              room_arrival=R6,
              relative_departure_coordinates=[0, 0],
              relative_arrival_coordinates=[1, 1])
    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R1,
               room_arrival=R7,
               relative_departure_coordinates=[1/2, 1],
               relative_arrival_coordinates=[(4*dx+0.5*ex)/(4*dx+ex), 0],
               relative_position=0.15/(0.3+1))
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R2,
               room_arrival=R7,
               relative_departure_coordinates=[1/2, 1],
               relative_arrival_coordinates=[(3*dx+0.5*ex)/(4*dx+ex), 0],
               relative_position=0.15/(0.3+0.75))
    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R3,
               room_arrival=R7,
               relative_departure_coordinates=[1/2, 1],
               relative_arrival_coordinates=[(2*dx+0.5*ex)/(4*dx+ex), 0],
               relative_position=0.15/(0.3+0.5))
    D13 = Door(two_way=False,
               tree=T13,
               room_departure=R4,
               room_arrival=R7,
               relative_departure_coordinates=[1/2, 1],
               relative_arrival_coordinates=[(dx+0.5*ex)/(4*dx+ex), 0],
               relative_position=0.15/(0.3+0.25))
    D14 = Door(two_way=False,
               tree=T14,
               room_departure=R5,
               room_arrival=R7,
               relative_departure_coordinates=[1/2, 1],
               relative_arrival_coordinates=[0.5*ex/(4*dx+ex), 0],
               relative_position=0.15/(0.3))
    D15 = Door(two_way=False,
               tree=T15,
               room_departure=R7,
               room_arrival=R0,
               relative_departure_coordinates=[1, 1],
               relative_arrival_coordinates=[1, 1])
    D16 = Door(two_way=False,
               tree=T16,
               room_departure=R0,
               room_arrival=RE,
               relative_departure_coordinates=[1/2, 0],
               relative_arrival_coordinates=[1/2, 1])

    level = Maze(start_room_index=0, 
                 exit_room_index=-1, 
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE], 
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16], 
                 fastest_solution='S0 D0 S5 D5 D7 S11 D12 D15 S2 D1 S8 D6 D8 S14 D13 D15 S0 S1 D1 S7 S8 S9 D6 D9 S16 S17 S18 D14 D15 S1 S2 D16',
                 level_color=Levels_colors_list.FROM_HUE(0.83, sa=1, li=0.3),
                 name='Permutation',
                 door_window_size=750,
                 keep_proportions=True)

    return level