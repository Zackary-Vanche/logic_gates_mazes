# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 10:01:25 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_solitaire():
    
    fast_solution_finding=False

    S0 = Switch(name='S0')
    S1 = Switch(name='S1', value=1)
    S2 = Switch(name='S2', value=1)
    S3 = Switch(name='S3', value=1)
    S4 = Switch(name='S4', value=1)
    S5 = Switch(name='S5', value=1)
    S6 = Switch(name='S6', value=1)
    S7 = Switch(name='S7', value=1)
    S8 = Switch(name='S8', value=1)
    S9 = Switch(name='S9', value=1)
    S10 = Switch(name='S10', value=1)
    S11 = Switch(name='S11', value=1)
    S12 = Switch(name='S12', value=1)
    S13 = Switch(name='S13', value=1)
    S14 = Switch(name='S14', value=1)
    S15 = Switch(name='S15', value=1)
    S16 = Switch(name='S16', value=1)
    S17 = Switch(name='S17', value=1)
    S18 = Switch(name='S18', value=1)
    S19 = Switch(name='S19', value=1)
    S20 = Switch(name='S20', value=1)
    S21 = Switch(name='S21', value=1)
    S22 = Switch(name='S22', value=1)
    S23 = Switch(name='S23', value=1)
    S24 = Switch(name='S24', value=1)
    S25 = Switch(name='S25')
    S26 = Switch(name='S26', value=1)
    S27 = Switch(name='S27', value=1)
    S28 = Switch(name='S28', value=1)
    S29 = Switch(name='S29', value=1)
    # S30 = Switch(name='S30')
    # S31 = Switch(name='S31')
    # S32 = Switch(name='S32')
    # S33 = Switch(name='S33')
    
    SN1 = Switch(value=1)
    # SN3 = Switch(value=3)
    
    tree_list_JUMPS = ['XOR',
                        Tree.tree_list_JUMP(5*2),
                        Tree.tree_list_JUMP(4*2),
                        Tree.tree_list_JUMP(3*2)]

    def tree_list_solitaire(k):
        return ['INFOREQU',
                    ['SUM'] + [Tree.tree_list_XOR(2)]*k,
                    [None]]
    
    def tree_list_EQU(k):
        return ['EQU', Tree.tree_list_BIN(k), Tree.tree_list_BIN(k)]
                    

    T0 = Tree(tree_list=[None],
              empty=True,
              name='T0',
              switches = [SN1])
    T1 = Tree(tree_list=[None],
              empty=True,
              name='T1',
              switches = [SN1])
    T2 = Tree(tree_list=['OR',
                          tree_list_solitaire(5),
                          Tree.tree_list_JUMP(5*2)],
              empty=True,
              name='T2',
              switches = [S0, S25,
                          S1, S20,
                          S2, S15,
                          S3, S10,
                          S4, S5,
                          SN1,
                          S0, S25,
                          S1, S20,
                          S2, S15,
                          S3, S10,
                          S4, S5,])
    T3 = Tree(tree_list=[None],
              empty=True,
              name='T3',
              switches = [SN1])
    T4 = Tree(tree_list=['OR',
                          tree_list_solitaire(4),
                          Tree.tree_list_JUMP(4*2)],
              empty=True,
              name='T4',
              switches = [S6, S26,
                          S7, S21,
                          S8, S16,
                          S9, S11,
                          SN1,
                          S6, S26,
                          S7, S21,
                          S8, S16,
                          S9, S11,])
    T5 = Tree(tree_list=tree_list_solitaire(2),
              empty=True,
              name='T5',
              switches = [S10, S3, S11, S9, SN1])
    T6 = Tree(tree_list=['OR',
                          tree_list_solitaire(3),
                          Tree.tree_list_JUMP(3*2)],
              empty=True,
              name='T6',
              switches = [S12, S27,
                          S13, S22,
                          S14, S17,
                          SN1,
                          S12, S27,
                          S13, S22,
                          S14, S17,])
    T7 = Tree(tree_list=['OR',
                          tree_list_solitaire(3),
                          Tree.tree_list_JUMP(3*2)],
              empty=True,
              name='T7',
              switches = [S15, S2,
                          S16, S8,
                          S17, S14,
                          SN1,
                          S15, S2,
                          S16, S8,
                          S17, S14,])
    T8 = Tree(tree_list=tree_list_solitaire(2),
              empty=True,
              name='T8',
              switches = [S18, S28, S19, S23, SN1])
    T9 = Tree(tree_list=['OR',
                          tree_list_solitaire(4),
                          Tree.tree_list_JUMP(4*2)],
              empty=True,
              name='T9',
              switches = [S20, S1,
                          S21, S7,
                          S22, S13,
                          S23, S19,
                          SN1,
                          S20, S1,
                          S21, S7,
                          S22, S13,
                          S23, S19,])
    T10 = Tree(tree_list=[None],
                empty=True,
                name='T10',
                switches = [SN1])
    T11 = Tree(tree_list=['OR',
                          Tree.tree_list_JUMP(5*2),
                          tree_list_solitaire(5),],
                empty=True,
                name='T11',
                switches = [S25, S0,
                            S26, S6,
                            S27, S12,
                            S28, S18,
                            S29, S24,
                            S25, S0,
                            S26, S6,
                            S27, S12,
                            S28, S18,
                            S29, S24,
                            SN1,],
                cut_expression=True,
                cut_expression_separator=')')
    T12 = Tree(tree_list=tree_list_JUMPS,
                empty=True,
                name='T12',
                switches = [
                            S0, S25,
                            S1, S20,
                            S2, S15,
                            S3, S10,
                            S4, S5,
 
                            S6, S26,
                            S7, S21,
                            S8, S16,
                            S9, S11,

                            S12, S27,
                            S13, S22,
                            S14, S17,],
              cut_expression=True,
              cut_expression_separator=')')
    T13 = Tree(tree_list=tree_list_JUMPS,
                empty=True,
                name='T13',
                switches = [
                            S0, S25,
                            S6, S26,
                            S12, S27,
                            S18, S28,
                            S24, S29,

                            S1, S20,
                            S7, S21,
                            S13, S22,
                            S19, S23,

                            S2, S15,
                            S8, S16,
                            S14, S17,
                            ],
              cut_expression=True,
              cut_expression_separator=')')
    T14 = Tree(tree_list=tree_list_JUMPS,
                empty=True,
                name='T14',
                switches = [
                            S4, S5,
                            S9, S11,
                            S14, S17,
                            S19, S23,
                            S24, S29,

                            S3, S10,
                            S8, S16,
                            S13, S22,
                            S18, S28,

                            S2, S15,
                            S7, S21,
                            S12, S27,
                            ],
                cut_expression=True,
                cut_expression_separator=')')
    T15 = Tree(tree_list=['EQU', Tree.tree_list_BIN(15), Tree.tree_list_BIN(15)],
                empty=True,
                name='T15',
                switches = [ S0,  S1,  S2,  S3,  S4,
                            S6,  S7,  S8,  S9,
                            S12, S13, S14,
                            S18, S19,
                            S24,
                            S25, S20, S15, S10,  S5,
                            S26, S21, S16, S11,
                            S27, S22, S17,
                            S28, S23,
                            S29,
                            ],
                cut_expression=True,
                cut_expression_separator=')')
    T16 = Tree(tree_list=['AND',
                          ['EQU', [None], Tree.tree_list_BIN(15)],
                          ['EQU', [None], Tree.tree_list_BIN(15)]],
                empty=True,
                name='T16',
                switches = [SN1,
                            S0,  S1,  S2,  S3,  S4,
                            S6,  S7,  S8,  S9,
                            S12, S13, S14,
                            S18, S19,
                            S24,
                            SN1,
                            S25, S20, S15, S10,  S5,
                            S26, S21, S16, S11,
                            S27, S22, S17,
                            S28, S23,
                            S29,],
                cut_expression=True,
                cut_expression_separator=')')
    
    dy = 2
    ey = 0.52
    ex = 1
    ax = 2 # 1.25
    
    # [R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19]
    # [      ,    S32, S33, S34, S35, S36, S37, S38, S39]
    
    #[       S34, S35, S36, S37, S38, S39]

    R0 = Room(name='R0',
              position = [0, dy, 5*ex+ax, ey],
              switches_list = [S0, S1, S2, S3, S4,])
    R1 = Room(name='R1',
              position = [5*ex+ax, dy+ey, ex+ax, ey],
              switches_list = [S5,])
    R2 = Room(name='R2',
              position = [0, 2*dy, 4*ex+ax, ey],
              switches_list = [S6, S7, S8, S9,])
    R3 = Room(name='R3',
              position = [4*ex+ax, 2*dy+ey, 2*ex+ax, ey],
              switches_list = [S10, S11,])
    R4 = Room(name='R4',
              position = [0, 3*dy, 3*ex+ax, ey],
              switches_list = [S12, S13, S14,])
    R5 = Room(name='R5',
              position = [3*ex+ax, 3*dy+ey, 3*ex+ax, ey],
              switches_list = [S15, S16, S17,])
    R6 = Room(name='R6',
              position = [0, 4*dy, 2*ex+ax, ey],
              switches_list = [S18, S19,])
    R7 = Room(name='R7',
              position = [2*ex+ax, 4*dy+ey, 4*ex+ax, ey],
              switches_list = [S20, S21, S22, S23,])
    R8 = Room(name='R8',
              position = [0, 5*dy, ex+ax, ey],
              switches_list = [S24,])
    R9 = Room(name='R9',
              position = [ex+ax, 5*dy+ey, 5*ex+ax, ey],
              switches_list = [S25, S26, S27, S28, S29,])
    R10 = Room(name='R10',
                position = [0, 6*dy+ey, 6.2*ex+2*ax, ey],
                switches_list = [])
    R11 = Room(name='R11',
                position = [2.75*ex, 0, 3.45*ex+2*ax, ey],
                switches_list = [])
    RE = Room(name='RE',
              position=[0, 0, 1.25, 2*ey],
              is_exit=True)   # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R11,
              room_arrival=R0,
              relative_departure_coordinates=[(2.25*ex+ax)/(3.45*ex+2*ax), 1],
              relative_arrival_coordinates=[1, 0])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R11,
              room_arrival=R1,
              relative_departure_coordinates=[(3.25*ex+ax)/(3.45*ex+2*ax), 1],
              relative_arrival_coordinates=[ex/(ex+ax), 0])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R0,
              room_arrival=R2,
              relative_departure_coordinates=[(4*ex+ax)/(5*ex+ax), 1],
              relative_arrival_coordinates=[1, 0])
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R1,
              room_arrival=R3,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[ex/(2*ex+ax), 0])
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R2,
              room_arrival=R4,
              relative_departure_coordinates=[(3*ex+ax)/(4*ex+ax), 1],
              relative_arrival_coordinates=[1, 0])
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R3,
              room_arrival=R5,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[ex/(3*ex+ax), 0])
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R4,
              room_arrival=R6,
              relative_departure_coordinates=[(2*ex+ax)/(3*ex+ax), 1],
              relative_arrival_coordinates=[1, 0])
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R5,
              room_arrival=R7,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[ex/(4*ex+ax), 0])
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R6,
              room_arrival=R8,
              relative_departure_coordinates=[(1*ex+ax)/(2*ex+ax), 1],
              relative_arrival_coordinates=[1, 0])
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R7,
              room_arrival=R9,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[ex/(5*ex+ax), 0])
    D10 = Door(two_way=False,
                tree=T10,
                room_departure=R8,
                room_arrival=R10,
                relative_departure_coordinates=[ax/(ex+ax), 1],
                relative_arrival_coordinates=[ax/(6.2*ex+2*ax), 0])
    D11 = Door(two_way=False,
                tree=T11,
                room_departure=R9,
                room_arrival=R10,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[(ex+ax)/(6.2*ex+2*ax), 0])
    D12 = Door(two_way=False,
                tree=T12,
                room_departure=R10,
                room_arrival=R11,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[1, 1],
                relative_position=0.25-0.01)
    D13 = Door(two_way=False,
                tree=T13,
                room_departure=R10,
                room_arrival=R11,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[1, 1],
                relative_position=0.25+0.5/3-0.01)
    D14 = Door(two_way=False,
                tree=T14,
                room_departure=R10,
                room_arrival=R11,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[1, 1],
                relative_position=0.25+2*0.5/3-0.01)
    D15 = Door(two_way=False,
                tree=T15,
                room_departure=R10,
                room_arrival=R11,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[1, 1],
                relative_position=0.75-0.01)
    D16 = Door(two_way=False,
                tree=T16,
                room_departure=R11,
                room_arrival=RE,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[1, 1/2])

    # [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24]
    
    level = Maze(start_room_index=11, 
                  exit_room_index=-1, 
                  rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, RE], 
                  doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16], 
                  fastest_solution=None,
                  level_color=Levels_colors_list.FROM_HUE(0, sa=0.35, li=0.49),
                  name='Solitaire',
                  door_window_size=789,
                  keep_proportions=True)

    return level

# def level_solitaire():
    
#     S0 = Switch(name='S0')
#     S1 = Switch(name='S1')
#     S2 = Switch(name='S2')
#     S3 = Switch(name='S3')
#     S4 = Switch(name='S4')
#     S5 = Switch(name='S5')
#     S6 = Switch(name='S6')
#     S7 = Switch(name='S7')
#     S8 = Switch(name='S8')
#     S9 = Switch(name='S9')
#     S10 = Switch(name='S10')
#     S11 = Switch(name='S11')
#     S12 = Switch(name='S12')
#     S13 = Switch(name='S13')
#     S14 = Switch(name='S14')
#     S15 = Switch(name='S15')
#     S16 = Switch(name='S16')
#     S17 = Switch(name='S17')
#     S18 = Switch(name='S18')
#     S19 = Switch(name='S19')
#     S20 = Switch(name='S20')
#     S21 = Switch(name='S21')
#     S22 = Switch(name='S22')
#     S23 = Switch(name='S23')
#     S24 = Switch(name='S24')
#     S25 = Switch(name='S25')
#     S26 = Switch(name='S26')
#     S27 = Switch(name='S27')
#     S28 = Switch(name='S28')
#     S29 = Switch(name='S29')
#     S30 = Switch(name='S30')
#     S31 = Switch(name='S31')
#     S32 = Switch(name='S32')
    
#     SN1 = Switch(value=1)

#     T0 = Tree(tree_list=[None],
#               empty=True,
#               name='T0',
#               switches = [SN1])
#     T1 = Tree(tree_list=[None],
#               empty=True,
#               name='T1',
#               switches = [SN1])
#     T2 = Tree(tree_list=[None],
#               empty=True,
#               name='T2',
#               switches = [SN1])
#     T3 = Tree(tree_list=[None],
#               empty=True,
#               name='T3',
#               switches = [SN1])
#     T4 = Tree(tree_list=[None],
#               empty=True,
#               name='T4',
#               switches = [SN1])
#     T5 = Tree(tree_list=[None],
#               empty=True,
#               name='T5',
#               switches = [SN1])
#     T6 = Tree(tree_list=[None],
#               empty=True,
#               name='T6',
#               switches = [SN1])
#     T7 = Tree(tree_list=[None],
#               empty=True,
#               name='T7',
#               switches = [SN1])
#     T8 = Tree(tree_list=[None],
#               empty=True,
#               name='T8',
#               switches = [SN1])
#     T9 = Tree(tree_list=[None],
#               empty=True,
#               name='T9',
#               switches = [SN1])
#     T10 = Tree(tree_list=[None],
#               empty=True,
#               name='T10',
#               switches = [SN1])
#     T11 = Tree(tree_list=[None],
#               empty=True,
#               name='T11',
#               switches = [SN1])
#     T12 = Tree(tree_list=[None],
#               empty=True,
#               name='T12',
#               switches = [SN1])
#     T13 = Tree(tree_list=[None],
#               empty=True,
#               name='T13',
#               switches = [SN1])
#     T14 = Tree(tree_list=[None],
#               empty=True,
#               name='T14',
#               switches = [SN1])
#     T15 = Tree(tree_list=[None],
#               empty=True,
#               name='T15',
#               switches = [SN1])
#     T16 = Tree(tree_list=[None],
#               empty=True,
#               name='T16',
#               switches = [SN1])
#     T17 = Tree(tree_list=[None],
#               empty=True,
#               name='T17',
#               switches = [SN1])
#     T18 = Tree(tree_list=[None],
#               empty=True,
#               name='T18',
#               switches = [SN1])
#     T19 = Tree(tree_list=[None],
#               empty=True,
#               name='T19',
#               switches = [SN1])
#     T20 = Tree(tree_list=[None],
#               empty=True,
#               name='T20',
#               switches = [SN1])
#     T21 = Tree(tree_list=[None],
#               empty=True,
#               name='T21',
#               switches = [SN1])
#     T22 = Tree(tree_list=[None],
#               empty=True,
#               name='T22',
#               switches = [SN1])
#     T23 = Tree(tree_list=[None],
#               empty=True,
#               name='T23',
#               switches = [SN1])
#     T24 = Tree(tree_list=[None],
#               empty=True,
#               name='T24',
#               switches = [SN1])
#     T25 = Tree(tree_list=[None],
#               empty=True,
#               name='T25',
#               switches = [SN1])
#     T26 = Tree(tree_list=[None],
#               empty=True,
#               name='T26',
#               switches = [SN1])
#     T27 = Tree(tree_list=[None],
#               empty=True,
#               name='T27',
#               switches = [SN1])
#     T28 = Tree(tree_list=[None],
#               empty=True,
#               name='T28',
#               switches = [SN1])
#     T29 = Tree(tree_list=[None],
#               empty=True,
#               name='T29',
#               switches = [SN1])
#     T30 = Tree(tree_list=[None],
#               empty=True,
#               name='T30',
#               switches = [SN1])
#     T31 = Tree(tree_list=[None],
#               empty=True,
#               name='T31',
#               switches = [SN1])
#     T32 = Tree(tree_list=[None],
#               empty=True,
#               name='T32',
#               switches = [SN1])
#     T33 = Tree(tree_list=[None],
#               empty=True,
#               name='T33',
#               switches = [SN1])
#     T34 = Tree(tree_list=[None],
#               empty=True,
#               name='T34',
#               switches = [SN1])
#     T35 = Tree(tree_list=[None],
#               empty=True,
#               name='T35',
#               switches = [SN1])
#     T36 = Tree(tree_list=[None],
#               empty=True,
#               name='T36',
#               switches = [SN1])
#     T37 = Tree(tree_list=[None],
#               empty=True,
#               name='T37',
#               switches = [SN1])
#     T38 = Tree(tree_list=[None],
#               empty=True,
#               name='T38',
#               switches = [SN1])
#     T39 = Tree(tree_list=[None],
#               empty=True,
#               name='T39',
#               switches = [SN1])
#     T40 = Tree(tree_list=[None],
#               empty=True,
#               name='T40',
#               switches = [SN1])
#     T41 = Tree(tree_list=[None],
#               empty=True,
#               name='T41',
#               switches = [SN1])
    
#     ex = 0.5
#     ey = 0.5
    
#     R0 = Room(name='R0',
#               position = [0, 0, ex, ey],
#               switches_list = [S0])
#     R1 = Room(name='R1',
#               position = [0, 1, ex, ey],
#               switches_list = [S1])
#     R2 = Room(name='R2',
#               position = [0, 2, ex, ey],
#               switches_list = [S2])
#     R3 = Room(name='R3',
#               position = [0, 3, ex, ey],
#               switches_list = [S3])
#     R4 = Room(name='R4',
#               position = [0, 4, ex, ey],
#               switches_list = [S4])
#     R5 = Room(name='R5',
#               position = [1, 0, ex, ey],
#               switches_list = [S5])
#     R6 = Room(name='R6',
#               position = [1, 1, ex, ey],
#               switches_list = [S6])
#     R7 = Room(name='R7',
#               position = [1, 2, ex, ey],
#               switches_list = [S7])
#     R8 = Room(name='R8',
#               position = [1, 3, ex, ey],
#               switches_list = [S8])
#     R9 = Room(name='R9',
#               position = [2, 0, ex, ey],
#               switches_list = [S9])
#     R10 = Room(name='R10',
#               position = [2, 1, ex, ey],
#               switches_list = [S10])
#     R11 = Room(name='R11',
#               position = [2, 2, ex, ey],
#               switches_list = [S11])
#     R12 = Room(name='R12',
#               position = [3, 0, ex, ey],
#               switches_list = [S12])
#     R13 = Room(name='R13',
#               position = [3, 1, ex, ey],
#               switches_list = [S13])
#     R14 = Room(name='R14',
#               position = [4, 0, ex, ey],
#               switches_list = [S14])
#     R15 = Room(name='R15',
#               position = [3, 3.25, 3*ex, 3*ey],
#               switches_list = [])
#     R16 = Room(name='R16',
#               position = [0, -1, 4+ex, ey/2],
#               switches_list = [])
#     R17 = Room(name='R17',
#               position = [-1, 0, 2*ex/3, 4+ey],
#               switches_list = [])
#     RE = Room(name='RE',
#               position=[4, 1, ex, ey],
#               is_exit=True)   # E pour exit ou end
#     D0 = Door(two_way=True,
#               tree=T0,
#               room_departure=R0,
#               room_arrival=R1)
#     D1 = Door(two_way=True,
#               tree=T1,
#               room_departure=R1,
#               room_arrival=R2)
#     D2 = Door(two_way=True,
#               tree=T2,
#               room_departure=R2,
#               room_arrival=R3)
#     D3 = Door(two_way=True,
#               tree=T3,
#               room_departure=R3,
#               room_arrival=R4)

#     D4 = Door(two_way=True,
#               tree=T4,
#               room_departure=R5,
#               room_arrival=R6)
#     D5 = Door(two_way=True,
#               tree=T5,
#               room_departure=R6,
#               room_arrival=R7)
#     D6 = Door(two_way=True,
#               tree=T6,
#               room_departure=R7,
#               room_arrival=R8)

#     D7 = Door(two_way=True,
#               tree=T7,
#               room_departure=R9,
#               room_arrival=R10)
#     D8 = Door(two_way=True,
#               tree=T8,
#               room_departure=R10,
#               room_arrival=R11)

#     D9 = Door(two_way=True,
#               tree=T9,
#               room_departure=R0,
#               room_arrival=R5)
#     D10 = Door(two_way=True,
#                tree=T10,
#                room_departure=R5,
#                room_arrival=R9)
#     D11 = Door(two_way=True,
#                tree=T11,
#                room_departure=R9,
#                room_arrival=R12)
#     D12 = Door(two_way=True,
#                tree=T12,
#                room_departure=R12,
#                room_arrival=R14)

#     D13 = Door(two_way=True,
#                tree=T13,
#                room_departure=R1,
#                room_arrival=R6)
#     D14 = Door(two_way=True,
#                tree=T14,
#                room_departure=R6,
#                room_arrival=R10)
#     D15 = Door(two_way=True,
#                tree=T15,
#                room_departure=R10,
#                room_arrival=R13)

#     D16 = Door(two_way=True,
#                tree=T16,
#                room_departure=R2,
#                room_arrival=R7)
#     D17 = Door(two_way=True,
#                tree=T17,
#                room_departure=R7,
#                room_arrival=R11)

#     D18 = Door(two_way=True,
#                 tree=T18,
#                 room_departure=R4,
#                 room_arrival=R8)
#     D19 = Door(two_way=True,
#                 tree=T19,
#                 room_departure=R8,
#                 room_arrival=R11)
#     D20 = Door(two_way=True,
#                 tree=T20,
#                 room_departure=R11,
#                 room_arrival=R13)
#     D21 = Door(two_way=True,
#                 tree=T21,
#                 room_departure=R13,
#                 room_arrival=R14)

#     D22 = Door(two_way=True,
#                tree=T22,
#                room_departure=R3,
#                room_arrival=R7)
#     D23 = Door(two_way=True,
#                tree=T23,
#                room_departure=R7,
#                room_arrival=R10)
#     D24 = Door(two_way=True,
#                tree=T24,
#                room_departure=R10,
#                room_arrival=R12)

#     D25 = Door(two_way=True,
#                tree=T25,
#                room_departure=R2,
#                room_arrival=R6)
#     D26 = Door(two_way=True,
#                tree=T26,
#                room_departure=R6,
#                room_arrival=R9)

#     D27 = Door(two_way=True,
#                tree=T27,
#                room_departure=R17,
#                room_arrival=R0)
#     D28 = Door(two_way=True,
#                tree=T28,
#                room_departure=R17,
#                room_arrival=R1)
#     D29 = Door(two_way=True,
#                tree=T29,
#                room_departure=R17,
#                room_arrival=R2)
#     D30 = Door(two_way=True,
#                tree=T30,
#                room_departure=R17,
#                room_arrival=R3)
#     D31 = Door(two_way=True,
#                tree=T31,
#                room_departure=R17,
#                room_arrival=R4)

#     D32 = Door(two_way=True,
#                tree=T32,
#                room_departure=R16,
#                room_arrival=R0)
#     D33 = Door(two_way=True,
#                tree=T33,
#                room_departure=R16,
#                room_arrival=R5)
#     D34 = Door(two_way=True,
#                tree=T34,
#                room_departure=R16,
#                room_arrival=R9)
#     D35 = Door(two_way=True,
#                tree=T35,
#                room_departure=R16,
#                room_arrival=R12)
#     D36 = Door(two_way=True,
#                tree=T36,
#                room_departure=R16,
#                room_arrival=R14)

#     D37 = Door(two_way=True,
#                tree=T37,
#                room_departure=R16,
#                room_arrival=R17,
#                relative_departure_coordinates=[0, 1/2],
#                relative_arrival_coordinates=[1/2, 0])

#     D38 = Door(two_way=True,
#                tree=T38,
#                room_departure=R15,
#                room_arrival=R17,
#                relative_departure_coordinates=[0, 1],
#                relative_arrival_coordinates=[0, 1])

#     # D39 = Door(two_way=True,
#     #            tree=T39,
#     #            room_departure=R39,
#     #            room_arrival=R40)
#     # D40 = Door(two_way=True,
#     #            tree=T40,
#     #            room_departure=R40,
#     #            room_arrival=R41)
#     # D41 = Door(two_way=True,
#     #            tree=T41,
#     #            room_departure=R41,
#     #            room_arrival=R42)
#     [R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17]
#     # [     D37, D38, D39, D40, D41]
#     # [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31, S32]
    
#     level = Maze(start_room_index=11, 
#                  exit_room_index=-1, 
#                  rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, RE], 
#                  doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10,
#                              D11, D12, D13, D14, D15, D16, D17, D18, D19, D20,
#                              D21, D22, D23, D24, D25, D26, D27, D28, D29, D30,
#                              D31, D32, D33, D34, D35, D36, D37, D38], 
#                  fastest_solution=None,
#                  level_color=Levels_colors_list.FROM_HUE(0, sa=0.35, li=0.49),
#                  name='Solitaire',
#                  door_window_size=700,
#                  keep_proportions=True)

#     return level