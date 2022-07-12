# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 21:04:44 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_dominating_set():
    
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')
    S15 = Switch(name='S15')
    S16 = Switch(name='S16')
    S17 = Switch(name='S17')

    T0 = Tree(tree_list=['INF',
                           ['SUM'] + [[None]]*9,
                           [None]],
               empty=True,
               name='T0',
               switches = [S0, S1, S2, S3, S4, S5, S6, S7, S8, Switch(value=3, name='3')])
    T1 = Tree(tree_list=Tree.tree_list_OR(2),
              empty=True,
              name='T1',
              switches = [S0, S1])
    T2 = Tree(tree_list=Tree.tree_list_OR(2),
              empty=True,
              name='T2',
              switches = [S0, S2])
    T3 = Tree(tree_list=Tree.tree_list_OR(2),
              empty=True,
              name='T3',
              switches = [S0, S3])
    T4 = Tree(tree_list=Tree.tree_list_OR(2),
              empty=True,
              name='T4',
              switches = [S1, S3])
    T5 = Tree(tree_list=Tree.tree_list_OR(2),
              empty=True,
              name='T5',
              switches = [S2, S3])
    T6 = Tree(tree_list=Tree.tree_list_OR(2),
              empty=True,
              name='T6',
              switches = [S2, S4])
    T7 = Tree(tree_list=Tree.tree_list_OR(2),
              empty=True,
              name='T7',
              switches = [S2, S5])
    T8 = Tree(tree_list=Tree.tree_list_OR(2),
              empty=True,
              name='T8',
              switches = [S2, S6])
    T9 = Tree(tree_list=Tree.tree_list_OR(2),
              empty=True,
              name='T9',
              switches = [S3, S6])
    T10 = Tree(tree_list=Tree.tree_list_OR(2),
               empty=True,
               name='T10',
               switches = [S4, S5])
    T11 = Tree(tree_list=Tree.tree_list_OR(2),
               empty=True,
               name='T11',
               switches = [S4, S7])
    T12 = Tree(tree_list=Tree.tree_list_OR(2),
               empty=True,
               name='T12',
               switches = [S4, S8])
    T13 = Tree(tree_list=Tree.tree_list_OR(2),
               empty=True,
               name='T13',
               switches = [S5, S6])
    T14 = Tree(tree_list=Tree.tree_list_OR(2),
               empty=True,
               name='T14',
               switches = [S5, S8])
    T15 = Tree(tree_list=Tree.tree_list_OR(2),
               empty=True,
               name='T15',
               switches = [S7, S8])
    T16 = Tree(tree_list=Tree.tree_list_AND(9),
               empty=True,
               name='T16',
               switches=[S9, S10, S11, S12, S13, S14, S15, S16, S17])

    R0 = Room(name='R0',
              position = [0, -0.25, 3, 1.5],
              switches_list = [S0, S1, S2, S3, S4, S5, S6, S7, S8])
    R1 = Room(name='R1',
              position = [0, 1.75, 0.6, 0.6],
              switches_list = [S9])
    R2 = Room(name='R2',
              position = [0, 3, 0.6, 0.6],
              switches_list = [S10])
    R3 = Room(name='R3',
              position = [2, 1.75, 0.6, 0.6],
              switches_list = [S11])
    R4 = Room(name='R4',
              position = [2, 3, 0.6, 0.6],
              switches_list = [S12])
    R5 = Room(name='R5',
              position = [4, 0.5, 0.6, 0.6],
              switches_list = [S13])
    R6 = Room(name='R6',
              position = [4, 1.75, 0.6, 0.6],
              switches_list = [S14])
    R7 = Room(name='R7',
              position = [4, 3, 0.6, 0.6],
              switches_list = [S15])
    R8 = Room(name='R8',
              position = [5.5, -0.125, 0.6, 0.6],
              switches_list = [S16])
    R9 = Room(name='R9',
              position = [5.5, 1.125, 0.6, 0.6],
              switches_list = [S17])
    RE = Room(name='RE',
              position=[5.5, 2.375, 0.6, 0.6],
              is_exit=True)   # E pour exit ou end
    
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1/2, 0.9])
    D1 = Door(two_way=True,
              tree=T1,
              room_departure=R1,
              room_arrival=R2)
    D2 = Door(two_way=True,
              tree=T2,
              room_departure=R1,
              room_arrival=R3)
    D3 = Door(two_way=True,
              tree=T3,
              room_departure=R1,
              room_arrival=R4)
    D4 = Door(two_way=True,
              tree=T4,
              room_departure=R2,
              room_arrival=R4)
    D5 = Door(two_way=True,
              tree=T5,
              room_departure=R3,
              room_arrival=R4)
    D6 = Door(two_way=True,
              tree=T6,
              room_departure=R3,
              room_arrival=R5)
    D7 = Door(two_way=True,
              tree=T7,
              room_departure=R3,
              room_arrival=R6)
    D8 = Door(two_way=True,
              tree=T8,
              room_departure=R3,
              room_arrival=R7)
    D9 = Door(two_way=True,
              tree=T9,
              room_departure=R4,
              room_arrival=R7)
    D10 = Door(two_way=True,
               tree=T10,
               room_departure=R5,
               room_arrival=R6)
    D11 = Door(two_way=True,
               tree=T11,
               room_departure=R5,
               room_arrival=R8)
    D12 = Door(two_way=True,
               tree=T12,
               room_departure=R5,
               room_arrival=R9)
    D13 = Door(two_way=True,
               tree=T13,
               room_departure=R6,
               room_arrival=R7)
    D14 = Door(two_way=True,
               tree=T14,
               room_departure=R6,
               room_arrival=R9)
    D15 = Door(two_way=True,
               tree=T15,
               room_departure=R8,
               room_arrival=R9)
    D16 = Door(two_way=True,
               tree=T16,
               room_departure=R7,
               room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16],
                 fastest_solution='S3 S4 D0 S9 D3 D4 S10 D4 D5 D6 D10 S14 D10 D11 S16 D11 D12 S17 D12 S13 D6 S11 D5 S12 D9 S15 D16',
                 level_color=Levels_colors_list.FROM_HUE(0.6),
                 name='Dominating set',
                 door_window_size=500,
                 keep_proportions=False)

    return level

if __name__ == "__main__":
    
    level = level_dominating_set

    solutions = level().find_all_solutions(verbose=3,
                                                 stop_at_first_solution=False)
    
    print(solutions[-1])