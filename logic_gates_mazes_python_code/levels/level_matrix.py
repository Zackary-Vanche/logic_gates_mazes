# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 20:28:05 2022

@author: utilisateur
"""

# Inversion matricielle

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_matrix():
    
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
    
    SN2 = Switch(name='2', value=2)
    SN3 = Switch(name='3', value=3)
    SN5 = Switch(name='5', value=5)
    SN7 = Switch(name='7', value=7)
    SN11 = Switch(name='11', value=11)
    SN13 = Switch(name='13', value=13)
    SN17 = Switch(name='17', value=17)
    SN19 = Switch(name='19', value=19)
    SN23 = Switch(name='23', value=23)
    SN29 = Switch(name='29', value=29)
    SN31 = Switch(name='31', value=31)
    SN37 = Switch(name='37', value=37)
    SN41 = Switch(name='41', value=41)
    SN43 = Switch(name='43', value=43)
    SN47 = Switch(name='47', value=47)
    SN53 = Switch(name='53', value=53)
    SN59 = Switch(name='59', value=59)
    SN61 = Switch(name='61', value=61)
    SN67 = Switch(name='67', value=67)
    SN71 = Switch(name='71', value=71)
    SN73 = Switch(name='73', value=73)
    SN79 = Switch(name='79', value=79)
    SN83 = Switch(name='83', value=83)
    SN89 = Switch(name='89', value=89)
    SN97 = Switch(name='97', value=97)
    
    SN4 = Switch(name='4', value=4)
    SN6 = Switch(name='6', value=6)
    SN10 = Switch(name='10', value=10)
    SN14 = Switch(name='14', value=14)
    SN22 = Switch(name='22', value=22)
    SN26 = Switch(name='26', value=26)
    SN34 = Switch(name='34', value=34)
    SN38 = Switch(name='38', value=38)
    SN46 = Switch(name='46', value=46)
    SN58 = Switch(name='58', value=58)
    SN62 = Switch(name='62', value=62)
    SN74 = Switch(name='74', value=74)
    SN82 = Switch(name='82', value=82)
    SN86 = Switch(name='86', value=86)
    SN94 = Switch(name='94', value=94)
    SN106 = Switch(name='106', value=106)
    SN118 = Switch(name='118', value=118)
    SN122 = Switch(name='122', value=122)
    SN134 = Switch(name='134', value=134)
    SN142 = Switch(name='142', value=142)
    SN146 = Switch(name='146', value=146)
    SN158 = Switch(name='158', value=158)
    SN166 = Switch(name='166', value=166)
    SN178 = Switch(name='178', value=178)
    SN194 = Switch(name='194', value=194)

    SN347 = Switch(name='347', value=347)
    SN387 = Switch(name='387', value=387)
    SN411 = Switch(name='411', value=411)
    SN443 = Switch(name='443', value=443)
    SN485 = Switch(name='485', value=485)
    
    tree_list_0 = ['EQU',
                           ['SUM'] + [['PROD', [None], [None]]]*10,
                           [None]]
    
    T0 = Tree(tree_list=tree_list_0,
              empty=True,
              name='T0',
              switches = [SN2, S0, SN4, S1,
                          SN13, S2, SN26, S3,
                          SN31, S4, SN62, S5,
                          SN53, S6, SN106, S7,
                          SN73, S8, SN146, S9, 
                         SN347])
    T1 = Tree(tree_list=tree_list_0,
              empty=True,
              name='T1',
              switches = [SN3, S0, SN6, S1,
                          SN17, S2, SN34, S3,
                          SN37, S4, SN74, S5,
                          SN59, S6, SN118, S7,
                          SN79, S8, SN158, S9,
                          SN387])
    T2 = Tree(tree_list=tree_list_0,
              empty=True,
              name='T2',
              switches = [SN5, S0, SN10, S1,
                          SN19, S2, SN38, S3,
                          SN41, S4, SN82, S5,
                          SN61, S6, SN122, S7,
                          SN83, S8, SN166, S9,
                          SN411])
    T3 = Tree(tree_list=tree_list_0,
              empty=True,
              name='T3',
              switches = [SN7, S0, SN14, S1,
                          SN23, S2, SN46, S3,
                          SN43, S4, SN86, S5,
                          SN67, S6, SN134, S7,
                          SN89, S8, SN178, S9,
                          SN443])
    T4 = Tree(tree_list=tree_list_0,
              empty=True,
              name='T4',
              switches = [SN11, S0, SN22, S1,
                          SN29, S2, SN58, S3,
                          SN47, S4, SN94, S5,
                          SN71, S6, SN142, S7,
                          SN97, S8, SN194, S9,
                          SN485])
    
    e = 4.5
    d = 6.6
    
    R0 = Room(name='R0',
              position = [0, 0, 4, 20],
              switches_list = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9])
    R1 = Room(name='R1',
              position = [d, 0, 2, 2],
              switches_list = [])
    R2 = Room(name='R2',
              position = [d, e, 2, 2],
              switches_list = [])
    R3 = Room(name='R3',
              position = [d, 2*e, 2, 2],
              switches_list = [])
    R4 = Room(name='R4',
              position = [d, 3*e, 2, 2],
              switches_list = [])
    RE = Room(name='RE',
              position=[d, 4*e, 2, 2],
              is_exit=True)   # E pour exit ou end
    
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[3.5/4, 1/20])
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
                 fastest_solution='S2 S5 S6 S8 S9 D0 D1 D2 D3 D4',
                 level_color=Levels_colors_list.BLACK_AND_GREEN,
                 name='Matrix',
                 door_window_size=950,
                 keep_proportions=True)

    return level

if __name__ == "__main__":
    
    level = level_matrix

    solutions = level().find_all_solutions(verbose=3,
                                           stop_at_first_solution=False)
    
    print(solutions[-1])