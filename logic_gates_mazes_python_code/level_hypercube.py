# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 12:07:53 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_hypercube():
    
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    SN = Switch(name='1', value=1)
    
    T0 = Tree(tree_list=[None],
                empty=True,
                name='T0',
                switches = [SN])
    T1 = Tree(tree_list=['AND', [None], Tree.tree_list_xor],
                empty=True,
                name='T1',
                switches = [S0, S2, S3])
    T2 = Tree(tree_list=[None],
                empty=True,
                name='T2',
                switches = [SN])
    T3 = Tree(tree_list=['AND',
                         Tree.tree_list_not,
                         Tree.tree_list_from_str('TTF FT')],
                empty=True,
                name='T3',
                switches = [S0, S1, S2, S3, S2, S3])
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
    
    R0 = Room(name='R0',
                position = [2, 5, 9, 0.5],
                switches_list = [])
    R1 = Room(name='R1',
                position = [0, 7, 3, 3],
                switches_list = [S0, S1, S2, S3])
    R2 = Room(name='R2',
                position = [10, 7, 3, 3],
                switches_list = [S4, S5, S6, S7])
    R3 = Room(name='R3',
                position = [0, 11.5, 13, 1],
                switches_list = [])
    RE = Room(name='RE',
              position = [5, 1.5, 3, 2],
              is_exit = True)  # E pour exit ou end
    
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[0, 0])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R3,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[0, 0])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R0,
              room_arrival=R2,
              relative_departure_coordinates=[1, 1],
              relative_arrival_coordinates=[1, 0])
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=[1, 1],
              relative_arrival_coordinates=[1, 0])
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R3,
              room_arrival=R0,
              relative_departure_coordinates=[4/12, 1/2],
              relative_arrival_coordinates=[2/8, 1/2],
              relative_position=0.35)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R3,
              room_arrival=R0,
              relative_departure_coordinates=[5/12, 1/2],
              relative_arrival_coordinates=[3/8, 1/2],
              relative_position=0.55)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R3,
              room_arrival=R0,
              relative_departure_coordinates=[6/12, 1/2],
              relative_arrival_coordinates=[4/8, 1/2],
              relative_position=0.75)
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R3,
              room_arrival=R0,
              relative_departure_coordinates=[7/12, 1/2],
              relative_arrival_coordinates=[5/8, 1/2],
              relative_position=0.55)
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R3,
              room_arrival=R0,
              relative_departure_coordinates=[8/12, 1/2],
              relative_arrival_coordinates=[6/8, 1/2],
              relative_position=0.35)
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R0,
              room_arrival=RE,
              relative_departure_coordinates=[1/2, 0],
              relative_arrival_coordinates=[1/2, 1])
    
    l_help_txt = [
"""
"""]
    
    level = Maze(start_room_index=0, 
              exit_room_index=-1, 
              rooms_list=[R0, R1, R2, R3, RE], 
              doors_list = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9],
              fastest_solution=None,
              level_color=Levels_colors_list.BEIGE_AND_BROWN,
              name='Hypercube',
              help_txt = l_help_txt,
              keep_proportions=True)
    return level