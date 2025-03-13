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
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')
    S20 = Switch(name='S20')
    S21 = Switch(name='S21')
    S22 = Switch(name='S22')
    S23 = Switch(name='S23')
    
    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    Slist_3 = [S9, S10, S11]
    Slist_4 = [S12, S13, S14]
    Slist_5 = [S15, S16, S17]
    Slist_6 = [S18, S19, S20]
    Slist_7 = [S21, S22, S23]
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
    V7 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_7)),
          name='V7',
          switches=Slist_7)

    Vlist = [V0, V1, V2, V3, V4, V5, V6, V7]
    l = [0, 1, 2, 3, 4, 5, 6, 7]
    rd_shuffle(l)
    
    VlE = []
    nl = []
    for iV in range(4):
        Si = [rd_choice([i for i in range(8)]) for _ in range(4)]
        SlV = []
        for b, i in enumerate(Si):
            SlV.extend([Vlist[i], 8, b])
        V = Tree(tree_list=["SUM"]+[["PROD", [None], ["POW", [None], [None]]]]*4,
                 name=f'V{len(VlE)+8}',
                 switches=SlV)
        VlE.append(V)
        n = 0
        for b, i in enumerate(Si):
            n += l[i]*8**i
        nl.append(n)
    Vsum_tl = ["SUM"]
    Vsum_Sl = []
    N = sum(nl)
    b = 0
    while N!=0:
        i = l.index(N%8)
        Vsum_Sl.extend([Vlist[i], 8, b])
        Vsum_tl.append(["PROD", [None], ["POW", [None], [None]]])
        N = N//8 
        b += 1
    Vsum = Tree(tree_list=Vsum_tl,
                name=f'V{len(VlE)+8}',
                switches=Vsum_Sl)
    VE = Tree(tree_list=["EQU", Tree.tree_list_SUM(4), [None]],
              name=f'V{len(VlE)+8+1}',
              switches=SlV+[Vsum])
    
    def get_tree(i):
        return Tree(tree_list=Tree.tree_list_DIFF(i+1),
                    name=f'T{i}',
                    switches=Vlist[:i+1])
    T0 = Tree(tree_list=[None],
              name='T0',
              switches=[1])
    T1 = get_tree(1)
    T2 = get_tree(2)
    T3 = get_tree(3)
    T4 = get_tree(4)
    T5 = get_tree(5)
    T6 = get_tree(6)
    T7 = Tree(tree_list=["AND",
                         Tree.tree_list_DIFF(8),
                         [None]],
                name='T7',
                switches=Vlist+[VE])

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=Slist_4)
    R5 = Room(name='R5',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=Slist_5)
    R6 = Room(name='R6',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=Slist_6)
    R7 = Room(name='R7',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=Slist_7)
    RE = Room(name='RE',
              position=[2*dx, 2*dy, ex, ey],
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
                room_arrival=R3)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R5)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R5,
                room_arrival=R6)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R6,
                room_arrival=R7)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R7,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='TODO',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.6)
    lcolor.surrounding_color = Color.IVORY
    lcolor.contour_color = Color.color_hls(hu=0, sa=1, li=0.3)
    return lcolor