# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 21:32:22 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_naturals():
    
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    
    tree_list_a_minus_b = ['SUM',
                               [None],
                               ['MINUS', [None]]]
    
    tree_list_0 = ['PROD',
                       [None],
                       tree_list_a_minus_b]
    
    tree_list_1 = ['SUM'] + [tree_list_0]*4
    
    tree_list_2 = ['ABS', tree_list_1]
    
    tree_list_3 = ['INF', tree_list_2, [None]]
    
    T0 = Tree(tree_list=tree_list_3,
              empty=True,
              name='T0',
              switches = [Switch(value=1, name='1'), S0, S1,
                          Switch(value=2, name='2'), S2, S3,
                          Switch(value=4, name='4'), S4, S5,
                          Switch(value=8, name='8'), S6, S7,
                          Switch(value=2, name='2')])
    T1 = Tree(tree_list=Tree.tree_list_and_8,
              empty=True,
              name='T1',
              switches = [S0, S1, S2, S3, S4, S5, S6, S7])
    
    R0 = Room(name='R0',
              position = [0, 0, 4, 1],
              switches_list = [S0, S2, S4, S6])
    R1 = Room(name='R1',
              position = [0, 4, 4, 1],
              switches_list = [S1, S3, S5, S7])
    RE = Room(name='RE',
              position=[2, 2, 2, 1],
              is_exit=True)   # E pour exit ou end
    
    D0 = Door(two_way=True,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[0, 0])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=RE,
              relative_departure_coordinates=[3/4, 0],
              relative_arrival_coordinates=[1/2, 1])

    level = Maze(start_room_index=0, 
             exit_room_index=-1, 
             rooms_list=[R0, R1, RE], 
             doors_list=[D0, D1], 
             fastest_solution='S0 D0 S3 D0 S2 D0 S3 S5 D0 S2 S4 D0 S3 D0 S2 D0 S3 S5 S7 D0 S2 S4 S6 D0 S3 D0 S2 D0 S3 S5 D0 S2 S4 D0 S3 D0 S2 D0 S1 D1',
             level_color=Levels_colors_list.FROM_HUE(0),
             name='Naturals',
             door_window_size = 800,
             keep_proportions = True)
    
    return level