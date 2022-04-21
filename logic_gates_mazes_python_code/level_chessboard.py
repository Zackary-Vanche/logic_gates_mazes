# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 20:00:02 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def level_chessboard():
    
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
    
    T0 = Tree(tree_list=[None],
                empty=True,
                name='T0',
                switches = [S2])
    T1 = Tree(tree_list=Tree.tree_list_or_2,
                empty=True,
                name='T1',
                switches = [S0, S2])
    T2 = Tree(tree_list=[None],
                empty=True,
                name='T2',
                switches = [S3])
    T3 = Tree(tree_list=Tree.tree_list_not,
                empty=True,
                name='T3',
                switches = [S5])
    T4 = Tree(tree_list=[None],
                empty=True,
                name='T4',
                switches = [S0])
    T5 = Tree(tree_list=Tree.tree_list_or_2,
                empty=True,
                name='T5',
                switches = [S0, S2])
    T6 = Tree(tree_list=[None],
                empty=True,
                name='T6',
                switches = [S5])
    T7 = Tree(tree_list=Tree.tree_list_not,
                empty=True,
                name='T7',
                switches = [S0])
    T8 = Tree(tree_list=[None],
                empty=True,
                name='T8',
                switches = [S6])
    T9 = Tree(tree_list=[None],
                empty=True,
                name='T9',
                switches = [S8])
    T10 = Tree(tree_list=[None],
                empty=True,
                name='T10',
                switches = [S3])
    T11 = Tree(tree_list=[None],
                empty=True,
                name='T11',
                switches = [S2])
    T12 = Tree(tree_list=[None],
                empty=True,
                name='T12',
                switches = [S8])
    T13 = Tree(tree_list=[None],
                empty=True,
                name='T13',
                switches = [S6])
    T14 = Tree(tree_list=Tree.tree_list_from_str('TTFTTT'),
                empty=True,
                name='T14',
                switches = [S1, S4, S6, S7, S10, S11])
    
    R0 = Room(name='R0',
              position = [0, 0, 9/7, 1],
              switches_list = [S0],
              surrounding_color=Color.WHITE)
    R1 = Room(name='R1',
              position = [4, 2, 9/7, 1],
              switches_list = [S1],
              surrounding_color=Color.BLACK)
    R2 = Room(name='R2',
              position = [0, 4, 9/7, 1],
              switches_list = [S2],
              surrounding_color=Color.WHITE)
    R3 = Room(name='R3',
              position = [2*9/7, 4, 9/7, 1],
              switches_list = [S3],
              surrounding_color=Color.BLACK)
    R4 = Room(name='R4',
              position = [6, 2, 9/7, 1],
              switches_list = [S4],
              surrounding_color=Color.WHITE)
    R5 = Room(name='R5',
              position = [2*9/7, 0, 9/7, 1],
              switches_list = [S5],
              surrounding_color=Color.BLACK)
    R6 = Room(name='R6',
              position = [4*9/7, 0, 9/7, 1],
              switches_list = [S6],
              surrounding_color=Color.WHITE)
    R7 = Room(name='R7',
              position = [0, 2, 9/7, 1],
              switches_list = [S7],
              surrounding_color=Color.BLACK)
    R8 = Room(name='R8',
              position = [4*9/7, 4, 9/7, 1],
              switches_list = [S8],
              surrounding_color=Color.WHITE)
    R9 = Room(name='R9',
              position = [6*9/7, 4, 9/7, 1],
              switches_list = [S9],
              surrounding_color=Color.BLACK)
    R10 = Room(name='R10',
               position = [2, 2, 9/7, 1],
               switches_list = [S10],
               surrounding_color=Color.WHITE)
    R11 = Room(name='R11',
               position = [6*9/7, 0, 9/7, 1],
               switches_list = [S11],
               surrounding_color=Color.BLACK)
    RE = Room(name='RE',
               position = [8.2, 2, 0.8, 1],
               switches_list = [],
               is_exit=True,
               surrounding_color=Color.WHITE)
    
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R5,
              surrounding_color=Color.BLACK)
    D1 = Door(two_way=True,
              tree=T1,
              room_departure=R0,
              room_arrival=R7,
              surrounding_color=Color.BLACK)
    D2 = Door(two_way=True,
              tree=T2,
              room_departure=R1,
              room_arrival=R6,
              surrounding_color=Color.BLACK)
    D3 = Door(two_way=True,
              tree=T3,
              room_departure=R1,
              room_arrival=R8,
              surrounding_color=Color.BLACK)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R2,
              room_arrival=R3,
              surrounding_color=Color.BLACK)
    D5 = Door(two_way=True,
              tree=T5,
              room_departure=R2,
              room_arrival=R7,
              surrounding_color=Color.BLACK)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R3,
              room_arrival=R8,
              surrounding_color=Color.BLACK)
    D7 = Door(two_way=True,
              tree=T7,
              room_departure=R3,
              room_arrival=R10,
              surrounding_color=Color.BLACK)
    D8 = Door(two_way=True,
              tree=T8,
              room_departure=R4,
              room_arrival=R9,
              surrounding_color=Color.BLACK)
    D9 = Door(two_way=True,
              tree=T9,
              room_departure=R4,
              room_arrival=R11,
              surrounding_color=Color.BLACK)
    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R5,
               room_arrival=R6,
               surrounding_color=Color.BLACK)
    D11 = Door(two_way=True,
               tree=T11,
               room_departure=R5,
               room_arrival=R10,
               surrounding_color=Color.BLACK)
    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R6,
               room_arrival=R11,
               surrounding_color=Color.BLACK)
    D13 = Door(two_way=False,
               tree=T13,
               room_departure=R8,
               room_arrival=R9,
               surrounding_color=Color.BLACK)
    D14 = Door(two_way=True,
               tree=T14,
               room_departure=R4,
               room_arrival=RE,
               surrounding_color=Color.BLACK,
               relative_departure_coordinates=[1, 1/2],
               relative_arrival_coordinates=[0, 1/2])
    
    l_help_txt = ["""If you remove the exit, the graph of this level is the graph of the possible moves of a knight in a 3*4 rectangle.
However, sometimes here doors are one-way only.
"""]
    
    level = Maze(start_room_index=0, 
             exit_room_index=-1, 
             rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, RE], 
             doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14], 
             fastest_solution="S0 D1 D5 S2 D5 S7 D1 S0 D0 D11 D7 S3 D7 S10 D11 D10 D2 D3 S8 D3 S1 D2 D12 S11 D9 S4 D14",
             level_color=Levels_colors_list.YELLOW_AND_GREY,
             uniform_surrounding_colors=False,
             name='Chessboard',
             help_txt=l_help_txt,
             door_window_size=500,
             keep_proportions=False,
             line_size=4)
    
    return level

if __name__ == "__main__":
    
    level_chessboard().find_all_solutions(verbose=2)