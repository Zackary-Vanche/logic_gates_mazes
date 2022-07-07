# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:14:12 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_fluid(): 
    
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    
    tree_list_0 = Tree.tree_list_anb
    tree_list_1 = Tree.tree_list_anb
    tree_list_2 = Tree.tree_list_FTT
    tree_list_3 = Tree.tree_list_from_str('FFTTTTT')
    tree_list_4 = [None]
    tree_list_5 = [None]
    
    T0  = Tree(tree_list=tree_list_0,  
           empty=True, 
           name='T0', 
           switches = [S0, S4])
    T1  = Tree(tree_list=tree_list_1,  
           empty=True, 
           name='T1', 
           switches = [S1, S5])
    T2  = Tree(tree_list=tree_list_2,  
           empty=True, 
           name='T2', 
           switches = [S0, S2, S4]) 
    T3  = Tree(tree_list=tree_list_3,  
           empty=True, 
           name='T3', 
           switches = [S0, S1, S3, S4, S5, S6, S7])
    T4  = Tree(tree_list=tree_list_4,  
           empty=True, 
           name='T4', 
           switches = [S6])
    T5  = Tree(tree_list=tree_list_5,  
           empty=True, 
           name='T5', 
           switches = [S7])
    
    position_R0 = [ 0, 0, 3, 2]
    position_R1 = [ 2, 3, 3, 2]
    position_R2 = [ 4, 0, 3, 2]
    position_R3 = [ 6, 3, 3, 2]
    position_RE = [ 8, 0, 3, 2]
    
    R0 = Room(name='R0', position = position_R0, switches_list = [S0, S4])
    R1 = Room(name='R1', position = position_R1, switches_list = [S1, S5])
    R2 = Room(name='R2', position = position_R2, switches_list = [S2, S6])
    R3 = Room(name='R3', position = position_R3, switches_list = [S3, S7])
    RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
    
    D0  = Door(two_way = False, tree = T0,  name='D0',  room_departure = R0, room_arrival = R1)
    D1  = Door(two_way = False, tree = T1,  name='D1',  room_departure = R1, room_arrival = R2)
    D2  = Door(two_way = False, tree = T2,  name='D2',  room_departure = R2, room_arrival = R3)
    D3  = Door(two_way = False, tree = T3,  name='D3',  room_departure = R3, room_arrival = RE)
    D4  = Door(two_way = True,  tree = T4,  name='D4',  room_departure = R0, room_arrival = R2)
    D5  = Door(two_way = True,  tree = T5,  name='D5',  room_departure = R1, room_arrival = R3)
    
    level = Maze(start_room_index=0, 
              exit_room_index=-1, 
              rooms_list=[R0, R1, R2, R3, RE], 
              doors_list = [D0, D1, D2, D3, D4, D5],
              fastest_solution='S0 D0 S1 D1 S2 S6 D4 S0 S4 D4 D2 S3 S7 D5 S1 S5 D5 D3',
              level_color=Levels_colors_list.BRIGHT_BLUE,
              name='Fluid')
    return level