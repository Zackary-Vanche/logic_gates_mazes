# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 20:42:39 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_travelling_salesman(fast_solution_finding=False):
    
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
    S36 = Switch(name='S36')
    S37 = Switch(name='S37')
    S38 = Switch(name='S38')
    S39 = Switch(name='S39')
    S40 = Switch(name='S40')
    S41 = Switch(name='S41')
    
    SN4 = Switch(name='4', value=4)
    SN6 = Switch(name='6', value=6)
    SN12 = Switch(name='12', value=12)
    SN18 = Switch(name='18', value=18)
    SN30 = Switch(name='30', value=30)
    SN42 = Switch(name='42', value=42)
    SN60 = Switch(name='60', value=60)
    
    SNlist = [SN4, SN6, SN12, SN18, SN30, SN42, SN60]
    
    tree_list_IN = ['IN', Tree.tree_list_BIN(6)] + [[None]]*7
    
    tree_list_DIST = ['DIST'] + [Tree.tree_list_BIN(3)]*4 # 12
    
    tree_list_SUM = ['SUM'] + [tree_list_DIST]*7 # 72
    
    tree_list_INF = ['INF', tree_list_SUM, [None]] # 73

    if fast_solution_finding:
        T0 = Tree(tree_list=tree_list_IN,
                  empty=True,
                  name='T0',
                  switches = [S0, S1, S2, S3, S4, S5] + SNlist)
        T1 = Tree(tree_list=['AND',
                             tree_list_IN,
                             ['DIFF'] + [Tree.tree_list_BIN(6)]*2],
                  empty=True,
                  name='T1',
                  switches = [S6, S7, S8, S9, S10, S11] + SNlist + [S0, S1, S2, S3, S4, S5,
                                                                    S6, S7, S8, S9, S10, S11])
        T2 = Tree(tree_list=['AND',
                             tree_list_IN,
                             ['DIFF'] + [Tree.tree_list_BIN(6)]*3],
                  empty=True,
                  name='T2',
                  switches = [S12, S13, S14, S15, S16, S17] + SNlist + [S0, S1, S2, S3, S4, S5,
                                                                        S6, S7, S8, S9, S10, S11,
                                                                        S12, S13, S14, S15, S16, S17])
        T3 = Tree(tree_list=['AND',
                             tree_list_IN,
                             ['DIFF'] + [Tree.tree_list_BIN(6)]*4],
                  empty=True,
                  name='T3',
                  switches = [S18, S19, S20, S21, S22, S23] + SNlist + [S0, S1, S2, S3, S4, S5,
                                                                        S6, S7, S8, S9, S10, S11,
                                                                        S12, S13, S14, S15, S16, S17,
                                                                        S18, S19, S20, S21, S22, S23])
        T4 = Tree(tree_list=['AND',
                             tree_list_IN,
                             ['DIFF'] + [Tree.tree_list_BIN(6)]*5],
                  empty=True,
                  name='T4',
                  switches = [S24, S25, S26, S27, S28, S29] + SNlist + [S0, S1, S2, S3, S4, S5,
                                                                        S6, S7, S8, S9, S10, S11,
                                                                        S12, S13, S14, S15, S16, S17,
                                                                        S18, S19, S20, S21, S22, S23,
                                                                        S24, S25, S26, S27, S28, S29])
        T5 = Tree(tree_list=tree_list_IN,
                  empty=True,
                  name='T5',
                  switches = [S30, S31, S32, S33, S34, S35] + SNlist)
    else:
        T0 = Tree(tree_list=tree_list_IN,
                  empty=True,
                  name='T0',
                  switches = [S0, S1, S2, S3, S4, S5] + SNlist)
        T1 = Tree(tree_list=tree_list_IN,
                  empty=True,
                  name='T1',
                  switches = [S6, S7, S8, S9, S10, S11] + SNlist)
        T2 = Tree(tree_list=tree_list_IN,
                  empty=True,
                  name='T2',
                  switches = [S12, S13, S14, S15, S16, S17] + SNlist)
        T3 = Tree(tree_list=tree_list_IN,
                  empty=True,
                  name='T3',
                  switches = [S18, S19, S20, S21, S22, S23] + SNlist)
        T4 = Tree(tree_list=tree_list_IN,
                  empty=True,
                  name='T4',
                  switches = [S24, S25, S26, S27, S28, S29] + SNlist)
        T5 = Tree(tree_list=tree_list_IN,
                  empty=True,
                  name='T5',
                  switches = [S30, S31, S32, S33, S34, S35] + SNlist)
    T6 = Tree(tree_list=['DIFF'] + [Tree.tree_list_BIN(6)]*7,
              empty=True,
              name='T6',
              switches = [S0, S1, S2, S3, S4, S5,
                          S6, S7, S8, S9, S10, S11,
                          S12, S13, S14, S15, S16, S17,
                          S18, S19, S20, S21, S22, S23,
                          S24, S25, S26, S27, S28, S29,
                          S30, S31, S32, S33, S34, S35,
                          S36, S37, S38, S39, S40, S41],
              cut_expression=True,
              cut_expression_separator=')')
    
    T7 = Tree(tree_list=['AND',
                         tree_list_IN,
                         tree_list_INF,
                         Tree.tree_list_NAND(2)],
              empty=True,
              name='T7',
              switches = [S36, S37, S38, S39, S40, S41] + SNlist + [
                   S0,  S1,  S2,  S3,  S4,  S5,  S6,  S7,  S8,  S9, S10, S11,
                   S6,  S7,  S8,  S9, S10, S11, S12, S13, S14, S15, S16, S17,
                  S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23,
                  S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29,
                  S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, S34, S35,
                  S30, S31, S32, S33, S34, S35, S36, S37, S38, S39, S40, S41,
                  S36, S37, S38, S39, S40, S41,  S0,  S1,  S2,  S3,  S4,  S5,
                  Switch(name='19', value=19),
                  S13, S31],
              cut_expression=True,
              cut_expression_separator=']')

    a = 3
    e = 1/100
    l = 0.75
    
    if fast_solution_finding:
        possible_switches_values = [[0, 0, 1, 0, 0, 0],
                                    [0, 1, 1, 0, 0, 0],
                                    [0, 0, 1, 1, 0, 0],
                                    [0, 1, 0, 0, 1, 0],
                                    [0, 1, 1, 1, 1, 0],
                                    [0, 1, 0, 1, 0, 1],
                                    [0, 0, 1, 1, 1, 1]]
    else:
        possible_switches_values = None

    R0 = Room(name='R0',
              position=[l, 1.5*a, 6, 1],
              switches_list = [S0, S1, S2, S3, S4, S5],
              possible_switches_values=possible_switches_values)
    R1 = Room(name='R1',
              position=[l, 0.5*a, 6, 1],
              switches_list = [S6, S7, S8, S9, S10, S11],
              possible_switches_values=possible_switches_values)
    R2 = Room(name='R2',
              position=[0, 0, 6, 1],
              switches_list = [S12, S13, S14, S15, S16, S17],
              possible_switches_values=possible_switches_values)
    R3 = Room(name='R3',
              position=[0, a, 6, 1],
              switches_list = [S18, S19, S20, S21, S22, S23],
              possible_switches_values=possible_switches_values)
    R4 = Room(name='R4',
              position=[0, 2*a, 6, 1],
              switches_list = [S24, S25, S26, S27, S28, S29],
              possible_switches_values=possible_switches_values)
    R5 = Room(name='R5',
              position=[0, 3*a, 6, 1],
              switches_list = [S30, S31, S32, S33, S34, S35],
              possible_switches_values=possible_switches_values)
    R6 = Room(name='R6',
              position=[l, 3.5*a, 6, 1],
              switches_list = [S36, S37, S38, S39, S40, S41],
              possible_switches_values=possible_switches_values)
    R7 = Room(name='R7',
              position=[l+4, 2.5*a, 2, 1],
              switches_list = [])
    RE = Room(name='RE',
              position=[l, 2.5*a, 3, 1],
              is_exit=True)   # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1-e, 1/2],
              relative_arrival_coordinates=[1-e, 1/2])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=[1, 0],
              relative_arrival_coordinates=[1, 0])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=[e, 1/2],
              relative_arrival_coordinates=[e, 1/2])
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=R4,
              relative_departure_coordinates=[e, 1/2],
              relative_arrival_coordinates=[e, 1/2])
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R4,
              room_arrival=R5,
              relative_departure_coordinates=[e, 1/2],
              relative_arrival_coordinates=[e, 1/2])
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R5,
              room_arrival=R6,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[0, 1])
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R6,
              room_arrival=R7,
              relative_departure_coordinates=[1-e, 1/2],
              relative_arrival_coordinates=[1-e, 1/2])
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R7,
              room_arrival=RE,
              relative_departure_coordinates=[0, 1/2],
              relative_arrival_coordinates=[1, 1/2])

    level = Maze(start_room_index=0, 
                 exit_room_index=-1, 
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE], 
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7], 
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(0.2, sa=0.5, li=0.4),
                 name='Travelling salesman',
                 door_window_size = 800,
                 keep_proportions = False)

    return level