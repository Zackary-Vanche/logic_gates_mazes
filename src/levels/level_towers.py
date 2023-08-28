from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_towers(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')

    S8 = Switch(name='S8', value=1)
    S9 = Switch(name='S9', value=1)

    S10 = Switch(name='S10')
    S11 = Switch(name='S11', value=1)

    S12 = Switch(name='S12', value=1)
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

    S24 = Switch(name='S24')
    S25 = Switch(name='S25')
    
    a0 = 0
    a1 = 1
    a2 = 2
    a3 = 3
    a4 = 4
    a5 = 5
    a6 = 6
    a7 = 7
    a8 = 8

    Slist = [S0, S1, S2, S3,
             S4, S5, S6, S7,
             S8, S9,
             S10, S11,
             S12, S13,
             S14, S15,
             S16, S17,
             S18, S19,
             S20, S21,
             S22, S23,
             S24, S25]
    
    tree_list_V2 = ['AND', ['IN'] + [[None]]*3, [None]]
    tree_list_DIFF2 = ['DIFF', [None], [None]]
    tree_list_EQU2 = ['EQU', [None], [None]]

    V0 = Tree(tree_list=Tree.tree_list_BIN(4),
              name='V0',
              switches=[S0, S1, S2, S3])
    V1 = Tree(tree_list=Tree.tree_list_BIN(4),
              name='V1',
              switches=[S4, S5, S6, S7])
    V2 = Tree(tree_list=['INF', [None], [None]],
              name='V2',
              switches=[V0, V1])

    Va0 = Tree(tree_list=tree_list_V2,
               name='V3',
               switches=[a0, V0, V1, V2])
    Va1 = Tree(tree_list=tree_list_V2,
               name='V4',
               switches=[a1, V0, V1, V2])
    Va2 = Tree(tree_list=tree_list_V2,
               name='V5',
               switches=[a2, V0, V1, V2])
    Va3 = Tree(tree_list=tree_list_V2,
               name='V6',
               switches=[a3, V0, V1, V2])
    Va4 = Tree(tree_list=tree_list_V2,
               name='V7',
               switches=[a4, V0, V1, V2])
    Va5 = Tree(tree_list=tree_list_V2,
               name='V8',
               switches=[a5, V0, V1, V2])
    Va6 = Tree(tree_list=tree_list_V2,
               name='V9',
               switches=[a6, V0, V1, V2])
    Va7 = Tree(tree_list=tree_list_V2,
               name='V10',
               switches=[a7, V0, V1, V2])
    Va8 = Tree(tree_list=tree_list_V2,
               name='V11',
               switches=[a8, V0, V1, V2])

    VR0 = Tree(tree_list=Tree.tree_list_BIN(2),
               name='V12',
               switches=[S8, S9])
    VR1 = Tree(tree_list=Tree.tree_list_BIN(2),
               name='V13',
               switches=[S10, S11])
    VR2 = Tree(tree_list=Tree.tree_list_BIN(2),
               name='V14',
               switches=[S12, S13])
    VR3 = Tree(tree_list=Tree.tree_list_BIN(2),
               name='V15',
               switches=[S14, S15])
    VR4 = Tree(tree_list=Tree.tree_list_BIN(2),
               name='V16',
               switches=[S16, S17])
    VR5 = Tree(tree_list=Tree.tree_list_BIN(2),
               name='V17',
               switches=[S18, S19])
    VR6 = Tree(tree_list=Tree.tree_list_BIN(2),
               name='V18',
               switches=[S20, S21])
    VR7 = Tree(tree_list=Tree.tree_list_BIN(2),
               name='V19',
               switches=[S22, S23])
    VR8 = Tree(tree_list=Tree.tree_list_BIN(2),
               name='V20',
               switches=[S24, S25])

    VEQUSET = Tree(tree_list=['EQUSET'] + [[None]]*18,
                   name='V21',
                   switches=[0, 0, 0, 0, 0, 0, 1, 2, 3,
                             VR0, VR1, VR2, VR3, VR4, VR5, VR6, VR7, VR8],
                   cut_expression_depth_1=True)
    VOR0 = Tree(tree_list=['OR'] + [['AND', [None], tree_list_EQU2]]*9,
                name='V22',
                switches=[Va0, VR0, 0,
                          Va1, VR1, 0,
                          Va2, VR2, 0,
                          Va3, VR3, 0,
                          Va4, VR4, 0,
                          Va5, VR5, 0,
                          Va6, VR6, 0,
                          Va7, VR7, 0,
                          Va8, VR8, 0],
               cut_expression_depth_1=True)
    tree_list_n0 = ['AND',
                    [None],
                    tree_list_EQU2,
                    tree_list_EQU2,
                    tree_list_EQU2]
    tree_list_n1 = ['AND',
                    [None],
                    tree_list_DIFF2,
                    tree_list_EQU2,
                    tree_list_EQU2]
    tree_list_n2 = ['AND',
                    [None],
                    tree_list_DIFF2,
                    tree_list_DIFF2,
                    tree_list_EQU2]
    VORNOT0 = Tree(tree_list=['OR',
                              tree_list_n0,
                              tree_list_n1,
                              tree_list_n2,
                              tree_list_n0,
                              tree_list_n1,
                              tree_list_n2,
                              tree_list_n0,
                              tree_list_n1,
                              tree_list_n2,],
                   name='V23',
                   switches=[Va0, VR0, 0, VR1, 0, VR2, 0,
                             Va1, VR0, 0, VR1, 0, VR2, 0,
                             Va2, VR0, 0, VR1, 0, VR2, 0,
                             Va3, VR3, 0, VR4, 0, VR5, 0,
                             Va4, VR3, 0, VR4, 0, VR5, 0,
                             Va5, VR3, 0, VR4, 0, VR5, 0,
                             Va6, VR6, 0, VR7, 0, VR8, 0,
                             Va7, VR6, 0, VR7, 0, VR8, 0,
                             Va8, VR6, 0, VR7, 0, VR8, 0,],
                   cut_expression_depth_1=True)
    VSUP = Tree(tree_list=['AND'] + [['SUPOREQU', [None], [None], [None]]]*3,
                name='V24',
                switches=[VR0, VR1, VR2,
                          VR3, VR4, VR5,
                          VR6, VR7, VR8,])
    V25 = Tree(tree_list=Tree.tree_list_AND(4),
               name='V25',
               switches=[VEQUSET, VOR0, VORNOT0, VSUP])

    # Trees
    
    tree_list_AND_2 = Tree.tree_list_AND(2)

    T0 = Tree(tree_list=tree_list_AND_2,
              name='T0',
              switches=[Va0, V25])
    T1 = Tree(tree_list=tree_list_AND_2,
              name='T1',
              switches=[Va1, V25])
    T2 = Tree(tree_list=tree_list_AND_2,
              name='T2',
              switches=[Va2, V25])
    T3 = Tree(tree_list=tree_list_AND_2,
              name='T3',
              switches=[Va3, V25])
    T4 = Tree(tree_list=tree_list_AND_2,
              name='T4',
              switches=[Va4, V25])
    T5 = Tree(tree_list=tree_list_AND_2,
              name='T5',
              switches=[Va5, V25])
    T6 = Tree(tree_list=tree_list_AND_2,
              name='T6',
              switches=[Va6, V25])
    T7 = Tree(tree_list=tree_list_AND_2,
              name='T7',
              switches=[Va7, V25])
    T8 = Tree(tree_list=tree_list_AND_2,
              name='T8',
              switches=[Va8, V25])

    T9 = Tree(tree_list=[None],
                name='T9',
                switches=[Va0])
    T10 = Tree(tree_list=[None],
                name='T10',
                switches=[Va1])
    T11 = Tree(tree_list=[None],
                name='T11',
                switches=[Va2])
    T12 = Tree(tree_list=[None],
                name='T12',
                switches=[Va3])
    T13 = Tree(tree_list=[None],
                name='T13',
                switches=[Va4])
    T14 = Tree(tree_list=[None],
                name='T14',
                switches=[Va5])
    T15 = Tree(tree_list=[None],
                name='T15',
                switches=[Va6])
    T16 = Tree(tree_list=[None],
                name='T16',
                switches=[Va7])
    T17 = Tree(tree_list=[None],
                name='T17',
                switches=[Va8])
    T18 = Tree(tree_list=["AND"] + [tree_list_EQU2]*11,
               name='T18',
               switches=[0, VR0,
                         0, VR1,
                         0, VR2,
                         0, VR3,
                         0, VR4,
                         0, VR5,
                         3, VR6,
                         2, VR7,
                         1, VR8,
                         V0, 0,
                         V1, 1])

    d = 1.5
    e = 0.75
    n = 2
    
    def pos(x):
        x = x-1
        return [x*d, -0.15*x*(x-8), e, n]

    R0 = Room(name='R0',
              position=[1*d, pos(5)[1]+n+1.25, 6*d+e, 0.75*e],
              switches_list=[S0, S1, S2, S3,
                             S4, S5, S6, S7])
    R1 = Room(name='R1',
                position=pos(1),
                switches_list=[S8, S9,])
    R2 = Room(name='R2',
                position=pos(2),
                switches_list=[S10, S11,])
    R3 = Room(name='R3',
                position=pos(3),
                switches_list=[S12, S13,])
    R4 = Room(name='R4',
                position=pos(4),
                switches_list=[S14, S15,])
    R5 = Room(name='R5',
                position=pos(5),
                switches_list=[S16, S17,])
    R6 = Room(name='R6',
                position=pos(6),
                switches_list=[S18, S19,])
    R7 = Room(name='R7',
                position=pos(7),
                switches_list=[S20, S21,])
    R8 = Room(name='R8',
                position=pos(8),
                switches_list=[S22, S23,])
    R9 = Room(name='R9',
                position=pos(9),
                switches_list=[S24, S25])
    R10 = Room(name='R10',
                position=[4*d, pos(1)[1]-2*e, e, e],
                switches_list=[])
    RE = Room(name='RE',
              position=[4*d, pos(1)[1]-4.5*e, e, e],
              is_exit=True)
    
    def rd_r0(k):
        a = 0.5
        return [(k+a)/(8+2*a), 0]

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=rd_r0(0),
                relative_arrival_coordinates=[1/2, 1])
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R2,
                relative_departure_coordinates=rd_r0(1),
                relative_arrival_coordinates=[1/2, 1])
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=R3,
                relative_departure_coordinates=rd_r0(2),
                relative_arrival_coordinates=[1/2, 1])
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R0,
                room_arrival=R4,
                relative_departure_coordinates=rd_r0(3),
                relative_arrival_coordinates=[1/2, 1])
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R0,
                room_arrival=R5,
                relative_departure_coordinates=rd_r0(4),
                relative_arrival_coordinates=[1/2, 1])
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R0,
                room_arrival=R6,
                relative_departure_coordinates=rd_r0(5),
                relative_arrival_coordinates=[1/2, 1])
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=R7,
                relative_departure_coordinates=rd_r0(6),
                relative_arrival_coordinates=[1/2, 1])
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R0,
                room_arrival=R8,
                relative_departure_coordinates=rd_r0(7),
                relative_arrival_coordinates=[1/2, 1])
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R0,
                room_arrival=R9,
                relative_departure_coordinates=rd_r0(8),
                relative_arrival_coordinates=[1/2, 1])
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R10,
                room_arrival=R1,
                relative_arrival_coordinates=[1/2, 1/4])
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R10,
                room_arrival=R2,
                relative_arrival_coordinates=[1/2, 1/4])
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R10,
                room_arrival=R3,
                relative_arrival_coordinates=[1/2, 1/4])
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R10,
                room_arrival=R4,
                relative_arrival_coordinates=[1/2, 1/4])
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R10,
                room_arrival=R5,
                relative_arrival_coordinates=[1/2, 1/4])
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R10,
                room_arrival=R6,
                relative_arrival_coordinates=[1/2, 1/4])
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R10,
                room_arrival=R7,
                relative_arrival_coordinates=[1/2, 1/4])
    D16 = Door(two_way=True,
                tree=T16,
                name='D16',
                room_departure=R10,
                room_arrival=R8,
                relative_arrival_coordinates=[1/2, 1/4])
    D17 = Door(two_way=True,
                tree=T17,
                name='D17',
                room_departure=R10,
                room_arrival=R9,
                relative_arrival_coordinates=[1/2, 1/4])
    D18 = Door(two_way=True,
                tree=T18,
                name='D18',
                room_departure=R10,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18],
                 fastest_solution="""
S1 S5 S6 D2 S12 D11 D15 S20 D6
S0 S1 S4 S6 D1 S11 D10 D12 S15 D3
S0 S2 S4 S6 D4 S16 D13 D15 S20 D6
S2 D0 S8 S9 D9 D15 S20 S21 D6
S5 D0 S8 D9 D13 S16 D4
S0 S1 S4 S5 D3 S15 D12 D16 S23 D7
S0 S1 S4 S5 S6 S7 D0 S8 D9 D17 S24 D8
S4 S7 D0 D9 D18""".replace('\n', ' '),
                 level_color=Levels_colors_list.FROM_HUE(hu=0.06, sa=0.35, li=0.5),
                 name='Towers',
                 keep_proportions=True,
                 door_window_size=335)
    
    return level