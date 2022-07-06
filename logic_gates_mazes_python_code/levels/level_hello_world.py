# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:15:46 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

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
"""You are trapped in the inside of a computer and want to reach the exit.

There are differents elements in this game :
    Rooms (R0, R1, R2, ..., EXIT) :  
        The room inside which you are is surrounded.
    Switches (S0, S1, S2, ...) : 
        If a switch is turned on, it is surrounded, and you say it is equal to 1.
        If it is turned off, it is equal to 0.
        To turn on a switch, write its name and press enter.
    Doors (D0, D1, D2, ...) :    
        If a door is open, it is surrounded, and you say it is equal to 1.
        If it is closed, it is equal to 0.
        To use a door, write its name and press enter.
        Diamond-shape doors are two-way while triangle-shaped doors are one-way only.      
If you made a mistake when taping the name of a door or a switch, you can always erase it by taping on the backspace key.
    
On the left size window of the game are equations that tell you when a door is open :
    (These equations work with any name of door or switch.)
    D0 = S0 means : 
        D0 is open if S0 is turned on.
    D2 = OR S1 S2 means :
        D1 is open if S1 or S2 is turned on (i.e. if (S0, S1) = (0,1) or (S0, S1) = (1,0) or (S0, S1) = (1,1))
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