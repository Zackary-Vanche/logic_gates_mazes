from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    
    Slist_0 = [S0, S1, S2]
    V0 = Tree(tree_list=Tree.tree_list_BIN(3),
          name='V0',
          switches=Slist_0)
    Slist_1 = [S3, S4, S5]
    V1 = Tree(tree_list=Tree.tree_list_BIN(3),
          name='V1',
          switches=Slist_1)
    l = [i for i in range(8)]
    rd_shuffle(l)
    l = l[:4]

    T0 = Tree(tree_list=["AND",
                         ["EQU", [None], Tree.tree_list_MIN(4)],
                         ["EQU", [None], Tree.tree_list_MAX(4)]],
                name='T0',
                switches=[V0]+l+[V1]+l)

    dx = 1.5
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, 2*ex, 3*ey],
                switches_list=Slist_0+Slist_1)
    RE = Room(name='RE',
              position=[1*dx, 0*dy, ex, 3*ey],
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
                 name='Extrema',
                 keep_proportions=True,
                 door_window_size=360,
                 random=True)
    
    sol_list = level.find_all_solutions()[0]
    assert len(sol_list) == 1
    level.fastest_solution = ' '.join(sol_list[0])
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.7, sa=0.25, li=0.7)
    lcolor.surrounding_color = Color.color_hls(hu=0.7, li=0.7, sa=1)
    lcolor.contour_color = Color.color_hls(hu=0.7, li=0.7, sa=1)
    return lcolor