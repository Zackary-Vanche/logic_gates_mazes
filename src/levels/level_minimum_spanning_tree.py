# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:30:34 2023

@author: zackary.vanche
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def level_minimum_spanning_tree(): 

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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17]
    
    n = 3
    
    tree_list_PROD = ['PROD', [None], [None]]
    tree_list_SUM_aux = ['SUM'] + [tree_list_PROD]*n
    tree_list_SUM = ['SUM'] + [tree_list_SUM_aux]*(len(Slist)//n)
    tree_list_0 = ['INFOREQU', tree_list_SUM, [None]]
    
    ln = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 42, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    T0 = Tree(tree_list=tree_list_0,
              name='T0',
              switches=[ln[0], S0,
                        ln[1], S1,
                        ln[2], S2,
                        ln[3], S3,
                        ln[4], S4,
                        ln[5], S5,
                        ln[6], S6,
                        ln[7], S7,
                        ln[8], S8,
                        ln[9], S9,
                        ln[10], S10,
                        ln[11], S11,
                        ln[12], S12,
                        ln[13], S13,
                        ln[14], S14,
                        ln[15], S15,
                        ln[16], S16,
                        ln[17], S17,
                        183],
              cut_expression=True)
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[S0])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[S1])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[S2])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[S3])
    T5 = Tree(tree_list=[None],
                name='T5',
                switches=[S4])
    T6 = Tree(tree_list=[None],
                name='T6',
                switches=[S5])
    T7 = Tree(tree_list=[None],
                name='T7',
                switches=[S6])
    T8 = Tree(tree_list=[None],
                name='T8',
                switches=[S7])
    T9 = Tree(tree_list=[None],
                name='T9',
                switches=[S8])
    T10 = Tree(tree_list=[None],
                name='T10',
                switches=[S9])
    T11 = Tree(tree_list=[None],
                name='T11',
                switches=[S10])
    T12 = Tree(tree_list=[None],
                name='T12',
                switches=[S11])
    T13 = Tree(tree_list=[None],
                name='T13',
                switches=[S12])
    T14 = Tree(tree_list=[None],
                name='T14',
                switches=[S13])
    T15 = Tree(tree_list=[None],
                name='T15',
                switches=[S14])
    T16 = Tree(tree_list=[None],
                name='T16',
                switches=[S15])
    T17 = Tree(tree_list=[None],
                name='T17',
                switches=[S16])
    T18 = Tree(tree_list=[None],
                name='T18',
                switches=[S17])
    T19 = Tree(tree_list=Tree.tree_list_AND(10),
                name='T19',
                switches=[S18, S19, S20, S21, S22, S23, S24, S25, S26, S27])
    
    ex = 1
    ey = 1
    dx = 1
    dy = 1

    R0 = Room(name='R0',
                position=[4*dx, 4*dy, 3*ex, 3*ey],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[0*dx, 6*dy, ex, ey],
                switches_list=[S18])
    R2 = Room(name='R2',
                position=[0*dx, 4*dy, ex, ey],
                switches_list=[S19])
    R3 = Room(name='R3',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S20])
    R4 = Room(name='R4',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S21])
    R5 = Room(name='R5',
                position=[2*dx, 4*dy, ex, ey],
                switches_list=[S22])
    R6 = Room(name='R6',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S23])
    R7 = Room(name='R7',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[S24])
    R8 = Room(name='R8',
                position=[4*dx, 2*dy, ex, ey],
                switches_list=[S25])
    R9 = Room(name='R9',
                position=[4*dx, 0*dy, ex, ey],
                switches_list=[S26])
    R10 = Room(name='R10',
                position=[6*dx, 0*dy, ex, ey],
                switches_list=[S27])
    RE = Room(name='RE',
              position=[6*dx, 2*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R5)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R3)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R5)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R2,
                room_arrival=R6)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R3,
                room_arrival=R4)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R3,
                room_arrival=R6)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R3,
                room_arrival=R7)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R4,
                room_arrival=R7)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R5,
                room_arrival=R6)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R5,
                room_arrival=R8)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R6,
                room_arrival=R7)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R6,
                room_arrival=R8)
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R6,
                room_arrival=R9)
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R7,
                room_arrival=R9)
    D16 = Door(two_way=True,
                tree=T16,
                name='D16',
                room_departure=R8,
                room_arrival=R9)
    D17 = Door(two_way=True,
                tree=T17,
                name='D17',
                room_departure=R8,
                room_arrival=R10)
    D18 = Door(two_way=True,
                tree=T18,
                name='D18',
                room_departure=R9,
                room_arrival=R10)
    D19 = Door(two_way=True,
                tree=T19,
                name='D19',
                room_departure=R10,
                room_arrival=RE)
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0.425, sa=0.4, li=0.375)
    lcolor.surrounding_color = Color.ORANGE

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19],
                 fastest_solution='S0 S1 S2 S4 S5 S7 S10 S13 S16 D0 S18 D1 S19 D3 S20 D6 S21 D6 D8 S24 D8 D3 D5 S23 D14 S26 D14 D5 D1 D2 S22 D11 S25 D17 S27 D19',
                 level_color=lcolor,
                 name='Minimum spanning tree',
                 keep_proportions=True,
                 door_window_size=500)
    
    return level
