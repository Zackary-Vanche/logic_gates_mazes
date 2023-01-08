# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 09:30:00 2023

@author: utilisateur
"""

from Maze import Maze
from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Levels_colors_list import Levels_colors_list

def aux_level_random_K2(door_trees_list = [[i for i in range(2**6)] for j in range(3)]):

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
              position = [0, 0, 3, 1],
              switches_list = [S0, S1, S2])
    R1 = Room(name='R1',
              position = [0, 2, 3, 1],
              switches_list = [S3, S4, S5])
    RE = Room(name='RE',
              position=[0, 3.5, 3, 1/2],
              is_exit=True)   # E pour exit ou end
    
    rp = 0.4
    
    D0 = Door(two_way=False,
              tree=get_tree(0),
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp)
    D1 = Door(two_way=False,
              tree=get_tree(1),
              room_departure=R1,
              room_arrival=R0,
              relative_position=rp)
    D2 = Door(two_way=False,
              tree=get_tree(2),
              room_departure=R1,
              room_arrival=RE,
              relative_departure_coordinates=[1/2, 1],
              relative_arrival_coordinates=[1/2, 0],
              relative_position=1/2)
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1] + [RE],
                 doors_list=[D0, D1, D2],
                 fastest_solution=None,
                 level_color=Levels_colors_list.RANDOM(),
                 name='Random - K2',
                 door_window_size=1475,
                 keep_proportions=False,
                 y_separation=40,
                 border=40)
    
    return level

def level_random_K2():
    # return aux_level_random_K2()
    return Maze.get_random_level_from_file(aux_level_random_K2)