from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle
from random import choice as rd_choice

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    
    V0 = Tree(tree_list=Tree.tree_list_NAND(4),
                name='V0',
                switches=[S0, S1, S2, S3])
    
    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[S0])
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[S1])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[S2])
    T3 = Tree(tree_list=Tree.tree_list_AND(3),
                name='T3',
                switches=[S3, S4, V0])

    dx = 1
    dy = 1
    ex = 0.75
    ey = 0.75
    
    pos_list = [[0*dx, 0*dy, ex, ey],
                [0*dx, 2*dy, ex, ey],
                [2*dx, 0*dy, ex, ey],
                [2*dx, 2*dy, ex, ey]]
    rd_shuffle(pos_list)

    R0 = Room(name='R0',
                position=pos_list[0],
                switches_list=[S0, S1, S2, S3])
    R1 = Room(name='R1',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[])
    if rd_choice([0, 1]):
        R2_slist = [S4]
        R3_slist = []
        sol = "S0 S1 S3 D0 D1 S4 D1 D3"
    else:
        R2_slist = []
        R3_slist = [S4]
        sol = "S0 S2 S3 D0 D2 S4 D2 D3"
    R2 = Room(name='R2',
                position=pos_list[1],
                switches_list=R2_slist)
    R3 = Room(name='R3',
                position=pos_list[2],
                switches_list=R3_slist)
    RE = Room(name='RE',
              position=pos_list[3],
              is_exit=True)

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R3)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, RE],
                 doors_list=[D0, D1, D2, D3],
                 fastest_solution=sol,
                 level_color=get_color(),
                 name='Easy',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def get_color():
    hu = 0.3
    lcolor = Levels_colors_list.FROM_HUE(hu, sa=0.3, li=0.2)
    lcolor.surrounding_color = Color.color_hls(hu, sa=0.7, li=0.7)
    lcolor.contour_color = Color.color_hls(hu, sa=0.7, li=0.7)
    return lcolor