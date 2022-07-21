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

    v = 1

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

    S18 = Switch(name='S18', value=v)
    S19 = Switch(name='S19')
    S20 = Switch(name='S20')

    S21 = Switch(name='S21')
    S22 = Switch(name='S22', value=v)
    S23 = Switch(name='S23')

    S24 = Switch(name='S24', value=v)
    S25 = Switch(name='S25', value=v)
    S26 = Switch(name='S26')

    S27 = Switch(name='S27')
    S28 = Switch(name='S28')
    S29 = Switch(name='S29', value=v)

    S30 = Switch(name='S30', value=v)
    S31 = Switch(name='S31')
    S32 = Switch(name='S32', value=v)

    S33 = Switch(name='S33')
    S34 = Switch(name='S34', value=v)
    S35 = Switch(name='S35', value=v)

    SN1 = Switch(name='1', value=1)
    SN2 = Switch(name='2', value=2)
    SN3 = Switch(name='3', value=3)
    SN4 = Switch(name='4', value=4)
    SN5 = Switch(name='5', value=5)
    SN6 = Switch(name='6', value=6)

    def tree_list_EQUSET_BIN(nequ, nbin):
        nequ2 = nequ*2
        return ['EQUSET'] + [Tree.tree_list_BIN(nbin)]*nequ2

    nbin = 3

    Slist = [S0, S1, S2,
             S3, S4, S5,
             S6, S7, S8,
             S9, S10, S11,
             S12, S13, S14,
             S15, S16, S17,
             S18, S19, S20,
             S21, S22, S23,
             S24, S25, S26,
             S27, S28, S29,
             S30, S31, S32,
             S33, S34, S35]
    Slist_reverse = list(reversed(Slist))

    T0 = Tree(tree_list=tree_list_EQUSET_BIN(2, nbin),
              empty=True,
              name='T0',
              switches = Slist[:6] + Slist_reverse[:6],
              cut_expression=True,
              cut_expression_separator=']')
    T1 = Tree(tree_list=tree_list_EQUSET_BIN(3, nbin),
              empty=True,
              name='T1',
              switches = Slist[:9] + Slist_reverse[:9],
              cut_expression=True,
              cut_expression_separator=']')
    T2 = Tree(tree_list=tree_list_EQUSET_BIN(4, nbin),
              empty=True,
              name='T2',
              switches = Slist[:12] + Slist_reverse[:12],
              cut_expression=True,
              cut_expression_separator=']')
    T3 = Tree(tree_list=tree_list_EQUSET_BIN(5, nbin),
              empty=True,
              name='T3',
              switches = Slist[:15] + Slist_reverse[:15],
              cut_expression=True,
              cut_expression_separator=']')
    T4 = Tree(tree_list=tree_list_EQUSET_BIN(6, nbin),
              empty=True,
              name='T4',
              switches = Slist[:18] + Slist_reverse[:18],
              cut_expression=True,
              cut_expression_separator=']')
    T5 = Tree(tree_list=['EQUSET'] + [[None]]*36,
              empty=True,
              name='T5',
              switches = Slist,
              cut_expression=True,
              cut_expression_separator=']')
    T6 = Tree(tree_list=[None],
              empty=True,
              name='T6',
              switches = [SN1])
    T7 = Tree(tree_list=['AND'] + [['EQU', [None], Tree.tree_list_BIN(3)]]*6,
              empty=True,
              name='T7',
              switches = [SN4, S0, S1, S2,
                          SN6, S3, S4, S5,
                          SN2, S6, S7, S8,
                          SN5, S9, S10, S11,
                          SN1, S12, S13, S14,
                          SN3, S15, S16, S17],
              cut_expression=True,
              cut_expression_separator=')')

    R0 = Room(name='R0',
              position = [0, 3.5, 3*5.5/6, 5.5],
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

    e = 0.7

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1, 5*e/6],
              relative_arrival_coordinates=[0, 7.5/8])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1, 4*e/6],
              relative_arrival_coordinates=[0, 6.5/8])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1, 3*e/6],
              relative_arrival_coordinates=[0, 5.5/8])
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1, 2*e/6],
              relative_arrival_coordinates=[0, 4.5/8])
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1, e/6],
              relative_arrival_coordinates=[0, 3.5/8])
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=[0.5/2, 1/8])
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R2,
              room_arrival=R0,
              relative_departure_coordinates=[1/2, 1],
              relative_arrival_coordinates=[2.5/(3*5.5/6), 0])
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
                 door_window_size=875,
                 keep_proportions=True)

    return level