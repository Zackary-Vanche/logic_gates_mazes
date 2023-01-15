# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 14:09:41 2023

@author: utilisateur
"""

from Maze import Maze
from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Levels_colors_list import Levels_colors_list

def aux_level_random_blind_alley(door_trees_list = [[i for i in range(2**12)] for j in range(4)],
                                 exit_number=None): # exit_number isn't usde but should remain as an argument

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8,]
    
    def get_tree(i):
        i_min = [0, 0, 3][i]
        i_max = [3, 6, 9][i]
        Slist_i = Slist[i_min:i_max]
        tree_list = []
        for j in door_trees_list[i]:
            str_j = format(j, f'0{len(Slist)}b')[::-1]
            bin_j = 0
            for k in range(i_min, i_max):
                bin_j += int(str_j[k]) * 2**(k-i_min)
            if bin_j not in tree_list:
                tree_list.append(bin_j)
        return Tree(['IN', Tree.tree_list_BIN(len(Slist_i))] + [[None]]*len(tree_list),
                     empty=True,
                     name=f'T{i}',
                     switches = Slist_i + tree_list,
                     cut_expression=True,
                     cut_expression_separator=')',
                     random_switches_bin_list=Slist_i)
    
    ex = 2
    ey = 0.5
    
    R0 = Room(name='R0',
              position = [0, 4, ex, ey],
              switches_list = [S0, S1, S2])
    R1 = Room(name='R1',
              position = [0, 3, ex, ey],
              switches_list = [S3, S4, S5])
    R2 = Room(name='R2',
              position = [0, 2, ex, ey],
              switches_list = [S6, S7, S8])
    RE = Room(name='RE',
              position=[0, 1, ex, ey],
              is_exit=True)   # E pour exit ou end
    
    D0 = Door(two_way=0,
                tree=get_tree(0),
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=0,
                tree=get_tree(1),
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=0,
                tree=get_tree(2),
                room_departure=R2,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2] + [RE],
                 doors_list=[D0, D1, D2],
                 fastest_solution=None,
                 level_color=Levels_colors_list.RANDOM(),
                 name='Random - Blind alley',
                 door_window_size=1525,
                 keep_proportions=False,
                 y_separation=40,
                 border=40,
                 random=True)
    
    return level

def level_random_blind_alley():
    # return aux_level_random_blind_alley()
    return Maze.get_random_level_from_file(aux_level_random_blind_alley)