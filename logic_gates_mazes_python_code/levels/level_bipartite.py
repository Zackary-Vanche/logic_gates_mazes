# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 08:42:08 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def level_bipartite():
    
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
    
    T0 = Tree(tree_list=[None],
              empty=True,
              name='T0',
              switches = [S0])
    T1 = Tree(tree_list=Tree.tree_list_xor,
              empty=True,
              name='T1',
              switches = [S1, S4])
    T2 = Tree(tree_list=Tree.tree_list_xor,
              empty=True,
              name='T2',
              switches = [S1, S5])
    T3 = Tree(tree_list=Tree.tree_list_xor,
              empty=True,
              name='T3',
              switches = [S1, S6])
    T4 = Tree(tree_list=Tree.tree_list_xor,
              empty=True,
              name='T4',
              switches = [S2, S4])
    T5 = Tree(tree_list=Tree.tree_list_xor,
              empty=True,
              name='T5',
              switches = [S2, S5])
    T6 = Tree(tree_list=Tree.tree_list_xor,
              empty=True,
              name='T6',
              switches = [S2, S6])
    T7 = Tree(tree_list=Tree.tree_list_xor,
              empty=True,
              name='T7',
              switches = [S3, S4])
    T8 = Tree(tree_list=Tree.tree_list_xor,
              empty=True,
              name='T8',
              switches = [S3, S5])
    T9 = Tree(tree_list=Tree.tree_list_xor,
              empty=True,
              name='T9',
              switches = [S3, S6])
    T10 = Tree(tree_list=Tree.tree_list_from_str('FFFFFF'),
              empty=True,
              name='T10',
              switches = [S1, S2, S3, S4, S5, S6])
    T11 = Tree(tree_list=Tree.tree_list_from_str('TTTTTT'),
              empty=True,
              name='T11',
              switches = [S7, S8, S9, S10, S11, S12])
    
    position_R0 = [10, 0, 2, 2]
    position_R1 = [6, 0, 2, 2]
    position_R2 = [0, 4, 2, 2]
    position_R3 = [6, 8, 2, 2]
    position_R4 = [0, 0, 2, 2]
    position_R5 = [6, 4, 2, 2]
    position_R6 = [0, 8, 2, 2]
    position_R7 = [10, 8, 2, 2]
    position_RE = [10, 4, 2, 2]
    
    R0 = Room(name='R0',
              position=position_R0,
              switches_list=[S0],
              surrounding_color=Color.WHITE)
    R1 = Room(name='R1',
              position=position_R1,
              switches_list=[S1, S7],
              surrounding_color=Color.TOTAL_RED)
    R2 = Room(name='R2',
              position=position_R2,
              switches_list=[S2, S8],
              surrounding_color=Color.TOTAL_GREEN)
    R3 = Room(name='R3',
              position=position_R3,
              switches_list=[S3, S9],
              surrounding_color=Color.TOTAL_BLUE)
    R4 = Room(name='R4',
              position=position_R4,
              switches_list=[S4, S10],
              surrounding_color=Color.TOTAL_RED)
    R5 = Room(name='R5',
              position=position_R5,
              switches_list=[S5, S11],
              surrounding_color=Color.TOTAL_GREEN)
    R6 = Room(name='R6',
              position=position_R6,
              switches_list=[S6, S12],
              surrounding_color=Color.TOTAL_BLUE)
    
    R7 = Room(name='R7',
              position=position_R7,
              switches_list=[],
              surrounding_color=Color.WHITE)
    RE = Room(name='RE',
              position=position_RE,
              is_exit=True)   # E pour exit ou end
    
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              surrounding_color=Color.WHITE)
    
    D1 = Door(two_way=True,
                tree=T1,
                room_departure=R1,
                room_arrival=R4,
                surrounding_color=Color.TOTAL_RED)
    D2 = Door(two_way=True,
                tree=T2,
                room_departure=R1,
                room_arrival=R5,
                surrounding_color=Color.TOTAL_YELLOW)
    D3 = Door(two_way=True,
                tree=T3,
                room_departure=R1,
                room_arrival=R6,
                relative_position=1/3,
                surrounding_color=Color.TOTAL_MAGENTA)

    D4 = Door(two_way=True,
                tree=T4,
                room_departure=R2,
                room_arrival=R4,
                surrounding_color=Color.TOTAL_YELLOW)
    D5 = Door(two_way=True,
                tree=T5,
                room_departure=R2,
                room_arrival=R5,
                relative_position=1/3,
                surrounding_color=Color.TOTAL_GREEN)
    D6 = Door(two_way=True,
                tree=T6,
                room_departure=R2,
                room_arrival=R6,
                surrounding_color=Color.TOTAL_CYAN)

    D7 = Door(two_way=True,
                tree=T7,
                room_departure=R3,
                room_arrival=R4,
                relative_position=1/3,
                surrounding_color=Color.TOTAL_MAGENTA)
    D8 = Door(two_way=True,
                tree=T8,
                room_departure=R3,
                room_arrival=R5,
                surrounding_color=Color.TOTAL_CYAN)
    D9 = Door(two_way=True,
                tree=T9,
                room_departure=R3,
                room_arrival=R6,
                surrounding_color=Color.TOTAL_BLUE)

    D10 = Door(two_way=False,
                tree=T10,
                room_departure=R3,
                room_arrival=R7,
                surrounding_color=Color.WHITE)
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R7,
               room_arrival=RE,
               surrounding_color=Color.WHITE)
    
    l_help_txt = ["""This level has several solutions.
"""]

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11],
                 fastest_solution="S0 D0 S1 D1 S4 D4 S8 D4 D7 S3 D8 S11 D2 D3 S12 D3 S1 S7 D1 S4 S10 D7 S3 S9 D10 D11",
                 level_color=Levels_colors_list.BLACK_AND_GREY_WHITE_CONTOUR,
                 uniform_surrounding_colors=False,
                 name='Bipartite',
                 help_txt=l_help_txt,
                 door_window_size=450,
                 border=100,
                 keep_proportions=False)

    return level

if __name__ == "__main__":
    
    solutions = level_bipartite().find_all_solutions(verbose=2, stop_at_first_solution=False)
    level_bipartite().try_solution(solutions[-1],
                                   verbose=3,
                                   allow_all_doors=True,
                                   allow_all_switches=True)
    
    assert len(solutions) == 1