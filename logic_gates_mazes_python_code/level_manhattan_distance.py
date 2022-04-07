# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 16:54:42 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_manhattan_distance():
    
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
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')
    S20 = Switch(name='S20')
    S21 = Switch(name='S21')
    S22 = Switch(name='S22')
    S23 = Switch(name='S23')
    S24 = Switch(name='S24')
    S25 = Switch(name='S25')
    S26 = Switch(name='S26')
    
    T0 = Tree(tree_list=Tree.tree_list_from_str('FTFF'),
              empty=True,
              name='T0',
              switches = [S0, S1, S2, S13])
    T1 = Tree(tree_list=Tree.tree_list_from_str('FTTT'),
              empty=True,
              name='T1',
              switches = [S3, S4, S5, S16])
    T2 = Tree(tree_list=Tree.tree_list_from_str('TFFFFT'),
              empty=True,
              name='T2',
              switches = [S0, S1, S2, S3, S4, S5])
    T3 = Tree(tree_list=Tree.tree_list_from_str('FTFFFT'),
              empty=True,
              name='T3',
              switches = [S6, S7, S8, S9, S15, S18])
    T4 = Tree(tree_list=Tree.tree_list_from_str('FTFT'),
              empty=True,
              name='T4',
              switches = [S3, S4, S5, S20])
    T5 = Tree(tree_list=Tree.tree_list_from_str('FFTTTT'),
              empty=True,
              name='T5',
              switches = [S6, S7, S8, S9, S15, S21])
    T6 = Tree(tree_list=Tree.tree_list_from_str('TFTFT'),
              empty=True,
              name='T6',
              switches = [S10, S11, S12, S21, S22])
    T7 = Tree(tree_list=Tree.tree_list_from_str('FTTFTT'),
              empty=True,
              name='T7',
              switches = [S6, S7, S8, S9, S13, S24])
    T8 = Tree(tree_list=Tree.tree_list_from_str('FTTTT'),
              empty=True,
              name='T8',
              switches = [S3, S10, S11, S12, S25])
    T9 = Tree(tree_list=['AND', Tree.tree_list_XOR3, [None]],
              empty=True,
              name='T9',
              switches = [S13, S14, S15, S26])
    T10 = Tree(tree_list=Tree.tree_list_from_str('FFTT'),
              empty=True,
              name='T10',
              switches = [S0, S1, S2, S14])
    T11 = Tree(tree_list=Tree.tree_list_from_str('TFFT'),
              empty=True,
              name='T11',
              switches = [S3, S4, S5, S20])
    T12 = Tree(tree_list=Tree.tree_list_from_str('FTFTTF'),
              empty=True,
              name='T12',
              switches = [S0, S1, S2, S3, S4, S5])
    T13 = Tree(tree_list=Tree.tree_list_from_str('TFTTT'),
              empty=True,
              name='T13',
              switches = [S6, S7, S8, S9, S21])
    T14 = Tree(tree_list=Tree.tree_list_from_str('TFTT'),
              empty=True,
              name='T14',
              switches = [S3, S4, S5, S16])
    T15 = Tree(tree_list=Tree.tree_list_from_str('TTTFFFT'),
              empty=True,
              name='T15',
              switches = [S4, S6, S7, S8, S9, S14, S18])
    T16 = Tree(tree_list=Tree.tree_list_from_str('FTTFT'),
              empty=True,
              name='T16',
              switches = [S10, S11, S12, S21, S22])
    T17 = Tree(tree_list=Tree.tree_list_from_str('TFFTFT'),
              empty=True,
              name='T17',
              switches = [S6, S7, S8, S9, S15, S17])
    T18 = Tree(tree_list=Tree.tree_list_from_str('TTFFT'),
              empty=True,
              name='T18',
              switches = [S10, S11, S12, S18, S19])
    T19 = Tree(tree_list=['AND', Tree.tree_list_XORN3, [None]],
              empty=True,
              name='T19',
              switches = [S13, S14, S15, S23])
    
    c = 1
    
    R0 = Room(name='R0',
              position = [0, 4, 3, 3],
              switches_list = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15])
    R1 = Room(name='R1',
              position = [4, 6, c, c],
              switches_list = [S16])
    R2 = Room(name='R2',
              position = [6, 6, c, c],
              switches_list = [S17])
    R3 = Room(name='R3',
              position = [4, 4, c, c],
              switches_list = [S18])
    R4 = Room(name='R4',
              position = [6, 4, c, c],
              switches_list = [S19])
    R5 = Room(name='R5',
              position = [0, 2, c, c],
              switches_list = [S20])
    R6 = Room(name='R6',
              position = [2, 2, c, c],
              switches_list = [S21])
    R7 = Room(name='R7',
              position = [4, 2, c, c],
              switches_list = [S22])
    R8 = Room(name='R8',
              position = [6, 2, c, c],
              switches_list = [S23])
    R9 = Room(name='R9',
              position = [0, 0, c, c],
              switches_list = [S24])
    R10 = Room(name='R10',
              position = [2, 0, c, c],
              switches_list = [S25])
    R11 = Room(name='R11',
              position = [4, 0, c, c],
              switches_list = [S26])
    RE = Room(name='RE',
              position = [6, 0, c, c],
              is_exit = True)  # E pour exit ou end
    
    D0  = Door(two_way = False,  
               tree = T0,  
               name='D0',  
               room_departure = R0, 
               room_arrival = R1,
               relative_departure_coordinates=[1, 5/6],
               relative_arrival_coordinates=[0, 1/2])
    D1  = Door(two_way=False,  
               tree = T1,  
               name='D1',  
               room_departure = R1, 
               room_arrival = R2)
    D2  = Door(two_way=False,  
               tree = T2,  
               name='D2',  
               room_departure = R0, 
               room_arrival = R3,
               relative_departure_coordinates=[1, 1/6],
               relative_arrival_coordinates=[0, 1/2])
    D3  = Door(two_way=False,  
               tree = T3,  
               name='D3',  
               room_departure = R3, 
               room_arrival = R4)
    D4  = Door(two_way=False,  
               tree = T4,  
               name='D4',  
               room_departure = R5, 
               room_arrival = R6)
    D5  = Door(two_way=False,  
               tree = T5,  
               name='D5',  
               room_departure = R6, 
               room_arrival = R7)
    D6  = Door(two_way=False,  
               tree = T6,  
               name='D6',  
               room_departure = R7, 
               room_arrival = R8)
    D7  = Door(two_way=False,  
               tree = T7,  
               name='D7',  
               room_departure = R9, 
               room_arrival = R10)
    D8  = Door(two_way=False,  
                tree = T8,  
                name='D8',  
                room_departure = R10, 
                room_arrival = R11)
    D9  = Door(two_way=False,  
               tree = T9,  
               name='D9',  
               room_departure = R11, 
               room_arrival = RE)
    D10  = Door(two_way=False,  
                tree = T10,  
                name='D10',  
                room_departure = R0, 
                room_arrival = R5,
                relative_departure_coordinates=[1/6, 0],
                relative_arrival_coordinates=[1/2, 1])
    D11  = Door(two_way=False,  
                tree = T11,  
                name='D11',  
                room_departure = R5, 
                room_arrival = R9)
    D12  = Door(two_way=False,  
                tree = T12,  
                name='D12',  
                room_departure = R0, 
                room_arrival = R6,
                relative_departure_coordinates=[5/6, 0],
                relative_arrival_coordinates=[1/2, 1])
    D13  = Door(two_way=False,  
                tree = T13,  
                name='D13',  
                room_departure = R6, 
                room_arrival = R10)
    D14  = Door(two_way=False,  
                tree = T14,  
                name='D14',  
                room_departure = R1, 
                room_arrival = R3)
    D15  = Door(two_way=False,  
                tree = T15,  
                name='D15',  
                room_departure = R3, 
                room_arrival = R7)
    D16  = Door(two_way=False,  
                tree = T16,  
                name='D16',  
                room_departure = R7, 
                room_arrival = R11)
    D17  = Door(two_way=False,  
                tree = T17,  
                name='D17',  
                room_departure = R2, 
                room_arrival = R4)
    D18  = Door(two_way=False,  
                tree = T18,  
                name='D18',  
                room_departure = R4, 
                room_arrival = R8)
    D19  = Door(two_way=False,  
                tree = T19,  
                name='D19',  
                room_departure = R8, 
                room_arrival = RE)
    
    l_help_txt = [
"""The cheat code might be very useful here.
"""]
    
    level = Maze(start_room_index=0, 
             exit_room_index=-1, 
             rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, RE], 
             doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9,
                         D10, D11, D12, D13, D14, D15, D16, D17, D18, D19], 
             fastest_solution='S2 S4 S6 S8 S9 S10 S11 S12 S14 D10 S20 D4 S21 D13 S25 D8 S26 D9',
             level_color=Levels_colors_list.BLACK_AND_GREY_ORANGE_CONTOUR,
             name='Manhattan_distance',
             help_txt=l_help_txt,
             door_window_size=500,
             keep_proportions=True,
             line_size=4)
    
    return level
    
if __name__ == "__main__":
    
    level_manhattan_distance().try_solution('S2 S4 S6 S8 S9 S10 S11 S12 S14 D10 S20 D4 S21 D13 S25 D8 S26 D9',
                                            verbose=2)
    
    # solutions = level_manhattan_distance().find_all_solutions(verbose=3, stop_at_first_solution=False)
