from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import randint as rd_randint

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
    
    V0 = Tree(tree_list=[None],
          name='V0',
          switches=[0])
    V1 = Tree(tree_list=[None],
          name='V1',
          switches=[1])
    V2 = Tree(tree_list=tl,
          name='V2',
          switches=[V0, V1]) # 1
    V3 = Tree(tree_list=tl,
          name='V3',
          switches=[V1, V2]) # 2
    V4 = Tree(tree_list=tl,
          name='V4',
          switches=[V2, V3]) # 3
    V5 = Tree(tree_list=tl,
          name='V5',
          switches=[V3, V4]) # 5
    V6 = Tree(tree_list=tl,
          name='V6',
          switches=[V4, V5]) # 8
    V7 = Tree(tree_list=tl,
          name='V7',
          switches=[V5, V6]) # 13
    V8 = Tree(tree_list=tl,
          name='V8',
          switches=[V6, V7]) # 21
    assert V8.get_value() == 21
    V9 = Tree(tree_list=["SUM"]+[Tree.tree_list_PROD(2)]*7,
          name='V9',
          switches=[V2, S0,
                    V3, S1,
                    V4, S2,
                    V5, S3,
                    V6, S4,
                    V7, S5,
                    V8, S6,])

    T0 = Tree(tree_list=Tree.tree_list_EQU(2),
                name='T0',
                switches=[V9, rd_randint(0, 53)])

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
                 name='Fibonacci numeration',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0, sa=0.15, li=0.7)
    lcolor.surrounding_color = Color.IVORY
    lcolor.contour_color = Color.IVORY
    return lcolor