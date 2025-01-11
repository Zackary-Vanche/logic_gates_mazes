
from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from random import random as rd_random

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    Sa = Switch(name='?', value=rd_choice([0, 1, 2, 3]))

    T0 = Tree(tree_list=["EQU", Tree.tree_list_BIN(2), [None],],
              name='T0',
              switches=[S0, S1, Sa])

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S0, S1])
    RE = Room(name='RE',
              position=[0*dx, 0*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Guess',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=rd_random(), sa=0.35, li=0.6)

