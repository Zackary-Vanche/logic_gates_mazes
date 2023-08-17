# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 21:26:57 2023

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from random import shuffle as rd_shuffle

def level_max_cut(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S5')
    S2 = Switch(name='S2')
    S3 = Switch(name='S1')
    S4 = Switch(name='S3')
    S5 = Switch(name='S4')
    S6 = Switch(name='S6')

    Slist = [S0, S1, S2, S3, S4, S5, S6]
    
    Sa = rd_choice([S0, S1, S2, S3])
    Sb = rd_choice([S4, S5, S6])
    
    Slist_tree_0 = [[S0, S1],
                    [S1, S2],
                    [S2, S3],
                    [S4, S5],
                    [S5, S6],
                    [S6, S4],
                    [S0, S4],
                    [S0, S5],
                    [S0, S6],
                    [S1, S4],
                    [S1, S5],
                    [S1, S6],
                    [S2, S4],
                    [S2, S5],
                    [S2, S6],
                    [S3, S4],
                    [S3, S5],
                    [S3, S6],]
    
    rd_shuffle(Slist_tree_0)
    
    Slist_tree_0 = [S for c in Slist_tree_0 for S in c]
    
    def tree_list_SUM_XOR(n):
        return ['SUM'] + [Tree.tree_list_XOR(2)]*n
    
    tree_list_0 = ['SUPOREQU',
                         ['SUM',
                          tree_list_SUM_XOR(6),
                          tree_list_SUM_XOR(6),
                          tree_list_SUM_XOR(6)],
                         [None]]
    
    T0 = Tree(tree_list=['AND',
                         tree_list_0,
                         ['INF', [None], [None]]],
              name='T0',
              switches=Slist_tree_0 + [3*4, Sa, Sb],
              cut_expression=True)

    R0 = Room(name='R0',
                position=[0, 2, 4, 2],
                switches_list=Slist)
    RE = Room(name='RE',
              position=[2, 0, 2, 1],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 1/4],
                relative_arrival_coordinates=[1/2, 1/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution="S3 S4 S6 D0",
                 level_color=Levels_colors_list.FROM_HUE(hu=0.5, sa=0.3, li=0.6),
                 name='Max-cut',
                 keep_proportions=True,
                 door_window_size=400)
    
    return level