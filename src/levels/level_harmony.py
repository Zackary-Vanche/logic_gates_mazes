from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def f(fast_solution_finding=False): 

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
    S24 = Switch(name='S24')
    S25 = Switch(name='S25')
    S26 = Switch(name='S26')
    S27 = Switch(name='S27')
    S28 = Switch(name='S28')
    S29 = Switch(name='S29')
    S30 = Switch(name='S30')
    S31 = Switch(name='S31')
    S32 = Switch(name='S32')
    S33 = Switch(name='S33')
    S34 = Switch(name='S34')
    S35 = Switch(name='S35')
    S36 = Switch(name='S36')

    # Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8,
    #          S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20]
    # Vlist = [V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11]

    V0 = Tree(tree_list=Tree.tree_list_XOR(2),
          name='V0',
          switches=[S3, S6])
    V1 = Tree(tree_list=Tree.tree_list_XOR(2),
          name='V1',
          switches=[S6, S7])
    V2 = Tree(tree_list=Tree.tree_list_XOR(2),
          name='V2',
          switches=[S0, S3])
    V3 = Tree(tree_list=Tree.tree_list_XOR(2),
          name='V3',
          switches=[S3, S4])
    V4 = Tree(tree_list=Tree.tree_list_XOR(2),
          name='V4',
          switches=[S4, S7])
    V5 = Tree(tree_list=Tree.tree_list_XOR(2),
          name='V5',
          switches=[S7, S8])
    V6 = Tree(tree_list=Tree.tree_list_XOR(2),
          name='V6',
          switches=[S0, S1])
    V7 = Tree(tree_list=Tree.tree_list_XOR(2),
          name='V7',
          switches=[S1, S4])
    V8 = Tree(tree_list=Tree.tree_list_XOR(2),
          name='V8',
          switches=[S4, S5])
    V9 = Tree(tree_list=Tree.tree_list_XOR(2),
          name='V9',
          switches=[S5, S8])
    V10 = Tree(tree_list=Tree.tree_list_XOR(2),
          name='V10',
          switches=[S1, S2])
    V11 = Tree(tree_list=Tree.tree_list_XOR(2),
          name='V11',
          switches=[S2, S5])
    V12 = Tree(tree_list=['SUPOREQU', Tree.tree_list_SUM(24), [None]],
          name='V12',
          switches=[V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11,
                    S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20,
                    15])
    
    T0 = Tree(tree_list=['INF', Tree.tree_list_SUM(9), [None]],
                name='T0',
                switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, 5])
    T1 = Tree(tree_list=['AND',
                         ['EQU', Tree.tree_list_SUM(2), [None]],
                         ['IN', Tree.tree_list_SUM(3), [None], [None]],
                         ['IN', Tree.tree_list_SUM(3), [None], [None]],
                         ['IN', Tree.tree_list_SUM(3), [None], [None]],
                         ['IN', Tree.tree_list_SUM(4), [None], [None]],
                         ['IN', Tree.tree_list_SUM(3), [None], [None]],
                         ['IN', Tree.tree_list_SUM(2), [None], [None]],
                         ['IN', Tree.tree_list_SUM(4), [None], [None]],
                         ['IN', Tree.tree_list_SUM(4), [None], [None]],
                         ['EQU', Tree.tree_list_SUM(2), [None]],
                         ['IN', Tree.tree_list_SUM(3), [None], [None]],
                         ['IN', Tree.tree_list_SUM(4), [None], [None]],
                         ['IN', Tree.tree_list_SUM(3), [None], [None]],
                         ['IN', Tree.tree_list_SUM(3), [None], [None]],
                         ['IN', Tree.tree_list_SUM(3), [None], [None]],
                         ['IN', Tree.tree_list_SUM(2), [None], [None]],
                         [None]],
                name='T1',
                switches=[S9, S10, 1,
                          S9, S11, V0, 0, 2,
                          S10, V1, S12, 0, 2,
                          S11, S13, V2, 0, 2,
                          V0, V1, V3, V4, 0, 2,
                          S12, V5, S14, 0, 2,
                          S13, S15, 0, 2,
                          V2, V3, V6, V7, 0, 2,
                          V4, V5, V8, V9, 0, 2,
                          S14, S16, 1,
                          S15, V6, S17, 0, 2,
                          V7, V8, V10, V11, 0, 2,
                          V9, S16, S18, 0, 2,
                          S17, V10, S19, 0, 2,
                          V11, S18, S20, 0, 2,
                          S19, S20, 0, 2,
                          V12],
                cut_expression_depth_1=True)
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[S9])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[S10])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[S11])
    T5 = Tree(tree_list=[None],
                name='T5',
                switches=[V0])
    T6 = Tree(tree_list=[None],
                name='T6',
                switches=[V1])
    T7 = Tree(tree_list=[None],
                name='T7',
                switches=[S12])
    T8 = Tree(tree_list=[None],
                name='T8',
                switches=[S13])
    T9 = Tree(tree_list=[None],
                name='T9',
                switches=[V2])
    T10 = Tree(tree_list=[None],
                name='T10',
                switches=[V3])
    T11 = Tree(tree_list=[None],
                name='T11',
                switches=[V4])
    T12 = Tree(tree_list=[None],
                name='T12',
                switches=[V5])
    T13 = Tree(tree_list=[None],
                name='T13',
                switches=[S14])
    T14 = Tree(tree_list=[None],
                name='T14',
                switches=[S15])
    T15 = Tree(tree_list=[None],
                name='T15',
                switches=[V6])
    T16 = Tree(tree_list=[None],
                name='T16',
                switches=[V7])
    T17 = Tree(tree_list=[None],
                name='T17',
                switches=[V8])
    T18 = Tree(tree_list=[None],
                name='T18',
                switches=[V9])
    T19 = Tree(tree_list=[None],
                name='T19',
                switches=[S16])
    T20 = Tree(tree_list=[None],
                name='T20',
                switches=[S17])
    T21 = Tree(tree_list=[None],
                name='T21',
                switches=[V10])
    T22 = Tree(tree_list=[None],
                name='T22',
                switches=[V11])
    T23 = Tree(tree_list=[None],
                name='T23',
                switches=[S18])
    T24 = Tree(tree_list=[None],
                name='T24',
                switches=[S19])
    T25 = Tree(tree_list=[None],
                name='T25',
                switches=[S20])
    T26 = Tree(tree_list=Tree.tree_list_AND(16),
                name='T26',
                switches=[S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, S34, S35, S36])

    dx = 1
    dy = 1.2
    ex = 0.8
    ey = 1
    
    epsilonx = 0.325
    epsilony = 0.325
    
    a = 0.15
    b = 2*a
    c = 3*a

    R0 = Room(name='R0',
                position=[-3*dx, 0*dy, 2*dx+ex+0.2, 2*dy+ey],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8])
    R1 = Room(name='R1',
                position=[-3*dx, 4*dy, 1*dx+ex+0.2, 3*dy],
                switches_list=[S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20])

    R2 = Room(name='R2',
                position=[0*dx+epsilonx, 6*dy+epsilony, ex, ey],
                switches_list=[S21])
    R3 = Room(name='R3',
                position=[0*dx+a, 4*dy, ex, ey],
                switches_list=[S22])
    R4 = Room(name='R4',
                position=[2*dx, 6*dy, ex, ey],
                switches_list=[S23])
    R5 = Room(name='R5',
                position=[0*dx+epsilonx+b, 2*dy+epsilony, ex, ey],
                switches_list=[S24])
    R6 = Room(name='R6',
                position=[2*dx+epsilonx+2*a, 4*dy+epsilony, ex, ey],
                switches_list=[S25])
    R7 = Room(name='R7',
                position=[4*dx+epsilonx, 6*dy+epsilony, ex, ey],
                switches_list=[S26])
    R8 = Room(name='R8',
                position=[0*dx+c, 0*dy, ex, ey],
                switches_list=[S27])
    R9 = Room(name='R9',
                position=[2*dx+2*b, 2*dy, ex, ey],
                switches_list=[S28])
    R10 = Room(name='R10',
                position=[4*dx+3*a, 4*dy, ex, ey],
                switches_list=[S29])
    R11 = Room(name='R11',
                position=[6*dx, 6*dy, ex, ey],
                switches_list=[S30])
    R12 = Room(name='R12',
                position=[2*dx+epsilonx+2*c, 0*dy+epsilony, ex, ey],
                switches_list=[S31])
    R13 = Room(name='R13',
                position=[4*dx+epsilonx+3*b, 2*dy+epsilony, ex, ey],
                switches_list=[S32])
    R14 = Room(name='R14',
                position=[6*dx+epsilonx+4*a, 4*dy+epsilony, ex, ey],
                switches_list=[S33])
    R15 = Room(name='R15',
                position=[4*dx+3*c, 0*dy, ex, ey],
                switches_list=[S34])
    R16 = Room(name='R16',
                position=[6*dx+4*b, 2*dy, ex, ey],
                switches_list=[S35])
    R17 = Room(name='R17',
                position=[6*dx+epsilonx+4*c, 0*dy+epsilony, ex, ey],
                switches_list=[S36])

    RE = Room(name='RE',
              position=[8*dx, 6*dy, ex, ey],
              is_exit=True)
    
    if fast_solution_finding:
        for room in [R2, R3, R4, R5,
                     R6, R7, R8, R9,
                     R10, R11, R12, R13,
                     R14, R15, R16, R17]:
            room.possible_switches_values = [[1]]

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[1/2, 0])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=[1, (2*dy+ey/2)/(3*dy+ey)],
                relative_arrival_coordinates=[0, 1/2])
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R4)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R3,
                room_arrival=R5)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R6)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R4,
                room_arrival=R6)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R4,
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
                room_departure=R6,
                room_arrival=R9)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R6,
                room_arrival=R10)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R7,
                room_arrival=R10)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R7,
                room_arrival=R11)
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R8,
                room_arrival=R12)
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R9,
                room_arrival=R12)
    D16 = Door(two_way=True,
                tree=T16,
                name='D16',
                room_departure=R9,
                room_arrival=R13)
    D17 = Door(two_way=True,
                tree=T17,
                name='D17',
                room_departure=R10,
                room_arrival=R13)
    D18 = Door(two_way=True,
                tree=T18,
                name='D18',
                room_departure=R10,
                room_arrival=R14)
    D19 = Door(two_way=True,
                tree=T19,
                name='D19',
                room_departure=R11,
                room_arrival=R14)
    D20 = Door(two_way=True,
                tree=T20,
                name='D20',
                room_departure=R12,
                room_arrival=R15)
    D21 = Door(two_way=True,
                tree=T21,
                name='D21',
                room_departure=R13,
                room_arrival=R15)
    D22 = Door(two_way=True,
                tree=T22,
                name='D22',
                room_departure=R13,
                room_arrival=R16)
    D23 = Door(two_way=True,
                tree=T23,
                name='D23',
                room_departure=R14,
                room_arrival=R16)
    D24 = Door(two_way=True,
                tree=T24,
                name='D24',
                room_departure=R15,
                room_arrival=R17)
    D25 = Door(two_way=True,
                tree=T25,
                name='D25',
                room_departure=R16,
                room_arrival=R17)
    D26 = Door(two_way=False,
                tree=T26,
                name='D26',
                room_departure=R11,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1,
                             R2, R3, R4, R5,
                             R6, R7, R8, R9,
                             R10, R11, R12, R13,
                             R14, R15, R16, R17,
                             RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26],
                 fastest_solution='S1 S6 S8 D0 S10 S11 S13 S14 S15 S18 S19 S20 D1 S21 D3 S23 D6 S25 D5 S22 D4 S24 D8 S27 D14 S31 D15 S28 D16 S32 D21 S34 D24 S36 D25 S35 D23 S33 D18 S29 D12 S26 D13 S30 D26',
                 level_color=get_color(),
                 name='Harmony',
                 keep_proportions=True,
                 door_window_size=350)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.7)
    lcolor.surrounding_color = Color.WHITE
    lcolor.contour_color = Color.WHITE
    lcolor.background_color = Color.color_hls(hu=0, li=0.1, sa=0.25)
    return lcolor