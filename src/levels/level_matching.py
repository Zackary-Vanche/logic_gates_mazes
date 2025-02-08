from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')

    T0 = Tree(tree_list=["AND",
                         Tree.tree_list_XOR(2),
                         Tree.tree_list_XOR(2),
                         Tree.tree_list_XOR(2),
                         Tree.tree_list_XOR(2),
                         ['NOT', Tree.tree_list_from_str('TFFT')]],
                name='T0',
                switches=[S0, S1,
                          S0, S2,
                          S1, S3,
                          S2, S3,
                          S0, S1, S2, S3],
                cut_expression_depth_1=True)

    dx = 1
    dy = 1
    ex = 0.6
    ey = 0.6

    R0 = Room(name='R0',
                position=[rd_choice([-1, 1])*dx, 0*dy, ex, ey],
                switches_list=[S0, S1, S2, S3])
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
                 fastest_solution="S1 S2 D0",
                 level_color=get_color(),
                 name='Matching',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.8, sa=0.3, li=0.2)