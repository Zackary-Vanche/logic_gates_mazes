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
    
    ########################
    
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
    
    ########################
    
    S18 = Switch(name='S18', value=1)
    S19 = Switch(name='S19')
    S20 = Switch(name='S20')
    
    S21 = Switch(name='S21')
    S22 = Switch(name='S22', value=1)
    S23 = Switch(name='S23')
    
    S24 = Switch(name='S24', value=1)
    S25 = Switch(name='S25', value=1)
    S26 = Switch(name='S26')
    
    S27 = Switch(name='S27')
    S28 = Switch(name='S28')
    S29 = Switch(name='S29', value=1)
    
    S30 = Switch(name='S30', value=1)
    S31 = Switch(name='S31')
    S32 = Switch(name='S32', value=1)
    
    ########################
    
    S33 = Switch(name='S33')
    S34 = Switch(name='S34')
    S35 = Switch(name='S35')
    
    S36 = Switch(name='S36')
    S37 = Switch(name='S37')
    S38 = Switch(name='S38')
    
    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    Slist_3 = [S9, S10, S11]
    Slist_4 = [S12, S13, S14]
    Slist_5 = [S15, S16, S17]
    Slist_6 = [S18, S19, S20]
    Slist_7 = [S21, S22, S23]
    Slist_8 = [S24, S25, S26]
    Slist_9 = [S27, S28, S29]
    Slist_10 = [S30, S31, S32]
    Slist_11 = [S33, S34, S35]
    Slist_12 = [S36, S37, S38]
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
    V8 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_8)),
          name='V8',
          switches=Slist_8)
    V9 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_9)),
          name='V9',
          switches=Slist_9)
    V10 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_10)),
          name='V10',
          switches=Slist_10)
    V11 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_11)),
          name='V11',
          switches=Slist_11)
    V12 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_12)),
          name='V12',
          switches=Slist_12)
    
    Vl = [V6, V7, V8, V9, V10]
    rd_shuffle(Vl)
    
    tl = Tree.tree_list_EQU(2)

    T0 = Tree(tree_list=Tree.tree_list_INF(2),
                name='T0',
                switches=[V0, 7])
    
    T1 = Tree(tree_list=tl,
                name='T1',
                switches=[V1, Vl[0]])
    T2 = Tree(tree_list=tl,
                name='T2',
                switches=[V2, Vl[1]])
    T3 = Tree(tree_list=tl,
                name='T3',
                switches=[V3, Vl[2]])
    T4 = Tree(tree_list=tl,
                name='T4',
                switches=[V4, Vl[3]])
    T5 = Tree(tree_list=tl,
                name='T5',
                switches=[V5, Vl[4]])
    
    T6 = Tree(tree_list=tl,
                name='T6',
                switches=[V1, V6])
    T7 = Tree(tree_list=tl,
                name='T7',
                switches=[V2, V7])
    T8 = Tree(tree_list=tl,
                name='T8',
                switches=[V3, V8])
    T9 = Tree(tree_list=tl,
                name='T9',
                switches=[V4, V9])
    T10 = Tree(tree_list=tl,
                name='T10',
                switches=[V5, V10])
    
    T11 = Tree(tree_list=["EQU", [None], Tree.tree_list_SUM(2)],
                name='T11',
                switches=[V11, V12, 1])
    T12 = Tree(tree_list=tl,
                name='T12',
                switches=[V11, V12])
    T13 = Tree(tree_list=Tree.tree_list_INF(2),
                name='T13',
                switches=[V12, V0])
    T14 = Tree(tree_list=["AND", Tree.tree_list_EQU(2), Tree.tree_list_INF(5)],
                name='T14',
                switches=[V0, V12, V1, V2, V3, V4, V5])

    dx = 0.9
    dy = 1.3
    ex = 0.375
    ey = 3*ex
    
    ay = dy/4
    
    dhu = 0.125
    PURPLE = tuple(Color.color_hls(hu=-dhu, li=0.2, sa=1))
    RED = tuple(Color.color_hls(hu=0, li=0.2, sa=1))
    ORANGE = tuple(Color.color_hls(hu=+dhu, li=0.2, sa=1))

    R0 = Room(name='R0',
                position=[2*dx, -1*dy, dx+ex, ex],
                switches_list=Slist_0,
                inside_color=RED)
    
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=Slist_1,
                inside_color=ORANGE)
    R2 = Room(name='R2',
                position=[2*dx, -ay, ex, ey],
                switches_list=Slist_2,
                inside_color=ORANGE)
    R3 = Room(name='R3',
                position=[3*dx, -2*ay, ex, ey],
                switches_list=Slist_3,
                inside_color=ORANGE)
    R4 = Room(name='R4',
                position=[4*dx, -3*ay, ex, ey],
                switches_list=Slist_4,
                inside_color=ORANGE)
    R5 = Room(name='R5',
                position=[5*dx, -4*ay, ex, ey],
                switches_list=Slist_5,
                inside_color=ORANGE)
    
    R6 = Room(name='R6',
                position=[5*dx, 1*dy, ex, ey],
                switches_list=Slist_6,
                inside_color=PURPLE)
    R7 = Room(name='R7',
                position=[4*dx, 1*dy-ay, ex, ey],
                switches_list=Slist_7,
                inside_color=PURPLE)
    R8 = Room(name='R8',
                position=[3*dx, 1*dy-2*ay, ex, ey],
                switches_list=Slist_8,
                inside_color=PURPLE)
    R9 = Room(name='R9',
                position=[2*dx, 1*dy-ay, ex, ey],
                switches_list=Slist_9,
                inside_color=PURPLE)
    R10 = Room(name='R10',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=Slist_10,
                inside_color=PURPLE)
    
    R11 = Room(name='R11',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=Slist_11,
                inside_color=RED)
    R12 = Room(name='R12',
                position=[0*dx, 0*dy-ey/4, ex, ey],
                switches_list=Slist_12,
                inside_color=RED)
    R13 = Room(name='R13',
                position=[0*dx, -1*dy, ex, ey/2],
                switches_list=[],
                inside_color=RED)
    RE = Room(name='RE',
              position=[1*dx, -1*dy, ex, ey/2],
              is_exit=True,
              inside_color=RED)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1/6, 1/2],
                relative_arrival_coordinates=[1/2, 1/6])
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
                room_arrival=R8)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R8,
                room_arrival=R9)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R9,
                room_arrival=R10)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R10,
                room_arrival=R11)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R11,
                room_arrival=R12)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R12,
                room_arrival=R13,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[1/2, 1])
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R13,
                room_arrival=R1)
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R13,
                room_arrival=RE)

    Dl = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14]
    for D in Dl:
        Rd = D.room_departure
        Ra = D.room_arrival
        hu_l = []
        cdict = {PURPLE:-dhu,
                 RED:0,
                 ORANGE:+dhu}
        for c in cdict.keys():
            hu = cdict[c]
            if Rd.inside_color == c:
                hu_l.append(hu)
            if Ra.inside_color == c:
                hu_l.append(hu)
        D.inside_color = Color.color_hls(hu=sum(hu_l)/2, li=0.2, sa=1)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, RE],
                 doors_list=Dl,
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Order of a permutation',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True,
                 uniform_inside_room_color=False)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.05, sa=1, li=0.2)