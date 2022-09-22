# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 08:59:20 2022

@author: utilisateur
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 20:18:40 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_panex():

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

    S12 = Switch(name='S12', value=v)
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')
    S15 = Switch(name='S15')

    S16 = Switch(name='S16')
    S17 = Switch(name='S17', value=v)
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')

    S20 = Switch(name='S20', value=v)
    S21 = Switch(name='S21', value=v)
    S22 = Switch(name='S22')
    S23 = Switch(name='S23')

    S24 = Switch(name='S24')
    S25 = Switch(name='S25')
    S26 = Switch(name='S26', value=v)
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
    S42 = Switch(name='S42')
    S43 = Switch(name='S43')

    S44 = Switch(name='S44')
    S45 = Switch(name='S45')
    S46 = Switch(name='S46')
    S47 = Switch(name='S47')

    S48 = Switch(name='S48')
    S49 = Switch(name='S49')
    S50 = Switch(name='S50')
    S51 = Switch(name='S51')

    S52 = Switch(name='S52', value=v)
    S53 = Switch(name='S53')
    S54 = Switch(name='S54')
    S55 = Switch(name='S55', value=v)

    S56 = Switch(name='S56')
    S57 = Switch(name='S57', value=v)
    S58 = Switch(name='S58')
    S59 = Switch(name='S59', value=v)

    S60 = Switch(name='S60', value=v)
    S61 = Switch(name='S61', value=v)
    S62 = Switch(name='S62')
    S63 = Switch(name='S63', value=v)

    S64 = Switch(name='S64')
    S65 = Switch(name='S65')
    S66 = Switch(name='S66', value=v)
    S67 = Switch(name='S67', value=v)

    tree_list_EQU_BIN = ['EQU', Tree.tree_list_BIN(4), Tree.tree_list_BIN(4)]

    T0 = Tree(tree_list=['AND',
                         tree_list_EQU_BIN,
                         Tree.tree_list_XOR(2),
                         Tree.tree_list_XNOR(2),
                         Tree.tree_list_OR(2),] + [Tree.tree_list_NOT]*4,
              empty=True,
              name='T0',
              switches = [S0, S1, S2, S3,
                          S4, S5, S6, S7,
                          S4, S5,
                          S6, S7,
                          S4, S7,
                          S8, S9, S10, S11])
    T1 = Tree(tree_list=['AND',
                         tree_list_EQU_BIN,
                         Tree.tree_list_XOR(2),
                         Tree.tree_list_NOT,
                         Tree.tree_list_NOT,] + [Tree.tree_list_NOT]*4,
              empty=True,
              name='T1',
              switches = [S0, S1, S2, S3,
                          S4, S5, S6, S7,
                          S4, S5, S6, S7,
                          S12, S13, S14, S15])
    T2 = Tree(tree_list=['AND',
                         tree_list_EQU_BIN,
                         [None],
                         Tree.tree_list_NOT,
                         Tree.tree_list_NOT,
                         Tree.tree_list_NOT,
                         Tree.tree_list_NOT,
                         Tree.tree_list_NOT,
                         Tree.tree_list_NOT,],
              empty=True,
              name='T2',
              switches = [S0, S1, S2, S3,
                          S4, S5, S6, S7,
                          S5, S6, S7,
                          S16, S17, S18, S19,])
    T3 = Tree(tree_list=['AND',
                         tree_list_EQU_BIN,
                         Tree.tree_list_XNOR(2),
                         Tree.tree_list_XOR(2),
                         Tree.tree_list_NOT] + [Tree.tree_list_NOT]*4,
              empty=True,
              name='T3',
              switches = [S0, S1, S2, S3,
                          S4, S5, S6, S7,
                          S4, S5,
                          S5, S6,
                          S7,
                          S20, S21, S22, S23,])
    T4 = Tree(tree_list=['AND',
                         tree_list_EQU_BIN,
                         Tree.tree_list_NOT,
                         Tree.tree_list_NOT,
                         [None],
                         Tree.tree_list_NOT,
                         Tree.tree_list_NOT,
                         Tree.tree_list_NOT,
                         Tree.tree_list_NOT,
                         Tree.tree_list_NOT,],
              empty=True,
              name='T4',
              switches = [S0, S1, S2, S3,
                          S4, S5, S6, S7,
                          S4, S5, S6, S7,
                          S24, S25, S26, S27])
    T5 = Tree(tree_list=['AND',
                         tree_list_EQU_BIN,
                         [None],
                         [None],
                         Tree.tree_list_XNOR(2)] + [Tree.tree_list_NOT]*4,
              empty=True,
              name='T5',
              switches = [S0, S1, S2, S3,
                          S4, S5, S6, S7,
                          S4, S6, S5, S7,
                          S28, S29, S30, S31])
    T6 = Tree(tree_list=['AND',
                         tree_list_EQU_BIN,
                         Tree.tree_list_XOR(2),
                         [None],
                         Tree.tree_list_NOT] + [Tree.tree_list_NOT]*4,
              empty=True,
              name='T6',
              switches = [S0, S1, S2, S3,
                          S4, S5, S6, S7,
                          S4, S5, S6, S7,
                          S32, S33, S34, S35])
    T7 = Tree(tree_list=['AND',
                         tree_list_EQU_BIN,
                         [None],
                         [None],
                         Tree.tree_list_NOT,
                         Tree.tree_list_NOT,
                         Tree.tree_list_NOT,
                         Tree.tree_list_NOT,
                         Tree.tree_list_NOT,],
              empty=True,
              name='T7',
              switches = [S0, S1, S2, S3,
                          S4, S5, S6, S7,
                          S5, S6, S7,
                          S36, S37, S38, S39])
    T8 = Tree(tree_list=['AND',
                         tree_list_EQU_BIN,
                         Tree.tree_list_XNOR(2),
                         Tree.tree_list_XNOR(2),
                         Tree.tree_list_XOR(2),] + [Tree.tree_list_NOT]*4,
              empty=True,
              name='T8',
              switches = [S0, S1, S2, S3,
                          S4, S5, S6, S7,
                          S4, S5,
                          S5, S6,
                          S6, S7,
                          S40, S41, S42, S43])
    T9 = Tree(tree_list=['AND',
                         tree_list_EQU_BIN,
                         Tree.tree_list_NOT,
                         Tree.tree_list_NOT,
                         Tree.tree_list_NOT,
                         [None],
                         Tree.tree_list_NOT,
                         Tree.tree_list_NOT,
                         Tree.tree_list_NOT,
                         Tree.tree_list_NOT,],
              empty=True,
              name='T9',
              switches = [S0, S1, S2, S3,
                          S4, S5, S6, S7,
                          S4, S5, S6, S7,
                          S44, S45, S46, S47])
    T10 = Tree(tree_list=['AND',
                          tree_list_EQU_BIN,
                          Tree.tree_list_from_str('TFFT TTT')] + [Tree.tree_list_NOT]*4,
              empty=True,
              name='T10',
              switches = [S0, S1, S2, S3,
                          S4, S5, S6, S7,
                          S4, S5, S6, S7,
                          S5, S6, S7,
                          S48, S49, S50, S51])
    T11 = Tree(tree_list=['AND',
                          tree_list_EQU_BIN,
                          Tree.tree_list_XOR(2),
                          Tree.tree_list_NOT,
                          [None],] + [Tree.tree_list_NOT]*4,
              empty=True,
              name='T11',
              switches = [S0, S1, S2, S3,
                          S4, S5, S6, S7,
                          S4, S5, S6, S7,
                          S52, S53, S54, S55])
    T12 = Tree(tree_list=['AND',
                          tree_list_EQU_BIN,
                          [None],
                          Tree.tree_list_NOT,
                          [None]] + [Tree.tree_list_NOT]*4,
              empty=True,
              name='T12',
              switches = [S0, S1, S2, S3,
                          S4, S5, S6, S7,
                          S5, S6, S7,
                          S56, S57, S58, S59])
    T13 = Tree(tree_list=['AND',
                          tree_list_EQU_BIN,
                          Tree.tree_list_XNOR(2),
                          Tree.tree_list_XOR(2),
                          [None]] + [Tree.tree_list_NOT]*4,
              empty=True,
              name='T13',
              switches = [S0, S1, S2, S3,
                          S4, S5, S6, S7,
                          S4, S5,
                          S5, S6,
                          S7,
                          S60, S61, S62, S63])
    T14 = Tree(tree_list=['AND',
                          tree_list_EQU_BIN,
                          Tree.tree_list_NOT,
                          Tree.tree_list_NOT,
                          [None],
                          [None],] + [Tree.tree_list_NOT]*4,
              empty=True,
              name='T14',
              switches = [S0, S1, S2, S3,
                          S4, S5, S6, S7,
                          S4, S5, S6, S7,
                          S64, S65, S66, S67])
    T15 = Tree(tree_list=['AND',
                          tree_list_EQU_BIN,
                          [None],
                          Tree.tree_list_NOT,
                          [None],] + [Tree.tree_list_NOT]*4,
              empty=True,
              name='T15',
              switches = [S0, S1, S2, S3,
                          S4, S5, S6, S7,
                          S4, S5, S6,
                          S28, S29, S30, S31])
    T16 = Tree(tree_list=['AND',
                          tree_list_EQU_BIN,
                          Tree.tree_list_XOR(2),
                          [None],
                          Tree.tree_list_NOT] + [Tree.tree_list_NOT]*4,
               empty=True,
               name='T16',
               switches = [S0, S1, S2, S3,
                           S4, S5, S6, S7,
                           S4, S5, S6, S7,
                           S32, S33, S34, S35])
    T17 = Tree(tree_list=['AND',
                          tree_list_EQU_BIN,
                          [None],
                          [None],
                          Tree.tree_list_NOT,] + [Tree.tree_list_NOT]*4,
               empty=True,
               name='T17',
               switches = [S0, S1, S2, S3,
                           S4, S5, S6, S7,
                           S5, S6, S7,
                           S36, S37, S38, S39])
    T18 = Tree(tree_list=['AND',
                          tree_list_EQU_BIN,
                          Tree.tree_list_XNOR(2),
                          Tree.tree_list_XNOR(2),
                          Tree.tree_list_XOR(2),] + [Tree.tree_list_NOT]*4,
               empty=True,
               name='T18',
               switches = [S0, S1, S2, S3,
                           S4, S5, S6, S7,
                           S4, S5,
                           S5, S6,
                           S6, S7,
                           S40, S41, S42, S43])
    T19 = Tree(tree_list=['AND',
                          tree_list_EQU_BIN,
                          Tree.tree_list_NOT,
                          Tree.tree_list_NOT,
                          Tree.tree_list_NOT,
                          [None],] + [Tree.tree_list_NOT]*4,
               empty=True,
               name='T19',
               switches = [S0, S1, S2, S3,
                           S4, S5, S6, S7,
                           S4, S5, S6, S7,
                           S44, S45, S46, S47])
    T20 = Tree(tree_list=['AND',
                          Tree.tree_list_XOR(2),
                          [None],
                          [None],
                          ['OR',
                           ['AND', [None]] + [Tree.tree_list_XNOR(2)]*4,
                           ['AND', Tree.tree_list_NOT] + [Tree.tree_list_XNOR(2)]*4]],
              empty=True,
              name='T20',
              switches = [S4, S5, S6, S7,
                          S4,
                          S8, S28,
                          S9, S29,
                          S10, S30,
                          S11, S31,
                          S4,
                          S8, S48,
                          S9, S49,
                          S10, S50,
                          S11, S51,],
              cut_expression=True)
    T21 = Tree(tree_list=['AND',
                          [None],
                          Tree.tree_list_NOT,
                          Tree.tree_list_NOT,
                          Tree.tree_list_NOT]  + [Tree.tree_list_XNOR(2)]*4,
               empty=True,
               name='T21',
               switches = [S4, S5, S6, S7,
                           S8, S12,
                           S9, S13,
                           S10, S14,
                           S11, S15,])
    T22 = Tree(tree_list=['AND',
                          Tree.tree_list_NOT,
                          [None],
                          Tree.tree_list_NOT,
                          Tree.tree_list_NOT]  + [Tree.tree_list_XNOR(2)]*4,
               empty=True,
               name='T22',
               switches = [S4, S5, S6, S7,
                           S12, S16,
                           S13, S17,
                           S14, S18,
                           S15, S19,])
    T23 = Tree(tree_list=['AND',
                          [None],
                          [None],
                          Tree.tree_list_NOT,
                          Tree.tree_list_NOT]  + [Tree.tree_list_XNOR(2)]*4,
               empty=True,
               name='T23',
               switches = [S4, S5, S6, S7,
                           S16, S20,
                           S17, S21,
                           S18, S22,
                           S19, S23,])
    T24 = Tree(tree_list=['AND',
                          Tree.tree_list_NOT,
                          Tree.tree_list_NOT,
                          [None],
                          Tree.tree_list_NOT]  + [Tree.tree_list_XNOR(2)]*4,
               empty=True,
               name='T24',
               switches = [S4, S5, S6, S7,
                           S20, S24,
                           S21, S25,
                           S22, S26,
                           S23, S27,])
    T25 = Tree(tree_list=['AND',
                          [None],
                          [None],
                          [None],
                          ['OR',
                           ['AND', Tree.tree_list_NOT] + [Tree.tree_list_XNOR(2)]*4,
                           ['AND', [None]] + [Tree.tree_list_XNOR(2)]*4]],
               empty=True,
               name='T25',
               switches = [S4, S6, S7,
                           S5,
                           S8, S28,
                           S9, S29,
                           S10, S30,
                           S11, S31,
                           S5,
                           S28, S48,
                           S29, S49,
                           S30, S50,
                           S31, S51,],
               cut_expression=True)
    T26 = Tree(tree_list=['AND',
                          [None],
                          Tree.tree_list_NOT,
                          [None],
                          Tree.tree_list_NOT]  + [Tree.tree_list_XNOR(2)]*4,
               empty=True,
               name='T26',
               switches = [S4, S5, S6, S7,
                           S28, S32,
                           S29, S33,
                           S30, S34,
                           S31, S35,])
    T27 = Tree(tree_list=['AND',
                          Tree.tree_list_NOT,
                          [None],
                          [None],
                          Tree.tree_list_NOT]  + [Tree.tree_list_XNOR(2)]*4,
               empty=True,
               name='T27',
               switches = [S4, S5, S6, S7,
                           S32, S36,
                           S33, S37,
                           S34, S38,
                           S35, S39,])
    T28 = Tree(tree_list=['AND',
                          [None],
                          [None],
                          [None],
                          Tree.tree_list_NOT]  + [Tree.tree_list_XNOR(2)]*4,
               empty=True,
               name='T28',
               switches = [S4, S5, S6, S7,
                           S36, S40,
                           S37, S41,
                           S38, S42,
                           S39, S43,])
    T29 = Tree(tree_list=['AND',
                          Tree.tree_list_NOT,
                          Tree.tree_list_NOT,
                          Tree.tree_list_NOT,
                          [None],]  + [Tree.tree_list_XNOR(2)]*4,
               empty=True,
               name='T29',
               switches = [S4, S5, S6, S7,
                           S40, S44,
                           S41, S45,
                           S42, S46,
                           S43, S47,])
    T30 = Tree(tree_list=['AND',
                          [None],
                          [None],
                          [None],
                          ['OR',
                           ['AND', Tree.tree_list_NOT] + [Tree.tree_list_XNOR(2)]*4,
                           ['AND', [None]] + [Tree.tree_list_XNOR(2)]*4]],
               empty=True,
               name='T30',
               switches = [S5, S6, S7,
                           S4,
                           S8, S48,
                           S9, S49,
                           S10, S50,
                           S11, S51,
                           S4,
                           S28, S48,
                           S29, S49,
                           S30, S50,
                           S31, S51,],
               cut_expression=True)
    T31 = Tree(tree_list=['AND',
                          [None],
                          Tree.tree_list_NOT,
                          Tree.tree_list_NOT,
                          [None],]  + [Tree.tree_list_XNOR(2)]*4,
              empty=True,
              name='T31',
              switches = [S4, S5, S6, S7,
                          S48, S52,
                          S49, S53,
                          S50, S54,
                          S51, S55,])
    T32 = Tree(tree_list=['AND',
                          Tree.tree_list_NOT,
                          [None],
                          Tree.tree_list_NOT,
                          [None],]  + [Tree.tree_list_XNOR(2)]*4,
              empty=True,
              name='T32',
              switches = [S4, S5, S6, S7,
                          S52, S56,
                          S53, S57,
                          S54, S58,
                          S55, S59,])
    T33 = Tree(tree_list=['AND',
                          [None],
                          [None],
                          Tree.tree_list_NOT,
                          [None],]  + [Tree.tree_list_XNOR(2)]*4,
              empty=True,
              name='T33',
              switches = [S4, S5, S6, S7,
                          S56, S60,
                          S57, S61,
                          S58, S62,
                          S59, S63,])
    T34 = Tree(tree_list=['AND',
                          Tree.tree_list_NOT,
                          Tree.tree_list_NOT,
                          [None],
                          [None],]  + [Tree.tree_list_XNOR(2)]*4,
              empty=True,
              name='T34',
              switches = [S4, S5, S6, S7,
                          S60, S64,
                          S61, S65,
                          S62, S66,
                          S63, S67,])
    T35 = Tree(tree_list=['AND',
                           ['DIFF', Tree.tree_list_BIN(3), [None]],
                           ['NOT', ['IN', Tree.tree_list_BIN(3), [None], [None]]],
                           ['NOT', ['IN', Tree.tree_list_BIN(3), [None], [None], [None]]]],
              empty=True,
              name='T35',
              switches = [
                          S16, S17, S18, Switch(value=1),
                          S20, S21, S22, Switch(value=1), Switch(value=2),
                          S24, S25, S26, Switch(value=1), Switch(value=2), Switch(value=3),
                          ],
              cut_expression=False,
              cut_expression_separator=']')
    T36 = Tree(tree_list=['AND',
                           ['DIFF', Tree.tree_list_BIN(3), [None]],
                           ['NOT', ['IN', Tree.tree_list_BIN(3), [None], [None]]],
                           ['NOT', ['IN', Tree.tree_list_BIN(3), [None], [None], [None]]]],
              empty=True,
              name='T36',
              switches = [
                          S56, S57, S58, Switch(value=1),
                          S60, S61, S62, Switch(value=1), Switch(value=2),
                          S64, S65, S66, Switch(value=1), Switch(value=2), Switch(value=3),],
              cut_expression=False,
              cut_expression_separator=']')
    T37 = Tree(tree_list=['AND'] + [['EQU', [None], Tree.tree_list_BIN(16)]]*2,
              empty=True,
              name='T37',
              switches = [Switch(value=52137), S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27,
                          Switch(value=17185), S52, S53, S54, S55, S56, S57, S58, S59, S60, S61, S62, S63, S64, S65, S66, S67,],
              cut_expression=True)
    
    ay = 0.9
    dx = 1.9
    ey = 0.85*ay
    lx = 3
    ly = 10*ay

    R0 = Room(name='R0',
              position = [0.8, 2*ay, 0.35, ly],
              switches_list = [S0, S1, S2, S3,])
    R1 = Room(name='R1',
              position = [2.8+2*dx+lx, 2*ay, 0.35, ly],
              switches_list = [S4, S5, S6, S7,])
    R2 = Room(name='R2',
              position = [2+dx+1, 0.6*ay, lx-2, 0.4*ay],
              switches_list = [])
    R3 = Room(name='R3',
              position = [2, 2*ay, lx, ey],
              switches_list = [S8, S9, S10, S11,])
    R4 = Room(name='R4',
              position = [2, 4*ay, lx, ey],
              switches_list = [S12, S13, S14, S15,])
    R5 = Room(name='R5',
              position = [2, 6*ay, lx, ey],
              switches_list = [S16, S17, S18, S19,])
    R6 = Room(name='R6',
              position = [2, 8*ay, lx, ey],
              switches_list = [S20, S21, S22, S23,])
    R7 = Room(name='R7',
              position = [2, 10*ay, lx, ey],
              switches_list = [S24, S25, S26, S27,])
    R8 = Room(name='R8',
              position = [2+dx, 3*ay, lx, ey],
              switches_list = [S28, S29, S30, S31,])
    R9 = Room(name='R9',
              position = [2+dx, 5*ay, lx, ey],
              switches_list = [S32, S33, S34, S35,])
    R10 = Room(name='R10',
              position = [2+dx, 7*ay, lx, ey],
              switches_list = [S36, S37, S38, S39,])
    R11 = Room(name='R11',
              position = [2+dx, 9*ay, lx, ey],
              switches_list = [S40, S41, S42, S43,])
    R12 = Room(name='R12',
              position = [2+dx, 11*ay, lx, ey],
              switches_list = [S44, S45, S46, S47,])
    R13 = Room(name='R13',
              position = [2+2*dx, 2*ay, lx, ey],
              switches_list = [S48, S49, S50, S51,])
    R14 = Room(name='R14',
              position = [2+2*dx, 4*ay, lx, ey],
              switches_list = [S52, S53, S54, S55,])
    R15 = Room(name='R15',
              position = [2+2*dx, 6*ay, lx, ey],
              switches_list = [S56, S57, S58, S59,])
    R16 = Room(name='R16',
              position = [2+2*dx, 8*ay, lx, ey],
              switches_list = [S60, S61, S62, S63,])
    R17 = Room(name='R17',
              position = [2+2*dx, 10*ay, lx, ey],
              switches_list = [S64, S65, S66, S67,])
    RE = Room(name='RE',
              position=[1.4, 0.6*ay, lx-2, 0.7*ay],
              is_exit=True)   # E pour exit ou end

    p1 = 0.45
    p2 = 0.65

    D0 = Door(two_way=True,
              tree=T0,
              room_departure=R0,
              room_arrival=R3,
              relative_departure_coordinates=[1, ey/2/ly],
              relative_arrival_coordinates=[0, 1/2])
    D1 = Door(two_way=True,
              tree=T1,
              room_departure=R0,
              room_arrival=R4,
              relative_departure_coordinates=[1, (2*ay+ey/2)/ly],
              relative_arrival_coordinates=[0, 1/2])
    D2 = Door(two_way=True,
              tree=T2,
              room_departure=R0,
              room_arrival=R5,
              relative_departure_coordinates=[1, (4*ay+ey/2)/ly],
              relative_arrival_coordinates=[0, 1/2])
    D3 = Door(two_way=True,
              tree=T3,
              room_departure=R0,
              room_arrival=R6,
              relative_departure_coordinates=[1, (6*ay+ey/2)/ly],
              relative_arrival_coordinates=[0, 1/2])
    D4 = Door(two_way=True,
              tree=T4,
              room_departure=R0,
              room_arrival=R7,
              relative_departure_coordinates=[1, (8*ay+ey/2)/ly],
              relative_arrival_coordinates=[0, 1/2])

    D5 = Door(two_way=True,
              tree=T5,
              room_departure=R0,
              room_arrival=R8,
              relative_departure_coordinates=[1, (1*ay+ey/2)/ly],
              relative_arrival_coordinates=[0, 1/2],
              relative_position=p1)
    D6 = Door(two_way=True,
              tree=T6,
              room_departure=R0,
              room_arrival=R9,
              relative_departure_coordinates=[1, (3*ay+ey/2)/ly],
              relative_arrival_coordinates=[0, 1/2],
              relative_position=p1)
    D7 = Door(two_way=True,
              tree=T7,
              room_departure=R0,
              room_arrival=R10,
              relative_departure_coordinates=[1, (5*ay+ey/2)/ly],
              relative_arrival_coordinates=[0, 1/2],
              relative_position=p1)
    D8 = Door(two_way=True,
              tree=T8,
              room_departure=R0,
              room_arrival=R11,
              relative_departure_coordinates=[1, (7*ay+ey/2)/ly],
              relative_arrival_coordinates=[0, 1/2],
              relative_position=p1)
    D9 = Door(two_way=True,
              tree=T9,
              room_departure=R0,
              room_arrival=R12,
              relative_departure_coordinates=[1, (9*ay+ey/2)/ly],
              relative_arrival_coordinates=[0, 1/2],
              relative_position=p1)

    D10 = Door(two_way=True,
               tree=T10,
               room_departure=R13,
               room_arrival=R1,
               relative_departure_coordinates=[1, 1/2],
               relative_arrival_coordinates=[0, ey/2/ly])
    D11 = Door(two_way=True,
               tree=T11,
               room_departure=R14,
               room_arrival=R1,
               relative_departure_coordinates=[1, 1/2],
               relative_arrival_coordinates=[0, (2*ay+ey/2)/ly])
    D12 = Door(two_way=True,
               tree=T12,
               room_departure=R15,
               room_arrival=R1,
               relative_departure_coordinates=[1, 1/2],
               relative_arrival_coordinates=[0, (4*ay+ey/2)/ly])
    D13 = Door(two_way=True,
               tree=T13,
               room_departure=R16,
               room_arrival=R1,
               relative_departure_coordinates=[1, 1/2],
               relative_arrival_coordinates=[0, (6*ay+ey/2)/ly])
    D14 = Door(two_way=True,
               tree=T14,
               room_departure=R17,
               room_arrival=R1,
               relative_departure_coordinates=[1, 1/2],
               relative_arrival_coordinates=[0, (8*ay+ey/2)/ly])

    D15 = Door(two_way=True,
               tree=T15,
               room_departure=R8,
               room_arrival=R1,
               relative_departure_coordinates=[1, 1/2],
               relative_arrival_coordinates=[0, (1*ay+ey/2)/ly],
               relative_position=p2)
    D16 = Door(two_way=True,
               tree=T16,
               room_departure=R9,
               room_arrival=R1,
               relative_departure_coordinates=[1, 1/2],
               relative_arrival_coordinates=[0, (3*ay+ey/2)/ly],
               relative_position=p2)
    D17 = Door(two_way=True,
               tree=T17,
               room_departure=R10,
               room_arrival=R1,
               relative_departure_coordinates=[1, 1/2],
               relative_arrival_coordinates=[0, (5*ay+ey/2)/ly],
               relative_position=p2)
    D18 = Door(two_way=True,
               tree=T18,
               room_departure=R11,
               room_arrival=R1,
               relative_departure_coordinates=[1, 1/2],
               relative_arrival_coordinates=[0, (7*ay+ey/2)/ly],
               relative_position=p2)
    D19 = Door(two_way=True,
               tree=T19,
               room_departure=R12,
               room_arrival=R1,
               relative_departure_coordinates=[1, 1/2],
               relative_arrival_coordinates=[0, (9*ay+ey/2)/ly],
               relative_position=p2)

    D20 = Door(two_way=True,
               tree=T20,
               room_departure=R2,
               room_arrival=R3)
    D21 = Door(two_way=True,
               tree=T21,
               room_departure=R3,
               room_arrival=R4)
    D22 = Door(two_way=True,
               tree=T22,
               room_departure=R4,
               room_arrival=R5)
    D23 = Door(two_way=True,
               tree=T23,
               room_departure=R5,
               room_arrival=R6)
    D24 = Door(two_way=True,
               tree=T24,
               room_departure=R6,
               room_arrival=R7)

    D25 = Door(two_way=True,
               tree=T25,
               room_departure=R2,
               room_arrival=R8,
               relative_position=0.3)
    D26 = Door(two_way=True,
               tree=T26,
               room_departure=R8,
               room_arrival=R9)
    D27 = Door(two_way=True,
               tree=T27,
               room_departure=R9,
               room_arrival=R10)
    D28 = Door(two_way=True,
               tree=T28,
               room_departure=R10,
               room_arrival=R11)
    D29 = Door(two_way=True,
               tree=T29,
               room_departure=R11,
               room_arrival=R12)

    D30 = Door(two_way=True,
               tree=T30,
               room_departure=R2,
               room_arrival=R13)
    D31 = Door(two_way=True,
               tree=T31,
               room_departure=R13,
               room_arrival=R14)
    D32 = Door(two_way=True,
               tree=T32,
               room_departure=R14,
               room_arrival=R15)
    D33 = Door(two_way=True,
               tree=T33,
               room_departure=R15,
               room_arrival=R16)
    D34 = Door(two_way=True,
               tree=T34,
               room_departure=R16,
               room_arrival=R17)

    D35 = Door(two_way=False,
               tree=T35,
               room_departure=R0,
               room_arrival=R1,
               relative_departure_coordinates=[1, 1],
               relative_arrival_coordinates=[0, 1],
               relative_position=0.75)
    
    D36 = Door(two_way=False,
               tree=T36,
               room_departure=R1,
               room_arrival=R0,
               relative_departure_coordinates=[0, 1],
               relative_arrival_coordinates=[1, 1],
               relative_position=0.75)

    D37 = Door(two_way=False,
               tree=T37,
               room_departure=R0,
               room_arrival=RE,
               relative_departure_coordinates=[1/2, 0],
               relative_arrival_coordinates=[0.3, 0.7])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, RE],
                 doors_list=[D0, D1, D2, D3, D4,
                             D5, D6, D7, D8, D9,
                             D10, D11, D12, D13, D14,
                             D15, D16, D17, D18, D19,
                             D20, D21, D22, D23, D24,
                             D25, D26, D27, D28, D29,
                             D30, D31, D32, D33, D34,
                             D35, D36, D37],
                 fastest_solution=None,
                 level_color=Levels_colors_list.BROWN,
                 name='Panex',
                 door_window_size=815,
                 keep_proportions=False,
                 y_separation=30)

    return level