# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:54:53 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_tree():
    
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
    T4 = Tree(tree_list=Tree.tree_list_from_str('FTTFFFFF'),
                empty=True,
                name='T4',
                switches = [S0, S1, S2, S3, S4, S5, S6, S7])
    T5 = Tree(tree_list=Tree.tree_list_from_str('FTTFFFFT'),
                empty=True,
                name='T5',
                switches = [S0, S1, S2, S3, S4, S5, S6, S7])
    T6 = Tree(tree_list=Tree.tree_list_from_str('FFFTTTTF'),
                empty=True,
                name='T6',
                switches = [S0, S1, S2, S3, S4, S5, S6, S7])
    T7 = Tree(tree_list=Tree.tree_list_from_str('FFFFFTTF'),
                empty=True,
                name='T7',
                switches = [S0, S1, S2, S3, S4, S5, S6, S7])
    T8 = Tree(tree_list=Tree.tree_list_from_str('FTTTTTTF'),
                empty=True,
                name='T8',
                switches = [S0, S1, S2, S3, S4, S5, S6, S7])
    T9 = Tree(tree_list=Tree.tree_list_from_str('FFFFFFFT'),
                empty=True,
                name='T9',
                switches = [S0, S1, S2, S3, S4, S5, S6, S7])
    T10 = Tree(tree_list=Tree.tree_list_from_str('FFFFFTTT'),
                empty=True,
                name='T10',
                switches = [S0, S1, S2, S3, S4, S5, S6, S7])
    T11 = Tree(tree_list=Tree.tree_list_from_str('FTTTTFFF'),
                empty=True,
                name='T11',
                switches = [S0, S1, S2, S3, S4, S5, S6, S7])
    T12 = Tree(tree_list=Tree.tree_list_from_str('FTTTTTTT'),
                empty=True,
                name='T12',
                switches = [S0, S1, S2, S3, S4, S5, S6, S7])
    T13 = Tree(tree_list=Tree.tree_list_from_str('FFFTTFFF'),
                empty=True,
                name='T13',
                switches = [S0, S1, S2, S3, S4, S5, S6, S7])
    T14 = Tree(tree_list=Tree.tree_list_from_str('FTTFFTTF'),
                empty=True,
                name='T14',
                switches = [S0, S1, S2, S3, S4, S5, S6, S7])
    T15 = Tree(tree_list=Tree.tree_list_from_str('FFFTTTTT'),
                empty=True,
                name='T15',
                switches = [S0, S1, S2, S3, S4, S5, S6, S7])
    T16 = Tree(tree_list=Tree.tree_list_from_str('FFFTTFFT'),
                empty=True,
                name='T16',
                switches = [S0, S1, S2, S3, S4, S5, S6, S7])
    T17 = Tree(tree_list=Tree.tree_list_from_str('FTTFFTTT'),
                empty=True,
                name='T17',
                switches = [S0, S1, S2, S3, S4, S5, S6, S7])
    T18 = Tree(tree_list=Tree.tree_list_from_str('FTTTTFFT'),
                empty=True,
                name='T18',
                switches = [S0, S1, S2, S3, S4, S5, S6, S7])
    T19 = Tree(tree_list=['AND',
                          Tree.tree_list_XNOR(2),
                          Tree.tree_list_XNOR(2),
                          Tree.tree_list_XNOR(2),
                          Tree.tree_list_XNOR(2)],
                empty=True,
                name='T19',
                switches = [S0, S1, S2, S3, S4, S5, S6, S7])
    T20 = Tree(tree_list=Tree.tree_list_from_str('TTFFTTTT'),
                empty=True,
                name='T20',
                switches = [S0, S1, S2, S3, S4, S5, S6, S7])
    
    R0 = Room(name='R0',
                position = [2, -2, 15, 0.4],
                switches_list = [])
    R1 = Room(name='R1',
                position = [-2, 0.5, 1.5, 5],
                switches_list = [S0, S2, S4, S6])
    R2 = Room(name='R2',
                position = [0, 0.5, 1.5, 5],
                switches_list = [S1, S3, S5, S7])
    R3 = Room(name='R3',
                position = [2, 6.6, 15, 0.4],
                switches_list = [])
    RE = Room(name='RE',
              position = [-2, -2, 1.5, 1],
              is_exit = True)  # E pour exit ou end
    
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[0, 0],
              relative_arrival_coordinates=[1/2, 0],
              relative_position=0.8)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R0,
              room_arrival=R2,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[1/2, 0],
              relative_position=0.4)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R1,
              room_arrival=R3,
              relative_departure_coordinates=[1/2, 1],
              relative_arrival_coordinates=[0, 1],
              relative_position=0.35)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=[1/2, 1],
              relative_arrival_coordinates=[0, 0],
              relative_position=0.6)
    n = 17
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R3,
              room_arrival=R0,
              relative_departure_coordinates=[1/n, 0],
              relative_arrival_coordinates=[1/n, 1],
              relative_position=1/9)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R3,
              room_arrival=R0,
              relative_departure_coordinates=[2/n, 0],
              relative_arrival_coordinates=[2/n, 1],
              relative_position=2/9)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R3,
              room_arrival=R0,
              relative_departure_coordinates=[3/n, 0],
              relative_arrival_coordinates=[3/n, 1],
              relative_position=3/9)
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R3,
              room_arrival=R0,
              relative_departure_coordinates=[4/n, 0],
              relative_arrival_coordinates=[4/n, 1],
              relative_position=4/9)
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R3,
              room_arrival=R0,
              relative_departure_coordinates=[5/n, 0],
              relative_arrival_coordinates=[5/n, 1],
              relative_position=5/9)
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R3,
              room_arrival=R0,
              relative_departure_coordinates=[6/n, 0],
              relative_arrival_coordinates=[6/n, 1],
              relative_position=6/9)
    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R3,
               room_arrival=R0,
               relative_departure_coordinates=[7/n, 0],
               relative_arrival_coordinates=[7/n, 1],
               relative_position=7/9)
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R3,
               room_arrival=R0,
               relative_departure_coordinates=[8/n, 0],
               relative_arrival_coordinates=[8/n, 1],
               relative_position=8/9)
    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R3,
               room_arrival=R0,
               relative_departure_coordinates=[9/n, 0],
               relative_arrival_coordinates=[9/n, 1],
               relative_position=1/9)
    D13 = Door(two_way=False,
               tree=T13,
               room_departure=R3,
               room_arrival=R0,
               relative_departure_coordinates=[10/n, 0],
               relative_arrival_coordinates=[10/n, 1],
               relative_position=2/9)
    D14 = Door(two_way=False,
               tree=T14,
               room_departure=R3,
               room_arrival=R0,
               relative_departure_coordinates=[11/n, 0],
               relative_arrival_coordinates=[11/n, 1],
               relative_position=3/9)
    D15 = Door(two_way=False,
               tree=T15,
               room_departure=R3,
               room_arrival=R0,
               relative_departure_coordinates=[12/n, 0],
               relative_arrival_coordinates=[12/n, 1],
               relative_position=4/9)
    D16 = Door(two_way=False,
               tree=T16,
               room_departure=R3,
               room_arrival=R0,
               relative_departure_coordinates=[13/n, 0],
               relative_arrival_coordinates=[13/n, 1],
               relative_position=5/9)
    D17 = Door(two_way=False,
               tree=T17,
               room_departure=R3,
               room_arrival=R0,
               relative_departure_coordinates=[14/n, 0],
               relative_arrival_coordinates=[14/n, 1],
               relative_position=6/9)
    D18 = Door(two_way=False,
               tree=T18,
               room_departure=R3,
               room_arrival=R0,
               relative_departure_coordinates=[15/n, 0],
               relative_arrival_coordinates=[15/n, 1],
               relative_position=7/9)
    D19 = Door(two_way=False,
               tree=T19,
               room_departure=R3,
               room_arrival=R0,
               relative_departure_coordinates=[16/n, 0],
               relative_arrival_coordinates=[16/n, 1],
               relative_position=8/9)
    D20 = Door(two_way=False,
               tree=T20,
               room_departure=R0,
               room_arrival=RE,
               relative_departure_coordinates=[0, 0],
               relative_arrival_coordinates=[1, 1/2],
               relative_position=1/2)
        
    level = Maze(start_room_index=0, 
                 exit_room_index=-1, 
                 rooms_list=[R0, R1, R2, R3, RE], 
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20], 
                 fastest_solution="D1 S7 D3 D9 D0 S6 D2 D19 D1 S5 S7 D3 D7 D0 S4 S6 D2 D19 D1 S3 S5 S7 D3 D16 D0 S2 S4 S6 D2 D19 D1 S1 S3 S5 D3 D17 D0 S0 S2 S4 D2 D19 D20",
                 level_color=Levels_colors_list.RED_AND_YELLOW,
                 name='Tree',
                 border = 30,
                 door_window_size = 500)

    return level

if __name__ == "__main__":
    
    level = level_tree

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
