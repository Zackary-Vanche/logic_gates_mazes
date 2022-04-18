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
    
    l_help_txt = [
"""
"""]
        
    level = Maze(start_room_index=0, 
                 exit_room_index=-1, 
                 rooms_list=[], 
                 doors_list = [], 
                 fastest_solution=None,
                 level_color=Levels_colors_list.YELLOW,
                 name='Tree',
                 help_txt = l_help_txt,
                 border = 30,
                 door_window_size = 500)

    return level