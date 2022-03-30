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
from numpy import  cos, pi
from fonction_affine import fonction_affine

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
    
    T0 = Tree(tree_list=[None],
           empty=True,
           name='T0',
           switches = [S0])
    T1 = Tree(tree_list=[None],
           empty=True,
           name='T1',
           switches = [S0])
    T2 = Tree(tree_list=[None],
           empty=True,
           name='T2',
           switches = [S0])
    T3 = Tree(tree_list=[None],
           empty=True,
           name='T3',
           switches = [S0])
    T4 = Tree(tree_list=[None],
           empty=True,
           name='T4',
           switches = [S0])
    T5 = Tree(tree_list=[None],
           empty=True,
           name='T5',
           switches = [S0])
    T6 = Tree(tree_list=[None],
           empty=True,
           name='T6',
           switches = [S0])
    T7 = Tree(tree_list=[None],
           empty=True,
           name='T7',
           switches = [S0])
    T8 = Tree(tree_list=[None],
           empty=True,
           name='T8',
           switches = [S0])
    T9 = Tree(tree_list=[None],
           empty=True,
           name='T9',
           switches = [S0])
    T10 = Tree(tree_list=[None],
           empty=True,
           name='T10',
           switches = [S0])
    T11 = Tree(tree_list=[None],
           empty=True,
           name='T11',
           switches = [S0])
    T12 = Tree(tree_list=[None],
           empty=True,
           name='T12',
           switches = [S0])
    T13 = Tree(tree_list=[None],
           empty=True,
           name='T13',
           switches = [S0])
    T14 = Tree(tree_list=[None],
           empty=True,
           name='T14',
           switches = [S0])
    T15 = Tree(tree_list=[None],
           empty=True,
           name='T15',
           switches = [S0])
    T16 = Tree(tree_list=[None],
           empty=True,
           name='T16',
           switches = [S0])
    T17 = Tree(tree_list=[None],
           empty=True,
           name='T17',
           switches = [S0])
    T18 = Tree(tree_list=[None],
           empty=True,
           name='T18',
           switches = [S0])
    T19 = Tree(tree_list=[None],
           empty=True,
           name='T19',
           switches = [S0])
    T20 = Tree(tree_list=[None],
           empty=True,
           name='T20',
           switches = [S0])
    T21 = Tree(tree_list=[None],
           empty=True,
           name='T21',
           switches = [S0])
    T22 = Tree(tree_list=[None],
           empty=True,
           name='T22',
           switches = [S0])
    T23 = Tree(tree_list=[None],
           empty=True,
           name='T23',
           switches = [S0])
    T24 = Tree(tree_list=[None],
           empty=True,
           name='T24',
           switches = [S0])
    T25 = Tree(tree_list=[None],
           empty=True,
           name='T25',
           switches = [S0])

    position_R = []
    position_R.append([-7, 0, 5, 22])
    position_R.append([4, 4, 2.5, 1.25])
    n = 12
    e = 8*7/(2*n-1)
    for i in range(n):
        (pente, coeff) = fonction_affine(0, 0, n-1, pi)
        x_middle = 16*(1+cos(pente*i+coeff))+12
        (pente, coeff) = fonction_affine(0, -pi/2, n-1, pi/2)
        y_rect = 16*(1.5-cos(pente*i+coeff))
        position_R.append([x_middle-y_rect/2, i*e, y_rect, 0.92*e])
    position_R.append([46, 21, 3.5, 1.25])
    position_RE = [53, 25, 4, 3]

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
    RE = Room(name='RE', position = position_RE, is_exit = True)  # E pour exit ou end
    
    p = 3/4
    
    D0  = Door(two_way = False,  
           tree = T0,  
           name='D0',  
           room_departure = R0, 
           room_arrival = R1, 
           relative_departure_coordinates = [1, 0],
           relative_arrival_coordinates = [0, 0],
           relative_position=2/3)
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
           room_arrival = RE)
    
    l_help_txt = [
"""
"""]
    
    level = Maze(start_room_index=0, 
             exit_room_index=-1, 
             rooms_list=[R0, R1, R2, R3, R4,
                 R5, R6, R7, R8, R9,
                 R10, R11, R12, R13, R14,
                 RE], 
             doors_list = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9,
                   D10, D11, D12, D13, D14, D15, D16, D17, D18, D19,
                   D20, D21, D22, D23, D24, D25], 
             fastest_solution=None,
             level_color=Levels_colors_list.BLACK_AND_WHITE,
             name='Sinusoidal',
             help_txt = l_help_txt,
             door_window_size = 500,
             y_separation=50,
             border = 60,
             # print_tree_gap=22,
             keep_proportions = False)
    
    return level