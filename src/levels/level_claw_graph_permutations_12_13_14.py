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
    
    Slist_0 = [S0, S1]
    Slist_1 = [S2, S3]
    Slist_2 = [S4, S5]
    Slist_3 = [S6, S7]
    Slist_4 = [S8, S9]
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
    
    tl1 = ["AND", Tree.tree_list_EQU(2), Tree.tree_list_EQU(2)]
    tl2 = ["AND", Tree.tree_list_EQU(2), [None]]

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[1])
    
    T1 = Tree(tree_list=tl1,
                name='T1',
                switches=[V0, 1, V1, V2])
    T2 = Tree(tree_list=tl2,
                name='T2',
                switches=[V0, 1, V5])
    
    T3 = Tree(tree_list=tl1,
                name='T3',
                switches=[V0, 2, V1, V3])
    T4 = Tree(tree_list=tl2,
                name='T4',
                switches=[V0, 2, V5])
    
    T5 = Tree(tree_list=tl1,
                name='T5',
                switches=[V0, 3, V1, V4])
    T6 = Tree(tree_list=tl2,
                name='T6',
                switches=[V0, 3, V5])
    
    l = [0, 1, 2, 3]
    rd_shuffle(l)
    
    T7 = Tree(tree_list=["AND"]+[Tree.tree_list_EQU(2)]*5,
                name='T7',
                switches=[V0, 3,
                          V1, l[0],
                          V2, l[1],
                          V3, l[2],
                          V4, l[3]])

    dx = 1
    dy = 1
    ex = 0.4
    ey = 0.4

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[1.5*dx, 1.5*dy, ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=Slist_4)
    RE = Room(name='RE',
              position=[2*dx, 0*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R0)
    
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R3)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R3,
                room_arrival=R0)
    
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R1,
                room_arrival=R4)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R4,
                room_arrival=R0)
    
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R0,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7,],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Claw graph permutations ({(12),(13),(14)})',
                 keep_proportions=True,
                 door_window_size=350,
                 random=True)
    
    return level

get_color = lambda : Levels_colors_list.different_hues(hu_index=5, inverse_hues=True)