# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 15:29:33 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_fractal():
    
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
    
    T0 = Tree(tree_list=Tree.tree_list_or_2,
              empty=True,
              name='T0',
              switches = [S0, S8])
    T1 = Tree(tree_list=[None],
              empty=True,
              name='T1',
              switches = [S14])
    T2 = Tree(tree_list=['AND', [None], Tree.tree_list_xnor],
              empty=True,
              name='T2',
              switches = [S0, S1, S2])
    T3 = Tree(tree_list=Tree.tree_list_from_str('TTF'),
              empty=True,
              name='T3',
              switches = [S0, S1, S2])
    T4 = Tree(tree_list=Tree.tree_list_from_str('TT'),
              empty=True,
              name='T4',
              switches = [S0, S1])
    T5 = Tree(tree_list=['AND', [None], Tree.tree_list_xor],
              empty=True,
              name='T5',
              switches = [S0, S3, S4])
    T6 = Tree(tree_list=Tree.tree_list_from_str('FT'),
              empty=True,
              name='T6',
              switches = [S1, S2])
    T7 = Tree(tree_list=[None],
              empty=True,
              name='T7',
              switches = [S10])
    T8 = Tree(tree_list=['AND', [None], Tree.tree_list_nor],
              empty=True,
              name='T8',
              switches = [S0, S5, S6])
    T9 = Tree(tree_list=Tree.tree_list_from_str('TT'),
              empty=True,
              name='T9',
              switches = [S3, S4])
    T10 = Tree(tree_list=[None],
              empty=True,
              name='T10',
              switches = [S7])
    T11 = Tree(tree_list=[None],
              empty=True,
              name='T11',
              switches = [S7])
    T12 = Tree(tree_list=Tree.tree_list_from_str('FF'),
              empty=True,
              name='T12',
              switches = [S3, S4])
    T13 = Tree(tree_list=Tree.tree_list_from_str('TT'),
              empty=True,
              name='T13',
              switches = [S9, S1])
    T14 = Tree(tree_list=[None],
              empty=True,
              name='T14',
              switches = [S9])
    T15 = Tree(tree_list=[None],
              empty=True,
              name='T15',
              switches = [S5])
    T16 = Tree(tree_list=[None],
              empty=True,
              name='T16',
              switches = [S11])
    T17 = Tree(tree_list=[None],
              empty=True,
              name='T17',
              switches = [S11])
    T18 = Tree(tree_list=[None],
              empty=True,
              name='T18',
              switches = [S8])
    T19 = Tree(tree_list=[None],
              empty=True,
              name='T19',
              switches = [S13])
    T20 = Tree(tree_list=[None],
              empty=True,
              name='T20',
              switches = [S13])
    T21 = Tree(tree_list=Tree.tree_list_from_str('FTTTTTFT'),
              empty=True,
              name='T21',
              switches = [S0, S1, S2, S3, S4, S6, S10, S12])
    T22 = Tree(tree_list=Tree.tree_list_from_str('FTTTTTFT'),
              empty=True,
              name='T22',
              switches = [S0, S1, S2, S3, S4, S6, S8, S10])
    
    R0 = Room(name='R0',
              position = [6, 10, 2, 2],
              switches_list = [S0])
    R1 = Room(name='R1',
              position = [5, 4, 1, 4],
              switches_list = [S1])
    R2 = Room(name='R2',
              position = [8, 4, 1, 4],
              switches_list = [S2])
    R3 = Room(name='R3',
              position = [0, 7, 3, 1],
              switches_list = [S3])
    R4 = Room(name='R4',
              position = [0, 4, 3, 1],
              switches_list = [S4])
    R5 = Room(name='R5',
              position = [11, 7, 3, 1],
              switches_list = [S5])
    R6 = Room(name='R6',
              position = [11, 4, 3, 1],
              switches_list = [S6])
    R7 = Room(name='R7',
              position = [3, 10, 1, 2],
              switches_list = [S7])
    R8 = Room(name='R8',
              position = [0, 10, 1, 2],
              switches_list = [S8])
    R9 = Room(name='R9',
              position = [3, 0, 1, 2],
              switches_list = [S9])
    R10 = Room(name='R10',
              position = [0, 0, 1, 2],
              switches_list = [S10])
    R11 = Room(name='R11',
              position = [10, 10, 1, 2],
              switches_list = [S11])
    R12 = Room(name='R12',
              position = [13, 10, 1, 2],
              switches_list = [S12])
    R13 = Room(name='R13',
              position = [10, 0, 1, 2],
              switches_list = [S13])
    R14 = Room(name='R14',
              position = [13, 0, 1, 2],
              switches_list = [S14])
    RE = Room(name='RE', position = [5.5, 0, 3, 2], is_exit=True)  # E pour exit ou end
    
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates = [1/4, 1/4], 
              relative_arrival_coordinates = [1/2, 7/8])
    D1 = Door(two_way=False,
                tree=T1,
                room_departure=R2,
                room_arrival=R0,
                relative_departure_coordinates = [1/2, 7/8], 
                relative_arrival_coordinates = [3/4, 1/4])
    D2 = Door(two_way=True,
                tree=T2,
                room_departure=R1,
                room_arrival=R2)

    D3 = Door(two_way=False,
                tree=T3,
                room_departure=R1,
                room_arrival=R3,
                relative_departure_coordinates = [1/2, 1/2], 
                relative_arrival_coordinates = [5/6, 1/2])
    D4 = Door(two_way=False,
                tree=T4,
                room_departure=R4,
                room_arrival=R1,
                relative_departure_coordinates = [5/6, 1/2], 
                relative_arrival_coordinates = [1/2, 1/2])
    D5 = Door(two_way=True,
                tree=T5,
                room_departure=R3,
                room_arrival=R4)

    D6 = Door(two_way=False,
                tree=T6,
                room_departure=R2,
                room_arrival=R5,
                relative_departure_coordinates = [1/2, 1/2], 
                relative_arrival_coordinates = [1/6, 1/2])
    D7 = Door(two_way=False,
                tree=T7,
                room_departure=R6,
                room_arrival=R2,
                relative_departure_coordinates = [1/6, 1/2], 
                relative_arrival_coordinates = [1/2, 1/2])
    D8 = Door(two_way=True,
                tree=T8,
                room_departure=R5,
                room_arrival=R6)

    D9 = Door(two_way=False,
                tree=T9,
                room_departure=R3,
                room_arrival=R7, 
                relative_arrival_coordinates = [1/2, 1/4])
    D10 = Door(two_way=False,
                tree=T10,
                room_departure=R8,
                room_arrival=R3,
                relative_departure_coordinates = [1/2, 1/4])
    D11 = Door(two_way=True,
                tree=T11,
                room_departure=R7,
                room_arrival=R8)

    D12 = Door(two_way=False,
                tree=T12,
                room_departure=R4,
                room_arrival=R9, 
                relative_arrival_coordinates = [1/2, 3/4])
    D13 = Door(two_way=False,
                tree=T13,
                room_departure=R10,
                room_arrival=R4,
                relative_departure_coordinates = [1/2, 3/4])
    D14 = Door(two_way=True,
                tree=T14,
                room_departure=R9,
                room_arrival=R10)

    D15 = Door(two_way=False,
                tree=T15,
                room_departure=R5,
                room_arrival=R11, 
                relative_arrival_coordinates = [1/2, 1/4])
    D16 = Door(two_way=False,
                tree=T16,
                room_departure=R12,
                room_arrival=R5,
                relative_departure_coordinates = [1/2, 1/4])
    D17 = Door(two_way=True,
                tree=T17,
                room_departure=R11,
                room_arrival=R12)

    D18 = Door(two_way=False,
                tree=T18,
                room_departure=R6,
                room_arrival=R13, 
                relative_arrival_coordinates = [1/2, 3/4])
    D19 = Door(two_way=False,
                tree=T19,
                room_departure=R14,
                room_arrival=R6,
                relative_departure_coordinates = [1/2, 3/4])
    D20 = Door(two_way=True,
                tree=T20,
                room_departure=R13,
                room_arrival=R14)

    D21 = Door(two_way=False,
                tree=T21,
                room_departure=R1,
                room_arrival=RE,
                relative_departure_coordinates = [1/2, 1/4], 
                relative_arrival_coordinates = [1/2, 3/4])
    D22 = Door(two_way=False,
                tree=T22,
                room_departure=R2,
                room_arrival=RE,
                relative_departure_coordinates = [1/2, 1/4], 
                relative_arrival_coordinates = [1/2, 3/4])
    
    l_help_txt = ["""As you see, several doors lead to the exit.
There is only one that can be opened."""]
    
    level = Maze(start_room_index=0, 
             exit_room_index=-1, 
             rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, RE], 
             doors_list = [D0, D1, D2,
                           D3, D4, D5,
                           D6, D7, D8,
                           D9, D10, D11,
                           D12, D13, D14,
                           D15, D16, D17,
                           D18, D19, D20,
                           D21, D22], 
             fastest_solution='S0 D0 S1 D3 S3 D5 S4 D4 D3 D9 S7 D11 S8 D10 S3 D5 S4 D12 S9 D14 S10 D13 S4 D4 S1 D2 S2 D6 S5 D15 S11 D17 S12 D16 S5 D8 D18 S13 D20 S14 D19 S6 D7 S2 D2 S1 D3 D5 S4 D12 D14 S10 D13 D4 D3 S3 D5 S4 D4 S1 D2 S2 D1 S0 D0 S1 D21',
             level_color=Levels_colors_list.BEIGE,
             name='Fractal',
             help_txt = l_help_txt,
             door_window_size=500,
             y_separation=50,
             border = 30,
             keep_proportions = False)
    
    return level

if __name__ == "__main__":
    
    solutions = level_fractal().find_all_solutions(verbose=0, stop_at_first_solution=False)
    
    assert len(solutions) == 1
    