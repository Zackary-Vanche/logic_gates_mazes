# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 11:42:48 2023

@author: zackary.vanche
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from Color import Color

def f():

    A0 = Switch(name='S0', value = rd_choice([0, 1]))
    A1 = Switch(name='S1', value = rd_choice([0, 1]))
    A2 = Switch(name='S2', value = rd_choice([0, 1]))
    A3 = Switch(name='S3', value = rd_choice([0, 1]))
    B0 = Switch(name='S4', value = rd_choice([0, 1]))
    B1 = Switch(name='S5', value = rd_choice([0, 1]))
    B2 = Switch(name='S6', value = rd_choice([0, 1]))
    B3 = Switch(name='S7', value = rd_choice([0, 1]))

    a = A0.value + A1.value*2 + A2.value*4 + A3.value*8
    b = B0.value + B1.value*2 + B2.value*4 + B3.value*8
    c = a+b
    str_c = bin(c)[2:]
    while len(str_c) < 5:
        str_c = '0' + str_c
    bin_c = []
    for k in str_c:
        bin_c.append(int(k))
    bin_c.reverse()
    
    tree_list_2 = ['XOR',
                   Tree.tree_list_XOR(2),
                   [None],]
    
    tree_list_3 = ['OR',
                   ['AND',
                    [None],
                    Tree.tree_list_XOR(2)],
                   Tree.tree_list_AND(2)]

    # C0 = A0 XOR B0
    V0 = Tree(tree_list=Tree.tree_list_XOR(2),
          name='V0',
          switches=[A0, B0])
    V1 = Tree(tree_list=Tree.tree_list_AND(2),
              name='V1',
              switches=[A0, B0])

    # C1 = (A1 AND B1) XOR (A1 XOR B1 AND V0)
    V2 = Tree(tree_list=tree_list_2,
          name='V2',
          switches=[A1, B1, V1])
    V3 = Tree(tree_list=tree_list_3,
              name='V3',
              switches=[V1,
                        A1, B1,
                        A1, B1])

    # C2 = (A2 AND B2) XOR (A2 XOR B2 AND V1)
    V4 = Tree(tree_list=tree_list_2,
          name='V4',
          switches=[A2, B2, V3])
    V5 = Tree(tree_list=tree_list_3,
          name='V5',
          switches=[V3,
                    A2, B2,
                    A2, B2])
    
    # C3 = (A3 AND B3) XOR (A3 XOR B3 AND V2)
    V6 = Tree(tree_list=tree_list_2,
          name='V6',
          switches=[A3, B3, V5])
    V7 = Tree(tree_list=tree_list_3,
          name='V7',
          switches=[V5,
                    A3, B3,
                    A3, B3])

    # C4 = (A3 AND B3 AND V3)
    V8 = Tree(tree_list=[None],
          name='V8',
          switches=[V7])
    
    # V9 = Tree(tree_list=[None],
    #       name='V9',
    #       switches=[1])
    
    C0 = Switch(name='S8')
    C1 = Switch(name='S9')
    C2 = Switch(name='S10')
    C3 = Switch(name='S11')
    C4 = Switch(name='S12')

    T0 = Tree(tree_list=['AND'] + [['EQU', [None], [None]]]*5,
                name='T0',
                switches=[C0, V0,
                          C1, V2,
                          C2, V4,
                          C3, V6,
                          C4, V8])

    dx = 1
    dy = 1
    ex = 1
    ey = 1

    R0 = Room(name='R0',
              position=[2*dx, 0*dy, 4*ex, 2*ey],
              switches_list=[A0, A1, A2, A3,
                             B0, B1, B2, B3])
    R1 = Room(name='R1',
              position=[0*dx, 3*dy, 6*ex, ey],
              switches_list=[C0, C1, C2, C3, C4])
    RE = Room(name='RE',
              position=[0*dx, 0*dy, ex, 2*ey],
              is_exit=True)

    D0 = Door(two_way=False,
              tree=T0,
              name='D0',
              room_departure=R1,
              room_arrival=RE,
              relative_departure_coordinates=[2/6, 1/2],
              relative_arrival_coordinates=[1/2, 3/4])
    
    sol = 'S8 ' * bin_c[0] + 'S9 ' * bin_c[1] + 'S10 ' * bin_c[2] + 'S11 ' * bin_c[3] + 'S12 ' * bin_c[4]
    sol = sol + 'D0'
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.4)
    lcolor.surrounding_color = Color.PURE_BLUE
    lcolor.contour_color = Color.PURE_BLUE

    level = Maze(start_room_index=1,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, RE],
                 doors_list=[D0],
                 fastest_solution=sol,
                 level_color=lcolor,
                 name='Circuit',
                 keep_proportions=True,
                 door_window_size=500)
    
    return level