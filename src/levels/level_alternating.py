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
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    Slist = [S0, S1, S2, S3, S4, S5, S6]
    
    tl = Tree.tree_list_SUM(2)
    
    V0 = Tree(tree_list=["SUM", Tree.tree_list_PROD(2), [None]],
          name='V0',
          switches=[2, S0, -1])
    V1 = Tree(tree_list=["SUM", Tree.tree_list_PROD(2), [None]],
          name='V1',
          switches=[2, S1, -1])
    V2 = Tree(tree_list=["SUM", Tree.tree_list_PROD(2), [None]],
          name='V2',
          switches=[2, S2, -1])
    V3 = Tree(tree_list=["SUM", Tree.tree_list_PROD(2), [None]],
          name='V3',
          switches=[2, S3, -1])
    V4 = Tree(tree_list=["SUM", Tree.tree_list_PROD(2), [None]],
          name='V4',
          switches=[2, S4, -1])
    V5 = Tree(tree_list=["SUM", Tree.tree_list_PROD(2), [None]],
          name='V5',
          switches=[2, S5, -1])
    V6 = Tree(tree_list=["SUM", Tree.tree_list_PROD(2), [None]],
          name='V6',
          switches=[2, S6, -1])
    V7 = Tree(tree_list=["SUM"]+[["PROD", [None], ["POW", [None], [None]]]]*7,
          name='V7',
          switches=[V0, 2, 0,
                    V1, 2, 1,
                    V2, 2, 2,
                    V3, 2, 3,
                    V4, 2, 4,
                    V5, 2, 5,
                    V6, 2, 6,
                    ],
          cut_expression_depth_1=True)

    n = 0
    for k in range(7):
        n += rd_choice([-1, +1]) * 2**k
        
    T0 = Tree(tree_list=Tree.tree_list_EQU(2),
                name='T0',
                switches=[V7, n])

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, 2*ex, ey],
                switches_list=Slist)
    RE = Room(name='RE',
              position=[0*dx, 1*dy, 2*ex, ey],
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
                 name='Alternating',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.3, sa=0.15, li=0.7)
    lcolor.surrounding_color = Color.IVORY
    lcolor.contour_color = Color.IVORY
    return lcolor