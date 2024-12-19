from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color
from random import shuffle as rd_shuffle
from random import choice as rd_choice

def f():
    
    ilist = [[0, 0, 0],
             [0, 1, 0],
             [1, 0, 0],
             [1, 1, 0],
             [0, 0, 1],
             [0, 1, 1],
             [1, 0, 1],
             [1, 1, 1]]
    #ilist.append(rd_choice(ilist))
    rd_shuffle(ilist)

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    
    S6 = Switch(name='S6', value=ilist[0][0])
    S7 = Switch(name='S7', value=ilist[0][1])
    S8 = Switch(name='S8', value=ilist[0][2])
    
    S9 = Switch(name='S9', value=ilist[1][0])
    S10 = Switch(name='S10', value=ilist[1][1])
    S11 = Switch(name='S11', value=ilist[1][2])
    
    S12 = Switch(name='S12', value=ilist[2][0])
    S13 = Switch(name='S13', value=ilist[2][1])
    S14 = Switch(name='S14', value=ilist[2][2])
    
    S15 = Switch(name='S15', value=ilist[3][0])
    S16 = Switch(name='S16', value=ilist[3][1])
    S17 = Switch(name='S17', value=ilist[3][2])
    
    S18 = Switch(name='S18', value=ilist[4][0])
    S19 = Switch(name='S19', value=ilist[4][1])
    S20 = Switch(name='S20', value=ilist[4][2])
    
    S21 = Switch(name='S21', value=ilist[5][0])
    S22 = Switch(name='S22', value=ilist[5][1])
    S23 = Switch(name='S23', value=ilist[5][2])
    
    S24 = Switch(name='S24', value=ilist[6][0])
    S25 = Switch(name='S25', value=ilist[6][1])
    S26 = Switch(name='S26', value=ilist[6][2])
    
    S27 = Switch(name='S27', value=ilist[7][0])
    S28 = Switch(name='S28', value=ilist[7][1])
    S29 = Switch(name='S29', value=ilist[7][2])

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
    
    Vlist = [V2, V3, V4, V5, V6, V7, V8, V9]
    
    value_list = []
    for V in Vlist:
        value_list.append(V.get_value())
        
    V10 = Tree(tree_list=['EQUSET'] + [[None]]*(2*len(value_list)),
               name='V10',
               switches=Vlist + value_list,
               cut_expression=True,
               cut_expression_separator=')')
    
    V11 = Tree(tree_list=['SUM'] + [['INFOREQU', [None], [None]]]*8 + [['MINUS', [None]]],
          name='V11',
          switches=[V2, V0,
                    V3, V0,
                    V4, V0,
                    V5, V0,
                    V6, V0,
                    V7, V0,
                    V8, V0,
                    V9, V0,
                    1])
    
    tree_list_12 = ['XOR',
                    ['INF', [None], [None]],
                    ['INF', [None], [None]]]
    V12 = Tree(tree_list=tree_list_12,
                name='V12',
                switches=[0, V11, V2, V0])
    V13 = Tree(tree_list=tree_list_12,
                name='V13',
                switches=[1, V11, V3, V0])
    V14 = Tree(tree_list=tree_list_12,
                name='V14',
                switches=[2, V11, V4, V0])
    V15 = Tree(tree_list=tree_list_12,
                name='V15',
                switches=[3, V11, V5, V0])
    V16 = Tree(tree_list=tree_list_12,
                name='V16',
                switches=[4, V11, V6, V0])
    V17 = Tree(tree_list=tree_list_12,
                name='V17',
                switches=[5, V11, V7, V0])
    V18 = Tree(tree_list=tree_list_12,
                name='V18',
                switches=[6, V11, V8, V0])
    V19 = Tree(tree_list=tree_list_12,
                name='V19',
                switches=[7, V11, V9, V0])
    
    V20 = Tree(tree_list=['OR'] + [['AND',
                                   ['EQU', [None], [None]],
                                   ['EQU', [None], [None]]]]*8,
                name='V20',
                switches=[V11, 0, V0, V2,
                          V11, 1, V0, V3,
                          V11, 2, V0, V4,
                          V11, 3, V0, V5,
                          V11, 4, V0, V6,
                          V11, 5, V0, V7,
                          V11, 6, V0, V8,
                          V11, 7, V0, V9],
                cut_expression_depth_1=True)
    V21 = Tree(tree_list=Tree.tree_list_NOR(8),
                name='V21',
                switches=[V12, V13, V14, V15, V16, V17, V18, V19])

    tree_list_4 = ['IN'] + [[None]]*3
    tree_list_20 = ['NAND',
                    ['SUP', [None], [None]],
                    Tree.tree_list_NOT]

    T0 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T0',
                switches=[V10, V20])
    T1 = Tree(tree_list=['AND', [None], [None]],
                name='T1',
                switches=[V10, V21])
    T2 = Tree(tree_list=Tree.tree_list_AND(3),
                name='T2',
                switches=[V10, V20, V21])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[V10])
    T4 = Tree(tree_list=tree_list_4,
                name='T4',
                switches=[V2, V0, V1])
    T5 = Tree(tree_list=tree_list_4,
                name='T5',
                switches=[V3, V0, V1])
    T6 = Tree(tree_list=tree_list_4,
                name='T6',
                switches=[V4, V0, V1])
    T7 = Tree(tree_list=tree_list_4,
                name='T7',
                switches=[V5, V0, V1])
    T8 = Tree(tree_list=tree_list_4,
                name='T8',
                switches=[V6, V0, V1])
    T9 = Tree(tree_list=tree_list_4,
                name='T9',
                switches=[V7, V0, V1])
    T10 = Tree(tree_list=tree_list_4,
                name='T10',
                switches=[V8, V0, V1])
    T11 = Tree(tree_list=tree_list_4,
                name='T11',
                switches=[V9, V0, V1])
    
    T12 = Tree(tree_list=[None],
                name='T12',
                switches=[V12])
    T13 = Tree(tree_list=[None],
                name='T13',
                switches=[V13])
    T14 = Tree(tree_list=[None],
                name='T14',
                switches=[V14])
    T15 = Tree(tree_list=[None],
                name='T15',
                switches=[V15])
    T16 = Tree(tree_list=[None],
                name='T16',
                switches=[V16])
    T17 = Tree(tree_list=[None],
                name='T17',
                switches=[V17])
    T18 = Tree(tree_list=[None],
                name='T18',
                switches=[V18])
    T19 = Tree(tree_list=[None],
                name='T19',
                switches=[V19])
    
    T20 = Tree(tree_list=tree_list_20,
                name='T20',
                switches=[V2, V0, V10])
    T21 = Tree(tree_list=tree_list_20,
                name='T21',
                switches=[V3, V0, V10])
    T22 = Tree(tree_list=tree_list_20,
                name='T22',
                switches=[V4, V0, V10])
    T23 = Tree(tree_list=tree_list_20,
                name='T23',
                switches=[V5, V0, V10])
    T24 = Tree(tree_list=tree_list_20,
                name='T24',
                switches=[V6, V0, V10])
    T25 = Tree(tree_list=tree_list_20,
                name='T25',
                switches=[V7, V0, V10])
    T26 = Tree(tree_list=tree_list_20,
                name='T26',
                switches=[V8, V0, V10])
    T27 = Tree(tree_list=tree_list_20,
                name='T27',
                switches=[V9, V0, V10])
               
    T28 = Tree(tree_list=['AND', Tree.tree_list_INF(len(Vlist)), Tree.tree_list_NOR(6)],
                name='T28',
                switches=Vlist + [S0, S1, S2, S3, S4, S5],
                cut_expression_depth_1=True)

    dx = 1
    dy = 1.6
    ex = 0.8
    ey = ex
    ey0 = 0.5

    R0 = Room(name='R0',
                position=[3*dx, -1*dy, 3*dx+ex, ey],
                switches_list=Slist0+Slist1)
    R1 = Room(name='R1',
                position=[0*dx, 2*ey+2*dy+1, 9*dx+ex, ey0],
                switches_list=[])
    R2 = Room(name='R2',
                position=[0*dx, 0*dy, 9*dx+ex, ey0],
                switches_list=[])
    R3 = Room(name='R3',
                position=[1*dx, 1*dy, ex, 3*ey],
                switches_list=Slist2)
    R4 = Room(name='R4',
                position=[2*dx, 1*dy, ex, 3*ey],
                switches_list=Slist3)
    R5 = Room(name='R5',
                position=[3*dx, 1*dy, ex, 3*ey],
                switches_list=Slist4)
    R6 = Room(name='R6',
                position=[4*dx, 1*dy, ex, 3*ey],
                switches_list=Slist5)
    R7 = Room(name='R7',
                position=[5*dx, 1*dy, ex, 3*ey],
                switches_list=Slist6)
    R8 = Room(name='R8',
                position=[6*dx, 1*dy, ex, 3*ey],
                switches_list=Slist7)
    R9 = Room(name='R9',
                position=[7*dx, 1*dy, ex, 3*ey],
                switches_list=Slist8)
    R10 = Room(name='R10',
                position=[8*dx, 1*dy, ex, 3*ey],
                switches_list=Slist9)
    RE = Room(name='RE',
              position=[8*dx, -1*dy, 1*dx+ex, ey],
              is_exit=True)
    
    def get_relative_coordinates_0(i):
        return [((i+1)*dx+ex/2)/(9*dx+ex), 0]
    def get_relative_coordinates_1(i):
        return [((i+1)*dx+ex/2)/(9*dx+ex), 1]
    
    rc0 = [1/2, 0]
    rc1 = [1/2, 1]
    
    rp = 0.75

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R2,
                room_arrival=R1,
                relative_departure_coordinates=[ex/2/(9*dx+ex), 1/2],
                relative_arrival_coordinates=[ex/2/(9*dx+ex), 1/2])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=[(9*dx+ex/2)/(9*dx+ex), 1/2],
                relative_arrival_coordinates=[(9*dx+ex/2)/(9*dx+ex), 1/2])
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R0,
                relative_departure_coordinates=[ex/2/(9*dx+ex), 0],
                relative_arrival_coordinates=[ex/2/(3*dx+ex), 3/4])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R0,
                room_arrival=R2,
                relative_departure_coordinates=[(3*dx+ex/2)/(3*dx+ex), 3/4],
                relative_arrival_coordinates=[(9*dx+ex/2)/(9*dx+ex), 0])
    
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R3,
                relative_departure_coordinates=get_relative_coordinates_1(0),
                relative_arrival_coordinates=rc0)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R2,
                room_arrival=R4,
                relative_departure_coordinates=get_relative_coordinates_1(1),
                relative_arrival_coordinates=rc0)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R2,
                room_arrival=R5,
                relative_departure_coordinates=get_relative_coordinates_1(2),
                relative_arrival_coordinates=rc0)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R2,
                room_arrival=R6,
                relative_departure_coordinates=get_relative_coordinates_1(3),
                relative_arrival_coordinates=rc0)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R2,
                room_arrival=R7,
                relative_departure_coordinates=get_relative_coordinates_1(4),
                relative_arrival_coordinates=rc0)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R2,
                room_arrival=R8,
                relative_departure_coordinates=get_relative_coordinates_1(5),
                relative_arrival_coordinates=rc0)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R2,
                room_arrival=R9,
                relative_departure_coordinates=get_relative_coordinates_1(6),
                relative_arrival_coordinates=rc0)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R2,
                room_arrival=R10,
                relative_departure_coordinates=get_relative_coordinates_1(7),
                relative_arrival_coordinates=rc0)

    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R1,
                room_arrival=R3,
                relative_departure_coordinates=get_relative_coordinates_0(0),
                relative_arrival_coordinates=rc1,
                relative_position=rp)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R1,
                room_arrival=R4,
                relative_departure_coordinates=get_relative_coordinates_0(1),
                relative_arrival_coordinates=rc1,
                relative_position=rp)
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R1,
                room_arrival=R5,
                relative_departure_coordinates=get_relative_coordinates_0(2),
                relative_arrival_coordinates=rc1,
                relative_position=rp)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R1,
                room_arrival=R6,
                relative_departure_coordinates=get_relative_coordinates_0(3),
                relative_arrival_coordinates=rc1,
                relative_position=rp)
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R1,
                room_arrival=R7,
                relative_departure_coordinates=get_relative_coordinates_0(4),
                relative_arrival_coordinates=rc1,
                relative_position=rp)
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R1,
                room_arrival=R8,
                relative_departure_coordinates=get_relative_coordinates_0(5),
                relative_arrival_coordinates=rc1,
                relative_position=rp)
    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=R1,
                room_arrival=R9,
                relative_departure_coordinates=get_relative_coordinates_0(6),
                relative_arrival_coordinates=rc1,
                relative_position=rp)
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R1,
                room_arrival=R10,
                relative_departure_coordinates=get_relative_coordinates_0(7),
                relative_arrival_coordinates=rc1,
                relative_position=rp)
    
    D20 = Door(two_way=False,
                tree=T20,
                name='D20',
                room_departure=R3,
                room_arrival=R1,
                relative_departure_coordinates=rc1,
                relative_arrival_coordinates=get_relative_coordinates_0(0),
                relative_position=rp)
    D21 = Door(two_way=False,
                tree=T21,
                name='D21',
                room_departure=R4,
                room_arrival=R1,
                relative_departure_coordinates=rc1,
                relative_arrival_coordinates=get_relative_coordinates_0(1),
                relative_position=rp)
    D22 = Door(two_way=False,
                tree=T22,
                name='D22',
                room_departure=R5,
                room_arrival=R1,
                relative_departure_coordinates=rc1,
                relative_arrival_coordinates=get_relative_coordinates_0(2),
                relative_position=rp)
    D23 = Door(two_way=False,
                tree=T23,
                name='D23',
                room_departure=R6,
                room_arrival=R1,
                relative_departure_coordinates=rc1,
                relative_arrival_coordinates=get_relative_coordinates_0(3),
                relative_position=rp)
    D24 = Door(two_way=False,
                tree=T24,
                name='D24',
                room_departure=R7,
                room_arrival=R1,
                relative_departure_coordinates=rc1,
                relative_arrival_coordinates=get_relative_coordinates_0(4),
                relative_position=rp)
    D25 = Door(two_way=False,
                tree=T25,
                name='D25',
                room_departure=R8,
                room_arrival=R1,
                relative_departure_coordinates=rc1,
                relative_arrival_coordinates=get_relative_coordinates_0(5),
                relative_position=rp)
    D26 = Door(two_way=False,
                tree=T26,
                name='D26',
                room_departure=R9,
                room_arrival=R1,
                relative_departure_coordinates=rc1,
                relative_arrival_coordinates=get_relative_coordinates_0(6),
                relative_position=rp)
    D27 = Door(two_way=False,
                tree=T27,
                name='D27',
                room_departure=R10,
                room_arrival=R1,
                relative_departure_coordinates=rc1,
                relative_arrival_coordinates=get_relative_coordinates_0(7),
                relative_position=rp)
    D28 = Door(two_way=False,
                tree=T28,
                name='D28',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 1/2])
    
    hu = 0.15
    lcolor = Level_color(background_color=Color.color_hls(hu, li=0.7, sa=0.3),
                         room_color=Color.color_hls(hu, li=0.4, sa=0.4),
                         letters_color=Color.BLACK,
                         contour_color=Color.color_hls(hu=0.9, li=0.1, sa=1),
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.color_hls(hu=0.9, li=0.1, sa=1))

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28],
                 fastest_solution=None,
                 level_color=lcolor,
                 name='Quick sort',
                 keep_proportions=True,
                 door_window_size=360,
                 random=True)
    
    return level
    