from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import randint as rd_randint
from random import random as rd_random

def f(): 

    S0 = Switch(name='S0', value=rd_randint(0, 1))
    S1 = Switch(name='S1', value=rd_randint(0, 1))
    S2 = Switch(name='S2', value=rd_randint(0, 1))
    S3 = Switch(name='S3', value=rd_randint(0, 1))
    S4 = Switch(name='S4', value=rd_randint(0, 1))
    S5 = Switch(name='S5', value=rd_randint(0, 1))
    S6 = Switch(name='S6', value=rd_randint(0, 1))
    S7 = Switch(name='S7', value=rd_randint(0, 1))
    S8 = Switch(name='S8', value=rd_randint(0, 1))
    S9 = Switch(name='S9', value=rd_randint(0, 1))
    S10 = Switch(name='S10', value=rd_randint(0, 1))
    S11 = Switch(name='S11', value=rd_randint(0, 1))

    Slist = [S0, S1, S2, S3,
             S4, S5, S6, S7,
             S8, S9, S10, S11]

    Slist_0 = [S0, S1, S4, S5]
    Slist_1 = [S1, S2, S5, S6]
    Slist_2 = [S2, S3, S6, S7]
    Slist_3 = [S4, S5, S8, S9]
    Slist_4 = [S5, S6, S9, S10]
    Slist_5 = [S6, S7, S10, S11]
    V0 = Tree(tree_list=Tree.tree_list_SUM(len(Slist_0)),
          name='V0',
          switches=Slist_0)
    V1 = Tree(tree_list=Tree.tree_list_SUM(len(Slist_1)),
          name='V1',
          switches=Slist_1)
    V2 = Tree(tree_list=Tree.tree_list_SUM(len(Slist_2)),
          name='V2',
          switches=Slist_2)
    V3 = Tree(tree_list=Tree.tree_list_SUM(len(Slist_3)),
          name='V3',
          switches=Slist_3)
    V4 = Tree(tree_list=Tree.tree_list_SUM(len(Slist_4)),
          name='V4',
          switches=Slist_4)
    V5 = Tree(tree_list=Tree.tree_list_SUM(len(Slist_5)),
          name='V5',
          switches=Slist_5)

    Vlist = [V0, V1, V2, V3, V4, V5]

    Slist_T0 = []
    for V in Vlist:
        Slist_T0.extend([V, V.get_value()])
    T0 = Tree(tree_list=["AND"] + [Tree.tree_list_EQU(2)]*len(Vlist),
              name='T0',
              switches=Slist_T0,
              cut_expression_depth_1=True)

    dx = 1
    dy = 1
    ex = 0.8
    ey = 0.8

    R0 = Room(name='R0',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=Slist)
    RE = Room(name='RE',
              position=[0*dx, 0*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE)
    
    sol_list = []
    for S in Slist:
        if S.value:
            sol_list.append(S.name)
        S.value = 0
    sol_list.append('D0')

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution=" ".join(sol_list),
                 level_color=get_color(),
                 name='Dots',
                 keep_proportions=True,
                 door_window_size=290,
                 random=True)
    
    return level

def get_color():
    hu = rd_random()
    lcolor = Levels_colors_list.FROM_HUE_light_background(hu, sa=0.5, li=0.35)
    lcolor.surrounding_color=Color.color_hls(hu=hu+0.5, sa=0.9, li=0.8)
    lcolor.contour_color=Color.color_hls(hu=hu+0.5, sa=0.9, li=0.8)
    return lcolor