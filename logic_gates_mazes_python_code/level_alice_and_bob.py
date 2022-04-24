# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 15:20:23 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_alice_and_bob():
    
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    
    T0 = Tree(tree_list=Tree.tree_list_xnor,
              empty=True,
              name='T0',
              switches = [S3, S4])
    T1 = Tree(tree_list=Tree.tree_list_xor,
              empty=True,
              name='T1',
              switches = [S3, S4])
    T2 = Tree(tree_list=[None],
                empty=True,
                name='T2',
                switches = [S0])
    T3 = Tree(tree_list=Tree.tree_list_not,
                empty=True,
                name='T3',
                switches = [S0])
    T4 = Tree(tree_list=Tree.tree_list_or_2,
                empty=True,
                name='T4',
                switches = [S1, S2])
    T5 = Tree(tree_list=Tree.tree_list_or_2,
                empty=True,
                name='T5',
                switches = [S1, S2])
    T6 = Tree(tree_list=Tree.tree_list_from_str("FFTF"),
                         #  ['AND',
                         # Tree.tree_list_from_str('FF'),
                         # Tree.tree_list_xor],
                empty=True,
                name='T6',
                switches = [S1, S2, S3, S4])
    
    R0 = Room(name='R0',
                position = [2, 2, 1, 1],
                switches_list = [S0])
    R1 = Room(name='R1',
                position = [0, 0, 1, 1],
                switches_list = [S1])
    R2 = Room(name='R2',
                position = [4, 2, 1, 1],
                switches_list = [S2])
    R3 = Room(name='R3',
                position = [0, 2, 1, 1],
                switches_list = [S3])
    R4 = Room(name='R4',
                position = [4, 0, 1, 1],
                switches_list = [S4])
    RE = Room(name='RE',
              position=[2, 0, 1, 1],
              is_exit=True)   # E pour exit ou end
    
    D0 = Door(two_way=False,
                tree=T0,
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=False,
                tree=T1,
                room_departure=R0,
                room_arrival=R2)
    D2 = Door(two_way=False,
                tree=T2,
                room_departure=R1,
                room_arrival=R3)
    D3 = Door(two_way=False,
                tree=T3,
                room_departure=R2,
                room_arrival=R4)
    D4 = Door(two_way=False,
                tree=T4,
                room_departure=R3,
                room_arrival=R0)
    D5 = Door(two_way=False,
                tree=T5,
                room_departure=R4,
                room_arrival=R0)
    D6 = Door(two_way=False,
                tree=T6,
                room_departure=R4,
                room_arrival=RE)
    
    l_help_txt = [
"""Alice wants to send a package to Bob.
"""]
    
    level = Maze(start_room_index=0, 
         exit_room_index=-1, 
         rooms_list=[R0, R1, R2, R3, R4, RE], 
         doors_list = [D0, D1, D2, D3, D4, D5, D6], 
         fastest_solution="S0 D0 S1 D2 S3 D4 S0 D1 D3 S4 D5 S0 D0 D2 S3 D4 S0 D1 S2 D3 S4 D5 S0 D0 S1 D2 S3 D4 S0 D1 S2 D3 D6",
         level_color=Levels_colors_list.WHITE,
         name='Alice and Bob',
         help_txt = l_help_txt,
         door_window_size = 550)
    
    return level

if __name__ == '__main__':
    
    solutions = level_alice_and_bob().find_all_solutions(verbose=2)
    
    for sol in solutions :
        level_alice_and_bob().try_solution(sol,
                                           allow_all_doors=True,
                                           allow_all_switches=True,
                                           verbose=3)