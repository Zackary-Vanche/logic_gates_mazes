# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:21:45 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_point_of_no_return():
    
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
    
    tree_list_0 = [None] 
    tree_list_1 = ['AND', Tree.tree_list_XNOR(2), [None]]
    tree_list_2 = ['AND', Tree.tree_list_XOR(2), [None]]
    tree_list_3 = ['AND', Tree.tree_list_OR(2), [None]]
    tree_list_4 = ['AND', Tree.tree_list_XOR(2), [None]]
    tree_list_5 = Tree.tree_list_AND(5)
    
    T0 = Tree(tree_list=tree_list_0, empty=True, name='T0', switches = [S0])
    T1 = Tree(tree_list=tree_list_1, empty=True, name='T1', switches = [S5, S7, S9],
          easy_logical_expression_PN = "& S9 XNOR S5 S7\n= & S9 ¬^ S5 S7")
    T2 = Tree(tree_list=tree_list_2, empty=True, name='T2', switches = [S6, S7, S9],
          easy_logical_expression_PN = "& S9 XOR S6 S7\n= & S9 ^ S6 S7")
    T3 = Tree(tree_list=tree_list_3, empty=True, name='T3', switches = [S5, S8, S9])
    T4 = Tree(tree_list=tree_list_4, empty=True, name='T4', switches = [S6, S8, S9],
          easy_logical_expression_PN = "& S9 XOR S6 S8\n= & S9 ^ S6 S8")
    T5 = Tree(tree_list=tree_list_5, empty=True, name='T5', switches = [S1, S2, S3, S4, S9])
    
    position_R0 = [  0,   2,  3,  4]
    position_R1 = [3.5,   0,  2,  2]
    position_R2 = [3.5,   6,  2,  2]
    position_R3 = [6.5,   0,  2,  2]
    position_R4 = [6.5,   6,  2,  2]
    position_R5 = [4.5, 3.5,  3,  1]
    position_RE = [  9,3.25,1.5,1.5]
    
    R0 = Room(name='R0', position = position_R0, switches_list = [S0, S5, S6, S7, S8])
    R1 = Room(name='R1', position = position_R1, switches_list = [S1])
    R2 = Room(name='R2', position = position_R2, switches_list = [S2])
    R3 = Room(name='R3', position = position_R3, switches_list = [S3])
    R4 = Room(name='R4', position = position_R4, switches_list = [S4])
    R5 = Room(name='R5', position = position_R5, switches_list = [S9])
    RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
    
    relative_departure_coordinates_D0 = [1, 1/2]
    relative_arrival_coordinates_D0   = [0, 1/2]
    relative_departure_coordinates_D1 = [1/3, 0]
    relative_arrival_coordinates_D1   = [1/2, 1]
    relative_departure_coordinates_D2 = [1/3, 1]
    relative_arrival_coordinates_D2   = [1/2, 0]
    relative_departure_coordinates_D3 = [2/3, 0]
    relative_arrival_coordinates_D3   = [1/2, 1]
    relative_departure_coordinates_D4 = [2/3, 1]
    relative_arrival_coordinates_D4   = [1/2, 0]
    relative_departure_coordinates_D5 = [1, 1/2]
    relative_arrival_coordinates_D5   = [0, 1/2]
    
    D0 = Door(two_way = False,
          tree = T0, 
          name='D0', 
          room_departure = R0, 
          room_arrival = R5,
          relative_departure_coordinates = relative_departure_coordinates_D0,
          relative_arrival_coordinates = relative_arrival_coordinates_D0)
    D1 = Door(two_way = True,  
          tree = T1, 
          name='D1', 
          room_departure = R5, 
          room_arrival = R1,
          relative_departure_coordinates = relative_departure_coordinates_D1,
          relative_arrival_coordinates = relative_arrival_coordinates_D1)
    D2 = Door(two_way = True,  
          tree = T2, 
          name='D2', 
          room_departure = R5, 
          room_arrival = R2,
          relative_departure_coordinates = relative_departure_coordinates_D2,
          relative_arrival_coordinates = relative_arrival_coordinates_D2)
    D3 = Door(two_way = True,  
          tree = T3, 
          name='D3', 
          room_departure = R5, 
          room_arrival = R3,
          relative_departure_coordinates = relative_departure_coordinates_D3,
          relative_arrival_coordinates = relative_arrival_coordinates_D3)
    D4 = Door(two_way = True,  
          tree = T4, 
          name='D4', 
          room_departure = R5, 
          room_arrival = R4,
          relative_departure_coordinates = relative_departure_coordinates_D4,
          relative_arrival_coordinates = relative_arrival_coordinates_D4)
    D5 = Door(two_way = True,  
          tree = T5, 
          name='D5', 
          room_departure = R5, 
          room_arrival = RE,
          relative_departure_coordinates = relative_departure_coordinates_D5,
          relative_arrival_coordinates = relative_arrival_coordinates_D5)
    
    level = Maze(start_room_index=0, 
             exit_room_index=-1, 
             rooms_list=[R0, R1, R2, R3, R4, R5, RE], 
             doors_list = [D0, D1, D2, D3, D4, D5],
             fastest_solution='S0 S5 S7 S8 D0 S9 D1 S1 D1 D2 S2 D2 D3 S3 D3 D4 S4 D4 D5',
             level_color=Levels_colors_list.DARK_BLUE,
             name='Point_of_no_return')
    
    return level