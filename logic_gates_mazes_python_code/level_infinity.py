# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:17:30 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_infinity(): 
    
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