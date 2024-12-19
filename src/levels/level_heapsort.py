from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color
from random import shuffle as rd_shuffle

def f():
    
    ilist = [[0, 1, 0],
             [1, 0, 0],
             [1, 1, 0],
             [0, 0, 1],
             [1, 0, 1],
             [0, 1, 1],
             [1, 1, 1]]
    rd_shuffle(ilist)
    #ilist.reverse()

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
    
    S12 = Switch(name='S12', value=ilist[4][0])
    S13 = Switch(name='S13', value=ilist[4][1])
    S14 = Switch(name='S14', value=ilist[4][2])
    
    S15 = Switch(name='S15', value=ilist[5][0])
    S16 = Switch(name='S16', value=ilist[5][1])
    S17 = Switch(name='S17', value=ilist[5][2])

    S18 = Switch(name='S18', value=ilist[6][0])
    S19 = Switch(name='S19', value=ilist[6][1])
    S20 = Switch(name='S20', value=ilist[6][2])
    
    S21 = Switch(name='S21', value=0)
    S22 = Switch(name='S22', value=0)
    S23 = Switch(name='S23', value=0)
    S24 = Switch(name='S24', value=1)
    S25 = Switch(name='S25', value=1)
    S26 = Switch(name='S26', value=1)
    S27 = Switch(name='S27', value=1)
    S28 = Switch(name='S28', value=1)
    S29 = Switch(name='S29', value=1)

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29]

    Slist0 = Slist[0:3]
    Slist1 = Slist[3:6]
    Slist2 = Slist[6:9]
    Slist3 = Slist[9:12]
    Slist4 = Slist[12:15]
    Slist5 = Slist[15:18]
    Slist6 = Slist[18:21]
    Slist7 = Slist[21:24]
    Slist8 = Slist[24:27]
    Slist9 = Slist[27:30]

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
    V8 = Tree(tree_list=Tree.tree_list_BIN(len(Slist8)),
          name='V8',
          switches=Slist8)
    V9 = Tree(tree_list=Tree.tree_list_BIN(len(Slist9)),
          name='V9',
          switches=Slist9)
    
    Vlist = [V0, V1, V2, V3, V4, V5, V6]
    
    value_list = []
    for V in Vlist:
        value_list.append(V.get_value())
        
    V10 = Tree(tree_list=['EQUSET'] + [[None]]*(2*len(value_list)),
                name='V10',
                switches=Vlist + value_list,
                cut_expression=True,
                cut_expression_separator=')')
    V11 = Tree(tree_list=['AND'] + [['XNOR',
                                     ['INF', [None], [None]],
                                     ['INFOREQU', [None], [None]]]]*6,
               name='V11',
               switches=[V0, V1, V8, 1,
                         V0, V2, V8, 2,
                         V1, V3, V8, 3,
                         V1, V4, V8, 4,
                         V2, V5, V8, 5,
                         V2, V6, V8, 6,
                         ],
               cut_expression_depth_1=True)

    Vlist = [V0, V1, V2, V3, V4, V5, V6, V7, V8, V9]

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[V10])
    T1 = Tree(tree_list=['AND',
                         ['EQU', [None], [None]],
                         [None]],
                name='T1',
                switches=[V7, 7, V11])
    T2 = Tree(tree_list=['EQU',
                         [None],
                         ['SUM',
                          [None],
                          ['MINUS', [None]]]],
                name='T2',
                switches=[V8, V9, 1])
    T3 = Tree(tree_list=['EQU', [None], [None]],
                name='T3',
                switches=[V8, V9])
    T4 = Tree(tree_list=['AND', [None]] + [['NAND',
                                    ['EQU', [None], [None]],
                                    ['SUP', [None], [None]]]]*6,
                name='T4',
                switches=[V10,
                          V8, 1, V0, V1,
                          V8, 2, V0, V2,
                          V8, 3, V1, V3,
                          V8, 4, V1, V4,
                          V8, 5, V2, V5,
                          V8, 6, V2, V6,],
                cut_expression_depth_1=True)
    T5 = Tree(tree_list=Tree.tree_list_IN(3),
                name='T5',
                switches=[V7, 1, 2])
    T6 = Tree(tree_list=["AND",
                         Tree.tree_list_IN(4),
                         ['SUP', [None], [None]]],
                name='T6',
                switches=[V7, 1, 3, 4, V8, 1])
    T7 = Tree(tree_list=["AND",
                         Tree.tree_list_IN(4),
                         ['SUP', [None], [None]]],
                name='T7',
                switches=[V7, 2, 5, 6, V8, 2])
    T8 = Tree(tree_list=["AND",
                         Tree.tree_list_EQU(2),
                         ['SUP', [None], [None]]],
                name='T8',
                switches=[V7, 3, V8, 3])
    T9 = Tree(tree_list=["AND",
                         Tree.tree_list_EQU(2),
                         ['SUP', [None], [None]]],
                name='T9',
                switches=[V7, 4, V8, 4])
    T10 = Tree(tree_list=["AND",
                          Tree.tree_list_EQU(2),
                          ['SUP', [None], [None]]],
                name='T10',
                switches=[V7, 5, V8, 5])
    T11 = Tree(tree_list=["AND",
                          Tree.tree_list_EQU(2),
                          ['SUP', [None], [None]]],
                name='T11',
                switches=[V7, 6, V8, 6])
    T12 = Tree(tree_list=[None],
                name='T12',
                switches=[1])
    T13 = Tree(tree_list=['EQU', [None], [None]],
                name='T13',
                switches=[V8, 1])
    T14 = Tree(tree_list=['EQU', [None], [None]],
                name='T14',
                switches=[V8, 2])
    T15 = Tree(tree_list=['EQU', [None], [None]],
                name='T15',
                switches=[V8, 3])
    T16 = Tree(tree_list=['EQU', [None], [None]],
                name='T16',
                switches=[V8, 4])
    T17 = Tree(tree_list=['EQU', [None], [None]],
                name='T17',
                switches=[V8, 5])
    T18 = Tree(tree_list=['EQU', [None], [None]],
                name='T18',
                switches=[V8, 6])
    T19 = Tree(tree_list=['AND',
                          ['INF'] + [[None]]*7,
                          ['EQU', [None], [None], [None], [None]]],
                name='T19',
                switches=Vlist + [V7, V8, V9, 0])

    dx = 1.6
    dx_bis = 9*dx/8
    dy = 1.3
    ex = 1
    ey = 1
    exe = 2
    eye = 2
    
    cx = 7*dx+ex

    R0 = Room(name='R0',
                position=[0, 2*dy, ex, 4*dy+ey],
                switches_list=Slist7)
    R1 = Room(name='R1',
                position=[0*dx, 0*dy, cx, ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[9*dx, 2*dy, ex, 2*dy+ey],
                switches_list=Slist8)
    R3 = Room(name='R3',
                position=[9*dx, 6*dy, ex, 2*dy+ey],
                switches_list=Slist9)
    R4 = Room(name='R4',
                position=[0*dx, 8*dy, cx, ey],
                switches_list=[])
    R5 = Room(name='R5',
                position=[4*dx_bis, 2*dy, ex, 2*dy+ey],
                switches_list=Slist0)
    R6 = Room(name='R6',
                position=[2*dx_bis, 3*dy, ex, 2*dy+ey],
                switches_list=Slist1)
    R7 = Room(name='R7',
                position=[6*dx_bis, 3*dy, ex, 2*dy+ey],
                switches_list=Slist2)
    R8 = Room(name='R8',
                position=[1*dx_bis, 4*dy, ex, 2*dy+ey],
                switches_list=Slist3)
    R9 = Room(name='R9',
                position=[3*dx_bis, 4*dy, ex, 2*dy+ey],
                switches_list=Slist4)
    R10 = Room(name='R10',
                position=[5*dx_bis, 4*dy, ex, 2*dy+ey],
                switches_list=Slist5)
    R11 = Room(name='R11',
                position=[7*dx_bis, 4*dy, ex, 2*dy+ey],
                switches_list=Slist6)
    RE = Room(name='RE',
              position=[9*dx+(ex-exe)/2, (ey-eye)/2, exe, eye],
              is_exit=True)
    
    def get_rc0(i):
        return [(dx+i*dx+ex/2)/cx, 0]
    def get_rc1(i):
        return [(dx+i*dx+ex/2)/cx, 1]
    
    rc0 = [1/2, 0]
    rc1 = [1/2, 1]

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[ex/2/cx, 1])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=[1, 1],
                relative_arrival_coordinates=[0, 0])
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4,
                relative_departure_coordinates=[0, (2*dy+ey/2)/(2*dy+ey)],
                relative_arrival_coordinates=[1, 1/2])
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R0,
                relative_departure_coordinates=[ex/2/cx, 0],
                relative_arrival_coordinates=[1/2, 1])
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R1,
                room_arrival=R5,
                relative_departure_coordinates=get_rc1(3),
                relative_arrival_coordinates=rc0)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R1,
                room_arrival=R6,
                relative_departure_coordinates=get_rc1(1),
                relative_arrival_coordinates=rc0)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R1,
                room_arrival=R7,
                relative_departure_coordinates=get_rc1(5),
                relative_arrival_coordinates=rc0)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R1,
                room_arrival=R8,
                relative_departure_coordinates=get_rc1(0),
                relative_arrival_coordinates=rc0)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R1,
                room_arrival=R9,
                relative_departure_coordinates=get_rc1(2),
                relative_arrival_coordinates=rc0)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R1,
                room_arrival=R10,
                relative_departure_coordinates=get_rc1(4),
                relative_arrival_coordinates=rc0)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R1,
                room_arrival=R11,
                relative_departure_coordinates=get_rc1(6),
                relative_arrival_coordinates=rc0)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R4,
                room_arrival=R5,
                relative_departure_coordinates=get_rc0(3),
                relative_arrival_coordinates=rc1)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R4,
                room_arrival=R6,
                relative_departure_coordinates=get_rc0(1),
                relative_arrival_coordinates=rc1)
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R4,
                room_arrival=R7,
                relative_departure_coordinates=get_rc0(5),
                relative_arrival_coordinates=rc1)
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R4,
                room_arrival=R8,
                relative_departure_coordinates=get_rc0(0),
                relative_arrival_coordinates=rc1)
    D16 = Door(two_way=True,
                tree=T16,
                name='D16',
                room_departure=R4,
                room_arrival=R9,
                relative_departure_coordinates=get_rc0(2),
                relative_arrival_coordinates=rc1)
    D17 = Door(two_way=True,
                tree=T17,
                name='D17',
                room_departure=R4,
                room_arrival=R10,
                relative_departure_coordinates=get_rc0(4),
                relative_arrival_coordinates=rc1)
    D18 = Door(two_way=True,
                tree=T18,
                name='D18',
                room_departure=R4,
                room_arrival=R11,
                relative_departure_coordinates=get_rc0(6),
                relative_arrival_coordinates=rc1)
    D19 = Door(two_way=True,
                tree=T19,
                name='D19',
                room_departure=R1,
                room_arrival=RE,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 1/2])
    
    hu = 0.05
    lcolor = Level_color(background_color=Color.color_hls(hu, li=0.7, sa=0.3),
                         room_color=Color.color_hls(hu, li=0.4, sa=0.4),
                         letters_color=Color.BLACK,
                         contour_color=Color.color_hls(hu=0.9, li=0.1, sa=1),
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.color_hls(hu=0.9, li=0.1, sa=1))

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19,],
                 fastest_solution=None,
                 level_color=lcolor,
                 name='Heap sort',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level