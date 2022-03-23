# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 13:12:20 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


class Levels:

    # Creation des niveaux

    def level_backward():

        S0 = Switch(name='S0')
        S1 = Switch(name='S1')
        S2 = Switch(name='S2')

        tree_list_0 = Tree.tree_list_anb
        tree_list_1 = ['AND', ['NOT', [None]], Tree.tree_list_and_2]

        T0 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T0',
                  switches=[S0, S1])
        T1 = Tree(tree_list=tree_list_1,
                  empty=True, name='T1',
                  switches=[S0, S1, S2],
                  easy_logical_expression_PN="& - S0 ( & S1 S2 )\n= & ( - S0 S1 S2 )")

        position_R0 = [3, 2, 2, 2]
        position_R1 = [0, 1, 2, 2]
        position_RE = [6, 3, 2, 2]

        R0 = Room(name='R0',
                  position=position_R0,
                  switches_list=[S0, S1])
        R1 = Room(name='R1',
                  position=position_R1,
                  switches_list=[S2])
        RE = Room(name='RE',
                  position=position_RE,
                  is_exit=True)   # E pour exit ou end

        relative_departure_coordinates_D0 = [0, 1/2]
        relative_arrival_coordinates_D0 = [0.98, 0.98]
        relative_departure_coordinates_D1 = [0.98, 0.98]
        relative_arrival_coordinates_D1 = [0, 1/2]

        D0 = Door(two_way=True,
                  tree=T0,
                  name='D0',
                  room_departure=R0,
                  room_arrival=R1,
                  relative_departure_coordinates=relative_departure_coordinates_D0,
                  relative_arrival_coordinates=relative_arrival_coordinates_D0)
        D1 = Door(two_way=True,
                  tree=T1,
                  name='D1',
                  room_departure=R0,
                  room_arrival=RE,
                  relative_departure_coordinates=relative_departure_coordinates_D1,
                  relative_arrival_coordinates=relative_arrival_coordinates_D1)

        l_help_txt = [
"""One new notation is used in this level :

    To simplify notations, parentheses are used.

    Instead of writing :
        D0 = & S0 & S1 S2
    you can write :
        D0 = & S0 ( & S1 S2 )
    or :
        D0 = & ( S0 S1 S2 )
    You can use this notation with more than 3 switches.
    You can also use it with | instead of &.

    In this level, the notation is used with negations :
        D0 = & - S0 ( & S1 S2 )
           = & ( - S0 S1 S2 )
"""]

        level = Maze(start_room_index=0,
                     exit_room_index=-1,
                     rooms_list=[R0, R1, RE],
                     doors_list=[D0, D1],
                     fastest_solution='S0 D0 S2 D0 S0 S1 D1',
                     level_color=Levels_colors_list.BROWN,
                     name='Backward',
                     help_txt=l_help_txt,
                     door_window_size=500)

        return level

    def level_binary():

        S0 = Switch(name='S0')
        S1 = Switch(name='S1')
        S2 = Switch(name='S2')
        S3 = Switch(name='S3')
        S4 = Switch(name='S4')
        S5 = Switch(name='S5')
        S6 = Switch(name='S6')
        T0 = Tree(tree_list=[None], empty=True, name='T0', switches=[S6])
        T1 = Tree(tree_list=[None], empty=True, name='T1', switches=[S3])
        T2 = Tree(tree_list=[None], empty=True, name='T2', switches=[S4])
        T3 = Tree(tree_list=[None], empty=True, name='T3', switches=[S0])
        T4 = Tree(tree_list=[None], empty=True, name='T4', switches=[S1])
        T5 = Tree(tree_list=[None], empty=True, name='T5', switches=[S2])
        T6 = Tree(tree_list=Tree.tree_list_and_7,
                  empty=True,
                  name='T6',
                  switches=[S0, S1, S2, S3, S4, S5, S6])

        position_R0 = [3, 2.9, 2, 2]
        position_R1 = [1, 0, 2, 2]
        position_R2 = [5, 0, 2, 2]
        position_R3 = [0, 3, 2, 2]
        position_R4 = [6, 3, 2, 2]
        position_R5 = [0, 6, 2, 2]
        position_R6 = [6, 6, 2, 2]
        position_RE = [3, 6, 2, 2]

        R0 = Room(name='R0', position=position_R0, switches_list=[S0])
        R1 = Room(name='R1', position=position_R1, switches_list=[S1])
        R2 = Room(name='R2', position=position_R2, switches_list=[S2])
        R3 = Room(name='R3', position=position_R3, switches_list=[S3])
        R4 = Room(name='R4', position=position_R4, switches_list=[S4])
        R5 = Room(name='R5', position=position_R5, switches_list=[S5])
        R6 = Room(name='R6', position=position_R6, switches_list=[S6])
        RE = Room(name='RE', position=position_RE, is_exit=True)
        # E pour exit ou end

        D0 = Door(two_way=True,
                  tree=T0,
                  name='D0',
                  room_departure=R3,
                  room_arrival=R1)
        D1 = Door(two_way=True,
                  tree=T1,
                  name='D1',
                  room_departure=R4,
                  room_arrival=R2)
        D2 = Door(two_way=True,
                  tree=T2,
                  name='D2',
                  room_departure=R0,
                  room_arrival=R3)
        D3 = Door(two_way=True,
                  tree=T3,
                  name='D3',
                  room_departure=R0,
                  room_arrival=R4)
        D4 = Door(two_way=True,
                  tree=T4,
                  name='D4',
                  room_departure=R3,
                  room_arrival=R5)
        D5 = Door(two_way=True,
                  tree=T5,
                  name='D5',
                  room_departure=R4,
                  room_arrival=R6)
        D6 = Door(two_way=True,
                  tree=T6,
                  name='D6',
                  room_departure=R0,
                  room_arrival=RE)

        l_help_txt = [
"""At every step, you have only one action possible :
    In the beginning, you can only turn on S0.
    Then, a door opens, so you use it...
    And so on...
"""]

        level = Maze(start_room_index=0,
                     exit_room_index=-1,
                     rooms_list=[R0, R1, R2, R3, R4, R5, R6, RE],
                     doors_list=[D0, D1, D2, D3, D4, D5, D6],
                     fastest_solution='S0 D3 S4 D3 D2 S3 D2 D3 D1 S2 D1 D5 S6 D5 D3 D2 D0 S1 D0 D4 S5 D4 D2 D6',
                     level_color=Levels_colors_list.BLUE_GREEN,
                     name='Binary',
                     help_txt=l_help_txt,
                     door_window_size=500)

        return level

    def level_cartesian():

        S0 = Switch(name='S0')
        S1 = Switch(name='S1')
        S2 = Switch(name='S2')
        S3 = Switch(name='S3')
        S4 = Switch(name='S4')
        S5 = Switch(name='S5')
        S6 = Switch(name='S6')
        S7 = Switch(name='S7')
        S8 = Switch(name='S8')

        T0 = Tree(tree_list=[None],
                  empty=True,
                  name='T0',
                  switches=[S0])
        T1 = Tree(tree_list=[None],
                  empty=True,
                  name='T1',
                  switches=[S0])
        T2 = Tree(tree_list=[None],
                  empty=True,
                  name='T2',
                  switches=[S7])
        T3 = Tree(tree_list=Tree.tree_list_anb,
                  empty=True,
                  name='T3',
                  switches=[S1, S2])
        T4 = Tree(tree_list=Tree.tree_list_bna,
                  empty=True,
                  name='T4',
                  switches=[S4, S8])
        T5 = Tree(tree_list=Tree.tree_list_xnor,
                  empty=True,
                  name='T5',
                  switches=[S5, S6])
        T6 = Tree(tree_list=["AND", Tree.tree_list_xor, [None]],
                  empty=True,
                  name='T6',
                  switches=[S0, S1, S2])
        T7 = Tree(tree_list=["AND", Tree.tree_list_xor, [None]],
                  empty=True,
                  name='T7',
                  switches=[S1, S2, S4])
        T8 = Tree(tree_list=Tree.tree_list_xor,
                  empty=True,
                  name='T8',
                  switches=[S5, S6])
        T9 = Tree(tree_list=Tree.tree_list_xnor,
                  empty=True,
                  name='T9',
                  switches=[S3, S8])
        T10 = Tree(tree_list=Tree.tree_list_from_str('FTTTTTT'),
                   empty=True,
                   name='T10',
                   switches=[S0, S2, S3, S4, S5, S7, S8])

        c = 1.2

        position_R0 = [0, 2, c, c]
        position_R1 = [0, 0, c, c]
        position_R2 = [2, 0, c, c]
        position_R3 = [4, 0, c, c]
        position_R4 = [4, 2, c, c]
        position_R5 = [4, 4, c, c]
        position_R6 = [2, 4, c, c]
        position_R7 = [2, 2, c, c]
        position_RE = [0, 4, c, c]

        R0 = Room(name='R0', position=position_R0, switches_list=[S0])
        R1 = Room(name='R1', position=position_R1, switches_list=[S1])
        R2 = Room(name='R2', position=position_R2, switches_list=[S2])
        R3 = Room(name='R3', position=position_R3, switches_list=[S3])
        R4 = Room(name='R4', position=position_R4, switches_list=[S4])
        R5 = Room(name='R5', position=position_R5, switches_list=[S5])
        R6 = Room(name='R6', position=position_R6, switches_list=[S6])
        R7 = Room(name='R7', position=position_R7, switches_list=[S7, S8])
        RE = Room(name='RE', position=position_RE,
                  is_exit=True)   # E pour exit ou end

        D0 = Door(two_way=False,
                  tree=T0,
                  name='D0',
                  room_departure=R0,
                  room_arrival=R1)
        D1 = Door(two_way=False,
                  tree=T1,
                  name='D1',
                  room_departure=R1,
                  room_arrival=R2)
        D2 = Door(two_way=False,
                  tree=T2,
                  name='D2',
                  room_departure=R2,
                  room_arrival=R3)
        D3 = Door(two_way=False,
                  tree=T3,
                  name='D3',
                  room_departure=R3,
                  room_arrival=R4)
        D4 = Door(two_way=False,
                  tree=T4,
                  name='D4',
                  room_departure=R4,
                  room_arrival=R5)
        D5 = Door(two_way=False,
                  tree=T5,
                  name='D5',
                  room_departure=R5,
                  room_arrival=R6)
        D6 = Door(two_way=False,
                  tree=T6,
                  name='D6',
                  room_departure=R2,
                  room_arrival=R7)
        D7 = Door(two_way=False,
                  tree=T7,
                  name='D7',
                  room_departure=R4,
                  room_arrival=R7)
        D8 = Door(two_way=False,
                  tree=T8,
                  name='D8',
                  room_departure=R6,
                  room_arrival=R7)
        D9 = Door(two_way=False,
                  tree=T9,
                  name='D9',
                  room_departure=R7,
                  room_arrival=R0)
        D10 = Door(two_way=False,
                   tree=T10,
                   name='D10',
                   room_departure=R0,
                   room_arrival=RE)

        l_help_txt = ["""
"""]

        level = Maze(start_room_index=0,
                     exit_room_index=-1,
                     rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                     doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10],
                     fastest_solution="S0 D0 D1 S2 D6 S7 D9 D0 S1 D1 S2 D2 S3 D3 S4 D7 S8 D9 D0 D1 D2 D3 S4 D4 D5 S6 D8 D9 D0 D1 D2 D3 D4 S5 D5 S6 D8 D9 D0 D1 D2 D3 S4 D7 D9 D0 S1 D1 S2 D6 D9 S0 D10",
                     level_color=Levels_colors_list.GREEN_GREY,
                     name='Cartesian',
                     help_txt=l_help_txt,
                     door_window_size=550,
                     keep_proportions=True)

        return level
    
    def level_crossroad():

        S0 = Switch(name='S0')
        S1 = Switch(name='S1')
        S2=Switch(name='S2')
        S3 = Switch(name='S3')
        S4 = Switch(name='S4')
        S5 = Switch(name='S5')
        
        tree_list_0 = [None] # S0
        tree_list_1 = [None] # S1
        tree_list_2 = [None] # S2
        tree_list_3 = [None] # S3
        tree_list_4 = [None] # S4
        tree_list_5 = Tree.tree_list_and_6 
        
        T0 = Tree(tree_list=tree_list_0, empty=True, name='T0', switches = [S0])
        T1 = Tree(tree_list=tree_list_1, empty=True, name='T1', switches = [S1])
        T2 = Tree(tree_list=tree_list_2, empty=True, name='T2', switches = [S2])
        T3 = Tree(tree_list=tree_list_3, empty=True, name='T3', switches = [S3])
        T4 = Tree(tree_list=tree_list_4, empty=True, name='T4', switches = [S4])
        T5 = Tree(tree_list=tree_list_5, empty=True, name='T5', switches = [S0, S1, S2, S3, S4, S5])
        
        position_R0 = [2.5,  5,  1.75,  1.75]
        position_R1 = [  0,2.5,  1.75,  1.75]
        position_R2 = [2.5,  0,  1.75,  1.75]
        position_R3 = [  5,2.5,  1.75,  1.75]
        position_RE = [5,0,1,1.5]
        
        R0 = Room(name='R0', position = position_R0, switches_list = [S0, S2])
        R1 = Room(name='R1', position = position_R1, switches_list = [S5])
        R2 = Room(name='R2', position = position_R2, switches_list = [S4])
        R3 = Room(name='R3', position = position_R3, switches_list = [S1, S3])
        RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
        
        D0 = Door(two_way = False, tree = T0, name='D0', room_departure = R0, room_arrival = R1)
        D1 = Door(two_way = False, tree = T1, name='D1', room_departure = R3, room_arrival = R0)
        D2 = Door(two_way = False, tree = T2, name='D2', room_departure = R0, room_arrival = R2, 
                  relative_departure_coordinates = [1/2, 0.9], relative_arrival_coordinates = [1/2, 0.9])
        D3 = Door(two_way = False, tree = T3, name='D3', room_departure = R1, room_arrival = R3, 
                  relative_departure_coordinates = [0.1, 1/2], relative_arrival_coordinates = [0.1, 1/2])
        D4 = Door(two_way = False, tree = T4, name='D4', room_departure = R2, room_arrival = R3)
        D5 = Door(two_way = False, tree = T5, name='D5', room_departure = R3, room_arrival = RE)
        
        l_help_txt = [
"""[Reminder] : To start the level again from the beginning, press [R].
"""]
        
        level = Maze(start_room_index=0, 
                     exit_room_index=-1, 
                     rooms_list=[R0, R1, R2, R3, RE], 
                     doors_list = [D0, D1, D2, D3, D4, D5], 
                     fastest_solution='S0 S2 D2 S4 D4 S1 S3 D1 D0 S5 D3 D5',
                     level_color=Levels_colors_list.YELLOW,
                     name='Crossroad',
                     help_txt = l_help_txt,
                     border = 30,
                     door_window_size = 500)

        return level

    def level_crystal():

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
        
        tree_list_0  = Tree.tree_list_and_9
        tree_list_1  = Tree.tree_list_TFT
        tree_list_2  = Tree.tree_list_FTF
        tree_list_3  = Tree.tree_list_TFT
        tree_list_4  = Tree.tree_list_FTF
        tree_list_5  = Tree.tree_list_TFT
        tree_list_6  = Tree.tree_list_FFT
        tree_list_7  = Tree.tree_list_and_2
        tree_list_8  = Tree.tree_list_from_str('TTFF')
        tree_list_9  = Tree.tree_list_nor
        tree_list_10 = Tree.tree_list_bna
        tree_list_11 = Tree.tree_list_anb
        tree_list_12 = Tree.tree_list_and_2
        
        T0   = Tree(tree_list=tree_list_0,   
                    empty=True, name='T0',   
                    switches = [S0, S1, S3, S4, S5, S6, S7, S9, S11])
        T1   = Tree(tree_list=tree_list_1,   
                    empty=True, name='T1',   
                    switches = [S0, S5, S6])
        T2   = Tree(tree_list=tree_list_2,   
                    empty=True, name='T2',   
                    switches = [S0, S5, S6])
        T3   = Tree(tree_list=tree_list_3,   
                    empty=True, name='T3',   
                    switches = [S0, S5, S6])
        T4   = Tree(tree_list=tree_list_4,   
                    empty=True, name='T4',   
                    switches = [S0, S5, S6])
        T5   = Tree(tree_list=tree_list_5,   
                    empty=True, name='T5',   
                    switches = [S0, S5, S6])
        T6   = Tree(tree_list=tree_list_6,   
                    empty=True, name='T6',   
                    switches = [S0, S6, S5])
        T7   = Tree(tree_list=tree_list_7,   
                    empty=True, name='T7',   
                    switches = [S5, S11])
        T8   = Tree(tree_list=tree_list_8,   
                    empty=True, name='T8',   
                    switches = [S3, S5, S7, S11])
        T9   = Tree(tree_list=tree_list_9,   
                    empty=True, name='T9',   
                    switches = [S2, S10])
        T10  = Tree(tree_list=tree_list_10,  
                    empty=True, name='T10',  
                    switches = [S1, S6])
        T11  = Tree(tree_list=tree_list_11,  
                    empty=True, name='T11',  
                    switches = [S4, S8])
        T12  = Tree(tree_list=tree_list_12,  
                    empty=True, name='T12',  
                    switches = [S0, S9])
        
        position_R0 = [  6, 12, 4, 4]
        position_R1 = [  0,  9, 4, 4]
        position_R2 = [ 12,  9, 4, 4]
        position_R3 = [  0,  3, 4, 4]
        position_R4 = [ 12,  3, 4, 4]
        position_R5 = [  6,  0, 4, 4]
        position_RE = [  4,5.4, 8,4.8]
        
        R0 = Room(name='R0', position = position_R0, switches_list = [S0, S6])
        R1 = Room(name='R1', position = position_R1, switches_list = [S1, S7])
        R2 = Room(name='R2', position = position_R2, switches_list = [S2, S8])
        R3 = Room(name='R3', position = position_R3, switches_list = [S3, S9])
        R4 = Room(name='R4', position = position_R4, switches_list = [S4, S10])
        R5 = Room(name='R5', position = position_R5, switches_list = [S5, S11])
        RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
        
        relative_departure_coordinates_D0  = [1/2,   0]
        relative_arrival_coordinates_D0    = [1/2,   1]
        relative_departure_coordinates_D1  = [  0,   0]
        relative_arrival_coordinates_D1    = [  1, 1/4]
        relative_departure_coordinates_D2  = [  1,   0]
        relative_arrival_coordinates_D2    = [  0, 1/4]
        relative_departure_coordinates_D3  = [3/4,   0]
        relative_arrival_coordinates_D3    = [3/4,   1]
        relative_departure_coordinates_D4  = [1/4,   0]
        relative_arrival_coordinates_D4    = [1/4,   1]  
        relative_departure_coordinates_D5  = [  1, 3/4]
        relative_arrival_coordinates_D5    = [  0,   1]
        relative_departure_coordinates_D6  = [  0, 3/4]
        relative_arrival_coordinates_D6    = [  1,   1]
        relative_departure_coordinates_D7  = [  1,   1]
        relative_arrival_coordinates_D7    = [  0, 3/4]
        relative_departure_coordinates_D8  = [  0,   1]
        relative_arrival_coordinates_D8    = [  1, 3/4]
        relative_departure_coordinates_D9  = [1/4,   1]
        relative_arrival_coordinates_D9    = [1/4,   0]
        relative_departure_coordinates_D10 = [3/4,   1]
        relative_arrival_coordinates_D10   = [3/4,   0]
        relative_departure_coordinates_D11 = [  0, 1/4]
        relative_arrival_coordinates_D11   = [  1,   0]
        relative_departure_coordinates_D12 = [  1, 1/4]
        relative_arrival_coordinates_D12   = [  0,   0]
        
        D0  = Door(two_way = False,  
                   tree = T0,  name='D0',  
                   room_departure = R0, 
                   room_arrival = RE, 
                  relative_departure_coordinates = relative_departure_coordinates_D0, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D0)
        D1  = Door(two_way = False,  
                   tree = T1,  name='D1',  
                   room_departure = R0, 
                   room_arrival = R1, 
                  relative_departure_coordinates = relative_departure_coordinates_D1, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D1)
        D2  = Door(two_way = False,  
                   tree = T2,  name='D2',  
                   room_departure = R0, 
                   room_arrival = R2, 
                  relative_departure_coordinates = relative_departure_coordinates_D2, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D2)
        D3  = Door(two_way = False,  
                   tree = T3,  name='D3',  
                   room_departure = R1, 
                   room_arrival = R3, 
                  relative_departure_coordinates = relative_departure_coordinates_D3, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D3)
        D4  = Door(two_way = False,  
                   tree = T4,  name='D4',  
                   room_departure = R2, 
                   room_arrival = R4, 
                  relative_departure_coordinates = relative_departure_coordinates_D4, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D4)
        D5  = Door(two_way = False,  
                   tree = T5,  name='D5',  
                   room_departure = R3, 
                   room_arrival = R5, 
                  relative_departure_coordinates = relative_departure_coordinates_D5, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D5)
        D6  = Door(two_way = False,  
                   tree = T6,  name='D6',  
                   room_departure = R4, 
                   room_arrival = R5, 
                  relative_departure_coordinates = relative_departure_coordinates_D6, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D6)
        D7  = Door(two_way = False,  
                   tree = T7,  name='D7',  
                   room_departure = R1, 
                   room_arrival = R0, 
                  relative_departure_coordinates = relative_departure_coordinates_D7, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D7)
        D8  = Door(two_way = False,  
                   tree = T8,  name='D8',  
                   room_departure = R2, 
                   room_arrival = R0, 
                  relative_departure_coordinates = relative_departure_coordinates_D8, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D8)
        D9  = Door(two_way = False,  
                   tree = T9,  name='D9',  
                   room_departure = R3, 
                   room_arrival = R1, 
                  relative_departure_coordinates = relative_departure_coordinates_D9, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D9)
        D10 = Door(two_way = False,  
                   tree = T10,  name='D10',  
                   room_departure = R4, 
                   room_arrival = R2, 
                  relative_departure_coordinates = relative_departure_coordinates_D10, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D10)
        D11 = Door(two_way = False,  
                   tree = T11,  name='D11',  
                   room_departure = R5, 
                   room_arrival = R3, 
                  relative_departure_coordinates = relative_departure_coordinates_D11, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D11)
        D12 = Door(two_way = False,  
                   tree = T12,  name='D12',  
                   room_departure = R5, 
                   room_arrival = R4, 
                  relative_departure_coordinates = relative_departure_coordinates_D12, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D12)
        
        l_help_txt = [
"""
"""]
        
        level = Maze(start_room_index=0, 
                     exit_room_index=-1, 
                     rooms_list=[R0, R1, R2, R3, R4, R5, RE], 
                     doors_list = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12], 
                     fastest_solution='S0 S6 D1 D3 S3 S9 D5 S5 D12 D10 D8 S0 S6 D2 D4 S4 D6 S11 D11 D9 S1 S7 D7 S0 S6 D0',
                     level_color=Levels_colors_list.SALMON_AND_GREY,
                     name='Crystal',
                     help_txt = l_help_txt,
                     door_window_size = 500,
                     border = 25)
        
        return level

    def level_dead_ends(): 
         
        S0  = Switch(name='S0')
        S1  = Switch(name='S1')
        S2  = Switch(name='S2')
        S3  = Switch(name='S3')
        S4  = Switch(name='S4')
        S5  = Switch(name='S5')
        S6  = Switch(name='S6')
        S7  = Switch(name='S7')
        S8  = Switch(name='S8')
        S9  = Switch(name='S9')
        S10 = Switch(name='S10')
        S11 = Switch(name='S11')
        # SN  = Switch(name='SN') # Switch Null
        
        tree_list_0  = ["AND_5", Tree.tree_list_not, [None], [None], [None], [None]]
        tree_list_1  = Tree.tree_list_TFF
        tree_list_2  = Tree.tree_list_nor
        tree_list_3  = Tree.tree_list_TFF
        tree_list_4  = Tree.tree_list_nor
        tree_list_5  = Tree.tree_list_nor
        tree_list_6  = Tree.tree_list_nor
        tree_list_7  = Tree.tree_list_nor
        tree_list_8  = Tree.tree_list_from_str('TT T')  # ['OR', Tree.tree_list_and_2, [None]]
        tree_list_9  = Tree.tree_list_anb
        tree_list_10 = ['AND_3', Tree.tree_list_xor, Tree.tree_list_xor, Tree.tree_list_not]
        tree_list_11 = Tree.tree_list_anb
        # tree_list_12 = ['NA', [None], [None]]
        tree_list_12 = ['NOT', [None]]
        tree_list_13 = Tree.tree_list_FFF
        tree_list_14 = tree_list_10[:]
        
        T0  = Tree(tree_list=tree_list_0,  empty=True, name='T0',  switches = [S0, S5, S6, S7, S8])
        T1  = Tree(tree_list=tree_list_1,  empty=True, name='T1',  switches = [S0, S1, S2])
        T2  = Tree(tree_list=tree_list_2,  empty=True, name='T2',  switches = [S3, S4])
        T3  = Tree(tree_list=tree_list_3,  empty=True, name='T3',  switches = [S0, S3, S4])
        T4  = Tree(tree_list=tree_list_4,  empty=True, name='T4',  switches = [S2, S8])
        T5  = Tree(tree_list=tree_list_5,  empty=True, name='T5',  switches = [S0, S5])
        T6  = Tree(tree_list=tree_list_6,  empty=True, name='T6',  switches = [S7, S10])
        T7  = Tree(tree_list=tree_list_7,  empty=True, name='T7',  switches = [S0, S6])
        T8  = Tree(tree_list=tree_list_8,  empty=True, name='T8',  switches = [S9, S11, S10])
        T9  = Tree(tree_list=tree_list_9,  empty=True, name='T9',  switches = [S0, S7])
        T10 = Tree(tree_list=tree_list_10, empty=True, name='T10', switches = [S1, S2, S3, S4, S6])
        T11 = Tree(tree_list=tree_list_11, empty=True, name='T11', switches = [S0, S8])
        T12 = Tree(tree_list=tree_list_12, empty=True, name='T12', switches = [S9])
        T13 = Tree(tree_list=tree_list_13, empty=True, name='T13', switches = [S9, S10, S11])
        T14 = Tree(tree_list=tree_list_14, empty=True, name='T14', switches = [S1, S3, S2, S4, S5])
        
        position_R0 = [    3,   4,   4,    2]
        position_R1 = [    1, 1.5,   3,    1]
        position_R2 = [    6, 1.5,   3,    1]
        position_R3 = [ -0.5,   4, 1.5,    2]
        position_R4 = [    9,   4, 1.5,    2]
        position_R5 = [    1,   7,   2,    1]
        position_R6 = [    7,   7,   2,    1]
        position_R7 = [    3, 8.5,   4, 1.25]
        position_RE = [    4, 0.1,   2,    1]
        
        R0 = Room(name='R0', position = position_R0, switches_list = [S0])
        R1 = Room(name='R1', position = position_R1, switches_list = [S1, S2])
        R2 = Room(name='R2', position = position_R2, switches_list = [S3, S4])
        R3 = Room(name='R3', position = position_R3, switches_list = [S5])
        R4 = Room(name='R4', position = position_R4, switches_list = [S6])
        R5 = Room(name='R5', position = position_R5, switches_list = [S7])
        R6 = Room(name='R6', position = position_R6, switches_list = [S8])
        R7 = Room(name='R7', position = position_R7, switches_list = [S9, S10, S11])
        RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
        
        e = 0.1
        
        relative_departure_coordinates_D0  = [1/2, 1/2]
        relative_arrival_coordinates_D0    = [1/2, 1/2]
        relative_departure_coordinates_D1  = [  0,   0]
        relative_arrival_coordinates_D1    = [2/3,   1]
        relative_departure_coordinates_D2  = [  1,   1]
        relative_arrival_coordinates_D2    = [1/4,   0]
        relative_departure_coordinates_D3  = [3/4,   0]
        relative_arrival_coordinates_D3    = [  0,   1]
        relative_departure_coordinates_D4  = [1/3,   1]
        relative_arrival_coordinates_D4    = [  1,   0]
        relative_departure_coordinates_D5  = [  0, 1/4]
        relative_arrival_coordinates_D5    = [  1, 1/4]
        relative_departure_coordinates_D6  = [  1, 3/4]
        relative_arrival_coordinates_D6    = [  0, 3/4]
        relative_departure_coordinates_D7  = [  1, 1/4]
        relative_arrival_coordinates_D7    = [  0, 1/4]
        relative_departure_coordinates_D8  = [  0, 3/4]
        relative_arrival_coordinates_D8    = [  1, 3/4]
        relative_departure_coordinates_D9  = [  0,   1]
        relative_arrival_coordinates_D9    = [1/2-e,   0+e]
        relative_departure_coordinates_D10 = [  1,   0]
        relative_arrival_coordinates_D10   = [1/4+e,   1-e]
        relative_departure_coordinates_D12 = [  0,   0]
        relative_arrival_coordinates_D12   = [3/4-e,   1-e]
        relative_departure_coordinates_D11 = [  1,   1]
        relative_arrival_coordinates_D11   = [1/2+e,   0+e]
        relative_departure_coordinates_D13 = [3/8,   1]
        relative_arrival_coordinates_D13   = [3/8,   0]
        relative_departure_coordinates_D14 = [5/8,   0]
        relative_arrival_coordinates_D14   = [5/8,   1]
        
        D0  = Door(two_way = False,  
                   tree = T0,  name='D0',  
                   room_departure = R0, 
                   room_arrival = RE, 
                  relative_departure_coordinates = relative_departure_coordinates_D0, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D0)
        D1  = Door(two_way = False,  
                   tree = T1,  name='D1',  
                   room_departure = R0, 
                   room_arrival = R1, 
                  relative_departure_coordinates = relative_departure_coordinates_D1, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D1)
        D2  = Door(two_way = False,  
                   tree = T2,  
                   name='D2',  
                   room_departure = R1, 
                   room_arrival = R0, 
                  relative_departure_coordinates = relative_departure_coordinates_D2, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D2)
        D3  = Door(two_way = False,  
                   tree = T3,  
                   name='D3',  
                   room_departure = R0, 
                   room_arrival = R2, 
                  relative_departure_coordinates = relative_departure_coordinates_D3, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D3)
        D4  = Door(two_way = False,  
                   tree = T4,  
                   name='D4',  
                   room_departure = R2, 
                   room_arrival = R0, 
                  relative_departure_coordinates = relative_departure_coordinates_D4, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D4)
        D5  = Door(two_way = False,  
                   tree = T5,  
                   name='D5',  
                   room_departure = R0, 
                   room_arrival = R3, 
                  relative_departure_coordinates = relative_departure_coordinates_D5, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D5)
        D6  = Door(two_way = False,  
                   tree = T6,  
                   name='D6',  
                   room_departure = R3, 
                   room_arrival = R0, 
                  relative_departure_coordinates = relative_departure_coordinates_D6, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D6)
        D7  = Door(two_way = False,  
                   tree = T7,  
                   name='D7',  
                   room_departure = R0, 
                   room_arrival = R4, 
                  relative_departure_coordinates = relative_departure_coordinates_D7, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D7)
        D8  = Door(two_way = False,  
                   tree = T8,  
                   name='D8',  
                   room_departure = R4, 
                   room_arrival = R0, 
                  relative_departure_coordinates = relative_departure_coordinates_D8, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D8)
        D9  = Door(two_way = False,  
                   tree = T9,  
                   name='D9',  
                   room_departure = R0, 
                   room_arrival = R5, 
                  relative_departure_coordinates = relative_departure_coordinates_D9, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D9)
        D10 = Door(two_way = False,  
                   tree = T10, 
                   name='D10',  
                   room_departure = R5, 
                   room_arrival = R0, 
                  relative_departure_coordinates = relative_departure_coordinates_D10, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D10)
        D11 = Door(two_way = False,  
                   tree = T11, 
                   name='D11',  
                   room_departure = R0, 
                   room_arrival = R6, 
                  relative_departure_coordinates = relative_departure_coordinates_D11, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D11)
        D12 = Door(two_way = False,  
                   tree = T12, 
                   name='D12',  
                   room_departure = R6, 
                   room_arrival = R0, 
                  relative_departure_coordinates = relative_departure_coordinates_D12, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D12)
        D13 = Door(two_way = False,  
                   tree = T13, 
                   name='D13',  
                   room_departure = R0, 
                   room_arrival = R7, 
                  relative_departure_coordinates = relative_departure_coordinates_D13, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D13)
        D14 = Door(two_way = False,  
                   tree = T14, 
                   name='D14',  
                   room_departure = R7, 
                   room_arrival = R0, 
                  relative_departure_coordinates = relative_departure_coordinates_D14, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D14)
        
        l_help_txt = [
"""
"""]
        
        level = Maze(start_room_index=0, 
                     exit_room_index=-1, 
                     rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE], 
                     doors_list = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14], 
                     fastest_solution="S0 D1 S1 D2 D3 S4 D4 D11 S8 D12 D13 S11 S9 D14 S0 D5 S5 D6 S0 D9 S7 D10 S0 D7 S6 D8 D0", 
                     level_color=Levels_colors_list.DARK_GREEN,
                     name='Dead_ends',
                     help_txt = l_help_txt,
                     door_window_size = 500,
                     border = 50)
        
        return level
    
    def level_electricity(): 
    
        v = 0
        w = 0
        
        S0 = Switch(name='S0', value = v)
        S1 = Switch(name='S1')
        S2 = Switch(name='S2', value = v)
        S3 = Switch(name='S3')
        S4 = Switch(name='S4', value = v)
        S5 = Switch(name='S5')
        S6 = Switch(name='S6')
        S7 = Switch(name='S7', value = v)
        S8 = Switch(name='S8', value = v)
        S9 = Switch(name='S9', value = v)
        
        S10 = Switch(name='S10')
        S11 = Switch(name='S11', value = w)
        S12 = Switch(name='S12', value = w)
        S13 = Switch(name='S13')
        S14 = Switch(name='S14', value = w)
        S15 = Switch(name='S15')
        S16 = Switch(name='S16', value = w)
        S17 = Switch(name='S17', value = w)
        
        # S10 S11
        # tree_list_1a = Tree.tree_list_and_2
        # tree_list_2a = Tree.tree_list_anb
        # tree_list_3a = Tree.tree_list_bna
        # S12 S13
        # tree_list_4a = Tree.tree_list_and_2
        # tree_list_5a = Tree.tree_list_anb
        # tree_list_6a = Tree.tree_list_bna
        # S14 S15
        # tree_list_7a = Tree.tree_list_and_2
        # tree_list_8a = Tree.tree_list_anb
        # tree_list_9a = Tree.tree_list_bna
        
        # S1 S2 S3
        tree_list_1b = Tree.tree_list_FFT
        # tree_list_2b = Tree.tree_list_FTF
        # tree_list_3b = Tree.tree_list_TFF
        # S4 S5 S6
        # tree_list_4b = Tree.tree_list_FFT
        # tree_list_5b = Tree.tree_list_FTF
        tree_list_6b = Tree.tree_list_TFF
        # S7 S8 S9
        tree_list_7b = Tree.tree_list_FFT
        # tree_list_8b = Tree.tree_list_FTF
        # tree_list_9b = Tree.tree_list_TFF
        
        tree_list_0  = ['AND', [None], ['NAND_3', tree_list_1b, tree_list_6b, tree_list_7b]]
        # tree_list_1  = ['AND', tree_list_1a, tree_list_1b]
        # tree_list_2  = ['AND', tree_list_2a, tree_list_2b]
        # tree_list_3  = ['AND', tree_list_3a, tree_list_3b]
        # tree_list_4  = ['AND', ['AND', tree_list_4a, ['NOT', tree_list_2a]], tree_list_4b]
        # tree_list_5  = ['AND', ['AND', tree_list_5a, ['NOT', tree_list_1a]], tree_list_5b]
        # tree_list_6  = ['AND', ['AND', tree_list_6a, ['NOT', tree_list_3a]], tree_list_6b]
        # tree_list_7  = ['AND', ['AND', tree_list_7a, ['NOT', tree_list_5a]], tree_list_7b]
        # tree_list_8  = ['AND', ['AND', tree_list_8a, ['NOT', tree_list_6a]], tree_list_8b]
        # tree_list_9  = ['AND', ['AND', tree_list_9a, ['NOT', tree_list_4a]], tree_list_9b]
        # tree_list_10 = ['AND', ['AND', ['NOR', tree_list_2a, tree_list_4a], ['NOT', tree_list_9a]], ['AND', [None], [None]]]
        
        T0   = Tree(tree_list=tree_list_0,  
                    empty=True, 
                    name='T0',   
                    switches = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9],
                    easy_logical_expression_PN = "& S0 -& [ & ( -S1 -S2 S3 ) & ( S4 -S5 -S6 ) & ( -S7 -S8 S9 ) ]")
        T1   = Tree(tree_list=Tree.tree_list_from_str('FFTTT'),   
                    empty=True, 
                    name='T1',   
                    switches = [S1, S2, S3, S10, S11])
        T2   = Tree(tree_list=Tree.tree_list_from_str('FTFTF'),   
                    empty=True, name='T2',   
                    switches = [S1, S2, S3, S10, S11])
        T3   = Tree(tree_list=Tree.tree_list_from_str('TFFFT'),   
                    empty=True, name='T3',   
                    switches = [S1, S2, S3, S10, S11])
        T4   = Tree(tree_list=['AND', Tree.tree_list_from_str('FFTTT'), Tree.tree_list_bona],   
                    empty=True, name='T4',   
                    switches = [S4, S5, S6, S12, S13, S10, S11])
        T5   = Tree(tree_list=['AND', Tree.tree_list_from_str('FTFTF'), Tree.tree_list_nand],   
                    empty=True, name='T5',   
                    switches = [S4, S5, S6, S12, S13, S10, S11])
        T6   = Tree(tree_list=['AND', Tree.tree_list_from_str('TFFFT'), Tree.tree_list_aonb],   
                    empty=True, name='T6',   
                    switches = [S4, S5, S6, S12, S13, S10, S11])
        T7   = Tree(tree_list=['AND', Tree.tree_list_from_str('FFTTT'), Tree.tree_list_bona],   
                    empty=True, name='T7',   
                    switches = [S7, S8, S9, S14, S15, S12, S13])
        T8   = Tree(tree_list=['AND', Tree.tree_list_from_str('FTFTF'), Tree.tree_list_aonb],   
                    empty=True, name='T8',   
                    switches = [S7, S8, S9, S14, S15, S12, S13])
        T9   = Tree(tree_list=['AND', Tree.tree_list_from_str('TFFFT'), Tree.tree_list_nand],   
                    empty=True, name='T9',   
                    switches = [S7, S8, S9, S14, S15, S12, S13])
        T10  = Tree(tree_list=['AND_5', Tree.tree_list_bona, Tree.tree_list_nand, Tree.tree_list_aonb, [None], [None]],  
                    empty=True, name='T10',  
                    switches = [S10, S11, S12, S13, S14, S15, S16, S17])

        d = 0
    
        position_R0 = [ 5.25,   0-d, 6,  4+d]
        position_R1 = [ 9.75, 5.5-d, 1,  4+d]
        position_R2 = [ 6.75,   5-d, 1,4.5+d]
        position_R3 = [ 3.75, 4.5-d, 1,  5+d]
        position_R4 = [ 0.75,   4-d, 1,5.5+d]
        position_RE = [ 0.75,   0-d, 2,  2+d]
        
        R0 = Room(name='R0', position = position_R0, switches_list = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9])
        R1 = Room(name='R1', position = position_R1, switches_list = [S10, S11])
        R2 = Room(name='R2', position = position_R2, switches_list = [S12, S13])
        R3 = Room(name='R3', position = position_R3, switches_list = [S14, S15])
        R4 = Room(name='R4', position = position_R4, switches_list = [S16, S17])
        RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
        
        e = 0.02
        
        relative_departure_coordinates_D0  = [11/12,   1]
        relative_arrival_coordinates_D0    = [1/2,   0]
        relative_departure_coordinates_D1  = [  0,   e]
        relative_arrival_coordinates_D1    = [  1,   e]
        relative_departure_coordinates_D2  = [  0, 1/2]
        relative_arrival_coordinates_D2    = [  1, 1/2]
        relative_departure_coordinates_D3  = [0.1, 1-e]
        relative_arrival_coordinates_D3    = [  1, 1-e]
        relative_departure_coordinates_D4  = [  0,   e]
        relative_arrival_coordinates_D4    = [  1,   e]
        relative_departure_coordinates_D5  = [  0, 1/2]
        relative_arrival_coordinates_D5    = [  1, 1/2]
        relative_departure_coordinates_D6  = [0.1, 1-e]
        relative_arrival_coordinates_D6    = [  1, 1-e]
        relative_departure_coordinates_D7  = [  0,   e]
        relative_arrival_coordinates_D7    = [  1,   e]
        relative_departure_coordinates_D8  = [  0, 1/2]
        relative_arrival_coordinates_D8    = [  1, 1/2]
        relative_departure_coordinates_D9  = [0.1, 1-e]
        relative_arrival_coordinates_D9    = [  1, 1-e]
        relative_departure_coordinates_D10 = [1/2, 1/4]
        relative_arrival_coordinates_D10   = [1/2, 1/2]
        
        D0  = Door(two_way = False,  
                   tree = T0,  name='D0',  
                   room_departure = R0, 
                   room_arrival = R1, 
                  relative_departure_coordinates = relative_departure_coordinates_D0, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D0)
        D1  = Door(two_way = False,  
                   tree = T1,  name='D1',  
                   room_departure = R1, 
                   room_arrival = R2, 
                  relative_departure_coordinates = relative_departure_coordinates_D1, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D1)
        D2  = Door(two_way = False,  
                   tree = T2,  
                   name='D2',  
                   room_departure = R1, 
                   room_arrival = R2, 
                  relative_departure_coordinates = relative_departure_coordinates_D2, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D2)
        D3  = Door(two_way = False,  
                   tree = T3,  
                   name='D3',  
                   room_departure = R1, 
                   room_arrival = R2, 
                  relative_departure_coordinates = relative_departure_coordinates_D3, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D3)
        D4  = Door(two_way = False,  
                   tree = T4,  
                   name='D4',  
                   room_departure = R2, 
                   room_arrival = R3, 
                  relative_departure_coordinates = relative_departure_coordinates_D4, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D4)
        D5  = Door(two_way = False,  
                   tree = T5,  
                   name='D5',  
                   room_departure = R2, 
                   room_arrival = R3, 
                  relative_departure_coordinates = relative_departure_coordinates_D5, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D5)
        D6  = Door(two_way = False,  
                   tree = T6,  
                   name='D6',  
                   room_departure = R2, 
                   room_arrival = R3, 
                  relative_departure_coordinates = relative_departure_coordinates_D6, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D6)
        D7  = Door(two_way = False,  
                   tree = T7,  
                   name='D7',  
                   room_departure = R3, 
                   room_arrival = R4, 
                  relative_departure_coordinates = relative_departure_coordinates_D7, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D7)
        D8  = Door(two_way = False,  
                   tree = T8,  
                   name='D8',  
                   room_departure = R3, 
                   room_arrival = R4, 
                  relative_departure_coordinates = relative_departure_coordinates_D8, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D8)
        D9  = Door(two_way = False,  
                   tree = T9,  
                   name='D9',  
                   room_departure = R3, 
                   room_arrival = R4, 
                  relative_departure_coordinates = relative_departure_coordinates_D9, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D9)
        D10 = Door(two_way = False,  
                   tree = T10,  
                   name='D10',  
                   room_departure = R4, 
                   room_arrival = RE, 
                  relative_departure_coordinates = relative_departure_coordinates_D10, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D10)
        
        l_help_txt = [
"""NAND can also apply to 3 parameters instead of 2:

    NAND truth table [D0 = NAND ( S0 S1 S2 )]:
        S0  S1  S2  D0
          0    0    0     1
          0    1    0     1
          1    0    0     1
          1    1    0     1
          0    0    1     1
          0    1    1     1
          1    0    1     1
          1    1    1     0  
"""]
        
        level = Maze(start_room_index=0, 
                      exit_room_index=-1, 
                      rooms_list=[R0, R1, R2, R3, R4, RE], 
                      doors_list = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10],
                      fastest_solution='S0 S1 S5 S8 D0 S11 D3 S12 D5 S14 D8 S16 S17 D10',
                      level_color=Levels_colors_list.GOLD_AND_SILVER,
                      name='Electricity',
                      help_txt = l_help_txt,
                      border = 70,
                      door_window_size = 575)
        
        return level
        
    def level_fluid(): 
        
        S0 = Switch(name='S0')
        S1 = Switch(name='S1')
        S2=Switch(name='S2')
        S3 = Switch(name='S3')
        S4 = Switch(name='S4')
        S5 = Switch(name='S5')
        S6 = Switch(name='S6')
        S7 = Switch(name='S7')
        
        tree_list_0 = Tree.tree_list_anb
        tree_list_1 = Tree.tree_list_anb
        tree_list_2 = Tree.tree_list_FTT
        tree_list_3 = Tree.tree_list_from_str('FFTTTTT')
        tree_list_4 = [None]
        tree_list_5 = [None]
        
        T0  = Tree(tree_list=tree_list_0,  
                   empty=True, 
                   name='T0', 
                   switches = [S0, S4])
        T1  = Tree(tree_list=tree_list_1,  
                   empty=True, 
                   name='T1', 
                   switches = [S1, S5])
        T2  = Tree(tree_list=tree_list_2,  
                   empty=True, 
                   name='T2', 
                   switches = [S0, S2, S4]) 
        T3  = Tree(tree_list=tree_list_3,  
                   empty=True, 
                   name='T3', 
                   switches = [S0, S1, S3, S4, S5, S6, S7])
        T4  = Tree(tree_list=tree_list_4,  
                   empty=True, 
                   name='T4', 
                   switches = [S6])
        T5  = Tree(tree_list=tree_list_5,  
                   empty=True, 
                   name='T5', 
                   switches = [S7])
        
        position_R0 = [ 0, 0, 3, 2]
        position_R1 = [ 2, 3, 3, 2]
        position_R2 = [ 4, 0, 3, 2]
        position_R3 = [ 6, 3, 3, 2]
        position_RE = [ 8, 0, 3, 2]
        
        R0 = Room(name='R0', position = position_R0, switches_list = [S0, S4])
        R1 = Room(name='R1', position = position_R1, switches_list = [S1, S5])
        R2 = Room(name='R2', position = position_R2, switches_list = [S2, S6])
        R3 = Room(name='R3', position = position_R3, switches_list = [S3, S7])
        RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
        
        D0  = Door(two_way = False, tree = T0,  name='D0',  room_departure = R0, room_arrival = R1)
        D1  = Door(two_way = False, tree = T1,  name='D1',  room_departure = R1, room_arrival = R2)
        D2  = Door(two_way = False, tree = T2,  name='D2',  room_departure = R2, room_arrival = R3)
        D3  = Door(two_way = False, tree = T3,  name='D3',  room_departure = R3, room_arrival = RE)
        D4  = Door(two_way = True,  tree = T4,  name='D4',  room_departure = R0, room_arrival = R2)
        D5  = Door(two_way = True,  tree = T5,  name='D5',  room_departure = R1, room_arrival = R3)
        
        l_help_txt = [
"""A truth table tells you the result of a logical expression.
Here are some examples :

    Negation truth table (D0 = -S0):
        S0  D0
          0     1
          1     0
          
    AND truth table (D0 = & S0 S1):
        S0  S1  D0
          0    0    0
          0    1    0
          1    0    0
          1    1    1
          
    OR truth table (D0 = | S0 S1):
        S0  S1  D0
          0    0    0
          0    1    1
          1    0    1
          1    1    1
"""]
        
        level = Maze(start_room_index=0, 
                      exit_room_index=-1, 
                      rooms_list=[R0, R1, R2, R3, RE], 
                      doors_list = [D0, D1, D2, D3, D4, D5],
                      fastest_solution='S0 D0 S1 D1 S2 S6 D4 S0 S4 D4 D2 S3 S7 D5 S1 S5 D5 D3',
                      level_color=Levels_colors_list.BRIGHT_BLUE,
                      name='Fluid',
                      help_txt = l_help_txt)
        return level
    
    def level_graph():
        
        S0  = Switch(name='S0')
        S1  = Switch(name='S1')
        S2  = Switch(name='S2')
        S3  = Switch(name='S3')
        S4  = Switch(name='S4')
        S5  = Switch(name='S5')
        S6  = Switch(name='S6')
        S7  = Switch(name='S7')
        S8  = Switch(name='S8')
        S9  = Switch(name='S9')
        S10 = Switch(name='S10')
        S11 = Switch(name='S11')
        S12 = Switch(name='S12')
        S13 = Switch(name='S13')
        S14 = Switch(name='S14')
        
        T0   = Tree(tree_list=['AND_6', [None], [None], [None], [None], Tree.tree_list_nand, Tree.tree_list_xnor],  
                    empty=True, name='T0',  switches = [S3, S11, S13, S14, S1, S10, S6, S12])
        T5  = Tree(tree_list=[None],  empty=True, name='T5', switches = [S2])
        T7   = Tree(tree_list=[None],  empty=True, name='T7',  switches = [S4])
        T11  = Tree(tree_list=[None],  empty=True, name='T11', switches = [S8])
        T14  = Tree(tree_list=[None],  empty=True, name='T14', switches = [S9])
        T17  = Tree(tree_list=[None],  empty=True, name='T17', switches = [S13])

        T4   = Tree(tree_list=Tree.tree_list_not,  empty=True, name='T4',  switches = [S2])
        T6   = Tree(tree_list=['AND_4', Tree.tree_list_not, Tree.tree_list_xor, Tree.tree_list_xor, Tree.tree_list_xor],
                                 empty=True, name='T6',  switches = [S3, S1, S6, S7, S10, S10, S12])
        T8   = Tree(tree_list=Tree.tree_list_not,  empty=True, name='T8',  switches = [S4])
        T9   = Tree(tree_list=Tree.tree_list_not,  empty=True, name='T9',  switches = [S9])
        T13  = Tree(tree_list=Tree.tree_list_not,  empty=True, name='T13', switches = [S8])
        T18  = Tree(tree_list=Tree.tree_list_not,  empty=True, name='T18', switches = [S13])
        
        T1   = Tree(tree_list=Tree.tree_list_anb,  empty=True, name='T1',  switches = [S0, S1])
        T3   = Tree(tree_list=[None],  empty=True, name='T3',  switches = [S0])
        T15  = Tree(tree_list=Tree.tree_list_xor,  empty=True, name='T15', switches = [S5, S9])
        T10  = Tree(tree_list=Tree.tree_list_not,  empty=True, name='T10', switches = [S5])
        T16  = Tree(tree_list=Tree.tree_list_nand,  empty=True, name='T16', switches = [S8, S14])
        T12  = Tree(tree_list=Tree.tree_list_xnor,  empty=True, name='T12', switches = [S8, S14])
        
        T2   = Tree(tree_list=Tree.tree_list_from_str('T'*6),  empty=True, name='T2',  
                    switches = [S0, S2, S3, S4, S8, S9])
        
        c = 2
        e = 0.15
        
        position_RE =  [12,  0,  c,  c]
        position_R0  = [ 8-e,  0-e,  c+2*e,  c+2*e]
        position_R1  = [ 4,  0,  c,  c]
        position_R2  = [ 0,  0,  c,  c]
        position_R3  = [12,  4,  c,  c]
        position_R4  = [ 8,  4,  c,  c]
        position_R5  = [ 4-e,  4-e,  c+2*e,  c+2*e]
        position_R6  = [ 0-e,  4-e,  c+2*e,  c+2*e]
        position_R7  = [12-e,  8-e,  c+2*e,  c+2*e]
        position_R8  = [ 8,  8,  c,  c]
        position_R9  = [ 4,  8,  c,  c]
        position_R10 = [ 0,  8,  c,  c]
        position_R11 = [12, 12,  c,  c]
        position_R12 = [ 8-e, 12-e,  c+2*e,  c+2*e]
        position_R13 = [ 4, 12,  c,  c]
        position_R14 = [ 0-e, 12-e,  c+2*e,  c+2*e]
        
        
        R0  = Room(name='R0',  position = position_R0,  switches_list = [S0])
        R1  = Room(name='R1',  position = position_R1,  switches_list = [S1])
        R2  = Room(name='R2',  position = position_R2,  switches_list = [S2])
        R3  = Room(name='R3',  position = position_R3,  switches_list = [S3])
        R4  = Room(name='R4',  position = position_R4,  switches_list = [S4])
        R5  = Room(name='R5',  position = position_R5,  switches_list = [S5])
        R6  = Room(name='R6',  position = position_R6,  switches_list = [S6])
        R7  = Room(name='R7',  position = position_R7,  switches_list = [S7])
        R8  = Room(name='R8',  position = position_R8,  switches_list = [S8])
        R9  = Room(name='R9',  position = position_R9,  switches_list = [S9])
        R10 = Room(name='R10', position = position_R10, switches_list = [S10])
        R11 = Room(name='R11', position = position_R11, switches_list = [S11])
        R12 = Room(name='R12', position = position_R12, switches_list = [S12])
        R13 = Room(name='R13', position = position_R13, switches_list = [S13])
        R14 = Room(name='R14', position = position_R14, switches_list = [S14])
        RE  = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
        
        b = False
        
        D0  = Door(two_way = b, tree = T0,  room_departure = R3, room_arrival = R0)
        D1  = Door(two_way = b, tree = T1,  room_departure = R0, room_arrival = R1)
        D2  = Door(two_way = b, tree = T2,  room_departure = R0, room_arrival = RE)
        D3  = Door(two_way = b, tree = T3,  room_departure = R1, room_arrival = R5)
        D4  = Door(two_way = b, tree = T4,  room_departure = R5, room_arrival = R2)
        D5  = Door(two_way = b, tree = T5,  room_departure = R2, room_arrival = R6)
        D6  = Door(two_way = b, tree = T6,  room_departure = R7, room_arrival = R3)
        D7  = Door(two_way = b, tree = T7,  room_departure = R4, room_arrival = R5)
        D8  = Door(two_way = b, tree = T8,  room_departure = R7, room_arrival = R4)
        D9  = Door(two_way = b, tree = T9,  room_departure = R5, room_arrival = R9) 
        D10 = Door(two_way = b, tree = T10, room_departure = R6, room_arrival = R10)
        D11 = Door(two_way = b, tree = T11, room_departure = R8, room_arrival = R7)
        D12 = Door(two_way = b, tree = T12, room_departure = R11, room_arrival = R7)
        D13 = Door(two_way = b, tree = T13, room_departure = R14, room_arrival = R8, 
                   relative_departure_coordinates=[1,0], relative_arrival_coordinates=[0,1])
        D14 = Door(two_way = b, tree = T14, room_departure = R9, room_arrival = R14,
                   relative_arrival_coordinates=[0.3, 0.5])
        D15 = Door(two_way = b, tree = T15, room_departure = R10, room_arrival = R14)
        D16 = Door(two_way = b, tree = T16, room_departure = R12, room_arrival = R11)
        D17 = Door(two_way = b, tree = T17, room_departure = R13, room_arrival = R12)
        D18 = Door(two_way = b, tree = T18, room_departure = R14, room_arrival = R13)
        
        l_help_txt = [ 
""
]
        
        level = Maze(start_room_index=0, 
                     exit_room_index=-1, 
                     rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, RE], 
                     doors_list = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18], 
                     fastest_solution="S0 D1 D3 D9 S9 D14 D18 S13 D17 S12 D16 S11 D12 D8 S4 D7 D4 S2 D5 S6 D10 D15 S14 D13 S8 D11 S7 D6 S3 D0 D2",
                     level_color=Levels_colors_list.BLACK_AND_BLUE,
                     name='Graph',
                     help_txt = l_help_txt,
                     door_window_size = 550)
        
        return level
    
    def level_hello_world():
        
        S0 = Switch(name='S0')
        S1 = Switch(name='S1')
        
        T0 = Tree(tree_list=[None], 
                  empty=True, 
                  name='T0', 
                  switches = [S0])
        T1 = Tree(tree_list=[None], 
                  empty=True, 
                  name='T1', 
                  switches = [S1])
        T2 = Tree(tree_list=Tree.tree_list_or_2, 
                  empty=True, 
                  name='T2', 
                  switches = [S0, S1], 
                  easy_logical_expression_PN = 'OR S0 S1\n= | S0 S1')
        
        c = 1
        e = 0.6
        
        position_R0 = [0,0,c,c]
        position_R1 = [e+c,0,c,c]
        position_R2 = [2*(e+c),0,c,c]
        position_RE = [3*(e+c),0,c,c]
        
        R0 = Room(name='R0', position = position_R0, switches_list = [S0])
        R1 = Room(name='R1', position = position_R1, switches_list = [S1])
        R2 = Room(name='R2', position = position_R2, switches_list = [])
        RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
        
        D0 = Door(two_way = True, 
                  tree = T0, 
                  name='D0', 
                  room_departure = R0, 
                  room_arrival = R1)
        D1 = Door(two_way = True, 
                  tree = T1, 
                  name='D1', 
                  room_departure = R1, 
                  room_arrival = R2)
        D2 = Door(two_way = False, 
                  tree = T2, 
                  name='D2', 
                  room_departure = R2, 
                  room_arrival = RE)
        
        l_help_txt = [                 
"""Your mission is getting to the exit.

There are differents elements in this game :
        Rooms (R0, R1, R2, ..., EXIT) :  
                The room inside which you are is surrounded.
        Switches (S0, S1, S2, ...) : 
                If a switch is turned on, it is surrounded, and you say it is equal to 1.
                If it is turned off, it is equal to 0.
                To turn on a switch, write its name and press enter.
        Doors (D0, D1, D2, ...) :    
                If a door is opened, it is surrounded, and you say it is equal to 1.
                If it is closed, it is equal to 0.
                To use a door, write its name and press enter.
                Diamond-shape doors are two-way while triangle-shaped doors are one-way only.      
If you made a mistake when taping the name of a door or a switch, you can always erase it by taping on the backspace key.
        
On the left size window of the game are equations that tell you when a door is open :
    (These equations work with any name of door or switch.)
    D0 = S0 means : 
            D0 is opened if S0 is turned on.
    D2 = OR S1 S2 means :
            D1 is opened if S1 or S2 is turned on (i.e. if (S0, S1) = (0,1) or (S0, S1) = (1,0) or (S0, S1) = (1,1))
            It can also be written : D2 = | S1 S2
        
To leave the help menu (or come back to it), press [H].
To start the level again from the beginning, press [B].
To go to the next level, press the right arrow key.
"""]
# To change the doors' notation, press [N]. -> depretated but it will maybe come back
        

        level = Maze(start_room_index=0, 
                     exit_room_index=-1, 
                     rooms_list=[R0, R1, R2, RE], 
                     doors_list = [D0, D1, D2], 
                     fastest_solution="S0 D0 S1 D1 D2",
                     level_color=Levels_colors_list.GREY,
                     name='Hello_World',
                     help_txt = l_help_txt,
                     door_window_size = 500,
                     keep_proportions = True)
        
        return level
        
    def level_infinity(): 
    
        S0 = Switch(name='S0')
        S1 = Switch(name='S1')
        S2=Switch(name='S2')
        S3 = Switch(name='S3')
        S4 = Switch(name='S4')
        S5 = Switch(name='S5')
        S6 = Switch(name='S6')
        S7 = Switch(name='S7')
        S8 = Switch(name='S8')
        S9 = Switch(name='S9')
        
        tree_list_0 = Tree.tree_list_anb
        tree_list_1 = Tree.tree_list_and_2
        tree_list_2 = Tree.tree_list_and_2
        tree_list_3 = Tree.tree_list_anb
        tree_list_4 = Tree.tree_list_and_2
        tree_list_5 = Tree.tree_list_and_3
        tree_list_6 = Tree.tree_list_and_2
        tree_list_7 = Tree.tree_list_anb
        tree_list_8 = Tree.tree_list_anb
        tree_list_9 = Tree.tree_list_anb
        tree_list_10 = Tree.tree_list_and_10
         
        T0  = Tree(tree_list=tree_list_0,  empty=True, name='T0', switches = [S0, S5])
        T8  = Tree(tree_list=tree_list_8,  empty=True, name='T8', switches = [S1, S6])
        T3  = Tree(tree_list=tree_list_3,  empty=True, name='T3', switches = [S3, S8])
        T9  = Tree(tree_list=tree_list_9,  empty=True, name='T9', switches = [S4, S9])
        T7  = Tree(tree_list=tree_list_7,  empty=True, name='T7', switches = [S2, S7])
        
        T4  = Tree(tree_list=tree_list_4,  empty=True, name='T4', switches = [S0, S2])
        T6  = Tree(tree_list=tree_list_6,  empty=True, name='T6', switches = [S0, S2])
        T1  = Tree(tree_list=tree_list_1,  empty=True, name='T1', switches = [S0, S2])
        T2  = Tree(tree_list=tree_list_2,  empty=True, name='T2', switches = [S0, S2])
        T5  = Tree(tree_list=tree_list_5,  empty=True, name='T5', switches = [S0, S2, S5])

        T10 = Tree(tree_list=tree_list_10, empty=True,name='T10', switches = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9])
        
        position_R0 = [4, 3,2,2]
        position_R1 = [8, 6,2,2]
        position_R2 = [6,10,2,2]
        position_R3 = [2,10,2,2]
        position_R4 = [0, 6,2,2]
        position_RE = [7.5, 3.25,1,1]
        
        R0 = Room(name='R0', position = position_R0, switches_list = [S0, S5])
        R1 = Room(name='R1', position = position_R1, switches_list = [S1, S6])
        R2 = Room(name='R2', position = position_R2, switches_list = [S2, S7])
        R3 = Room(name='R3', position = position_R3, switches_list = [S3, S8])
        R4 = Room(name='R4', position = position_R4, switches_list = [S4, S9])
        RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
        
        D0  = Door(two_way = False,  tree = T0,  name='D0',  room_departure = R0, room_arrival = R1)
        D1  = Door(two_way = False,  tree = T1,  name='D1',  room_departure = R1, room_arrival = R2)
        D2  = Door(two_way = False,  tree = T2,  name='D2',  room_departure = R2, room_arrival = R3)
        D3  = Door(two_way = False,  tree = T3,  name='D3',  room_departure = R3, room_arrival = R4)
        D4  = Door(two_way = False,  tree = T4,  name='D4',  room_departure = R0, room_arrival = R4)
        D5  = Door(two_way = False,  tree = T5,  name='D5',  room_departure = R3, room_arrival = R0)
        D6  = Door(two_way = False,  tree = T6,  name='D6',  room_departure = R4, room_arrival = R1)
        D7  = Door(two_way = False,  tree = T7,  name='D7',  room_departure = R2, room_arrival = R0)
        D8  = Door(two_way = False,  tree = T8,  name='D8',  room_departure = R1, room_arrival = R3)
        D9  = Door(two_way = False,  tree = T9,  name='D9',  room_departure = R4, room_arrival = R2)
        D10 = Door(two_way = False,  tree = T10, name='D10',  room_departure = R0, room_arrival = RE)
        
        l_help_txt = [
"""A cheat code exists.
If you add the letter A before a command :
    You can turn on a switch even if you are not in its room.
    You can use a door even if it is not open.
    If a door is one-way, you can use it even if you are not in the good room. 
    
Writing A D10 allows you to end this level by cheating.

You can also use the cheat code to go directly in a room by giving its name :
    A R2 allows you to go in the room R2.
The name of the exit room is RE.

"""]
        
        level = Maze(start_room_index=0, 
                      exit_room_index=-1, 
                      rooms_list=[R0, R1, R2, R3, R4, RE], 
                      doors_list = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10],
                      fastest_solution='S0 D0 S1 D8 S3 D3 S4 D9 S2 D7 S5 D4 S9 D6 S6 D1 S7 D2 S8 D5 D10',
                      level_color=Levels_colors_list.BLACK_AND_YELLOW,
                      name='Infinity',
                      help_txt = l_help_txt,
                      border = 50,
                      keep_proportions=False)
        return level
    
    def level_icone():
        
        # Only used to make the icone of the game
        
        S0 = Switch(name='S0')
        
        T0 = Tree(tree_list=[None], 
                  empty=True, 
                  name='T0', 
                  switches = [S0])
        
        c = 1.5
        
        position_R0 = [0,0,c,c]
        position_RE = [2,0,c,c]
        
        R0 = Room(name='R0', position = position_R0, switches_list = [S0])
        RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
        
        D0 = Door(two_way = True, 
                  tree = T0, 
                  name='D0', 
                  room_departure = R0, 
                  room_arrival = RE)
        
        l_help_txt = [                 
"""
"""]
# To change the doors' notation, press [N]. -> depretated but it will maybe come back
        

        level = Maze(start_room_index=0, 
                     exit_room_index=-1, 
                     rooms_list=[R0, RE], 
                     doors_list = [D0], 
                     fastest_solution="S0 D0",
                     level_color=Levels_colors_list.BLACK_AND_WHITE_2,
                     name='Icone',
                     help_txt = l_help_txt,
                     door_window_size = 500,
                     keep_proportions = True)
        
        return level
        
    def level_linear(): 
        
        S0 = Switch(name='S0')
        S1 = Switch(name='S1')
        S2=Switch(name='S2')
        S3 = Switch(name='S3')
        S4 = Switch(name='S4')
        S5 = Switch(name='S5')
        S6 = Switch(name='S6')
        S7 = Switch(name='S7')
        
        tree_list_0 = Tree.tree_list_and_2
        tree_list_1 = Tree.tree_list_anb
        tree_list_2 = Tree.tree_list_bna
        tree_list_3 = Tree.tree_list_nor
        
        T0 = Tree(tree_list=tree_list_0, empty=True, name='T0', switches = [S0, S1], easy_logical_expression_PN = 'AND S0 S1\n= & S0 S1')
        T1 = Tree(tree_list=tree_list_1, empty=True, name='T1', switches = [S2, S3], easy_logical_expression_PN = 'AND S2 NOT S3\n= & S2 - S3')
        T2 = Tree(tree_list=tree_list_2, empty=True, name='T2', switches = [S4, S5], easy_logical_expression_PN = 'AND NOT S4 S5\n= & - S2 S3')
        T3 = Tree(tree_list=tree_list_3, empty=True, name='T3', switches = [S6, S7], easy_logical_expression_PN = 'NOR S6 S7\n= & - S6 - S7\n= -| S6 S7')
        
        position_R0 = [ 1,  16,  12, 2]
        position_R1 = [ 2,  12,  10, 2]
        position_R2 = [ 3,   8,  8,  2]
        position_R3 = [ 4,   4,  6,  2]
        position_RE = [ 5,   0,  4,  2]
        
        R0 = Room(name='R0', position = position_R0, switches_list = [S0, S1])
        R1 = Room(name='R1', position = position_R1, switches_list = [S2, S3])
        R2 = Room(name='R2', position = position_R2, switches_list = [S4, S5])
        R3 = Room(name='R3', position = position_R3, switches_list = [S6, S7])
        RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
        
        D0 = Door(two_way = True, 
                  tree = T0, 
                  name='D0', 
                  room_departure = R0, 
                  room_arrival = R1)
        D1 = Door(two_way = True, 
                  tree = T1, 
                  name='D1', 
                  room_departure = R1, 
                  room_arrival = R2)
        D2 = Door(two_way = True, 
                  tree = T2, 
                  name='D2', 
                  room_departure = R2, 
                  room_arrival = R3)
        D3 = Door(two_way = True, 
                  tree = T3, 
                  name='D3', 
                  room_departure = R3, 
                  room_arrival = RE)
        
        l_help_txt = [
"""Several new notations are used in this level :
    
    Negation :
        NOT S0 = 1 if S0 = 0
        NOT S0 = 0 if S0 = 1
        -S0 = NOT S0
        Be carefull with the negation, because you have :
            - 1 = 0
            - 0 = 1
        
    D0 = AND S0 S1 means :
        D0 is opened if (S0, S1) = (1,1)
        It can also be written : 
            D2 = & S0 S1
        
    By combining these notations, you can write :
        D1 = & S2 - S3 means :
            D1 is opened if (S2, S3) = (1,0)
        D2 = AND - S4 S5 means :
            D2 is opened if (S4, S5) = (0,1)
        D3 = & - S6 - S7  S6 S7 means :
            D3 is opened if (S6, S7) = (0,0)
            It can also be written :
                D3 = NOR S6 S7
                D3 = -| S6 S7
"""]
        
        level = Maze(start_room_index=0, 
                     exit_room_index=-1, 
                     rooms_list=[R0, R1, R2, R3, RE], 
                     doors_list = [D0, D1, D2, D3], 
                     fastest_solution='S0 S1 D0 S2 D1 S5 D2 D3',
                     level_color=Levels_colors_list.BRIGHT_GREEN,
                     name='Linear',
                     help_txt = l_help_txt,
                     door_window_size = 500,
                     keep_proportions = True)
        
        return level
      
    def level_loop():
    
        S0 = Switch(name='S0')
        S1 = Switch(name='S1')
        S2=Switch(name='S2')
        S3 = Switch(name='S3')
        
        tree_list_0 = [None] # S0
        tree_list_1 = [None] # S1
        tree_list_2 = [None] # S2
        tree_list_3 = Tree.tree_list_bna
        
        T0 = Tree(tree_list=tree_list_0, empty=True, name='T0', switches = [S0])
        T1 = Tree(tree_list=tree_list_1, empty=True, name='T1', switches = [S1])
        T2 = Tree(tree_list=tree_list_2, empty=True, name='T2', switches = [S2])
        T3 = Tree(tree_list=tree_list_3, empty=True, name='T3', switches = [S0, S3])
        
        position_R0 = [1,0,2,2]
        position_R1 = [4,1,2,2]
        position_R2 = [3,4,2,2]
        position_RE = [0,3,2,2]
        
        R0 = Room(name='R0', position = position_R0, switches_list = [S0])
        R1 = Room(name='R1', position = position_R1, switches_list = [S1])
        R2 = Room(name='R2', position = position_R2, switches_list = [S2, S3])
        RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
        
        D0 = Door(two_way = False, tree = T0, name='D0', room_departure = R0, room_arrival = R1)
        D1 = Door(two_way = False, tree = T1, name='D1', room_departure = R1, room_arrival = R2)
        D2 = Door(two_way = False, tree = T2, name='D2', room_departure = R2, room_arrival = R0)
        D3 = Door(two_way = False, tree = T3, name='D3', room_departure = R0, room_arrival = RE)
        
        l_help_txt = [
"""To change level, you can use :
    
    the right arrow key to go to the next level
    the left arrow key to go to the previous level
    the down arrow key to go to the first level
    the up arrow key to go to the last level
    
    L and the number of the level you want to go to.
    For instance, L12 will make you go to the level number 12.
"""]
        
        level = Maze(start_room_index=0, 
                     exit_room_index=-1, 
                     rooms_list=[R0, R1, R2, RE], 
                     doors_list = [D0, D1, D2, D3], 
                     fastest_solution='S0 D0 S1 D1 S2 S3 D2 S0 D3',
                     level_color=Levels_colors_list.BRIGHT_RED,
                     name='Loop',
                     help_txt = l_help_txt,
                     door_window_size = 500,
                     border = 60,
                     keep_proportions = True)
        
        return level
    
    def level_odd(): 
    
        S0 = Switch(name='S0')
        S1 = Switch(name='S1')
        S2=Switch(name='S2')
        S3 = Switch(name='S3')
        S4 = Switch(name='S4')
        
        tree_list_0 = Tree.tree_list_and_5
        tree_list_5 = Tree.tree_list_nor
        tree_list_4 = Tree.tree_list_bna
        tree_list_6 = Tree.tree_list_anb
        tree_list_1 = Tree.tree_list_FTF
        tree_list_2 = Tree.tree_list_FFT
        tree_list_3 = Tree.tree_list_from_str('TTTF')
        
        T0 = Tree(tree_list=tree_list_0, empty=True, name='T0', switches = [S0, S1, S2, S3, S4])
        T1 = Tree(tree_list=tree_list_1, empty=True, name='T1', switches = [S0, S1, S4])
        T2 = Tree(tree_list=tree_list_2, empty=True, name='T2', switches = [S0, S2, S4])
        T3 = Tree(tree_list=tree_list_3, empty=True, name='T3', switches = [S0, S1, S3, S4])
        T4 = Tree(tree_list=tree_list_4, empty=True, name='T4', switches = [S0, S4])
        T5 = Tree(tree_list=tree_list_5, empty=True, name='T5', switches = [S0, S4])
        T6 = Tree(tree_list=tree_list_6, empty=True, name='T6', switches = [S0, S4])
        
        position_R0 = [3,3,2,2]
        position_R1 = [3,0,2,2]
        position_R2 = [0,6.5,2,2]
        position_R3 = [6,6.5,2,2]
        position_RE = [3,6,2,2]
        
        R0 = Room(name='R0', position = position_R0, switches_list = [S0, S4])
        R1 = Room(name='R1', position = position_R1, switches_list = [S1])
        R2 = Room(name='R2', position = position_R2, switches_list = [S2])
        R3 = Room(name='R3', position = position_R3, switches_list = [S3])
        RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
        
        a = 0
        b = 1
        
        relative_departure_coordinates_D2 = [a, b]
        relative_arrival_coordinates_D2   = [b, a]
        relative_departure_coordinates_D3 = [b, b]
        relative_arrival_coordinates_D3   = [a, a]
        relative_departure_coordinates_D4 = [a, a]
        relative_arrival_coordinates_D4   = [a, a]
        relative_departure_coordinates_D5 = [b, a]
        relative_arrival_coordinates_D5   = [b, a]
        relative_departure_coordinates_D6 = [b, b]
        relative_arrival_coordinates_D6   = [a, b]
        
        D0  = Door(two_way = True,  
                   tree = T0,  
                   name='D0',  
                   room_departure = R0, 
                   room_arrival = RE)
        D1  = Door(two_way = True,  
                   tree = T1,  
                   name='D1',  
                   room_departure = R0, 
                   room_arrival = R1)
        D2  = Door(two_way = True,  
                   tree = T2,  name='D2',  
                   room_departure = R0, 
                   room_arrival = R2,
                   relative_departure_coordinates = relative_departure_coordinates_D2,
                   relative_arrival_coordinates = relative_arrival_coordinates_D2)
        D3  = Door(two_way = True,  
                   tree = T3,  name='D3',  
                   room_departure = R0, 
                   room_arrival = R3,
                   relative_departure_coordinates = relative_departure_coordinates_D3,
                   relative_arrival_coordinates = relative_arrival_coordinates_D3)
        D4  = Door(two_way = True,  
                   tree = T4,  name='D4',  
                   room_departure = R1, 
                   room_arrival = R2,
                   relative_departure_coordinates = relative_departure_coordinates_D4,
                   relative_arrival_coordinates = relative_arrival_coordinates_D4)
        D5  = Door(two_way = True,  
                   tree = T5,  name='D5',  
                   room_departure = R1, 
                   room_arrival = R3,
                   relative_departure_coordinates = relative_departure_coordinates_D5,
                   relative_arrival_coordinates = relative_arrival_coordinates_D5)
        D6  = Door(two_way = True,  
                   tree = T6,  name='D6',  
                   room_departure = R2, 
                   room_arrival = R3,
                   relative_departure_coordinates = relative_departure_coordinates_D6,
                   relative_arrival_coordinates = relative_arrival_coordinates_D6)
        
        l_help_txt = [
"""
To leave the game, you can click an the cross but also press [Q] or [ESCAPE].
"""]
        
        level = Maze(start_room_index=0, 
                     exit_room_index=-1, 
                     rooms_list=[R0, R1, R2, R3, RE], 
                     doors_list = [D0, D1, D2, D3, D4, D5, D6],
                     fastest_solution='S4 D2 D4 S1 D4 D2 S4 D1 D5 S3 D5 D1 S0 D3 D6 S2 D6 D3 S4 D0', 
                     level_color=Levels_colors_list.PURPLE,
                     name='Odd',
                     help_txt = l_help_txt,
                     border = 60,
                     door_window_size = 500,
                     keep_proportions = True)
        
        return level
    
    def level_parallel(): 
        
        S0  = Switch(name='S0')
        S1  = Switch(name='S1')
        S2  = Switch(name='S2')
        S3  = Switch(name='S3')
        S4  = Switch(name='S4')
        S5  = Switch(name='S5')
        
        tree_list=Tree.tree_list_anb
        tree_list_4 = Tree.tree_list_FTT
        
        T0  = Tree(tree_list=tree_list,    empty=True, name='T0',  switches = [S0, S3])
        T1  = Tree(tree_list=tree_list,    empty=True, name='T1',  switches = [S1, S4])
        T2  = Tree(tree_list=tree_list,    empty=True, name='T2',  switches = [S2, S5])
        T3  = Tree(tree_list=tree_list,    empty=True, name='T3',  switches = [S0, S3])
        T4  = Tree(tree_list=tree_list_4,  empty=True, name='T4',  switches = [S1, S4, S5])
        T5  = Tree(tree_list=tree_list,    empty=True, name='T5',  switches = [S2, S5])
        T6  = Tree(tree_list=Tree.tree_list_and_6,  empty=True, name='T6',  switches = [S0, S1, S2, S3, S4, S5])
        
        position_R0 = [  0,   0,   6,    1]
        position_R1 = [  3,   2,   2,    1]
        position_R2 = [  0,   4,   6,    1]
        position_RE = [  1,   2,   1,    1]
        
        R0 = Room(name='R0', position = position_R0, switches_list = [S0, S3])
        R1 = Room(name='R1', position = position_R1, switches_list = [S1, S4])
        R2 = Room(name='R2', position = position_R2, switches_list = [S2, S5])
        RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
        
        relative_departure_coordinates_D0  = [1/2,   1]
        relative_arrival_coordinates_D0    = [  0,   0]
        relative_departure_coordinates_D1  = [  0,   1]
        relative_arrival_coordinates_D1    = [1/2,   0]
        relative_departure_coordinates_D2  = [0.01,   0]
        relative_arrival_coordinates_D2    = [0.01,   1]
        relative_departure_coordinates_D3  = [  1,   0]
        relative_arrival_coordinates_D3    = [5/6,   1]
        relative_departure_coordinates_D4  = [5/6,   0]
        relative_arrival_coordinates_D4    = [  1,   1]
        relative_departure_coordinates_D5  = [0.99,   1]
        relative_arrival_coordinates_D5    = [0.99,   0]
        relative_departure_coordinates_D6  = [1.5/6,   1]
        relative_arrival_coordinates_D6    = [1/2,   0]
        
        D0  = Door(two_way = False,  
                   tree = T0,  name='D0',  
                   room_departure = R0, 
                   room_arrival = R1, 
                  relative_departure_coordinates = relative_departure_coordinates_D0, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D0)
        D1  = Door(two_way = False,  
                   tree = T1,  name='D1',  
                   room_departure = R1, 
                   room_arrival = R2, 
                  relative_departure_coordinates = relative_departure_coordinates_D1, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D1)
        D2  = Door(two_way = False,  
                   tree = T2,  
                   name='D2',  
                   room_departure = R2, 
                   room_arrival = R0, 
                  relative_departure_coordinates = relative_departure_coordinates_D2, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D2)
        D3  = Door(two_way = False,  
                   tree = T3,  
                   name='D3',  
                   room_departure = R1, 
                   room_arrival = R0, 
                  relative_departure_coordinates = relative_departure_coordinates_D3, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D3)
        D4  = Door(two_way = False,  
                   tree = T4,  
                   name='D4',  
                   room_departure = R2, 
                   room_arrival = R1, 
                  relative_departure_coordinates = relative_departure_coordinates_D4, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D4)
        D5  = Door(two_way = False,  
                   tree = T5,  
                   name='D5',  
                   room_departure = R0, 
                   room_arrival = R2, 
                  relative_departure_coordinates = relative_departure_coordinates_D5, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D5)
        D6  = Door(two_way = False,  
                   tree = T6,  
                   name='D6',  
                   room_departure = R0, 
                   room_arrival = RE, 
                  relative_departure_coordinates = relative_departure_coordinates_D6, 
                  relative_arrival_coordinates = relative_arrival_coordinates_D6)
        
        l_help_txt = [ 
""
]
        
        """[Reminder] : To change the doors' notation, press [N].

        There are 2 notations :
            The first one is the easy one.
            The second one only uses the symbols &, | and -.
        """
        
        level = Maze(start_room_index=0, 
                     exit_room_index=-1, 
                     rooms_list=[R0, R1, R2, RE], 
                     doors_list = [D0, D1, D2, D3, D4, D5, D6], 
                     fastest_solution='S0 D0 S1 D1 S2 D2 D0 S1 S4 D3 D5 S5 D4 S1 D3 S3 D6', 
                     level_color=Levels_colors_list.PINK,
                     name='Parallel',
                     help_txt = l_help_txt,
                     border = 50)
        
        return level
    
    def level_point_of_no_return():
        
        S0 = Switch(name='S0')
        S1 = Switch(name='S1')
        S2=Switch(name='S2')
        S3 = Switch(name='S3')
        S4 = Switch(name='S4')
        S5 = Switch(name='S5')
        S6 = Switch(name='S6')
        S7 = Switch(name='S7')
        S8 = Switch(name='S8')
        S9 = Switch(name='S9')
        
        tree_list_0 = [None] 
        tree_list_1 = ['AND', Tree.tree_list_xnor, [None]]
        tree_list_2 = ['AND', Tree.tree_list_xor, [None]]
        tree_list_3 = ['AND', Tree.tree_list_or_2, [None]]
        tree_list_4 = ['AND', Tree.tree_list_xor, [None]]
        tree_list_5 = Tree.tree_list_and_5
        
        T0 = Tree(tree_list=tree_list_0, empty=True, name='T0', switches = [S0])
        T1 = Tree(tree_list=tree_list_1, empty=True, name='T1', switches = [S5, S7, S9],
                  easy_logical_expression_PN = "& S9 XNOR S5 S7\n= & S9 -^ S5 S7")
        T2 = Tree(tree_list=tree_list_2, empty=True, name='T2', switches = [S6, S7, S9],
                  easy_logical_expression_PN = "& S9 XOR S6 S7\n= & S9 ^ S6 S7")
        T3 = Tree(tree_list=tree_list_3, empty=True, name='T3', switches = [S5, S8, S9])
        T4 = Tree(tree_list=tree_list_4, empty=True, name='T4', switches = [S6, S8, S9],
                  easy_logical_expression_PN = "& S9 XOR S6 S8\n= & S9 ^ S6 S8")
        T5 = Tree(tree_list=tree_list_5, empty=True, name='T5', switches = [S1, S2, S3, S4, S9])
        
        position_R0 = [  0,   2,  3,  4]
        position_R1 = [3.5,   0,  2,  2]
        position_R2 = [3.5,   6,  2,  2]
        position_R3 = [6.5,   0,  2,  2]
        position_R4 = [6.5,   6,  2,  2]
        position_R5 = [4.5, 3.5,  3,  1]
        position_RE = [  9,3.25,1.5,1.5]
        
        R0 = Room(name='R0', position = position_R0, switches_list = [S0, S5, S6, S7, S8])
        R1 = Room(name='R1', position = position_R1, switches_list = [S1])
        R2 = Room(name='R2', position = position_R2, switches_list = [S2])
        R3 = Room(name='R3', position = position_R3, switches_list = [S3])
        R4 = Room(name='R4', position = position_R4, switches_list = [S4])
        R5 = Room(name='R5', position = position_R5, switches_list = [S9])
        RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
        
        relative_departure_coordinates_D0 = [1, 1/2]
        relative_arrival_coordinates_D0   = [0, 1/2]
        relative_departure_coordinates_D1 = [1/3, 0]
        relative_arrival_coordinates_D1   = [1/2, 1]
        relative_departure_coordinates_D2 = [1/3, 1]
        relative_arrival_coordinates_D2   = [1/2, 0]
        relative_departure_coordinates_D3 = [2/3, 0]
        relative_arrival_coordinates_D3   = [1/2, 1]
        relative_departure_coordinates_D4 = [2/3, 1]
        relative_arrival_coordinates_D4   = [1/2, 0]
        relative_departure_coordinates_D5 = [1, 1/2]
        relative_arrival_coordinates_D5   = [0, 1/2]
        
        D0 = Door(two_way = False,
                  tree = T0, 
                  name='D0', 
                  room_departure = R0, 
                  room_arrival = R5,
                  relative_departure_coordinates = relative_departure_coordinates_D0,
                  relative_arrival_coordinates = relative_arrival_coordinates_D0)
        D1 = Door(two_way = True,  
                  tree = T1, 
                  name='D1', 
                  room_departure = R5, 
                  room_arrival = R1,
                  relative_departure_coordinates = relative_departure_coordinates_D1,
                  relative_arrival_coordinates = relative_arrival_coordinates_D1)
        D2 = Door(two_way = True,  
                  tree = T2, 
                  name='D2', 
                  room_departure = R5, 
                  room_arrival = R2,
                  relative_departure_coordinates = relative_departure_coordinates_D2,
                  relative_arrival_coordinates = relative_arrival_coordinates_D2)
        D3 = Door(two_way = True,  
                  tree = T3, 
                  name='D3', 
                  room_departure = R5, 
                  room_arrival = R3,
                  relative_departure_coordinates = relative_departure_coordinates_D3,
                  relative_arrival_coordinates = relative_arrival_coordinates_D3)
        D4 = Door(two_way = True,  
                  tree = T4, 
                  name='D4', 
                  room_departure = R5, 
                  room_arrival = R4,
                  relative_departure_coordinates = relative_departure_coordinates_D4,
                  relative_arrival_coordinates = relative_arrival_coordinates_D4)
        D5 = Door(two_way = True,  
                  tree = T5, 
                  name='D5', 
                  room_departure = R5, 
                  room_arrival = RE,
                  relative_departure_coordinates = relative_departure_coordinates_D5,
                  relative_arrival_coordinates = relative_arrival_coordinates_D5)
        
        l_help_txt = [
"""Two new operands are used in this level : XOR and XNOR

    XOR means exclusive or.
    XNOR is its opposite.
    
    XOR truth table (D0 = XOR S0 S1 = ^ S0 S1):
        S0  S1  D0
          0    0    0
          0    1    1
          1    0    1
          1    1    0  
    In other words, D0 is opened if S0 = S1.
          
    XNOR truth table (D0 = XNOR S0 S1 = -^ S0 S1):
        S0  S1  D0
          0    0    1
          0    1    0
          1    0    0
          1    1    1    
    In other words, D0 is opened if S0 is different from S1.
    
    You can write :
        XOR S0 S1 = | & S0 - S1 & - S0 S1 
        XNOR S0 S1 = | & S0 S1 & - S0 - S1
        XNOR S0 S1 = - XOR S0 S1
"""]
        
        level = Maze(start_room_index=0, 
                     exit_room_index=-1, 
                     rooms_list=[R0, R1, R2, R3, R4, R5, RE], 
                     doors_list = [D0, D1, D2, D3, D4, D5],
                     fastest_solution='S0 S5 S7 S8 D0 S9 D1 S1 D1 D2 S2 D2 D3 S3 D3 D4 S4 D4 D5',
                     level_color=Levels_colors_list.DARK_BLUE,
                     name='Point_of_no_return',
                     help_txt = l_help_txt)
        
        return level
    
    def level_recurrence():
        
        S0 = Switch(name='S0')
        S1 = Switch(name='S1')
        S2=Switch(name='S2')
        S3 = Switch(name='S3')
        S4 = Switch(name='S4')
        S5 = Switch(name='S5')
        S6 = Switch(name='S6')
        
        tree_list_0 = Tree.tree_list_or_4
        tree_list_1 = [None]
        tree_list_2 = ['AND', Tree.tree_list_not, Tree.tree_list_or_3]
        tree_list_3 = [None]
        tree_list_4 = ['AND', Tree.tree_list_nor, Tree.tree_list_or_2]
        tree_list_5 = [None]
        # tree_list_6 = ['BNA', Tree.tree_list_or_3, Tree.tree_list_and_4]
        tree_list_6 = Tree.tree_list_from_str('FTFTFTT')
        
        T0 = Tree(tree_list=tree_list_0, empty=True, name='T0', switches = [S0, S2, S4, S6])
        T1 = Tree(tree_list=tree_list_1, empty=True, name='T1', switches = [S1])
        T2 = Tree(tree_list=tree_list_2, empty=True, name='T2', switches = [S0, S2, S4, S6])
        T3 = Tree(tree_list=tree_list_3, empty=True, name='T3', switches = [S3])
        T4 = Tree(tree_list=tree_list_4, empty=True, name='T4', switches = [S0, S2, S4, S6])
        T5 = Tree(tree_list=tree_list_5, empty=True, name='T5', switches = [S5])
        T6 = Tree(tree_list=tree_list_6, empty=True, name='T6', switches = [S0, S1, S2, S3, S4, S5, S6])
        
        position_R0 = [0,4,2,2]
        position_R1 = [0,0,2,2]
        position_R2 = [4,0,2,2]
        position_R3 = [4,4,2,2]
        position_RE = [2.5,2.5,1,1]
        
        R0 = Room(name='R0', position = position_R0, switches_list = [S0, S1])
        R1 = Room(name='R1', position = position_R1, switches_list = [S2, S3])
        R2 = Room(name='R2', position = position_R2, switches_list = [S4, S5])
        R3 = Room(name='R3', position = position_R3, switches_list = [S6])
        RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
        
        relative_departure_coordinates_D0 = [1/3,   0]
        relative_arrival_coordinates_D0   = [1/3,   1]
        relative_departure_coordinates_D1 = [2/3,   1]
        relative_arrival_coordinates_D1   = [2/3,   0]
        relative_departure_coordinates_D2 = [  1, 1/3]
        relative_arrival_coordinates_D2   = [  0, 1/3]
        relative_departure_coordinates_D3 = [  0, 2/3]
        relative_arrival_coordinates_D3   = [  1, 2/3]
        relative_departure_coordinates_D4 = [2/3,   1]
        relative_arrival_coordinates_D4   = [2/3,   0]
        relative_departure_coordinates_D5 = [1/3,   0]
        relative_arrival_coordinates_D5   = [1/3,   1]
        relative_departure_coordinates_D6 = [  0,   0]
        relative_arrival_coordinates_D6   = [0.85, 0.85]
        
        D0 = Door(two_way = False, 
                  tree = T0, 
                  name='D0', 
                  room_departure = R0, 
                  room_arrival = R1,
                  relative_departure_coordinates = relative_departure_coordinates_D0,
                  relative_arrival_coordinates = relative_arrival_coordinates_D0)
        D1 = Door(two_way = False, 
                  tree = T1, 
                  name='D1', 
                  room_departure = R1, 
                  room_arrival = R0,
                  relative_departure_coordinates = relative_departure_coordinates_D1,
                  relative_arrival_coordinates = relative_arrival_coordinates_D1)
        D2 = Door(two_way = False, 
                  tree = T2, 
                  name='D2', 
                  room_departure = R1, 
                  room_arrival = R2,
                  relative_departure_coordinates = relative_departure_coordinates_D2,
                  relative_arrival_coordinates = relative_arrival_coordinates_D2)
        D3 = Door(two_way = False, 
                  tree = T3, 
                  name='D3', 
                  room_departure = R2, 
                  room_arrival = R1,
                  relative_departure_coordinates = relative_departure_coordinates_D3,
                  relative_arrival_coordinates = relative_arrival_coordinates_D3)
        D4 = Door(two_way = False, 
                  tree = T4, 
                  name='D4', 
                  room_departure = R2, 
                  room_arrival = R3,
                  relative_departure_coordinates = relative_departure_coordinates_D4,
                  relative_arrival_coordinates = relative_arrival_coordinates_D4)
        D5 = Door(two_way = False, 
                  tree = T5, 
                  name='D5', 
                  room_departure = R3, 
                  room_arrival = R2,
                  relative_departure_coordinates = relative_departure_coordinates_D5,
                  relative_arrival_coordinates = relative_arrival_coordinates_D5)
        D6 = Door(two_way = False, 
                  tree = T6, 
                  name='D6', room_departure = R3, 
                  room_arrival = RE,
                  relative_departure_coordinates = relative_departure_coordinates_D6,
                  relative_arrival_coordinates = relative_arrival_coordinates_D6)
        
        l_help_txt = [
"""Sometime, square brackets can be used instead of parentheses.
"""]
        
        level = Maze(start_room_index=0, 
                     exit_room_index=-1, 
                     rooms_list=[R0, R1, R2, R3, RE], 
                     doors_list = [D0, D1, D2, D3, D4, D5, D6], 
                     fastest_solution='S0 S1 D0 S2 D1 S0 D0 S3 D2 S4 D3 S2 D2 S5 D4 S6 D5 S4 D4 D6',
                     level_color=Levels_colors_list.BLACK_AND_WHITE,
                     name='Recurrence',
                     help_txt = l_help_txt,
                     border = 55)
        
        return level 
    
    def level_square():
        
        S0 = Switch(name='S0')
        S1 = Switch(name='S1')
        S2=Switch(name='S2')
        S3 = Switch(name='S3')
        
        T0 = Tree(tree_list=Tree.tree_list_from_str('TFTT'), empty=True, name='T0', switches = [S0, S1, S2, S3])
        T1 = Tree(tree_list=Tree.tree_list_from_str('TFFT'), empty=True, name='T1', switches = [S0, S1, S2, S3])
        T2 = Tree(tree_list=Tree.tree_list_from_str('TFFF'), empty=True, name='T2', switches = [S0, S1, S2, S3])
        T3 = Tree(tree_list=Tree.tree_list_from_str('TTTT'), empty=True, name='T3', switches = [S0, S1, S2, S3])
        T4 = Tree(tree_list=Tree.tree_list_from_str('TTTT'), empty=True, name='T4', switches = [S0, S1, S2, S3])
        
        position_R0 = [2,0,3,2]
        position_R1 = [0,3,5,2]
        position_RE = [0,0,1.25,2]
        
        R0 = Room(name='R0', position = position_R0, switches_list = [S0, S2])
        R1 = Room(name='R1', position = position_R1, switches_list = [S1, S3])
        RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
        
        relative_departure_coordinates_D0  = [  0,   1]
        relative_arrival_coordinates_D0    = [  0,   0]
        relative_departure_coordinates_D1  = [1/3,   0]
        relative_arrival_coordinates_D1    = [1/3,   1]
        relative_departure_coordinates_D2  = [2/3,   1]
        relative_arrival_coordinates_D2    = [2/3,   0]
        relative_departure_coordinates_D3  = [0.98, 0.02]
        relative_arrival_coordinates_D3    = [0.98, 0.98]
        relative_departure_coordinates_D4  = [  0, 1/2]
        relative_arrival_coordinates_D4    = [  1, 1/2]
        
        D0  = Door(two_way = False,  
                   tree = T0,  
                   name='D0',  
                   room_departure = R0, 
                   room_arrival = R1, 
                   relative_departure_coordinates = relative_departure_coordinates_D0, 
                   relative_arrival_coordinates = relative_arrival_coordinates_D0)
        D1  = Door(two_way = False,  
                   tree = T1,  
                   name='D1',  
                   room_departure = R1, 
                   room_arrival = R0, 
                   relative_departure_coordinates = relative_departure_coordinates_D1, 
                   relative_arrival_coordinates = relative_arrival_coordinates_D1)
        D2  = Door(two_way = False,  
                   tree = T2,  
                   name='D2',  
                   room_departure = R0, 
                   room_arrival = R1, 
                   relative_departure_coordinates = relative_departure_coordinates_D2, 
                   relative_arrival_coordinates = relative_arrival_coordinates_D2)
        D3  = Door(two_way = False,  
                   tree = T3,  
                   name='D3',  
                   room_departure = R1, 
                   room_arrival = R0, 
                   relative_departure_coordinates = relative_departure_coordinates_D3, 
                   relative_arrival_coordinates = relative_arrival_coordinates_D3)
        D4  = Door(two_way = False,  
                   tree = T4,  
                   name='D4',  
                   room_departure = R0, 
                   room_arrival = RE, 
                   relative_departure_coordinates = relative_departure_coordinates_D4, 
                   relative_arrival_coordinates = relative_arrival_coordinates_D4)
        
        l_help_txt = [
"""Instead of writing actions one by one, one can write several at a time, separated by spaces.
For instance, you can write :
    S0 S1 D0
if you want to turn on S0, S1 and then use the door D0.
"""]
        
        level = Maze(start_room_index=0, 
                     exit_room_index=-1, 
                     rooms_list=[R0, R1, RE], 
                     doors_list = [D0, D1, D2, D3, D4], 
                     fastest_solution="S0 D2 S3 D1 S2 D0 S1 D3 D4",
                     level_color=Levels_colors_list.DARK_RED,
                     name='Square',
                     help_txt = l_help_txt,
                     door_window_size = 500,
                     border = 60,
                     keep_proportions = True)
        
        return level
    
    def level_tetrahedron(): 

        S0 = Switch(name='S0')
        S1 = Switch(name='S1')
        S2 = Switch(name='S2')
        S3 = Switch(name='S3')
        S4 = Switch(name='S4')
        S5 = Switch(name='S5')
        S6 = Switch(name='S6')
        S7 = Switch(name='S7')
        
        tree_list_0 = Tree.tree_list_from_str("TFTTFFFF FTTFFTTT")
        tree_list_1 = Tree.tree_list_from_str("FFFFTFFF FFTFFFFT")
        tree_list_2 = Tree.tree_list_from_str("FFTTTFFF TFTFFFFT TTTFTTTT")
        tree_list_3 = Tree.tree_list_from_str("FFTFFFTT TTTFTTFT")
        tree_list_4 = Tree.tree_list_from_str("TFTTFFFF TFTFTTFT")
        tree_list_5 = Tree.tree_list_from_str("FFTFTFFF TTTFTTTT")
        tree_list_6 = Tree.tree_list_from_str("TFTFTTFF")
        
        ls = [S0, S1, S2, S3, S4, S5, S6, S7]
        
        T0 = Tree(tree_list=tree_list_0, empty=True, name='T0', switches = ls[:]*2, cut_expression = True)
        T1 = Tree(tree_list=tree_list_1, empty=True, name='T1', switches = ls[:]*2, cut_expression = True)
        T2 = Tree(tree_list=tree_list_2, empty=True, name='T2', switches = ls[:]*3, cut_expression = True,
                  easy_logical_expression_PN = """| [ & ( - S0 - S1 S2 S3 S4 - S5 - S6 - S7 )
& ( S0 - S1 S2 - S3 - S4 - S5 - S6 S7 )
& ( S0 S1 S2 - S3 S4 S5 S6 S7 )  ]""")
        T3 = Tree(tree_list=tree_list_3, empty=True, name='T3', switches = ls[:]*2, cut_expression = True)
        T4 = Tree(tree_list=tree_list_4, empty=True, name='T4', switches = ls[:]*2, cut_expression = True)
        T5 = Tree(tree_list=tree_list_5, empty=True, name='T5', switches = ls[:]*2, cut_expression = True)
        T6 = Tree(tree_list=tree_list_6, empty=True, name='T6', switches = ls[:])
        
        d = 3
        r = 1.25
        
        position_R0 = [   2,  5,  2,  2]
        position_R1 = [   0,  2,  2,  2]
        position_R2 = [   3,  0,  2,  2]
        position_R3 = [   5,  3,  2,  2]
        position_RE = [   d,  d,  r,  r]
        
        R0 = Room(name='R0', position = position_R0, switches_list = [S0, S4])
        R1 = Room(name='R1', position = position_R1, switches_list = [S1, S5])
        R2 = Room(name='R2', position = position_R2, switches_list = [S2, S6])
        R3 = Room(name='R3', position = position_R3, switches_list = [S3, S7])
        RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
        
        d0 = 0.02
        d1 = 1-d0
        
        D0 = Door(two_way = True, tree = T0, room_departure = R0, room_arrival = R1, 
                  relative_departure_coordinates = [d0, d1], 
                  relative_arrival_coordinates = [d0, d1])
        D1 = Door(two_way = True, tree = T1, room_departure = R0, room_arrival = R2, 
                  relative_departure_coordinates = [d0, d0], 
                  relative_arrival_coordinates = [d0, d1])
        D2 = Door(two_way = True, tree = T2, room_departure = R0, room_arrival = R3, 
                  relative_departure_coordinates = [d1, d1], 
                  relative_arrival_coordinates = [d1, d1])
        D3 = Door(two_way = True, tree = T3, room_departure = R1, room_arrival = R2, 
                  relative_departure_coordinates = [d0, d0], 
                  relative_arrival_coordinates = [d0, d0])
        D4 = Door(two_way = True, tree = T4, room_departure = R1, room_arrival = R3, 
                  relative_departure_coordinates = [d1, d0], 
                  relative_arrival_coordinates = [d0, d0])
        D5 = Door(two_way = True, tree = T5, room_departure = R2, room_arrival = R3, 
                  relative_departure_coordinates = [d1, d0], 
                  relative_arrival_coordinates = [d1, d0])
        D6 = Door(two_way = True, tree = T6, room_departure = R3, room_arrival = RE,
                  relative_departure_coordinates = [d0, d1], 
                  relative_arrival_coordinates = [0.7, 0.7])
        
        l_help_txt = [
"""
"""]
        
        level = Maze(start_room_index=0, 
                     exit_room_index=-1, 
                     rooms_list=[R0, R1, R2, R3, RE], 
                     doors_list = [D0, D1, D2, D3, D4, D5, D6], 
                     fastest_solution="S4 D1 S2 D5 S3 D2 S0 S4 D0 D4 S3 S7 D2 S0 D1 S6 D3 S1 S5 D0 S0 S4 D2 D5 S6 D3 S1 D4 S7 D6",
                     level_color=Levels_colors_list.PURPLE_BLUE,
                     name='Tetrahedron',
                     help_txt = l_help_txt,
                     border = 30,
                     door_window_size = 550,
                     keep_proportions = True)
        
        return level
    
    def level_xor(): 
        
        S0 = Switch(name='S0')
        S1 = Switch(name='S1')
        S2=Switch(name='S2')
        S3 = Switch(name='S3')
        S4 = Switch(name='S4')
        S5 = Switch(name='S5')
        S6 = Switch(name='S6')
        S7 = Switch(name='S7')
        S8 = Switch(name='S8')
        
        tree_list_0 = Tree.tree_list_nand
        tree_list_1 = ['AND',  Tree.tree_list_aonb,  [None]]
        tree_list_2 = ['AND',  Tree.tree_list_bona,  [None]]
        tree_list_3 = ['AND',  Tree.tree_list_XOR3,  [None]]
        tree_list_4 = ['AND',  Tree.tree_list_XNOR3, [None]]
        tree_list_5 = ['AND',  Tree.tree_list_XOR3,  [None]]
        tree_list_6 = ['AND',  Tree.tree_list_XNOR3, [None]]
        tree_list_7 = ['AND',  Tree.tree_list_XOR3,  [None]]
        tree_list_8 = Tree.tree_list_from_str('TF TT TT') # ['OR_3', Tree.tree_list_anb, Tree.tree_list_and_2, Tree.tree_list_and_2]
        
        T0  = Tree(tree_list=tree_list_0,  empty=True, name='T0', switches = [S6, S7], easy_logical_expression_PN = "NAND S6 S7\n= -& S6 S7")
        T1  = Tree(tree_list=tree_list_1,  empty=True, name='T1', switches = [S6, S7, S8])
        T2  = Tree(tree_list=tree_list_2,  empty=True, name='T2', switches = [S6, S7, S8])
        T3  = Tree(tree_list=tree_list_3,  empty=True, name='T3', switches = [S0, S1, S2, S8])
        T4  = Tree(tree_list=tree_list_4,  empty=True, name='T4', switches = [S1, S2, S3, S8])
        T5  = Tree(tree_list=tree_list_5,  empty=True, name='T5', switches = [S2, S3, S4, S8])
        T6  = Tree(tree_list=tree_list_6,  empty=True, name='T6', switches = [S3, S4, S5, S8])
        T7  = Tree(tree_list=tree_list_7,  empty=True, name='T7', switches = [S4, S5, S6, S8])
        T8  = Tree(tree_list=tree_list_8,  empty=True, name='T8', switches = [S1, S4, S1, S3, S2, S4])
        
        position_R0 = [ 0,  0,  2,  4]
        position_R1 = [ 1,5.5,  1,1.5]
        position_R2 = [ 4,  6,  1,  1]
        position_R3 = [ 8,  6,  1,  1]
        position_R4 = [ 4,  4,  1,  1]
        position_R5 = [ 8,  4,  1,  1]
        position_R6 = [ 4,  2,  1,  1]
        position_R7 = [ 8,  2,  1,  1]
        position_R8 = [ 4,  0,  1,  1]
        position_RE = [ 8,  0,  1,  1]
        
        R0 = Room(name='R0', position = position_R0, switches_list = [S0, S1, S2, S3, S4, S5, S6, S7])
        R1 = Room(name='R1', position = position_R1, switches_list = [S8])
        R2 = Room(name='R2', position = position_R2, switches_list = [])
        R3 = Room(name='R3', position = position_R3, switches_list = [])
        R4 = Room(name='R4', position = position_R4, switches_list = [])
        R5 = Room(name='R5', position = position_R5, switches_list = [])
        R6 = Room(name='R6', position = position_R6, switches_list = [])
        R7 = Room(name='R7', position = position_R7, switches_list = [])
        R8 = Room(name='R8', position = position_R8, switches_list = [])
        RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
        
        D0 = Door(two_way = False, tree = T0, name='D0', room_departure = R0, room_arrival = R1, relative_departure_coordinates = [1/2, 1], relative_arrival_coordinates = [1/2, 0])
        D1 = Door(two_way = False, tree = T1, name='D1', room_departure = R1, room_arrival = R2)
        D2 = Door(two_way = False, tree = T2, name='D2', room_departure = R2, room_arrival = R3)
        D3 = Door(two_way = False, tree = T3, name='D3', room_departure = R3, room_arrival = R4)
        D4 = Door(two_way = False, tree = T4, name='D4', room_departure = R4, room_arrival = R5)
        D5 = Door(two_way = False, tree = T5, name='D5', room_departure = R5, room_arrival = R6)
        D6 = Door(two_way = False, tree = T6, name='D6', room_departure = R6, room_arrival = R7)
        D7 = Door(two_way = False, tree = T7, name='D7', room_departure = R7, room_arrival = R8)
        D8 = Door(two_way = False, tree = T8, name='D8', room_departure = R8, room_arrival = RE)
        
        l_help_txt = [
"""New operands are used in this level :
    
    NAND truth table (D0 = NAND S0 S1):
        S0  S1  D0
          0    0    1
          0    1    1
          1    0    1
          1    1    0  
          
    XOR and XNOR are used with 3 parameters instead of 2.
          
    XOR and XNOR truth table [D0 = XOR ( S0 S1 S2 ); D1 = XNOR ( S0 S1 S2 )]:
        S0  S1  S2  D0  D1
          0    0    0     0    0
          0    1    0     1    0
          1    0    0     1    0
          1    1    0     0    1
          0    0    1     1    0
          0    1    1     0    1
          1    0    1     0    1
          1    1    1     0    0    
    In other words:
        D0 is opened if there is exactly one switch among S0, S1 and S2 that is turned on.
        D1 is opened if there is exactly one switch among S0, S1 and S2 that is turned off.
"""]
        
        level = Maze(start_room_index=0, 
                     exit_room_index=-1, 
                     rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, RE], 
                     doors_list = [D0, D1, D2, D3, D4, D5, D6, D7, D8], 
                     fastest_solution='S1 S3 S5 D0 S8 D1 D2 D3 D4 D5 D6 D7 D8',
                     level_color=Levels_colors_list.RED_AND_ORANGE,
                     name='XOR',
                     help_txt = l_help_txt,
                     door_window_size = 550)
        
        return level
        
    levels_functions_list = [#level_icone,
                             level_hello_world,         # GREY
                             level_linear,             # BRIGHT GREEN
                             level_loop,               # RED
                             level_backward,           # BROWN
                             level_binary,             # BRIGHT BLUE AND GREY
                             level_crossroad,          # YELLOW
                             level_square,             # BLACK AND RED
                             level_fluid,              # GREEN_BLUE
                             level_odd,                # PURPLE
                             level_point_of_no_return, # BLUE
                             level_recurrence,         # BLACK AND WHITE
                             level_parallel,           # PINK
                             level_infinity,           # YELLOW AND BLACK
                             level_crystal,            # SALMON AND BRIGHT_GREY
                             level_tetrahedron,        # PURPLE_BLUE
                             level_cartesian,          # GREEN AND GREY
                             level_xor,                # RED AND ORANGE
                             level_graph,              # BLACK AND BLUE
                             level_dead_ends,          # DARK GREEN
                             level_electricity         # YELLOW AND SILVER
                             ] 

    number_of_levels = len(levels_functions_list)
    
    levels_list = [None for k in range(number_of_levels)]
    
    def get_level(level_number):
        if Levels.levels_list[level_number] == None:
            Levels.levels_list[level_number] = Levels.levels_functions_list[level_number]()
        else:
            Levels.levels_list[level_number].reboot_solution()
        return Levels.levels_list[level_number]
    
if __name__ == "__main__":
    
    # for level in Levels.levels_list:
    #     print(level.name)
    #     depth_dict = {}
    #     max_depth = 0
    #     max_depth_tree_name=''
    #     for door in level.doors_list():
    #         tree = door.tree
    #         depth = tree.get_depth()
    #         depth_dict[tree.name] = depth
    #         if depth >= max_depth:
    #             max_depth = depth
    #             max_depth_tree_name=tree.name
    #         print(tree.name, depth)
    
    # solutions = Levels.level_graph().find_all_solutions(stop_at_first_solution=False, verbose = 3)
    
    # mini = float('inf')
    # sol_mini = ''
    # for sol in solutions:
    #     level = Levels.level_graph()
    #     level.try_solution(sol, verbose = 0, allow_all_doors=True, allow_all_switches=True)
    #     m = 0
    #     for S in level.switches_list():
    #         m = m + S.value
    #     print(m)
    #     print(sol)
    #     if m < mini:
    #         mini = m
    #         sol_mini = sol
            
    # print(mini)
    # print(sol_mini)
    # Levels.level_graph().try_solution(sol_mini, verbose = 3, allow_all_doors=True, allow_all_switches=True)
    
    for level_function in Levels.levels_functions_list:
        level = level_function()
    
    # solutions = Levels.level_cartesian().find_all_solutions(stop_at_first_solution=False, verbose = 3)
    
    # These 2 lines
    # calculates the values that k4 doors
    # should have 
    # in order to the solution to be sol
    sol = "S4 D1 S2 D5 S3 D2 S0 S4 D0 D4 S3 S7 D2 S0 D1 S6 D3 S1 S5 D0 S0 S4 D2 D5 S6 D3 S1 D4 S7 D6"
    Levels.level_k4().try_solution(sol, verbose = 3, allow_all_doors=True, allow_all_switches=True)
    
    
    pass
    