from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color
import numpy as np
from random import random as rd_random

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')

    Slist = [S0, S1, S2, S3, S4, S5]
    
    tree_list_BIN_6 = Tree.tree_list_BIN(6)

    Vlist = []
    for i in range(len(Slist)):
        Vlist.append(Tree(tree_list=tree_list_BIN_6,
                          name=f'V{2*i}',
                          switches=Slist[:]))
        Vlist.append(Tree(tree_list=tree_list_BIN_6,
                          name=f'V{2*i+1}',
                          switches=Slist[::-1]))
        Slist = Slist[1:] + [Slist[0]]
        
    Slist0 = []
    for i in range(1, len(Vlist)):
        Slist0.append(Vlist[0])
        Slist0.append(Vlist[i])
    
    T0 = Tree(tree_list=['AND'] + [['INF', [None], [None]]]*(len(Slist0)//2),
                name='T0',
                switches=Slist0,
                cut_expression_depth_1=False)

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, 3*ex, 2*ey],
                switches_list=[S0, S1, S2, S3, S4, S5])
    
    alpha = -rd_random()*np.pi/8
    
    RE = Room(name='RE',
              position=[4*ex*np.cos(alpha), 4*ex*np.sin(alpha), ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[2.5/3, 1/4])
    
    hu = 0.3
    sa = 0.6
    li = 0.8
    lcolor = Level_color(background_color=Color.color_hls(hu, li, sa),
                         room_color=Color.color_hls(hu, li / 4, 0.8 * sa),
                         letters_color=Color.BLACK,
                         contour_color=Color.YELLOW,
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.YELLOW)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution="S0 S1 S3 D0",
                 level_color=lcolor,
                 name='Circle',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level