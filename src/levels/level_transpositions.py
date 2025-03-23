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
    
    S6 = Switch(name='S6', value=1)
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    
    S9 = Switch(name='S9')
    S10 = Switch(name='S10', value=1)
    S11 = Switch(name='S11')
    
    S12 = Switch(name='S12', value=1)
    S13 = Switch(name='S13', value=1)
    S14 = Switch(name='S14')
    
    S15 = Switch(name='S15')
    S16 = Switch(name='S16')
    S17 = Switch(name='S17', value=1)
    
    S18 = Switch(name='S18', value=1)
    S19 = Switch(name='S19')
    S20 = Switch(name='S20', value=1)
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20]
    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    Slist_3 = [S9, S10, S11]
    Slist_4 = [S12, S13, S14]
    Slist_5 = [S15, S16, S17]
    Slist_6 = [S18, S19, S20]
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
    V5 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_5)),
          name='V5',
          switches=Slist_5)
    V6 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_6)),
          name='V6',
          switches=Slist_6)
    Vlist = [V2, V3, V4, V5, V6]
    V7 = Tree(tree_list=Tree.tree_list_EQUSET(len(Vlist)*2),
          name='V7',
          switches=Vlist+[1, 2, 3, 4, 5])
    
    tl = ["IN"]+[[None]]*3

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[V7])
    T1 = Tree(tree_list=tl,
                name='T1',
                switches=[1, V0, V1])
    T2 = Tree(tree_list=tl,
                name='T2',
                switches=[2, V0, V1])
    T3 = Tree(tree_list=tl,
                name='T3',
                switches=[3, V0, V1])
    T4 = Tree(tree_list=tl,
                name='T4',
                switches=[4, V0, V1])
    T5 = Tree(tree_list=tl,
                name='T5',
                switches=[5, V0, V1])
    l = [1, 2, 3, 4, 5]
    rd_shuffle(l)
    T6 = Tree(tree_list=['AND'] + [['EQU', [None], [None]]] * 7,
              name='T6',
              switches=[7, V0,
                        7, V1,
                        l[0], V2,
                        l[1], V3,
                        l[2], V4,
                        l[3], V5,
                        l[4], V6],
              cut_expression=True)

    dx = 1.25
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, 4*dx+ex, ey],
                switches_list=Slist_0+Slist_1)
    R1 = Room(name='R1',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[0*dx, 1.1*dy, ex, 3*ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[1*dx, 1.75*dy, ex, 3*ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[2*dx, 2*dy, ex, 3*ey],
                switches_list=Slist_4)
    R5 = Room(name='R5',
                position=[3*dx, 1.75*dy, ex, 3*ey],
                switches_list=Slist_5)
    R6 = Room(name='R6',
                position=[4*dx, 1.1*dy, ex, 3*ey],
                switches_list=Slist_6)
    RE = Room(name='RE',
              position=[2*dx, -1*dy, ex, ey],
              is_exit=True)
    
    rac = [1/2, 1/6]

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                relative_arrival_coordinates=rac)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R3,
                relative_arrival_coordinates=rac)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R4,
                relative_arrival_coordinates=rac)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R1,
                room_arrival=R5,
                relative_arrival_coordinates=rac)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R1,
                room_arrival=R6,
                relative_arrival_coordinates=rac)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Transpositions',
                 keep_proportions=True,
                 door_window_size=425,
                 random=True)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(0, sa=1, li=0.2)