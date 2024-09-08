from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color
from random import shuffle as rd_shuffle

def level_merge_sort():
    
    ilist = [[0, 0, 0],
             [0, 1, 0],
             [1, 0, 0],
             [1, 1, 0]]
    rd_shuffle(ilist)

    S0 = Switch(name='S0', value=ilist[0][0])
    S1 = Switch(name='S1', value=ilist[0][1])
    S2 = Switch(name='S2', value=ilist[0][2])
    
    S3 = Switch(name='S3', value=ilist[1][0])
    S4 = Switch(name='S4', value=ilist[1][1])
    S5 = Switch(name='S5', value=ilist[1][2])
    
    S6 = Switch(name='S6', value=ilist[2][0])
    S7 = Switch(name='S7', value=ilist[2][1])
    S8 = Switch(name='S8', value=ilist[2][2])
    
    S9 = Switch(name='S9', value=ilist[3][0])
    S10 = Switch(name='S10', value=ilist[3][1])
    S11 = Switch(name='S11', value=ilist[3][2])
    
    S12 = Switch(name='S12', value=1)
    S13 = Switch(name='S13', value=1)
    S14 = Switch(name='S14', value=1)
    
    S15 = Switch(name='S15', value=1)
    S16 = Switch(name='S16', value=1)
    S17 = Switch(name='S17', value=1)
    
    S18 = Switch(name='S18', value=1)
    S19 = Switch(name='S19', value=1)
    S20 = Switch(name='S20', value=1)
    
    S21 = Switch(name='S21', value=1)
    S22 = Switch(name='S22', value=1)
    S23 = Switch(name='S23', value=1)

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23]

    Slist0 = Slist[0:3]
    Slist1 = Slist[3:6]
    Slist2 = Slist[6:9]
    Slist3 = Slist[9:12]
    Slist4 = Slist[12:15]
    Slist5 = Slist[15:18]
    Slist6 = Slist[18:21]
    Slist7 = Slist[21:24]

    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist0)),
          name='V0',
          switches=Slist0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(len(Slist1)),
          name='V1',
          switches=Slist1)
    V2 = Tree(tree_list=Tree.tree_list_BIN(len(Slist2)),
          name='V2',
          switches=Slist2)
    V3 = Tree(tree_list=Tree.tree_list_BIN(len(Slist3)),
          name='V3',
          switches=Slist3)
    V4 = Tree(tree_list=Tree.tree_list_BIN(len(Slist4)),
          name='V4',
          switches=Slist4)
    V5 = Tree(tree_list=Tree.tree_list_BIN(len(Slist5)),
          name='V5',
          switches=Slist5)
    V6 = Tree(tree_list=Tree.tree_list_BIN(len(Slist6)),
          name='V6',
          switches=Slist6)
    V7 = Tree(tree_list=Tree.tree_list_BIN(len(Slist7)),
          name='V7',
          switches=Slist7)
    V8 = Tree(tree_list=['AND'] + [Tree.tree_list_INF(2)]*2,
          name='V8',
          switches=[V0, V1, V2, V3])
    V9 = Tree(tree_list=['EQUSET'] + [[None]]*8,
          name='V9',
          switches=[V0, V1, V2, V3, 0, 1, 2, 3])
    V10 = Tree(tree_list=['EQU'] + [[None]]*5,
          name='V10',
          switches=[7, V4, V5, V6, V7])
    V11 = Tree(tree_list=['MIN'] + [[None]]*2,
          name='V11',
          switches=[V0, V2])
    V12 = Tree(tree_list=['AND'] + [Tree.tree_list_INFOREQU(2)]*2,
          name='V12',
          switches=[V0, V1, V2, V3])

    Vlist = [V0, V1, V2, V3, V4, V5, V6, V7]

    T0 = Tree(tree_list=Tree.tree_list_from_str('TF'),
                name='T0',
                switches=[V10, V8])
    T1 = Tree(tree_list=Tree.tree_list_from_str('TF'),
                name='T1',
                switches=[V10, V8])
    T2 = Tree(tree_list=Tree.tree_list_from_str('TF'),
                name='T2',
                switches=[V10, V8])
    T3 = Tree(tree_list=Tree.tree_list_from_str('TF'),
                name='T3',
                switches=[V10, V8])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[V12])
    T5 = Tree(tree_list=['EQU', [None], [None]],
                name='T5',
                switches=[V0, V1])
    T6 = Tree(tree_list=['EQU', [None], [None]],
                name='T6',
                switches=[V1, 7])
    T7 = Tree(tree_list=[None],
                name='T7',
                switches=[V12])
    T8 = Tree(tree_list=['EQU', [None], [None]],
                name='T8',
                switches=[V2, V3])
    T9 = Tree(tree_list=['EQU', [None], [None]],
                name='T9',
                switches=[V3, 7])
    T10 = Tree(tree_list=Tree.tree_list_AND(3),
                name='T10',
                switches=[V8, V9, V10])
    T11 = Tree(tree_list=Tree.tree_list_AND(3),
                name='T11',
                switches=[V8, V9, V10])
    T12 = Tree(tree_list=[None],
                name='T12',
                switches=[V12])
    T13 = Tree(tree_list=['EQU', [None], [None]],
                name='T13',
                switches=[V6, V7])
    T14 = Tree(tree_list=['EQU', [None], [None]],
                name='T14',
                switches=[V5, V6])
    T15 = Tree(tree_list=['EQU', [None], [None]],
                name='T15',
                switches=[V4, V5])
    T16 = Tree(tree_list=['AND',
                          ['EQU', [None], [None]],
                          ['INF', [None], [None]]],
                name='T16',
                switches=[V7, V11, V6, V7])
    T17 = Tree(tree_list=['AND',
                          ['EQU', [None], [None]],
                          ['INF', [None], [None]]],
                name='T17',
                switches=[V6, V11, V5, V6])
    T18 = Tree(tree_list=['AND',
                          ['EQU', [None], [None]],
                          ['INF', [None], [None]]],
                name='T18',
                switches=[V5, V11, V4, V5])
    T19 = Tree(tree_list=['EQU', [None], [None]],
                name='T19',
                switches=[V4, V11])
    T20 = Tree(tree_list=['AND',
                          ['EQUSET'] + [[None]]*8,
                          Tree.tree_list_INF(4),
                          ['EQU']+[[None]]*5],
                name='T20',
                switches=[V4, V5, V6, V7, 0, 1, 2, 3,
                          V4, V5, V6, V7,
                          V0, V1, V2, V3, 7])

    dx = 2
    dy = 1
    ex = 0.6
    ey = 0.6
    
    ey0 = 0.25
    eye = 0.4
    
    ax = 0.05
    ay = ax
    
    n = 4.5
    
    deltay1 = n*ey+ay
    deltay2 = deltay1+ey0+ay

    R0 = Room(name='R0',
                position=[0*dx, deltay1, 3*dx+ex, ey0],
                switches_list=[])
    R1 = Room(name='R1',
                position=[0*dx, 0*dy, ex, n*ey],
                switches_list=Slist0)
    R2 = Room(name='R2',
                position=[1*dx, 0*dy, ex, n*ey],
                switches_list=Slist1)
    R3 = Room(name='R3',
                position=[2*dx, 0*dy, ex, n*ey],
                switches_list=Slist2)
    R4 = Room(name='R4',
                position=[3*dx, 0*dy, ex, n*ey],
                switches_list=Slist3)
    R5 = Room(name='R5',
                position=[0*dx, deltay2, ex, 3*ey],
                switches_list=Slist4)
    R6 = Room(name='R6',
                position=[1*dx, deltay2, ex, 3*ey],
                switches_list=Slist5)
    R7 = Room(name='R7',
                position=[2*dx, deltay2, ex, 3*ey],
                switches_list=Slist6)
    R8 = Room(name='R8',
                position=[3*dx, deltay2, ex, 3*ey],
                switches_list=Slist7)
    RE = Room(name='RE',
              position=[dx+ex+ax, 0, dx-ex-2*ax, ey],
              is_exit=True)
    
    p = 0.2
    rp = 0.6

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[(dx+ex)/2/(3*dx+ex), 0],
                relative_arrival_coordinates=[1, p])
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R2,
                relative_departure_coordinates=[(dx+ex)/2/(3*dx+ex), 0],
                relative_arrival_coordinates=[0, p])
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=R3,
                relative_departure_coordinates=[(2*dx+dx/2+ex/2)/(3*dx+ex), 0],
                relative_arrival_coordinates=[1, p])
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R0,
                room_arrival=R4,
                relative_departure_coordinates=[(2*dx+dx/2+ex/2)/(3*dx+ex), 0],
                relative_arrival_coordinates=[0, p])
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[(dx+ex)/2/(3*dx+ex), 0],
                relative_arrival_coordinates=[1, 1-p],
                relative_position=rp)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=[1/2, p],
                relative_arrival_coordinates=[1/2, p])
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R2,
                room_arrival=R0,
                relative_departure_coordinates=[1, 1-p],
                relative_arrival_coordinates=[1/2, 0])
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R0,
                room_arrival=R3,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[0, 1-p],
                relative_position=rp)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R3,
                room_arrival=R4,
                relative_departure_coordinates=[1/2, p],
                relative_arrival_coordinates=[1/2, p])
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R4,
                room_arrival=R0,
                relative_departure_coordinates=[0, 1-p],
                relative_arrival_coordinates=[(2*dx+dx/2+ex/2)/(3*dx+ex), 0])
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R2,
                room_arrival=R0,
                relative_departure_coordinates=[0, 1-p],
                relative_arrival_coordinates=[(dx+ex)/2/(3*dx+ex), 0])
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R3,
                room_arrival=R0,
                relative_departure_coordinates=[1, 1-p],
                relative_arrival_coordinates=[(2*dx+dx/2+ex/2)/(3*dx+ex), 0])
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R0,
                room_arrival=R8,
                relative_departure_coordinates=[(2*dx+dx/2+ex/2)/(3*dx+ex), 1],
                relative_arrival_coordinates=[0, 1-p],
                relative_position=0.7)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R8,
                room_arrival=R7,
                relative_departure_coordinates=[0, 1-p],
                relative_arrival_coordinates=[1, 1-p])
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R7,
                room_arrival=R6,
                relative_departure_coordinates=[0, 1-p],
                relative_arrival_coordinates=[1, 1-p])
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R6,
                room_arrival=R5,
                relative_departure_coordinates=[0, 1-p],
                relative_arrival_coordinates=[1, 1-p])
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R8,
                room_arrival=R0,
                relative_departure_coordinates=[0, 1-p],
                relative_arrival_coordinates=[(2*dx+dx/2+ex/2)/(3*dx+ex), 1],
                relative_position=0.7)
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R7,
                room_arrival=R0,
                relative_departure_coordinates=[0, 1-p],
                relative_arrival_coordinates=[1/2, 1])
    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=R6,
                room_arrival=R0,
                relative_departure_coordinates=[1, 1-p],
                relative_arrival_coordinates=[1/2, 1])
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R5,
                room_arrival=R0,
                relative_departure_coordinates=[1, 1-p],
                relative_arrival_coordinates=[(dx+ex)/2/(3*dx+ex), 1])
    D20 = Door(two_way=False,
                tree=T20,
                name='D20',
                room_departure=R0,
                room_arrival=RE)
    
    hu = 0.4
    lcolor = Level_color(background_color=Color.color_hls(hu, li=0.7, sa=0.3),
                         room_color=Color.color_hls(hu, li=0.4, sa=0.4),
                         letters_color=Color.BLACK,
                         contour_color=Color.color_hls(hu=0.9, li=0.1, sa=1),
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.color_hls(hu=0.9, li=0.1, sa=1))

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9,
                             D10, D11,
                             D12, D13, D14, D15, D16, D17, D18, D19, D20],
                 fastest_solution=None,
                 level_color=lcolor,
                 name='Merge sort',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level