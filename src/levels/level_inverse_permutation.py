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
    S15 = Switch(name='S15')
    S16 = Switch(name='S16')
    S17 = Switch(name='S17')
    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    Slist_3 = [S9, S10, S11]
    Slist_4 = [S12, S13, S14]
    Slist_5 = [S15, S16, S17]
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

    Vlist = [V0, V1, V2, V3, V4, V5]
    l = [1, 2, 3, 4, 5, 6]
    rd_shuffle(l)

    for i in range(6):
        V = Tree(tree_list=["SUM"]+[["PROD", [None], Tree.tree_list_EQU(2)]]*6,
                 name=f'V{i+6}',
                 switches=[0, Vlist[i], l[0],
                           1, Vlist[i], l[1],
                           2, Vlist[i], l[2],
                           3, Vlist[i], l[3],
                           4, Vlist[i], l[4],
                           5, Vlist[i], l[5]])
        Vlist.append(V)
    
    tl = Tree.tree_list_EQU(2)

    T0 = Tree(tree_list=tl,
                name='T0',
                switches=[Vlist[6], 0])
    T1 = Tree(tree_list=tl,
                name='T1',
                switches=[Vlist[7], 1])
    T2 = Tree(tree_list=tl,
                name='T2',
                switches=[Vlist[8], 2])
    T3 = Tree(tree_list=tl,
                name='T3',
                switches=[Vlist[9], 3])
    T4 = Tree(tree_list=tl,
                name='T4',
                switches=[Vlist[10], 4])
    T5 = Tree(tree_list=tl,
                name='T5',
                switches=[Vlist[11], 5])

    dx = 0.8
    dy = 1
    ex0 = 0.3
    ey0 = 0.95
    ex1 = 0.75
    ey1 = 0.5
    
    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex0, ey0],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[1*dx+(ex0-ex1)/2, 0*dy+(ey0-ey1)/2, ex1, ey1],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[2*dx, 0*dy, ex0, ey0],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[0*dx, 1*dy, ex0, ey0],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[1*dx+(ex0-ex1)/2, 1*dy+(ey0-ey1)/2, ex1, ey1],
                switches_list=Slist_4)
    R5 = Room(name='R5',
                position=[2*dx, 1*dy, ex0, ey0],
                switches_list=Slist_5)
    RE = Room(name='RE',
              position=[1*dx+(ex0-ex1)/2, 2*dy, ex1, ey1],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 1/2])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 1/2])
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3,
                relative_departure_coordinates=[1/2, 0.8],
                relative_arrival_coordinates=[1/2, 0.2])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 1/2])
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R5,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 1/2])
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R5,
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 0.8],
                relative_arrival_coordinates=[1/2, 0.2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Inverse permutation',
                 keep_proportions=True,
                 door_window_size=530,
                 random=True)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.025, sa=0.3, li=0.2)
    lcolor.contour_color = Color.color_hls(hu=0.025/2, sa=1, li=0.6)
    lcolor.surrounding_color = Color.color_hls(hu=0.025/2, sa=0.7, li=0.6)
    return lcolor