# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 22:09:24 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_river():
    
    S0 = Switch(name='S0', value=1)
    S1 = Switch(name='S1', value=1)
    S2 = Switch(name='S2', value=1)
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    SN = Switch(name='1', value=1)
    
    T0 = Tree(tree_list=[None],
              empty=True,
              name='T0',
              switches = [SN])
    T1 = Tree(tree_list=[None],
              empty=True,
              name='T1',
              switches = [SN])
    T2 = Tree(tree_list=[None],
              empty=True,
              name='T2',
              switches = [SN])
    T3 = Tree(tree_list=[None],
              empty=True,
              name='T3',
              switches = [SN])
    T4 = Tree(tree_list=['NOR',
                         Tree.tree_list_xnor,
                         Tree.tree_list_xnor],
              empty=True,
              name='T4',
              switches = [S0, S1, S1, S2])
    T5 = Tree(tree_list=[None],
              empty=True,
              name='T5',
              switches = [S0])
    T6 = Tree(tree_list=['AND_3',
                         Tree.tree_list_XOR3,
                         Tree.tree_list_XOR3,
                         Tree.tree_list_XOR3],
              empty=True,
              name='T6',
              switches = [S0, S3, S6, S1, S4, S7, S2, S5, S8])
    T7 = Tree(tree_list=[None],
              empty=True,
              name='T7',
              switches = [S0])
    
    R0 = Room(name='R0',
              position = [1.75, 1, 1, 2],
              switches_list = [])
    R1 = Room(name='R1',
              position = [3.5, 0, 2.5, 1],
              switches_list = [S0, S1, S2])
    R2 = Room(name='R2',
              position = [3.5, 3, 2.5, 1],
              switches_list = [S3, S4, S5])
    R3 = Room(name='R3',
              position = [7, 0, 1, 4],
              switches_list = [S6, S7, S8])
    R4 = Room(name='R4',
              position = [5.5, 1.5, 0.5, 1],
              switches_list = [])
    R5 = Room(name='R5',
              position = [4, 1.5, 0.5, 1],
              switches_list = [])
    RE = Room(name='RE',
              position = [0, 1, 1, 2],
              is_exit = True)  # E pour exit ou end
    
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R3,
              relative_departure_coordinates=[3/4, 1/2],
              relative_arrival_coordinates=[1/2, 1/8])
    # D2 = Door(two_way=False,
    #           tree=T2,
    #           room_departure=R0,
    #           room_arrival=R2)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=[3/4, 1/2],
              relative_arrival_coordinates=[1/2, 7/8])
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R3,
              room_arrival=R4,
              relative_position=0.55)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R4,
              room_arrival=R5)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R5,
              room_arrival=R0)
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R0,
              room_arrival=RE)
    
    l_help_txt = [
"""
"""]
    
    level = Maze(start_room_index=0, 
              exit_room_index=-1, 
              rooms_list=[R0, R1, R2, R3, R4, R5, RE], 
              doors_list = [D0, D1, D3, D4, D5, D6, D7],
              fastest_solution=None,
              level_color=Levels_colors_list.BLUE_AND_GREEN,
              name='River',
              help_txt = l_help_txt,
              keep_proportions=False,
              door_window_size=500,
              y_separation=100)
    
    return level