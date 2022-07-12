# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 21:09:33 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_independent_set():
    
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    
    tree_list_4 = ['AND'] + [Tree.tree_list_NAND(2)]*4
    tree_list_6 = ['AND'] + [Tree.tree_list_NAND(2)]*6
    
    T0 = Tree(tree_list=tree_list_6,
              empty=True,
              name='T0',
              switches = [S0, S1, S1, S2,
                          S3, S4, S4, S5,
                          S6, S7, S7, S8])
    T1 = Tree(tree_list=tree_list_6,
              empty=True,
              name='T1',
              switches = [S0, S3, S3, S6,
                          S1, S4, S4, S7,
                          S2, S5, S5, S8])
    T2 = Tree(tree_list=tree_list_4,
              empty=True,
              name='T2',
              switches = [S1, S5,
                          S0, S4, S4, S8,
                          S3, S7])
    T3 = Tree(tree_list=tree_list_4,
              empty=True,
              name='T3',
              switches = [S1, S3,
                          S2, S4, S4, S6,
                          S5, S7])
    T4 = Tree(tree_list=['SUP',
                           ['SUM'] + [[None]]*9,
                           [None]],
              empty=True,
              name='T4',
              switches = [S0, S1, S2, S3, S4, S5, S6, S7, S8, Switch(value=3, name='3')])
    
    e = 2.5
    p = 2/3

    R0 = Room(name='R0',
              position = [0, e, 4*e+1.4, 1],
              switches_list = [S0, S1, S2, S3, S4, S5, S6, S7, S8])
    R1 = Room(name='R1',
              position = [0, 0, 1, 1],
              switches_list = [])
    R2 = Room(name='R2',
              position = [e, -3*p, 1, 1],
              switches_list = [])
    R3 = Room(name='R3',
              position = [2*e, -4*p, 1, 1],
              switches_list = [])
    R4 = Room(name='R4',
              position = [3*e, -3*p, 1, 1],
              switches_list = [])
    RE = Room(name='RE',
              position=[4*e, 0, 1.4, 1.4],
              is_exit=True)   # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[0.5/(4*e+1.4), 1/2])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=R4)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R4,
              room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4],
                 fastest_solution='S0 S2 S6 S8 D0 D1 D2 D3 D4',
                 level_color=Levels_colors_list.FROM_HUE(0.2),
                 name='Independent set',
                 door_window_size=600,
                 keep_proportions=True)

    return level

if __name__ == "__main__":
    
    level = level_independent_set

    solutions = level().find_all_solutions(verbose=3,
                                           stop_at_first_solution=False)
    
    print(solutions[-1])