from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

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
    # S21 = Switch(name='S21')
    
    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4]
    Slist_2 = [S5, S6]
    Slist_3 = [S7, S8, S9, S10]
    Slist_4 = [S11, S12, S13, S14]
    SlistE = [S15, S16, S17, S18, S19, S20]
    
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
    
    tree_list_EQU = ['EQU', [None], [None]]
    
    tree_list_IN = ['IN'] + [[None]]*4

    T0 = Tree(tree_list=['OR'] + [['AND',
                                   tree_list_EQU,
                                   tree_list_IN]]*4,
                name='T0',
                switches=[V2, 0, V0, 0, 1, 2,
                          V2, 1, V0, 0, 3, 4,
                          V2, 2, V0, 1, 3, 5,
                          V2, 3, V0, 2, 4, 5],
                cut_expression_depth_1=True)
    T1 = Tree(tree_list=['OR'] + [['AND',
                                   tree_list_EQU,
                                   ['EQUSET',
                                    [None],
                                    [None],
                                    [None],
                                    [None]]]]*6,
                name='T1',
                switches=[V0, 0, V1, V2, 0, 1, 
                          V0, 1, V1, V2, 0, 2,
                          V0, 2, V1, V2, 0, 3,
                          V0, 3, V1, V2, 1, 2,
                          V0, 4, V1, V2, 1, 3,
                          V0, 5, V1, V2, 2, 3,],
                cut_expression_depth_1=True)
    T2 = Tree(tree_list=['EQU', [None], [None]],
                name='T2',
                switches=[V1, V2])
    T3 = Tree(tree_list=['EQU',
                         [None],
                         ['SUM', [None], [None]]],
                name='T3',
                switches=[V3, V4, 1])
    T4 = Tree(tree_list=['EQU'] + [[None]]*2,
                name='T4',
                switches=[V3, V4])
    T5 = Tree(tree_list=['AND'] + [['NAND',
                                    Tree.tree_list_NOT,
                                    ['EQU', [None], [None]],]]*6,
                name='T5',
                switches=[S15, 0, V0,
                          S16, 1, V0,
                          S17, 2, V0,
                          S18, 3, V0,
                          S19, 4, V0,
                          S20, 5, V0],
                cut_expression=True)
    T6 = Tree(tree_list=tree_list_EQU,
                name='T6',
                switches=[V0, 0])
    T7 = Tree(tree_list=tree_list_EQU,
                name='T7',
                switches=[V0, 1])
    T8 = Tree(tree_list=tree_list_EQU,
                name='T8',
                switches=[V0, 2])
    T9 = Tree(tree_list=tree_list_EQU,
                name='T9',
                switches=[V0, 3])
    T10 = Tree(tree_list=tree_list_EQU,
                name='T10',
                switches=[V0, 4])
    T11 = Tree(tree_list=tree_list_EQU,
                name='T11',
                switches=[V0, 5])
    T12 = Tree(tree_list=['AND',
                          Tree.tree_list_from_str('F'*5+'T'*6),
                          ['INF', [None], [None]]],
                name='T12',
                switches=Slist_0+Slist_1+SlistE+[V3, 16],
                cut_expression=True)
    
    ex = 1
    ey = 0.75
    dx = 1
    dy = 0.75

    R0 = Room(name='R0',
                position=[2*dx, 0*dy, 3*ex, ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[1*dx, 2*dy, 2*ex, ey],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[4*dx, 2*dy, 2*ex, ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[4*dx, 4*dy, 3*ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[0*dx, 4*dy, 3*ex, ey],
                switches_list=Slist_4)
    R5 = Room(name='R5',
                position=[3*dx, 6*dy, ex, ey/2],
                switches_list=[])
    R6 = Room(name='R6',
                position=[-0.25*dx, 5.5*dy, ex, ey],
                switches_list=[S15])
    R7 = Room(name='R7',
                position=[0*dx, 7*dy, ex, ey],
                switches_list=[S16])
    R8 = Room(name='R8',
                position=[1.5*dx, 7.5*dy, ex, ey],
                switches_list=[S17])
    R9 = Room(name='R9',
                position=[4.5*dx, 7.5*dy, ex, ey],
                switches_list=[S18])
    R10 = Room(name='R10',
                position=[6*dx, 7*dy, ex, ey],
                switches_list=[S19])
    R11 = Room(name='R11',
                position=[6.25*dx, 5.5*dy, ex, ey],
                switches_list=[S20])
    # R12 = Room(name='R12',
    #             position=[7, 6, ex, ey],
    #             switches_list=[])
    RE = Room(name='RE',
              position=[3*dx, 7.75*dy, ex, ey],
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
                room_arrival=R5,
                relative_position=0.525)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R5,
                room_arrival=R0)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R5,
                room_arrival=R6)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R5,
                room_arrival=R7)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R5,
                room_arrival=R8)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R5,
                room_arrival=R9)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R5,
                room_arrival=R10)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R5,
                room_arrival=R11)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R5,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12],
                 fastest_solution='S0 D0 S4 D1 S6 D2 S7 D3 S11 D4 D7 S16 D7 D5 S1 D0 S3 S4 D1 S5 S6 D2 S7 S8 D3 S11 S12 D4 D9 S18 D9 D5 S0 S1 S2 D0 S4 D1 S6 D2 S7 D3 S11 D4 D10 S19 D10 D5 S0 D0 S3 D1 S5 D2 S7 S8 S9 D3 S11 S12 S13 D4 D11 S20 D11 D5 D0 S3 D1 S5 D2 S7 D3 S11 D4 D5 S0 S1 S2 D0 S3 S4 D1 S5 S6 D2 S7 S8 D3 S11 S12 D4 D8 S17 D8 D5 S1 D0 S3 D1 S5 D2 S7 D3 S11 D4 D6 S15 D6 D5 D0 S3 D1 S5 D2 S7 S8 S9 S10 D3 S11 S12 S13 S14 D4 D12',
                 level_color=get_color(),
                 name='Chinese postman problem',
                 keep_proportions=True,
                 door_window_size=400)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.6, sa=0.5, li=0.5)
    return lcolor