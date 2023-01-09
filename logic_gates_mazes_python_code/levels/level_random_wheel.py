# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 21:43:10 2023

@author: utilisateur
"""

from Maze import Maze
from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Levels_colors_list import Levels_colors_list

n_switches = 5
n_doors = 11

def aux_level_random_wheel(door_trees_list = [[i for i in range(2**n_switches)] for j in range(n_doors)]):

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    
    Slist = [S0, S1, S2, S3, S4]
    
    assert len(Slist) == n_switches
    
    def get_tree(i):
        return Tree(['IN', Tree.tree_list_BIN(len(Slist))] + [[None]]*len(door_trees_list[i]),
                     empty=True,
                     name=f'T{i}',
                     switches = Slist + door_trees_list[i],
                     cut_expression=True)
    
    position_R0 = [4, 7, 1, 1]
    position_R1 = [4, 3, 1, 1]
    position_R2 = [8, 6, 1, 1]
    position_R3 = [6, 10, 1, 1]
    position_R4 = [2, 10, 1, 1]
    position_R5 = [0, 6, 1, 1]
    position_RE = [7.5, 3.25, 1, 1]
    
    R0 = Room(name='R0',
              position = position_R0,
              switches_list = [])
    R1 = Room(name='R1',
              position = position_R1,
              switches_list = [S0])
    R2 = Room(name='R2',
              position = position_R2,
              switches_list = [S1])
    R3 = Room(name='R3',
              position = position_R3,
              switches_list = [S2])
    R4 = Room(name='R4',
              position = position_R4,
              switches_list = [S3])
    R5 = Room(name='R5',
              position = position_R5,
              switches_list = [S4])
    RE = Room(name='RE',
              position=position_RE,
              is_exit=True)   # E pour exit ou end
    
    D0 = Door(two_way=True,
              tree=get_tree(0),
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=True,
              tree=get_tree(1),
              room_departure=R0,
              room_arrival=R2)
    D2 = Door(two_way=True,
              tree=get_tree(2),
              room_departure=R0,
              room_arrival=R3)
    D3 = Door(two_way=True,
              tree=get_tree(3),
              room_departure=R0,
              room_arrival=R4)
    D4 = Door(two_way=True,
              tree=get_tree(4),
              room_departure=R0,
              room_arrival=R5)
    D5 = Door(two_way=True,
              tree=get_tree(5),
              room_departure=R1,
              room_arrival=R2)
    D6 = Door(two_way=True,
              tree=get_tree(6),
              room_departure=R2,
              room_arrival=R3)
    D7 = Door(two_way=True,
              tree=get_tree(7),
              room_departure=R3,
              room_arrival=R4)
    D8 = Door(two_way=True,
              tree=get_tree(8),
              room_departure=R4,
              room_arrival=R5)
    D9 = Door(two_way=True,
              tree=get_tree(9),
              room_departure=R5,
              room_arrival=R1)
    D10 = Door(two_way=True,
              tree=get_tree(10),
              room_departure=R0,
              room_arrival=RE,
              relative_position=0.3)
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10],
                 fastest_solution=None,
                 level_color=Levels_colors_list.RANDOM(),
                 name='Random - Wheel',
                 door_window_size=850,
                 keep_proportions=True,
                 y_separation=40,
                 border=40)
    
    return level

def level_random_wheel():
    # return aux_level_random_wheel()
    return Maze.get_random_level_from_file(aux_level_random_wheel)