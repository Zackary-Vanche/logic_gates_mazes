# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 19:14:13 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_bis_repetita():
    
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    
    T0 = Tree(tree_list=Tree.tree_list_xor,
                empty=True,
                name='T0',
                switches = [S0, S1])
    T1 = Tree(tree_list=Tree.tree_list_xor,
                empty=True,
                name='T1',
                switches = [S1, S2])
    T2 = Tree(tree_list=[None],
                empty=True,
                name='T2',
                switches = [S2])
    T3 = Tree(tree_list=Tree.tree_list_from_str('FFF'),
                empty=True,
                name='T3',
                switches = [S0, S1, S2])
    
    R0 = Room(name='R0',
              position = [0, 0, 3, 3],
              switches_list = [S0])
    R1 = Room(name='R1',
              position = [2, 4, 1, 1],
              switches_list = [S1])
    R2 = Room(name='R2',
              position = [4, 4, 3, 3],
              switches_list = [S2])
    RE = Room(name='RE',
              position = [4, 2, 1, 1],
              is_exit = True)  # E pour exit ou end
    
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_position=0.7)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2,
              relative_position=0.35)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R0,
              relative_position=0.5)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R2,
              room_arrival=RE,
              relative_position=0.7)
    
    l_help_txt = [
"""One new operand is used in this level : XOR

    XOR means exclusive or.
    D0 = XOR S0 S1 = ^ S0 S1 means :
        D0 is open if S0 is different from S1.
"""]
        
    level = Maze(start_room_index=0, 
                 exit_room_index=-1, 
                 rooms_list=[R0, R1, R2, RE], 
                 doors_list=[D0, D1, D2, D3], 
                 fastest_solution="S0 D0 S1 D1 S2 D2 S0 D0 S1 D1 S2 D3",
                 level_color=Levels_colors_list.BRIGHT_AND_DARK_BLUE,
                 name='Bis repetita',
                 help_txt = l_help_txt,
                 border = 30,
                 door_window_size = 500,
                 keep_proportions=True)

    return level