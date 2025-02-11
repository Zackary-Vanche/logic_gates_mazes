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
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14]

    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    Slist_3 = [S9, S10, S11]
    Slist_4 = [S12, S13, S14]
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
    
    Vl = [Tree(tree_list=Tree.tree_list_INF(2),
               name=f'V{5+i}',
               switches=[[V0, V1, V2, V3, V4,][i], 6]) for i in range(5)]
    
    Vl.extend([Tree(tree_list=["INFOREQU", ["SUM"] + [Tree.tree_list_EQU(2)]*5, [None]],
               name=f'V{5+i+len(Vl)}',
               switches=[V0, i,
                         V1, i,
                         V2, i,
                         V3, i,
                         V4, i,
                         1]) for i in range(6)])
    
    V = Tree(tree_list=Tree.tree_list_AND(len(Vl)),
               name='V16',
               switches=Vl)
    
    Sl_list = [Slist_0,
               Slist_1,
               Slist_2,
               Slist_3,
               Slist_4,
               ]
    bin_list = [[0, 1, 0],
                [1, 0, 0],
                [1, 1, 0],
                [0, 0, 1],
                [1, 0, 1]]
    rd_shuffle(bin_list)
    value_list = [b[0]+2*b[1]+4*b[2] for b in bin_list]
    
    for i in range(len(Sl_list)):
        for j in range(len(Sl_list[i])):
            Sl_list[i][j].value = bin_list[i][j]
            
    S0.value = 1
    S1.value = 1
    S2.value = 1

    T0 = Tree(tree_list=["AND", Tree.tree_list_EQU(2), [None]],
                name='T0',
                switches=[V0, value_list[0], V])
    T1 = Tree(tree_list=["AND", Tree.tree_list_EQU(2), [None]],
                name='T1',
                switches=[V0, value_list[1], V])
    T2 = Tree(tree_list=["AND", Tree.tree_list_EQU(2), [None]],
                name='T2',
                switches=[V0, value_list[2], V])
    T3 = Tree(tree_list=["AND", Tree.tree_list_EQU(2), [None]],
                name='T3',
                switches=[V0, value_list[3], V])
    T4 = Tree(tree_list=["AND", Tree.tree_list_EQU(2), [None]],
                name='T4',
                switches=[V0, value_list[4], V])

    dx = 0.8
    dy = 1
    ex = 1
    ey = 0.6

    R0 = Room(name='R0',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[0*dx, 3*dy, ex, ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[4*dx, 3*dy, ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[4*dx, 1*dy, ex, ey],
                switches_list=Slist_4)
    RE = Room(name='RE',
              position=[2*dx, 0*dy, ex, ey],
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
                room_departure=R0,
                room_arrival=R4)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R0,
                room_arrival=RE)
    
    Rl = [R1, R2, R3, R4]
    Rnames = [R.name for R in Rl]
    rd_shuffle(Rnames)
    Rpos = [R.position for R in Rl]
    rd_shuffle(Rpos)
    for i, R in enumerate(Rl):
        R.name = Rnames[i]
        R.position = Rpos[i]
    
    Dl = [D0, D1, D2, D3, D4]
    Dnames = [D.name for D in Dl]
    rd_shuffle(Dnames)
    for i, D in enumerate(Dl):
        D.name = Dnames[i]

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=Dl,
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Keys',
                 keep_proportions=True,
                 door_window_size=385,
                 random=True)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.15, sa=0.4, li=0.2)