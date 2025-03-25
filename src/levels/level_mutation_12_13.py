from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle

def f(): 

    S0 = Switch(name='S0', value=1)
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3', value=1)
    S4 = Switch(name='S4', value=1)
    S5 = Switch(name='S5', value=1)
    Slist_0 = [S0, S1]
    Slist_1 = [S2, S3]
    Slist_2 = [S4, S5]
    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_0)),
          name='V0',
          switches=Slist_0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_1)),
          name='V1',
          switches=Slist_1)
    V2 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_2)),
          name='V2',
          switches=Slist_2)
    V3 = Tree(tree_list=Tree.tree_list_EQUSET(2*3),
              name='V3',
              switches=[V0, V1, V2, 1, 2, 3])

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[1])
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[1])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[1])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[1])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[V3])
    l = [1, 2, 3]
    rd_shuffle(l)
    T5 = Tree(tree_list=["AND"]+[Tree.tree_list_EQU(2)]*3,
                name='T5',
                switches=[V0, l[0], V1, l[1], V2, l[2]])

    dx = 1.2
    dy = 1
    ex = 0.6
    ey = 0.5
    a = 0.2

    R0 = Room(name='R0',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[])
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=Slist_0)
    R2 = Room(name='R2',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=Slist_1)
    R3 = Room(name='R3',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=Slist_2)
    RE = Room(name='RE',
              position=[0*dx+a, 2*dy-a, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R2)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R3)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R3)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R3,
                room_arrival=R0)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R0,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Mutation ({(12),(13)})',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

get_color = lambda : Levels_colors_list.different_hues(hu_index=1, inverse_hues=True)