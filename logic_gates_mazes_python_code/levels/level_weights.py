# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 15:06:39 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_weights(fast_solution_finding=False):

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
    
    SN1 = Switch(value=1)
    SN2 = Switch(value=2)
    SN3 = Switch(value=3)
    
    def tree_list_EQU_SUM(k):
        return ['EQU', [None], ['SUM'] + [[None]]*k]
    
    if fast_solution_finding:
        tree_list_fast_solution_finding = ['AND',
                                           [None],
                                           tree_list_EQU_SUM(3),
                                           tree_list_EQU_SUM(4),
                                           tree_list_EQU_SUM(3),
                                           tree_list_EQU_SUM(3),
                                           tree_list_EQU_SUM(4),
                                           tree_list_EQU_SUM(3),
                                           tree_list_EQU_SUM(3),
                                           tree_list_EQU_SUM(4),
                                           tree_list_EQU_SUM(3),
                                           tree_list_EQU_SUM(2),
                                           tree_list_EQU_SUM(3),
                                           tree_list_EQU_SUM(2),]
        Slist = [SN1, S0, S3, S12,
                 SN2, S1, S4, S12, S13,
                 SN2, S2, S5, S13,
                 SN1, S5, S8, S14,
                 SN3, S4, S7, S14, S15,
                 SN3, S3, S6, S15,
                 SN1, S6, S9, S16,
                 SN2, S7, S10, S16, S17,
                 SN3, S8, S11, S17,
                 SN2, S11, S18,
                 SN2, S10, S18, S19,
                 SN1, S9, S19,]
        T0 = Tree(tree_list=tree_list_fast_solution_finding,
                  empty=True,
                  name='T0',
                  switches = [S0] + Slist,
                  cut_expression=True)
        T1 = Tree(tree_list=tree_list_fast_solution_finding,
                  empty=True,
                  name='T1',
                  switches = [S1] + Slist,
                  cut_expression=True)
        T2 = Tree(tree_list=tree_list_fast_solution_finding,
                  empty=True,
                  name='T2',
                  switches = [S2] + Slist,
                  cut_expression=True)
    else:
        T0 = Tree(tree_list=[None],
                  empty=True,
                  name='T0',
                  switches = [S0])
        T1 = Tree(tree_list=[None],
                  empty=True,
                  name='T1',
                  switches = [S1])
        T2 = Tree(tree_list=[None],
                  empty=True,
                  name='T2',
                  switches = [S2])
    T3 = Tree(tree_list=[None],
              empty=True,
              name='T3',
              switches = [S3])
    T4 = Tree(tree_list=[None],
              empty=True,
              name='T4',
              switches = [S4])
    T5 = Tree(tree_list=[None],
              empty=True,
              name='T5',
              switches = [S5])
    T6 = Tree(tree_list=[None],
              empty=True,
              name='T6',
              switches = [S6])
    T7 = Tree(tree_list=[None],
              empty=True,
              name='T7',
              switches = [S7])
    T8 = Tree(tree_list=[None],
              empty=True,
              name='T8',
              switches = [S8])
    T9 = Tree(tree_list=[None],
              empty=True,
              name='T9',
              switches = [S9])
    T10 = Tree(tree_list=[None],
              empty=True,
              name='T10',
              switches = [S10])
    T11 = Tree(tree_list=[None],
              empty=True,
              name='T11',
              switches = [S11])
    T12 = Tree(tree_list=[None],
              empty=True,
              name='T12',
              switches = [S12])
    T13 = Tree(tree_list=[None],
              empty=True,
              name='T13',
              switches = [S13])
    T14 = Tree(tree_list=[None],
              empty=True,
              name='T14',
              switches = [S14])
    T15 = Tree(tree_list=[None],
              empty=True,
              name='T15',
              switches = [S15])
    T16 = Tree(tree_list=[None],
              empty=True,
              name='T16',
              switches = [S16])
    T17 = Tree(tree_list=[None],
              empty=True,
              name='T17',
              switches = [S17])
    T18 = Tree(tree_list=[None],
              empty=True,
              name='T18',
              switches = [S18])
    T19 = Tree(tree_list=[None],
              empty=True,
              name='T19',
              switches = [S19])
    T20 = Tree(tree_list=['AND',
                          Tree.tree_list_AND(12),
                          tree_list_EQU_SUM(3),
                          tree_list_EQU_SUM(4),
                          tree_list_EQU_SUM(3),
                          tree_list_EQU_SUM(3),
                          tree_list_EQU_SUM(4),
                          tree_list_EQU_SUM(3),
                          tree_list_EQU_SUM(3),
                          tree_list_EQU_SUM(4),
                          tree_list_EQU_SUM(3),
                          tree_list_EQU_SUM(2),
                          tree_list_EQU_SUM(3),
                          tree_list_EQU_SUM(2),
                          ],
              empty=True,
              name='T20',
              switches = [S20, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31,
                          SN1, S0, S3, S12,
                          SN2, S1, S4, S12, S13,
                          SN2, S2, S5, S13,
                          SN1, S5, S8, S14,
                          SN3, S4, S7, S14, S15,
                          SN3, S3, S6, S15,
                          SN1, S6, S9, S16,
                          SN2, S7, S10, S16, S17,
                          SN3, S8, S11, S17,
                          SN2, S11, S18,
                          SN2, S10, S18, S19,
                          SN1, S9, S19,
                          ],
              cut_expression=True)
    
    ex = 1.5
    ey = 0.75
    
    R0 = Room(name='R0',
              position = [ex, 9, 9*ex, 1.8*ex],
              switches_list = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19])
    R1 = Room(name='R1',
              position = [ex, 7, ex, ey],
              switches_list = [S20])
    R2 = Room(name='R2',
              position = [5*ex, 7, ex, ey],
              switches_list = [S21])
    R3 = Room(name='R3',
              position = [9*ex, 7, ex, ey],
              switches_list = [S22])
    R4 = Room(name='R4',
              position = [(8+1/3)*ex, 5, ex, ey],
              switches_list = [S23])
    R5 = Room(name='R5',
              position = [5*ex, 5, ex, ey],
              switches_list = [S24])
    R6 = Room(name='R6',
              position = [(1+2/3)*ex, 5, ex, ey],
              switches_list = [S25])
    R7 = Room(name='R7',
              position = [(2+1/3)*ex, 3, ex, ey],
              switches_list = [S26])
    R8 = Room(name='R8',
              position = [5*ex, 3, ex, ey],
              switches_list = [S27])
    R9 = Room(name='R9',
              position = [(7+2/3)*ex, 3, ex, ey],
              switches_list = [S28])
    R10 = Room(name='R10',
              position = [7*ex, 1, ex, ey],
              switches_list = [S29])
    R11 = Room(name='R11',
              position = [5*ex, 1, ex, ey],
              switches_list = [S30])
    R12 = Room(name='R12',
               position = [3*ex, 1, ex, ey],
               switches_list = [S31])
    RE = Room(name='RE',
              position=[5*ex, -0.5, ex, 0.4],
              is_exit=True)   # E pour exit ou end
    
    rp = 1/2
    rdc = [1/2, 1/2]
    rac = [1/2, 1/2]

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_position=0.525,
              relative_departure_coordinates=[0.5/9, 0],
              relative_arrival_coordinates=[1/2, 1])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R0,
              room_arrival=R2,
              relative_position=rp,
              relative_departure_coordinates=[1/2, 0],
              relative_arrival_coordinates=[1/2, 1])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R0,
              room_arrival=R3,
              relative_position=0.525,
              relative_departure_coordinates=[8.5/9, 0],
              relative_arrival_coordinates=[1/2, 1])
    D3 = Door(two_way=True,
              tree=T3,
              room_departure=R1,
              room_arrival=R6,
              relative_position=rp,
              relative_departure_coordinates=rdc,
              relative_arrival_coordinates=rac)
    D4 = Door(two_way=True,
              tree=T4,
              room_departure=R2,
              room_arrival=R5,
              relative_position=rp,
              relative_departure_coordinates=rdc,
              relative_arrival_coordinates=rac)
    D5 = Door(two_way=True,
              tree=T5,
              room_departure=R3,
              room_arrival=R4,
              relative_position=rp,
              relative_departure_coordinates=rdc,
              relative_arrival_coordinates=rac)
    D6 = Door(two_way=True,
              tree=T6,
              room_departure=R6,
              room_arrival=R7,
              relative_position=rp,
              relative_departure_coordinates=rdc,
              relative_arrival_coordinates=rac)
    D7 = Door(two_way=True,
              tree=T7,
              room_departure=R5,
              room_arrival=R8,
              relative_position=rp,
              relative_departure_coordinates=rdc,
              relative_arrival_coordinates=rac)
    D8 = Door(two_way=True,
              tree=T8,
              room_departure=R4,
              room_arrival=R9,
              relative_position=rp,
              relative_departure_coordinates=rdc,
              relative_arrival_coordinates=rac)
    D9 = Door(two_way=True,
              tree=T9,
              room_departure=R7,
              room_arrival=R12,
              relative_position=rp,
              relative_departure_coordinates=rdc,
              relative_arrival_coordinates=rac)
    D10 = Door(two_way=True,
               tree=T10,
               room_departure=R8,
               room_arrival=R11,
               relative_position=rp,
               relative_departure_coordinates=rdc,
               relative_arrival_coordinates=rac)
    D11 = Door(two_way=True,
               tree=T11,
               room_departure=R9,
               room_arrival=R10,
               relative_position=rp,
               relative_departure_coordinates=rdc,
               relative_arrival_coordinates=rac)
    D12 = Door(two_way=True,
               tree=T12,
               room_departure=R1,
               room_arrival=R2,
               relative_position=rp,
               relative_departure_coordinates=[1, 1/2],
               relative_arrival_coordinates=[0, 1/2])
    D13 = Door(two_way=True,
               tree=T13,
               room_departure=R2,
               room_arrival=R3,
               relative_position=rp,
               relative_departure_coordinates=[1, 1/2],
               relative_arrival_coordinates=[0, 1/2])
    D14 = Door(two_way=True,
               tree=T14,
               room_departure=R4,
               room_arrival=R5,
               relative_position=rp,
               relative_departure_coordinates=[0, 1/2],
               relative_arrival_coordinates=[1, 1/2])
    D15 = Door(two_way=True,
               tree=T15,
               room_departure=R5,
               room_arrival=R6,
               relative_position=rp,
               relative_departure_coordinates=[0, 1/2],
               relative_arrival_coordinates=[1, 1/2])
    D16 = Door(two_way=True,
               tree=T16,
               room_departure=R7,
               room_arrival=R8,
               relative_position=rp,
               relative_departure_coordinates=[1, 1/2],
               relative_arrival_coordinates=[0, 1/2])
    D17 = Door(two_way=True,
               tree=T17,
               room_departure=R8,
               room_arrival=R9,
               relative_position=rp,
               relative_departure_coordinates=[1, 1/2],
               relative_arrival_coordinates=[0, 1/2])
    D18 = Door(two_way=True,
               tree=T18,
               room_departure=R10,
               room_arrival=R11,
               relative_position=rp,
               relative_departure_coordinates=rdc,
               relative_arrival_coordinates=rac)
    D19 = Door(two_way=True,
               tree=T19,
               room_departure=R11,
               room_arrival=R12,
               relative_position=rp,
               relative_departure_coordinates=rdc,
               relative_arrival_coordinates=rac)
    D20 = Door(two_way=True,
               tree=T20,
               room_departure=R11,
               room_arrival=RE,
               relative_position=rp,
               relative_departure_coordinates=[1/2, 0],
               relative_arrival_coordinates=[1/2, 1],
               is_open=False)
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20],
                 fastest_solution="S2 S3 S4 S6 S7 S8 S11 S13 S15 S17 S18 S19 D2 S22 D13 S21 D4 D15 D3 S20 D3 D6 S26 D6 S25 D15 S24 D7 S27 D17 D8 S23 D8 S28 D11 S29 D18 D19 S31 D19 S30 S2 S3 S4 S6 S7 S8 S11 S13 S15 S17 S18 S19 D2 S22 D13 S21 D4 S24 D15 S25 D3 S20 D3 D6 S26 D6 D15 D7 S27 D17 S28 D8 S23 D8 D11 S29 D18 S30 D19 S31 D19 D20",
                 level_color=Levels_colors_list.FROM_HUE(hu=0.45, sa=0.2, li=0.5),
                 name='Weights',
                 door_window_size=600,
                 keep_proportions=True,
                 y_separation=40,
                 border=40)
    
    return level