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
    
    S4 = Switch(name='S4', value=1)
    S5 = Switch(name='S5')
    
    S6 = Switch(name='S6')
    S7 = Switch(name='S7', value=1)
    
    S8 = Switch(name='S8', value=1)
    S9 = Switch(name='S9', value=1)
    
    Slist_0 = [S0, S1,]
    Slist_1 = [S2, S3,]
    Slist_2 = [S4, S5,]
    Slist_3 = [S6, S7,]
    Slist_4 = [S8, S9,]
    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_0)),
          name='V0',
          switches=Slist_0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_1)),
          name='V1',
          switches=Slist_1)
    V2 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_2)),
          name='V2',
          switches=Slist_2)
    V3 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_3)),
          name='V3',
          switches=Slist_3)
    V4 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_4)),
          name='V4',
          switches=Slist_4)
    V5 = Tree(tree_list=Tree.tree_list_EQUSET(4*2),
              name='V5',
              switches=[V1, V2, V3, V4, 0, 1, 2, 3])

    tl = Tree.tree_list_EQU(2)

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[V5])
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[V5])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[V5])
    T3 = Tree(tree_list=tl,
                name='T3',
                switches=[V0, 1])
    T4 = Tree(tree_list=tl,
                name='T4',
                switches=[V0, 1])
    T5 = Tree(tree_list=tl,
                name='T5',
                switches=[V0, 2])
    T6 = Tree(tree_list=tl,
                name='T6',
                switches=[V0, 2])
    T7 = Tree(tree_list=tl,
                name='T7',
                switches=[V0, 3])
    T8 = Tree(tree_list=tl,
                name='T8',
                switches=[V0, 3])
    l = [0, 1, 2, 3]
    rd_shuffle(l)
    
    T9 = Tree(tree_list=["AND"]+[Tree.tree_list_EQU(2)]*5,
                name='T9',
                switches=[V0, 3,
                          V1, l[0],
                          V2, l[1],
                          V3, l[2],
                          V4, l[3]])

    dx = 0.5
    dy = 0.5
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[3*dx, 5*dy, ex, ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[1*dx, 3*dy, ex, ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[3*dx, 3*dy, ex, ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[5*dx, 3*dy, ex, ey],
                switches_list=[])
    R4 = Room(name='R4',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=Slist_1)
    R5 = Room(name='R5',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=Slist_2)
    R6 = Room(name='R6',
                position=[4*dx, 1*dy, ex, ey],
                switches_list=Slist_3)
    R7 = Room(name='R7',
                position=[6*dx, 1*dy, ex, ey],
                switches_list=Slist_4)
    RE = Room(name='RE',
              position=[3*dx, 0*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=R3)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R4)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R1,
                room_arrival=R5)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R2,
                room_arrival=R5)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R2,
                room_arrival=R6)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R3,
                room_arrival=R6)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R3,
                room_arrival=R7)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R2,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Structure ({(12),(23),(34)})',
                 keep_proportions=True,
                 door_window_size=350,
                 random=True)
    
    return level

def get_color():
    hu = 0.175 - 0.5/7
    lcolor = Levels_colors_list.FROM_HUE(hu=hu, sa=0.5, li=0.15)
    lcolor.surrounding_color = Color.color_hls(hu=hu+0.1, sa=1, li=0.7)
    lcolor.contour_color = Color.color_hls(hu=hu-0.1, sa=1, li=0.7)
    return lcolor