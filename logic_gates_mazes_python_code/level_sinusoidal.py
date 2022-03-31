# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:23:02 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_sinusoidal():
    
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
    SN = Switch(name='SN')
    
    T0 = Tree(tree_list=Tree.tree_list_not,
              empty=True,
              name='T0',
              switches = [SN],
              easy_logical_expression_PN='1')
    T1 = Tree(tree_list=Tree.tree_list_from_str('TF'),
              empty=True,
              name='T1',
              switches = [S4, S5])
    T2 = Tree(tree_list=[None],
              empty=True,
               name='T2',
               switches = [S6])
    T3 = Tree(tree_list=[None],
              empty=True,
               name='T3',
               switches = [S7])
    T4 = Tree(tree_list=Tree.tree_list_from_str('TFT'),
              empty=True,
              name='T4',
              switches = [S3, S8, S9])
    T5 = Tree(tree_list=Tree.tree_list_from_str('TFT'),
              empty=True,
              name='T5',
              switches = [S2, S8, S9])
    T6 = Tree(tree_list=Tree.tree_list_from_str('TTF'),
              empty=True,
              name='T6',
              switches = [S0, S10, S14])
    T7 = Tree(tree_list=Tree.tree_list_from_str('F'),
              empty=True,
              name='T7',
              switches = [S11])
    T8 = Tree(tree_list=Tree.tree_list_from_str('F'),
              empty=True,
              name='T8',
              switches = [S12])
    T9 = Tree(tree_list=[None],
              empty=True,
              name='T9',
              switches = [S13])
    T10 = Tree(tree_list=Tree.tree_list_from_str('FTF'),
               empty=True,
               name='T10',
               switches = [S2, S10, S14])
    T11 = Tree(tree_list=Tree.tree_list_from_str('TF'),
               empty=True,
               name='T11',
               switches = [S0, S15])
    T12 = Tree(tree_list=Tree.tree_list_from_str('F'),
               empty=True,
               name='T12',
               switches = [S16])
    T13 = Tree(tree_list=Tree.tree_list_from_str('TTF'),
               empty=True,
               name='T13',
               switches = [S3, S5, S10])
    T14 = Tree(tree_list=Tree.tree_list_from_str('FT'),
               empty=True,
               name='T14',
               switches = [S6, S12])
    T15 = Tree(tree_list=Tree.tree_list_from_str('FT'),
               empty=True,
               name='T15',
               switches = [S7, S16])
    T16 = Tree(tree_list=[None],
               empty=True,
               name='T16',
               switches = [S8])
    T17 = Tree(tree_list=Tree.tree_list_from_str('TFT'),
               empty=True,
               name='T17',
               switches = [S1, S9, S15])
    T18 = Tree(tree_list=Tree.tree_list_from_str('FTF'),
               empty=True,
               name='T18',
               switches = [S1, S5, S10])
    T19 = Tree(tree_list=Tree.tree_list_from_str('TF'),
               empty=True,
               name='T19',
               switches = [S11, S13])
    T20 = Tree(tree_list=Tree.tree_list_from_str('FT'),
               empty=True,
               name='T20',
               switches = [S6, S12])
    T21 = Tree(tree_list=Tree.tree_list_from_str('TF'),
               empty=True,
               name='T21',
               switches = [S11, S13])
    T22 = Tree(tree_list=[None],
               empty=True,
               name='T22',
               switches = [S14])
    T23 = Tree(tree_list=Tree.tree_list_from_str('FFT'),
               empty=True,
               name='T23',
               switches = [S4, S9, S15])
    T24 = Tree(tree_list=Tree.tree_list_from_str('FT'),
               empty=True,
               name='T24',
               switches = [S7, S16])
    T26 = Tree(tree_list=Tree.tree_list_XOR5,
               empty=True,
               name='T26',
               switches = [S6, S7, S8, S13, S14])
    T25 = Tree(tree_list=['AND', Tree.tree_list_XOR3, Tree.tree_list_XOR5],
               empty=True,
               name='T25',
               switches = [S0, S1, S2,
                           S5, S11, S12, S15, S16])

    position_R = [[-10, 2, 4.5, 26.78],
                  [4, 2, 5, 2.5],
                  [29.0, 0.0, 30.0, 2],
                  [31.17, 2.43, 24.37, 2],
                  [31.87, 4.87, 19.19, 2],
                  [31.04, 7.3, 14.89, 2],
                  [28.74, 9.74, 11.81, 2],
                  [25.18, 12.17, 10.2, 2],
                  [20.62, 14.61, 10.2, 2],
                  [15.45, 17.04, 11.81, 2],
                  [10.08, 19.48, 14.89, 2],
                  [4.95, 21.91, 19.19, 2],
                  [0.47, 24.35, 24.37, 2],
                  [-3.0, 26.78, 30.0, 2],
                  [50.5, 20, 4, 2],
                  [38, 26.78, 4, 2]]
    
    position_RE = [50, 26.78, 7, 2]

    R0 = Room(name='R0',
          position = position_R[0],
          switches_list = [S0, S1, S2, S3, S4])
    R1 = Room(name='R1',
          position = position_R[1],
          switches_list = [])
    R2 = Room(name='R2',
          position = position_R[2],
          switches_list = [S5])
    R3 = Room(name='R3',
          position = position_R[3],
          switches_list = [S6])
    R4 = Room(name='R4',
          position = position_R[4],
          switches_list = [S7])
    R5 = Room(name='R5',
          position = position_R[5],
          switches_list = [S8])
    R6 = Room(name='R6',
          position = position_R[6],
          switches_list = [S9])
    R7 = Room(name='R7',
          position = position_R[7],
          switches_list = [S10])
    R8 = Room(name='R8',
          position = position_R[8],
          switches_list = [S11])
    R9 = Room(name='R9',
          position = position_R[9],
          switches_list = [S12])
    R10 = Room(name='R10',
          position = position_R[10],
          switches_list = [S13])
    R11 = Room(name='R11',
          position = position_R[11],
          switches_list = [S14])
    R12 = Room(name='R12',
          position = position_R[12],
          switches_list = [S15])
    R13 = Room(name='R13',
          position = position_R[13],
          switches_list = [S16])
    R14 = Room(name='R14',
          position = position_R[14],
          switches_list = [])
    R15 = Room(name='R15',
          position = position_R[15],
          switches_list = [])
    RE = Room(name='RE', position = position_RE, is_exit = True)  # E pour exit ou end
    
    p = 3/4
    
    D0  = Door(two_way = False,  
           tree = T0,  
           name='D0',  
           room_departure = R0, 
           room_arrival = R1, 
           relative_departure_coordinates = [1, 1.25/26.78],
           relative_arrival_coordinates = [0, 1/2],
           relative_position=1/2)
    D1  = Door(two_way = True,  
            tree = T1,  
            name='D1',  
            room_departure = R1, 
            room_arrival = R2, 
            relative_arrival_coordinates = [0, 0])
    D2  = Door(two_way = True,  
            tree = T2,  
            name='D2',  
            room_departure = R1, 
            room_arrival = R3, 
            relative_arrival_coordinates = [0, 0],
            relative_position=p)
    D3  = Door(two_way = True,  
            tree = T3,  
            name='D3',  
            room_departure = R1, 
            room_arrival = R4, 
            relative_arrival_coordinates = [0, 0])
    D4  = Door(two_way = True,  
            tree = T4,  
            name='D4',  
            room_departure = R1, 
            room_arrival = R5, 
            relative_arrival_coordinates = [0, 0],
            relative_position=p)
    D5  = Door(two_way = True,  
            tree = T5,  
            name='D5',  
            room_departure = R1, 
            room_arrival = R6, 
            relative_arrival_coordinates = [0, 0])
    D6  = Door(two_way = True,  
            tree = T6,  
            name='D6',  
            room_departure = R1, 
            room_arrival = R7, 
            relative_arrival_coordinates = [0, 0],
            relative_position=p)
    D7  = Door(two_way = True,  
            tree = T7,  
            name='D7',  
            room_departure = R1, 
            room_arrival = R8, 
            relative_arrival_coordinates = [0, 0])
    D8  = Door(two_way = True,  
            tree = T8,  
            name='D8',  
            room_departure = R1, 
            room_arrival = R9, 
            relative_arrival_coordinates = [0, 0],
            relative_position=p)
    D9  = Door(two_way = True,  
            tree = T9,  
            name='D9',  
            room_departure = R1, 
            room_arrival = R10, 
            relative_arrival_coordinates = [0, 0])
    D10  = Door(two_way = True,  
            tree = T10,  
            name='D10',  
            room_departure = R1, 
            room_arrival = R11, 
            relative_arrival_coordinates = [0, 0],
            relative_position=p)
    D11  = Door(two_way = True,  
            tree = T11,  
            name='D11',  
            room_departure = R1, 
            room_arrival = R12, 
            relative_arrival_coordinates = [0, 0])
    D12  = Door(two_way = True,  
            tree = T12,  
            name='D12',  
            room_departure = R1, 
            room_arrival = R13, 
            relative_arrival_coordinates = [0, 0],
            relative_position=p)
    D13  = Door(two_way = True,  
            tree = T13,  
            name='D13',  
            room_departure = R14, 
            room_arrival = R2, 
            relative_arrival_coordinates = [1, 1],
            relative_position=p)
    D14  = Door(two_way = True,  
            tree = T14,  
            name='D14',  
            room_departure = R14, 
            room_arrival = R3, 
            relative_arrival_coordinates = [1, 1])
    D15  = Door(two_way = True,  
            tree = T15,  
            name='D15',  
            room_departure = R14, 
            room_arrival = R4, 
            relative_arrival_coordinates = [1, 1],
            relative_position=p)
    D16  = Door(two_way = True,  
            tree = T16,  
            name='D16',  
            room_departure = R14, 
            room_arrival = R5, 
            relative_arrival_coordinates = [1, 1])
    D17  = Door(two_way = True,  
            tree = T17,  
            name='D17',  
            room_departure = R14, 
            room_arrival = R6, 
            relative_arrival_coordinates = [1, 1],
            relative_position=p)
    D18  = Door(two_way = True,  
            tree = T18,  
            name='D18',  
            room_departure = R14, 
            room_arrival = R7, 
            relative_arrival_coordinates = [1, 1])
    D19  = Door(two_way = True,  
            tree = T19,  
            name='D19',  
            room_departure = R14, 
            room_arrival = R8, 
            relative_arrival_coordinates = [1, 1],
            relative_position=p)
    D20  = Door(two_way = True,  
            tree = T20,  
            name='D20',  
            room_departure = R14, 
            room_arrival = R9, 
            relative_arrival_coordinates = [1, 1])
    D21  = Door(two_way = True,  
            tree = T21,  
            name='D21',  
            room_departure = R14, 
            room_arrival = R10, 
            relative_arrival_coordinates = [1, 1],
            relative_position=p)
    D22  = Door(two_way = True,  
            tree = T22,  
            name='D22',  
            room_departure = R14, 
            room_arrival = R11, 
            relative_arrival_coordinates = [1, 1])
    D23  = Door(two_way = True,  
            tree = T23,  
            name='D23',  
            room_departure = R14, 
            room_arrival = R12, 
            relative_arrival_coordinates = [1, 1],
            relative_position=p)
    D24  = Door(two_way = True,  
            tree = T24,  
            name='D24',  
            room_departure = R14, 
            room_arrival = R13, 
            relative_arrival_coordinates = [1, 1]) 
    D25  = Door(two_way = True,  
           tree = T25,  
           name='D25',  
           room_departure = R14, 
           room_arrival = R15)
    D26  = Door(two_way = True,  
                tree = T26,  
                name='D26',  
                room_departure = R15, 
                room_arrival = RE)
    
    l_help_txt = [
"""Several new notations are used in this level :
    
    D0 = 1 means that D0 is always open.
    
    XOR (and XNOR) can be used with more than 3 parameters :
        D0 = XOR(S0, S1, ...) means :
            D0 is open if there is exactly one switch among its parameters that is turned on.
        D0 = XNOR(S0, S1, ...) means :
            D0 is open if there is exactly one switch among its parameters that is turned off.
"""]
    
    level = Maze(start_room_index=0, 
             exit_room_index=-1, 
             rooms_list=[R0, R1,
                         R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13,
                         R14, R15, RE], 
             doors_list = [D0,
                           D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12,
                           D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24,
                           D25, D26], 
             fastest_solution="S0 S3 S4 D0 D1 S5 D13 D18 S10 D6 D10 S14 D22 D25 D26",
             level_color=Levels_colors_list.PURPLE_BLUE,
             name='Sinusoidal',
             help_txt = l_help_txt,
             door_window_size = 425,
             y_separation=50,
             border = 30,
             keep_proportions = False)
    
    return level

if __name__ == '__main__':
    
    # from numpy import  cos, pi
    # from fonction_affine import fonction_affine
    
    # position_R = []
    # position_R.append([-9, 0, 5, 22])  # R0
    # position_R.append([4, 4, 5, 2.5])  # R1
    # n = 12
    # e = 8*7/(2*n-1)
    # for i in range(n):
    #     (pente, coeff) = fonction_affine(0, 0, n-1, pi)
    #     x_middle = 16*(1+cos(pente*i+coeff))+12
    #     (pente, coeff) = fonction_affine(0, -pi/2, n-1, pi/2)
    #     y_rect = 20*(1.5-cos(pente*i+coeff))
    #     position_R.append([x_middle-y_rect/2, i*e, y_rect, 0.85*e])
    # position_R.append([45, 20, 4, 2])  # R14
    # for i in range(len(position_R)):
    #     for j in range(len(position_R[i])):
    #         position_R[i][j] = round(position_R[i][j], 2)
    # print(position_R)
    
    level_sinusoidal().try_solution("S0 S3 S4 D0 D1 S5 D13 D18 S10 D6 D10 S14 D22 D25 D26", verbose = 2)
    level_sinusoidal().find_all_solutions(verbose = 2, stop_at_first_solution = False)