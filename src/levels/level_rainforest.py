from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def level_rainforest(fast_solution_finding=False): 

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

    Slist0 = [S0, S1,
              S1, S2,
              S2, S3]
    
    V0 = Tree(tree_list=['INF', Tree.tree_list_BIN(4), [None]],
              name='V0',
              switches=[S0, S1, S2, S3, 8])
    V1 = Tree(tree_list=['SUPOREQU', Tree.tree_list_BIN(4), [None]],
              name='V1',
              switches=[S0, S1, S2, S3, 8])
    

    T0 = Tree(tree_list=['AND',
                         Tree.tree_list_XOR(2),
                         Tree.tree_list_XOR(2),
                         Tree.tree_list_XOR(2)],
                name='T0',
                switches=Slist0)
    T1 = Tree(tree_list=['AND',
                         Tree.tree_list_XNOR(2),
                         Tree.tree_list_XOR(2),
                         Tree.tree_list_XOR(2)],
                name='T1',
                switches=Slist0)
    T2 = Tree(tree_list=['AND',
                         Tree.tree_list_XOR(2),
                         Tree.tree_list_XNOR(2),
                         Tree.tree_list_XOR(2)],
                name='T2',
                switches=Slist0)
    T3 = Tree(tree_list=['AND',
                         Tree.tree_list_XNOR(2),
                         Tree.tree_list_XNOR(2),
                         Tree.tree_list_XOR(2)],
                name='T3',
                switches=Slist0)
    T4 = Tree(tree_list=['AND',
                         Tree.tree_list_XOR(2),
                         Tree.tree_list_XOR(2),
                         Tree.tree_list_XNOR(2)],
                name='T4',
                switches=Slist0)
    T5 = Tree(tree_list=['AND',
                         Tree.tree_list_XNOR(2),
                         Tree.tree_list_XOR(2),
                         Tree.tree_list_XNOR(2)],
                name='T5',
                switches=Slist0)
    T6 = Tree(tree_list=['AND',
                         Tree.tree_list_XOR(2),
                         Tree.tree_list_XNOR(2),
                         Tree.tree_list_XNOR(2)],
                name='T6',
                switches=Slist0)
    T7 = Tree(tree_list=['AND',
                         Tree.tree_list_XNOR(2),
                         Tree.tree_list_XNOR(2),
                         Tree.tree_list_XNOR(2)],
                name='T7',
                switches=Slist0)
    T8 = Tree(tree_list=[None],
                name='T8',
                switches=[V0])
    T9 = Tree(tree_list=[None],
                name='T9',
                switches=[V1])
    T10 = Tree(tree_list=[None],
                name='T10',
                switches=[V0])
    T11 = Tree(tree_list=[None],
                name='T11',
                switches=[V1])
    T12 = Tree(tree_list=[None],
                name='T12',
                switches=[V0])
    T13 = Tree(tree_list=[None],
                name='T13',
                switches=[V1])
    T14 = Tree(tree_list=[None],
                name='T14',
                switches=[V0])
    T15 = Tree(tree_list=[None],
                name='T15',
                switches=[V1])
    T16 = Tree(tree_list=[None],
                name='T16',
                switches=[V0])
    T17 = Tree(tree_list=[None],
                name='T17',
                switches=[V1])
    T18 = Tree(tree_list=[None],
                name='T18',
                switches=[V0])
    T19 = Tree(tree_list=[None],
                name='T19',
                switches=[V1])
    T20 = Tree(tree_list=[None],
                name='T20',
                switches=[V0])
    T21 = Tree(tree_list=[None],
                name='T21',
                switches=[V1])
    T22 = Tree(tree_list=[None],
                name='T22',
                switches=[V0])
    T23 = Tree(tree_list=[None],
                name='T23',
                switches=[V1])
    T24 = Tree(tree_list=Tree.tree_list_AND(16),
                name='T24',
                switches=[S4, S5, S6, S7,
                          S8, S9, S10, S11,
                          S12, S13, S14, S15,
                          S16, S17, S18, S19])

    dx = 1
    dy = 1
    ex = 1.2
    ey = 0.95
    
    if fast_solution_finding:
        room_of_possible_switches = Room(name='R',
                                         position=[0, 0, 1, 1],
                                         switches_list=[Switch(value=1)])
    else:
        room_of_possible_switches = None

    R0 = Room(name='R0',
                position=[4*dx, 5*dy, 2*dx+ex, ey],
                switches_list=[S0, S1, S2, S3])
    R1 = Room(name='R1',
                position=[4*dx, 3*dy, ex, ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[2*dx, 4*dy, ex, ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[2*dx, 6*dy, ex, ey],
                switches_list=[])
    R4 = Room(name='R4',
                position=[4*dx, 7*dy, ex, ey],
                switches_list=[])
    R5 = Room(name='R5',
                position=[6*dx, 7*dy, ex, ey],
                switches_list=[])
    R6 = Room(name='R6',
                position=[8*dx, 6*dy, ex, ey],
                switches_list=[])
    R7 = Room(name='R7',
                position=[8*dx, 4*dy, ex, ey],
                switches_list=[])
    R8 = Room(name='R8',
                position=[6*dx, 3*dy, ex, ey],
                switches_list=[])
    R9 = Room(name='R9',
                position=[3*dx, 0*dy, ex, ey],
                switches_list=[S4],
                room_of_possible_switches=room_of_possible_switches)
    R10 = Room(name='R10',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S5],
                room_of_possible_switches=room_of_possible_switches)
    R11 = Room(name='R11',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S6],
                room_of_possible_switches=room_of_possible_switches)
    R12 = Room(name='R12',
                position=[0*dx, 3*dy, ex, ey],
                switches_list=[S7],
                room_of_possible_switches=room_of_possible_switches)
    R13 = Room(name='R13',
                position=[0*dx, 7*dy, ex, ey],
                switches_list=[S8],
                room_of_possible_switches=room_of_possible_switches)
    R14 = Room(name='R14',
                position=[1*dx, 8*dy, ex, ey],
                switches_list=[S9],
                room_of_possible_switches=room_of_possible_switches)
    R15 = Room(name='R15',
                position=[2*dx, 9*dy, ex, ey],
                switches_list=[S10],
                room_of_possible_switches=room_of_possible_switches)
    R16 = Room(name='R16',
                position=[3*dx, 10*dy, ex, ey],
                switches_list=[S11],
                room_of_possible_switches=room_of_possible_switches)
    R17 = Room(name='R17',
                position=[7*dx, 10*dy, ex, ey],
                switches_list=[S12],
                room_of_possible_switches=room_of_possible_switches)
    R18 = Room(name='R18',
                position=[8*dx, 9*dy, ex, ey],
                switches_list=[S13],
                room_of_possible_switches=room_of_possible_switches)
    R19 = Room(name='R19',
                position=[9*dx, 8*dy, ex, ey],
                switches_list=[S14],
                room_of_possible_switches=room_of_possible_switches)
    R20 = Room(name='R20',
                position=[10*dx, 7*dy, ex, ey],
                switches_list=[S15],
                room_of_possible_switches=room_of_possible_switches)
    R21 = Room(name='R21',
                position=[10*dx, 3*dy, ex, ey],
                switches_list=[S16],
                room_of_possible_switches=room_of_possible_switches)
    R22 = Room(name='R22',
                position=[9*dx, 2*dy, ex, ey],
                switches_list=[S17],
                room_of_possible_switches=room_of_possible_switches)
    R23 = Room(name='R23',
                position=[8*dx, 1*dy, ex, ey],
                switches_list=[S18],
                room_of_possible_switches=room_of_possible_switches)
    R24 = Room(name='R24',
                position=[7*dx, 0*dy, ex, ey],
                switches_list=[S19],
                room_of_possible_switches=room_of_possible_switches)
    RE = Room(name='RE',
              position=[5*dx, 1*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R2,
                relative_departure_coordinates=[0.5/3, 1/2])
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=R3,
                relative_departure_coordinates=[0.5/3, 1/2])
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R0,
                room_arrival=R4)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R0,
                room_arrival=R5)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R0,
                room_arrival=R6,
                relative_departure_coordinates=[2.5/3, 1/2])
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=R7,
                relative_departure_coordinates=[2.5/3, 1/2])
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R0,
                room_arrival=R8)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R1,
                room_arrival=R9)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R1,
                room_arrival=R10)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R2,
                room_arrival=R11)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R2,
                room_arrival=R12)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R3,
                room_arrival=R13)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R3,
                room_arrival=R14)
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R4,
                room_arrival=R15)
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R4,
                room_arrival=R16)
    D16 = Door(two_way=True,
                tree=T16,
                name='D16',
                room_departure=R5,
                room_arrival=R17)
    D17 = Door(two_way=True,
                tree=T17,
                name='D17',
                room_departure=R5,
                room_arrival=R18)
    D18 = Door(two_way=True,
                tree=T18,
                name='D18',
                room_departure=R6,
                room_arrival=R19)
    D19 = Door(two_way=True,
                tree=T19,
                name='D19',
                room_departure=R6,
                room_arrival=R20)
    D20 = Door(two_way=True,
                tree=T20,
                name='D20',
                room_departure=R7,
                room_arrival=R21)
    D21 = Door(two_way=True,
                tree=T21,
                name='D21',
                room_departure=R7,
                room_arrival=R22)
    D22 = Door(two_way=True,
                tree=T22,
                name='D22',
                room_departure=R8,
                room_arrival=R23)
    D23 = Door(two_way=True,
                tree=T23,
                name='D23',
                room_departure=R8,
                room_arrival=R24)
    D24 = Door(two_way=True,
                tree=T24,
                name='D24',
                room_departure=R0,
                room_arrival=RE)
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0.4, sa=0.5, li=0.3)
    c = Color.IVORY
    lcolor.inside_room_color = c
    lcolor.letters_color = c
    lcolor.surrounding_color = c
    lcolor.contour_color = c
    lcolor.background_color = [0, 0, 50]

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24],
                 fastest_solution='D7 D22 S18 D22 D7 S0 D6 D20 S16 D20 D6 S0 S1 D4 D16 S12 D16 D4 S0 D5 D18 S14 D18 D5 S0 S1 S2 D1 D10 S6 D10 D1 S0 D0 D8 S4 D8 D0 S0 S1 D2 D12 S8 D12 D2 S0 D3 D14 S10 D14 D3 S0 S1 S2 S3 D3 D15 S11 D15 D3 S0 D2 D13 S9 D13 D2 S0 S1 D0 D9 S5 D9 D0 S0 D1 D11 S7 D11 D1 S0 S1 S2 D5 D19 S15 D19 D5 S0 D4 D17 S13 D17 D4 S0 S1 D6 D21 S17 D21 D6 S0 D7 D23 S19 D23 D7 D24',
                 level_color=lcolor,
                 name='Rainforest',
                 keep_proportions=False,
                 door_window_size=300)
    
    return level
