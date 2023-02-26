# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 15:10:53 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_sujiko():
    
    fast_solution_finding=False
    # TODO
    # No solution found when fast_solution_finding==True -> solve this
    
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
    
    SN1 = Switch(name='1', value=1)
    
    tree_list_EQU = ['EQU', ['SUM'] + [Tree.tree_list_BIN(3)]*4, [None]]

    if fast_solution_finding:
        
        def tree_list_DIFF(k):
            return ['DIFF'] + [Tree.tree_list_BIN(3)]*k
        
        T0 = Tree(tree_list=[None],
                  empty=True,
                  name='T0',
                  switches = [SN1])
        T1 = Tree(tree_list=tree_list_DIFF(2),
                  empty=True,
                  name='T1',
                  switches = [S0, S1, S2,
                              S3, S4, S5])
        T2 = Tree(tree_list=tree_list_DIFF(3),
                  empty=True,
                  name='T2',
                  switches = [S0, S1, S2,
                              S3, S4, S5,
                              S6, S7, S8])
        T3 = Tree(tree_list=tree_list_DIFF(4),
                  empty=True,
                  name='T3',
                  switches = [S0, S1, S2,
                              S3, S4, S5,
                              S6, S7, S8,
                              S9, S10, S11])
        T4 = Tree(tree_list=['AND', tree_list_EQU, tree_list_DIFF(5)],
                  empty=True,
                  name='T4',
                  switches = [S0, S1, S2,
                              S3, S4, S5,
                              S9, S10, S11,
                              S12, S13, S14,
                              Switch(value=14),
                              S0, S1, S2,
                              S3, S4, S5,
                              S6, S7, S8,
                              S9, S10, S11,
                              S12, S13, S14
                              ],
                  cut_expression=True,
                  cut_expression_separator=']')
        T5 = Tree(tree_list=['AND', tree_list_EQU, tree_list_DIFF(6)],
                  empty=True,
                  name='T5',
                  switches = [S3, S4, S5,
                              S6, S7, S8,
                              S12, S13, S14,
                              S15, S16, S17,
                              Switch(value=13),
                              S0, S1, S2,
                              S3, S4, S5,
                              S6, S7, S8,
                              S9, S10, S11,
                              S12, S13, S14,
                              S15, S16, S17,
                              ],
                  cut_expression=True,
                  cut_expression_separator=')')
        T6 = Tree(tree_list=tree_list_DIFF(7),
                  empty=True,
                  name='T6',
                  switches = [S0, S1, S2,
                              S3, S4, S5,
                              S6, S7, S8,
                              S9, S10, S11,
                              S12, S13, S14,
                              S15, S16, S17,
                              S18, S19, S20,],
                  cut_expression=True,
                  cut_expression_separator=')')
        T7 = Tree(tree_list=['AND', tree_list_EQU, tree_list_DIFF(8)],
                  empty=True,
                  name='T7',
                  switches = [S9, S10, S11,
                              S12, S13, S14,
                              S18, S19, S20,
                              S21, S22, S23,
                              Switch(value=12),
                              S0, S1, S2,
                              S3, S4, S5,
                              S6, S7, S8,
                              S9, S10, S11,
                              S12, S13, S14,
                              S15, S16, S17,
                              S18, S19, S20,
                              S21, S22, S23
                              ],
                  cut_expression=True,
                  cut_expression_separator=')')
        T8 = Tree(tree_list=['AND',
                             ['EQU', ['SUM'] + [Tree.tree_list_BIN(3)]*3 + [Tree.tree_list_BIN(4)], [None]],
                             ['DIFF'] + [Tree.tree_list_BIN(3)]*8 + [Tree.tree_list_BIN(4)]],
                  empty=True,
                  name='T8',
                  switches = [S12, S13, S14,
                              S15, S16, S17,
                              S21, S22, S23,
                              S24, S25, S26, S27,
                              Switch(value=11),
                              S0, S1, S2,
                              S3, S4, S5,
                              S6, S7, S8,
                              S9, S10, S11,
                              S12, S13, S14,
                              S15, S16, S17,
                              S18, S19, S20,
                              S21, S22, S23,
                              S24, S25, S26, S27],
                  cut_expression=True,
                  cut_expression_separator=')')
    else:
        T0 = Tree(tree_list=[None],
                  empty=True,
                  name='T0',
                  switches = [SN1])
        T1 = Tree(tree_list=[None],
                  empty=True,
                  name='T1',
                  switches = [SN1])
        T2 = Tree(tree_list=[None],
                  empty=True,
                  name='T2',
                  switches = [SN1])
        T3 = Tree(tree_list=[None],
                  empty=True,
                  name='T3',
                  switches = [SN1])
        T4 = Tree(tree_list=tree_list_EQU,
                  empty=True,
                  name='T4',
                  switches = [S0, S1, S2,
                              S3, S4, S5,
                              S9, S10, S11,
                              S12, S13, S14,
                              Switch(value=14)
                              ],
                  cut_expression=True,
                  cut_expression_separator=']')
        T5 = Tree(tree_list=tree_list_EQU,
                  empty=True,
                  name='T5',
                  switches = [S3, S4, S5,
                              S6, S7, S8,
                              S12, S13, S14,
                              S15, S16, S17,
                              Switch(value=13)
                              ],
                  cut_expression=True,
                  cut_expression_separator=']')
        T6 = Tree(tree_list=Tree.tree_list_OR(2),
                  empty=True,
                  name='T6',
                  switches = [S12, S16],
                  cut_expression=False,
                  cut_expression_separator=')')
        T7 = Tree(tree_list=tree_list_EQU,
                  empty=True,
                  name='T7',
                  switches = [S9, S10, S11,
                              S12, S13, S14,
                              S18, S19, S20,
                              S21, S22, S23,
                              Switch(value=12)
                              ],
                  cut_expression=True,
                  cut_expression_separator=']')
        T8 = Tree(tree_list=['AND',
                             ['EQU', ['SUM'] + [Tree.tree_list_BIN(3)]*3 + [Tree.tree_list_BIN(4)], [None]],
                             ['DIFF'] + [Tree.tree_list_BIN(3)]*8 + [Tree.tree_list_BIN(4)]],
                  empty=True,
                  name='T8',
                  switches = [S12, S13, S14,
                              S15, S16, S17,
                              S21, S22, S23,
                              S24, S25, S26, S27,
                              Switch(value=11),
                              S0, S1, S2,
                              S3, S4, S5,
                              S6, S7, S8,
                              S9, S10, S11,
                              S12, S13, S14,
                              S15, S16, S17,
                              S18, S19, S20,
                              S21, S22, S23,
                              S24, S25, S26, S27],
                  cut_expression=True,
                  cut_expression_separator=')')
    
    lx = 1
    ly = 4
    dx = lx+1.25
    dy = ly+1.5
    ey = 1.2
    
    R0 = Room(name='R0',
              position = [3*dx, 0, lx, ly],
              switches_list = [S0, S1, S2])
    R1 = Room(name='R1',
              position = [2*dx, -ey, lx, ly],
              switches_list = [S3, S4, S5])
    R2 = Room(name='R2',
              position = [dx, 0, lx, ly],
              switches_list = [S6, S7, S8])
    R3 = Room(name='R3',
              position = [0, -ey, lx, ly],
              switches_list = [S9, S10, S11])
    R4 = Room(name='R4',
              position = [0, dy, lx, ly],
              switches_list = [S12, S13, S14])
    R5 = Room(name='R5',
              position = [dx, dy-ey, lx, ly],
              switches_list = [S15, S16, S17])
    R6 = Room(name='R6',
              position = [2*dx, dy, lx, ly],
              switches_list = [S18, S19, S20])
    R7 = Room(name='R7',
              position = [3*dx, dy-ey, lx, ly],
              switches_list = [S21, S22, S23])
    R8 = Room(name='R8',
              position = [4*dx, dy-ey, lx, ly+1],
              switches_list = [S24, S25, S26, S27])
    RE = Room(name='RE',
              position=[4*dx-0.1, -ey, lx+0.2, ly-1],
              is_exit=True)   # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[0, 0],
              relative_arrival_coordinates=[1, 0])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[1, 1])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=[0, 0],
              relative_arrival_coordinates=[1, 0])
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=R4)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R4,
              room_arrival=R5,
              relative_departure_coordinates=[1, 0],
              relative_arrival_coordinates=[0, 0])
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R5,
              room_arrival=R6,
              relative_departure_coordinates=[1, 1],
              relative_arrival_coordinates=[0, 1])
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R6,
              room_arrival=R7,
              relative_departure_coordinates=[1, 0],
              relative_arrival_coordinates=[0, 0])
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R7,
              room_arrival=R8,
              relative_departure_coordinates=[1, 1],
              relative_arrival_coordinates=[0, 1])
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R8,
              room_arrival=RE,
              relative_departure_coordinates=[1/2, 0],
              relative_arrival_coordinates=[1/2, 1])
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8],
                 fastest_solution='S2 D0 S3 S4 D1 S6 S7 S8 D2 S10 S11 D3 S12 D4 S16 D5 S18 S20 D6 D7 S27 D8',
                 level_color=Levels_colors_list.FROM_HUE(0.9, sa=1, li=0.3),
                 name='Sujiko',
                 door_window_size=700,
                 keep_proportions=True)

    return level