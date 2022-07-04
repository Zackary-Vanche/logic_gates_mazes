# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 12:07:53 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_tesseract():
    
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    SN = Switch(name='1', value=1)
    
    T0 = Tree(tree_list=[None],
                empty=True,
                name='T0',
                switches = [SN])
    T1 = Tree(tree_list=[None],
                empty=True,
                name='T1',
                switches = [SN])
    T2 = Tree(tree_list=[None],
                empty=True,
                name='T2',
                switches = [SN])
    T3 = Tree(tree_list=[None],
                empty=True,
                name='T3',
                switches = [SN])
    T4 = Tree(tree_list=[None],
                empty=True,
                name='T4',
                switches = [SN])
    T5 = Tree(tree_list=[None],
                empty=True,
                name='T5',
                switches = [SN])
    T6 = Tree(tree_list=[None],
                empty=True,
                name='T6',
                switches = [SN])
    T7 = Tree(tree_list=[None],
                empty=True,
                name='T7',
                switches = [SN])
    T8 = Tree(tree_list=[None],
                empty=True,
                name='T8',
                switches = [SN])
    T9 = Tree(tree_list=[None],
                empty=True,
                name='T9',
                switches = [SN])
    T10 = Tree(tree_list=[None],
                empty=True,
                name='T10',
                switches = [SN])
    T11 = Tree(tree_list=[None],
                empty=True,
                name='T11',
                switches = [SN])
    T12 = Tree(tree_list=[None],
                empty=True,
                name='T12',
                switches = [SN])
    T13 = Tree(tree_list=[None],
                empty=True,
                name='T13',
                switches = [SN])
    T14 = Tree(tree_list=[None],
                empty=True,
                name='T14',
                switches = [SN])
    T15 = Tree(tree_list=[None],
                empty=True,
                name='T15',
                switches = [SN])
    T16 = Tree(tree_list=['NOR',
                         ['AND',
                         Tree.tree_list_not,
                         Tree.tree_list_from_str('TTF FT')],
                         ['AND', [None], Tree.tree_list_xor]],
                empty=True,
                name='T16',
                switches = [S0, S1, S2, S3, S2, S3, S0, S2, S3])
    T17 = Tree(tree_list=['NOR',
                          ['AND',
                          Tree.tree_list_not,
                          Tree.tree_list_from_str('TTF FT')],
                          ['AND', [None], Tree.tree_list_xor]],
                empty=True,
                name='T17',
                switches = [S4, S5, S6, S7, S6, S7, S4, S6, S7])
    T18 = Tree(tree_list=['AND',
                         Tree.tree_list_xnor,
                         Tree.tree_list_xnor,
                         Tree.tree_list_xnor],
                empty=True,
                name='T18',
                switches = [S1, S5, S2, S6, S3, S7])
    T19 = Tree(tree_list=['AND',
                         Tree.tree_list_xnor,
                         Tree.tree_list_xnor,
                         Tree.tree_list_xnor],
                empty=True,
                name='T19',
                switches = [S0, S4, S2, S6, S3, S7])
    T20 = Tree(tree_list=['AND',
                         Tree.tree_list_xnor,
                         Tree.tree_list_xnor,
                         Tree.tree_list_xnor],
                empty=True,
                name='T20',
                switches = [S0, S4, S1, S5, S3, S7])
    T21 = Tree(tree_list=['AND',
                         Tree.tree_list_xnor,
                         Tree.tree_list_xnor,
                         Tree.tree_list_xnor],
                empty=True,
                name='T21',
                switches = [S0, S4, S1, S5, S2, S6])
    T22 = Tree(tree_list=Tree.tree_list_from_str('T'*8),
                empty=True,
                name='T22',
                switches = [S0, S1, S2, S3, S4, S5, S6, S7])
    
    cx = 1
    cy = 1.5
    y0 = 6
    px = 2.25
    x1 = 2.25
    x2 = 9.75#2+9-x1+cx
    
    R0 = Room(name='R0',
              position = [2.5, 3.5, 8, 0.5],
              switches_list = [])
    R1 = Room(name='R1',
              position = [x1, y0, cx, cy],
              switches_list = [S0])
    R2 = Room(name='R2',
              position = [x1-px, y0+0.25, cx, cy],
              switches_list = [S1])
    R3 = Room(name='R3',
              position = [x1-1.75*px, y0+0.5, cx, cy],
              switches_list = [S2])
    R4 = Room(name='R4',
              position = [x1-2.3*px, y0+0.75, cx, cy],
              switches_list = [S3])
    R5 = Room(name='R5',
              position = [x2, y0, cx, cy],
              switches_list = [S4])
    R6 = Room(name='R6',
              position = [x2+px, y0+0.25, cx, cy],
              switches_list = [S5])
    R7 = Room(name='R7',
              position = [x2+1.75*px, y0+0.5, cx, cy],
              switches_list = [S6])
    R8 = Room(name='R8',
              position = [x2+2.3*px, y0+0.75, cx, cy],
              switches_list = [S7])
    R9 = Room(name='R9',
              position = [0, 10, 3.5, 0.5],
              switches_list = [])
    R10 = Room(name='R10',
               position = [9.5, 10, 3.5, 0.5],
               switches_list = [])
    R11 = Room(name='R11',
               position = [4, 11.25, 5, 0.5],
               switches_list = [])
    RE = Room(name='RE',
              position = [5.75, 5, 1.5, 1],
              is_exit = True)  # E pour exit ou end
    
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1/9, 1],
              relative_arrival_coordinates=[1, 0],
              relative_position=0.75)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R0,
              room_arrival=R2,
              relative_departure_coordinates=[2/3/9, 1],
              relative_arrival_coordinates=[2/3, 0],
              relative_position=0.4)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R0,
              room_arrival=R3,
              relative_departure_coordinates=[1/3/9, 1],
              relative_arrival_coordinates=[1/3, 0],
              relative_position=0.7)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R0,
              room_arrival=R4,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[0, 0],
              relative_position=0.8)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R1,
              room_arrival=R9,
              relative_departure_coordinates=[1, 1],
              relative_arrival_coordinates=[1, 0],
              relative_position=0.3)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R2,
              room_arrival=R9,
              relative_departure_coordinates=[2/3, 1],
              relative_arrival_coordinates=[2/3, 0],
              relative_position=0.7)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R3,
              room_arrival=R9,
              relative_departure_coordinates=[1/3, 1],
              relative_arrival_coordinates=[1/3, 0],
              relative_position=0.5)
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R4,
              room_arrival=R9,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[0, 0],
              relative_position=0.4)
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R0,
              room_arrival=R5,
              relative_departure_coordinates=[(9-1)/9, 1],
              relative_arrival_coordinates=[0, 0],
              relative_position=0.75)
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R0,
              room_arrival=R6,
              relative_departure_coordinates=[(9-2/3)/9, 1],
              relative_arrival_coordinates=[1/3, 0],
              relative_position=0.4)
    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R0,
               room_arrival=R7,
               relative_departure_coordinates=[(9-1/3)/9, 1],
               relative_arrival_coordinates=[2/3, 0],
               relative_position=0.7)
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R0,
               room_arrival=R8,
               relative_departure_coordinates=[1, 1],
               relative_arrival_coordinates=[1, 0],
               relative_position=0.8)
    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R5,
               room_arrival=R10,
               relative_departure_coordinates=[0, 1],
               relative_arrival_coordinates=[0, 0],
               relative_position=0.3)
    D13 = Door(two_way=False,
               tree=T13,
               room_departure=R6,
               room_arrival=R10,
               relative_departure_coordinates=[1/3, 1],
               relative_arrival_coordinates=[1/3, 0],
               relative_position=0.7)
    D14 = Door(two_way=False,
               tree=T14,
               room_departure=R7,
               room_arrival=R10,
               relative_departure_coordinates=[2/3, 1],
               relative_arrival_coordinates=[2/3, 0],
               relative_position=0.5)
    D15 = Door(two_way=False,
               tree=T15,
               room_departure=R8,
               room_arrival=R10,
               relative_departure_coordinates=[1, 1],
               relative_arrival_coordinates=[1, 0],
               relative_position=0.4)
    D16 = Door(two_way=False,
               tree=T16,
               room_departure=R9,
               room_arrival=R11,
               relative_departure_coordinates=[0, 1],
               relative_arrival_coordinates=[0, 1])
    D17 = Door(two_way=False,
               tree=T17,
               room_departure=R10,
               room_arrival=R11,
               relative_departure_coordinates=[1, 1],
               relative_arrival_coordinates=[1, 1])
    D18 = Door(two_way=False,
               tree=T18,
               room_departure=R11,
               room_arrival=R0,
               relative_departure_coordinates=[0, 0],
               relative_arrival_coordinates=[2.5/8, 1],
               relative_position=0.35)
    D19 = Door(two_way=False,
               tree=T19,
               room_departure=R11,
               room_arrival=R0,
               relative_departure_coordinates=[0.5/3, 0],
               relative_arrival_coordinates=[3/8, 1],
               relative_position=0.55)
    D20 = Door(two_way=False,
               tree=T20,
               room_departure=R11,
               room_arrival=R0,
               relative_departure_coordinates=[2.5/3, 0],
               relative_arrival_coordinates=[5/8, 1],
               relative_position=0.55)
    D21 = Door(two_way=False,
               tree=T21,
               room_departure=R11,
               room_arrival=R0,
               relative_departure_coordinates=[1, 0],
               relative_arrival_coordinates=[5.5/8, 1],
               relative_position=0.35)
    D22 = Door(two_way=False,
               tree=T22,
               room_departure=R0,
               room_arrival=RE,
               relative_departure_coordinates=[1/2, 1],
               relative_arrival_coordinates=[1/2, 0])
    
    l_help_txt = [
"""One new notation is used in this level :
    
    D0 = 1 means that D0 is always open.
    
The tesseract is hidden in the equations.
"""]
    
    level = Maze(start_room_index=0, 
              exit_room_index=-1, 
              rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, RE], 
              doors_list = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22],
              fastest_solution="D2 S2 D6 D16 D20 D10 S6 D14 D17 D18 D3 S3 D7 D16 D21 D11 S7 D15 D17 D18 D0 S0 D4 D16 D18 D8 S4 D12 D17 D18 D1 S1 D5 D16 D19 D9 S5 D13 D17 D18 D22",
              level_color=Levels_colors_list.BLACK_AND_WHITE,
              name='Tesseract',
              help_txt = l_help_txt,
              keep_proportions=False,
              door_window_size=550,
              y_separation=50)
    return level

if __name__ == "__main__":
    
    level = level_tesseract

    solutions = level().find_all_solutions(verbose=3,
                                           stop_at_first_solution=False)
    
    level().try_solution(solutions[-1],
                         verbose=3,
                         allow_all_doors=True,
                         allow_all_switches=True)
    
    solutions_reverse = level().find_all_solutions(verbose=3,
                                                         stop_at_first_solution=False,
                                                         reverse_actions_order=True)
    
    level().try_solution(solutions_reverse[-1],
                               verbose=3,
                               allow_all_doors=True,
                               allow_all_switches=True)
    
    print(solutions[-1])
    print(solutions_reverse[-1])