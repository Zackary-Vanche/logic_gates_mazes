# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:38:58 2023

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import randint as rd_randint
from random import shuffle as rd_shuffle


def base2(l):
    return sum([l[i] * 2 ** i for i in range(len(l))])


def level_five():
    n = 5

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

    Slist_tot = [S0, S1, S2, S3, S4,
                 S5, S6, S7, S8, S9,
                 S10, S11, S12, S13, S14,
                 S15, S16, S17, S18, S19,
                 S20, S21, S22, S23, S24]
    for S in Slist_tot:
        S.value = rd_randint(0, 1)

    MOD_list = [n for i in range(50)]

    Slist0 = [S0, S1, S2, S3, S4]
    Slist1 = [S5, S6, S7, S8, S9]
    Slist2 = [S10, S11, S12, S13, S14]
    Slist3 = [S15, S16, S17, S18, S19]
    Slist4 = [S20, S21, S22, S23, S24]

    fastest_solution_list = []
    for i in range(5):
        Slist = [Slist0, Slist1, Slist2, Slist3, Slist4][i]
        for S in Slist:
            if S.value:
                fastest_solution_list.append(S.name)
        fastest_solution_list.append(f'D{i}')
    fastest_solution_list.append('D5')
    # fastest_solution = ' '.join(fastest_solution_list) # The actual fastest solution might be shorter

    SlistT = [[S0, S5, S10, S15, S20],
              [S1, S6, S11, S16, S21],
              [S2, S7, S12, S17, S22],
              [S3, S8, S13, S18, S23],
              [S4, S9, S14, S19, S24],

              [S0, S6, S12, S18, S24],
              [S4, S8, S12, S16, S20],

              [S0, S20, S24, S4, S12],
              [S5, S21, S19, S3, S12],
              [S10, S22, S14, S2, S12],
              [S15, S23, S9, S1, S12],

              [S6, S16, S18, S8, S12],
              [S11, S17, S13, S7, S12],
              ]

    rd_shuffle(Slist0)
    rd_shuffle(Slist1)
    rd_shuffle(Slist2)
    rd_shuffle(Slist3)
    rd_shuffle(Slist4)
    rd_shuffle(SlistT)
    for Slist in SlistT:
        rd_shuffle(Slist)

    EQU_list = []

    for Slist in [Slist0, Slist1, Slist2, Slist3, Slist4]:
        Slist_values = [S.value for S in Slist]
        EQU_list.append(base2(Slist_values))
    for Slist in SlistT:
        Slist_values = [S.value for S in Slist]
        EQU_list.append(base2(Slist_values))

    for i in range(len(EQU_list)):
        EQU_list[i] = EQU_list[i] % 5

    Slist5 = []
    for i in range(len(SlistT)):
        Slist5.append(EQU_list[i + n])
        Slist5.extend(SlistT[i])
        Slist5.append(MOD_list[i + n])

    tree_list = ['EQU',
                 [None],
                 ['MOD', Tree.tree_list_BIN(n), [None]]]

    T0 = Tree(tree_list=tree_list,
              empty=True,
              name='T0',
              switches=[EQU_list[0]] + Slist0 + [MOD_list[0]])
    T1 = Tree(tree_list=tree_list,
              empty=True,
              name='T1',
              switches=[EQU_list[1]] + Slist1 + [MOD_list[1]])
    T2 = Tree(tree_list=tree_list,
              empty=True,
              name='T2',
              switches=[EQU_list[2]] + Slist2 + [MOD_list[2]])
    T3 = Tree(tree_list=tree_list,
              empty=True,
              name='T3',
              switches=[EQU_list[3]] + Slist3 + [MOD_list[3]])
    T4 = Tree(tree_list=tree_list,
              empty=True,
              name='T4',
              switches=[EQU_list[4]] + Slist4 + [MOD_list[4]])
    T5 = Tree(tree_list=['AND'] + [tree_list] * (n + 2),
              empty=True,
              name='T5',
              switches=Slist5,
              cut_expression=True,
              cut_expression_separator=f' {n}')

    ex = 5
    exe = 1
    ey = 0.35

    R0 = Room(name='R0',
              position=[0, 6, ex, ey],
              switches_list=Slist0)
    R1 = Room(name='R1',
              position=[0, 5, ex, ey],
              switches_list=Slist1)
    R2 = Room(name='R2',
              position=[0, 4, ex, ey],
              switches_list=Slist2)
    R3 = Room(name='R3',
              position=[0, 3, ex, ey],
              switches_list=Slist3)
    R4 = Room(name='R4',
              position=[0, 2, ex, ey],
              switches_list=Slist4)
    R5 = Room(name='R5',
              position=[ex / 2 - exe / 2, 1, exe, ey],
              switches_list=[])
    RE = Room(name='RE',
              position=[ex / 2 - exe / 2, 0, exe, ey],
              is_exit=True)  # E pour exit ou end
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1 / 2, 1 / 2],
              relative_arrival_coordinates=[1 / 2, 1 / 2])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=R4)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R4,
              room_arrival=R5)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R5,
              room_arrival=RE)

    for S in Slist_tot:
        S.value = 0

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0.925, sa=1, li=0.2),
                 name='Five',
                 random=True,
                 door_window_size=800,
                 keep_proportions=True,
                 y_separation=40,
                 border=40,
                 unique_solution=False)

    return level