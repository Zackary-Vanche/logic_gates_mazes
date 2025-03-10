from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

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

    tree_list_1 = ['AND', Tree.tree_list_XNOR(2), Tree.tree_list_XOR(2)]
    T0 = Tree(tree_list=['AND',
                         ['EQU',
                          [None],
                          Tree.tree_list_SUM(9),],
                         Tree.tree_list_NAND(4)],
                    name='T0',
                    switches=[4, S0, S1, S2, S3, S4, S5, S6, S7, S8,
                              S0, S3, S6, S7],
                    cut_expression=True)
    T1 = Tree(tree_list=tree_list_1,
                    name='T1',
                    switches=[S0, S1, S9, S10])
    T2 = Tree(tree_list=tree_list_1,
                    name='T2',
                    switches=[S1, S2, S10, S11])
    T3 = Tree(tree_list=tree_list_1,
                    name='T3',
                    switches=[S3, S4, S12, S13])
    T4 = Tree(tree_list=tree_list_1,
                    name='T4',
                    switches=[S4, S5, S13, S14])
    T5 = Tree(tree_list=tree_list_1,
                    name='T5',
                    switches=[S6, S7, S15, S16])
    T6 = Tree(tree_list=['AND', Tree.tree_list_XOR(2), Tree.tree_list_XOR(2)],
                    name='T6',
                    switches=[S7, S8, S16, S17])
    T7 = Tree(tree_list=tree_list_1,
                    name='T7',
                    switches=[S0, S3, S9, S12])
    T8 = Tree(tree_list=tree_list_1,
                    name='T8',
                    switches=[S3, S6, S12, S15])
    T9 = Tree(tree_list=tree_list_1,
                    name='T9',
                    switches=[S1, S4, S10, S13])
    T10 = Tree(tree_list=tree_list_1,
                    name='T10',
                    switches=[S4, S7, S13, S16])
    T11 = Tree(tree_list=tree_list_1,
                    name='T11',
                    switches=[S2, S5, S11, S14])
    T12 = Tree(tree_list=tree_list_1,
                    name='T12',
                    switches=[S5, S8, S14, S17])
    T13 = Tree(tree_list=tree_list_1,
                    name='T13',
                    switches=[S0, S4, S9, S13])
    T14 = Tree(tree_list=tree_list_1,
                    name='T14',
                    switches=[S1, S3, S10, S12])
    T15 = Tree(tree_list=Tree.tree_list_AND(9),
                name='T15',
                switches=[S9, S10, S11, S12, S13, S14, S15, S16, S17])

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5
    epsilonx = 0.2
    epsilony = 0.2

    R0 = Room(name='R0',
                position=[-1*dx, 0*dy, ex+0.1, 2*dy],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8])
    R1 = Room(name='R1',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S9])
    R2 = Room(name='R2',
                position=[0*dx, 1*dy+epsilony, ex, ey],
                switches_list=[S10])
    R3 = Room(name='R3',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S11])
    R4 = Room(name='R4',
                position=[1*dx+epsilonx, 0*dy, ex, ey],
                switches_list=[S12])
    R5 = Room(name='R5',
                position=[1*dx+epsilonx, 1*dy+epsilony, ex, ey],
                switches_list=[S13])
    R6 = Room(name='R6',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S14])
    R7 = Room(name='R7',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[S15])
    R8 = Room(name='R8',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S16])
    R9 = Room(name='R9',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S17])
    RE = Room(name='RE',
              position=[-1*dx, 2*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R4,
                room_arrival=R5)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R5,
                room_arrival=R6)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R7,
                room_arrival=R8)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R8,
                room_arrival=R9)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R1,
                room_arrival=R4)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R4,
                room_arrival=R7)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R2,
                room_arrival=R5)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R5,
                room_arrival=R8)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R3,
                room_arrival=R6)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R6,
                room_arrival=R9)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R1,
                room_arrival=R5,
                relative_position=0.35)
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R2,
                room_arrival=R4,
                relative_position=0.35)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R3,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15],
                 fastest_solution='S0 S4 S5 S8 D0 S9 D13 S13 D4 S14 D12 S17 D6 S16 D5 S15 D8 S12 D14 S10 D2 S11 D15',
                 level_color=get_color(),
                 name='Intersection',
                 keep_proportions=True,
                 door_window_size=375)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.92, sa=0.2, li=0.7)
    lcolor.surrounding_color = Color.IVORY
    lcolor.contour_color = Color.IVORY
    return lcolor

"""
S2 S5 S8 D0 S9 D1 S10 D9 S13 D3 S12 D8 S15 D5 S16 D6 S17 D12 S14 D11 S11 D15
S0 S3 S6 S7 D0 S9 D7 S12 D8 S15 D5 S16 D6 S17 D12 S14 D4 S13 D9 S10 D2 S11 D15
S0 S4 S5 S8 D0 S9 D13 S13 D4 S14 D12 S17 D6 S16 D5 S15 D8 S12 D14 S10 D2 S11 D15
D0 S9 D1 S10 D9 S13 D3 D7 D0 S1 S2 S5 S8 D0 D7 S12 D8 S15 D5 S16 D6 S17 D12 S14 D11 S11 D15
D0 S9 D1 S10 D9 S13 D3 D7 D0 S2 S4 S5 S8 D0 D7 S12 D8 S15 D5 S16 D6 S17 D12 S14 D11 S11 D15
D0 S9 D1 S10 D9 S13 D3 S12 D8 S15 D5 D10 S13 D13 D0 S0 S4 S7 D0 D13 S13 D10 S16 D6 S17 D12 S14 D11 S11 D15
D0 S9 D1 S10 D9 S13 D3 S12 D8 S15 D5 D10 S13 D13 D0 S0 S1 S4 S7 D0 D13 S13 D10 S16 D6 S17 D12 S14 D11 S11 D15
D0 S9 D1 S10 D9 S13 D3 S12 D8 S15 D5 D10 S13 D13 D0 S0 S3 S4 S7 D0 D13 S13 D10 S16 D6 S17 D12 S14 D11 S11 D15
D0 S9 D1 S10 D9 S13 D3 S12 D8 S15 D5 D10 S13 D13 D0 S0 S4 S6 S7 D0 D13 S13 D10 S16 D6 S17 D12 S14 D11 S11 D15
D0 S9 D1 S10 D9 S13 D3 S12 D8 S15 D5 D10 S13 D13 D0 S2 S3 S5 S8 D0 D13 S13 D10 S16 D6 S17 D12 S14 D11 S11 D15
D0 S9 D1 S10 D9 S13 D3 S12 D8 S15 D5 D10 S13 D13 D0 S2 S5 S6 S8 D0 D13 S13 D10 S16 D6 S17 D12 S14 D11 S11 D15
"""