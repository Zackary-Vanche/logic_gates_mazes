# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 21:25:35 2023

@author: utilisateur
"""

from Maze import Maze
from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Levels_colors_list import Levels_colors_list

def aux_level_random_binary_tree(door_trees_list = [[i for i in range(2**6)] for j in range(7)]):

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    
    Slist = [S0, S1, S2, S3, S4, S5]
    
    def get_tree(i):
        return Tree(['IN', Tree.tree_list_BIN(len(Slist))] + [[None]]*len(door_trees_list[i]),
                     empty=True,
                     name=f'T{i}',
                     switches = Slist + door_trees_list[i],
                     cut_expression=True,
                     cut_expression_separator=')')
    
    R0 = Room(name='R0',
              position = [2, 2, 1, 1],
              switches_list = [])
    R1 = Room(name='R1',
              position = [0, 2, 1, 1],
              switches_list = [S0])
    R2 = Room(name='R2',
              position = [0, 4, 1, 1],
              switches_list = [S1])
    R3 = Room(name='R3',
              position = [2, 0, 1, 1],
              switches_list = [S2])
    R4 = Room(name='R4',
              position = [0, 0, 1, 1],
              switches_list = [S3])
    R5 = Room(name='R5',
              position = [0, 6, 1, 1],
              switches_list = [S4])
    R6 = Room(name='R6',
              position = [2, 6, 1, 1],
              switches_list = [S5])
    RE = Room(name='RE',
              position=[2, 4, 1, 1],
              is_exit=True)   # E pour exit ou end
    
    D0 = Door(two_way=True,
              tree=get_tree(0),
              room_departure=R0,
              room_arrival=RE)
    D1 = Door(two_way=True,
              tree=get_tree(1),
              room_departure=R0,
              room_arrival=R1)
    D2 = Door(two_way=True,
              tree=get_tree(2),
              room_departure=R0,
              room_arrival=R2)
    D3 = Door(two_way=True,
              tree=get_tree(3),
              room_departure=R1,
              room_arrival=R3)
    D4 = Door(two_way=True,
              tree=get_tree(4),
              room_departure=R1,
              room_arrival=R4)
    D5 = Door(two_way=True,
              tree=get_tree(5),
              room_departure=R2,
              room_arrival=R5)
    D6 = Door(two_way=True,
              tree=get_tree(6),
              room_departure=R2,
              room_arrival=R6)
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution=None,
                 level_color=Levels_colors_list.RANDOM(),
                 name='Random - Binary Tree',
                 door_window_size=1475,
                 keep_proportions=False,
                 y_separation=40,
                 border=40)
    
    return level

def level_random_binary_tree():
    # return aux_level_random_binary_tree()
    return Maze.get_random_level_from_file(aux_level_random_binary_tree)