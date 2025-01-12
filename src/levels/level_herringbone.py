from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
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
    
    V0 = Tree(tree_list=["AND"] + [Tree.tree_list_XOR(4)]*4,
                name='V0',
                switches=[S0, S1, S4, S7,
                          S1, S2, S4, S5,
                          S2, S3, S5, S6,
                          S0, S3, S6, S7],
                cut_expression_depth_1=True)

    T0 = Tree(tree_list=Tree.tree_list_from_str('FT'),
                name='T0',
                switches=[S0, V0])
    T1 = Tree(tree_list=Tree.tree_list_NOT,
                name='T1',
                switches=[S1])
    T2 = Tree(tree_list=Tree.tree_list_NOT,
                name='T2',
                switches=[S2])
    T3 = Tree(tree_list=Tree.tree_list_NOT,
                name='T3',
                switches=[S3])
    T4 = Tree(tree_list=Tree.tree_list_from_str('FT'),
                name='T4',
                switches=[S1, V0])
    T5 = Tree(tree_list=Tree.tree_list_NOT,
                name='T5',
                switches=[S2])
    T6 = Tree(tree_list=Tree.tree_list_NOT,
                name='T6',
                switches=[S3])
    T7 = Tree(tree_list=Tree.tree_list_NOT,
                name='T7',
                switches=[S0])
    T8 = Tree(tree_list=Tree.tree_list_NOT,
                name='T8',
                switches=[S1])
    T9 = Tree(tree_list=Tree.tree_list_NOT,
                name='T9',
                switches=[S4])
    T10 = Tree(tree_list=Tree.tree_list_NOT,
                name='T10',
                switches=[S5])
    T11 = Tree(tree_list=Tree.tree_list_NOT,
                name='T11',
                switches=[S5])
    T12 = Tree(tree_list=Tree.tree_list_NOT,
                name='T12',
                switches=[S6])
    T13 = Tree(tree_list=Tree.tree_list_NOT,
                name='T13',
                switches=[S6])
    T14 = Tree(tree_list=Tree.tree_list_NOT,
                name='T14',
                switches=[S7])
    T15 = Tree(tree_list=Tree.tree_list_NOT,
                name='T15',
                switches=[S7])
    T16 = Tree(tree_list=Tree.tree_list_NOT,
                name='T16',
                switches=[S4])
    T17 = Tree(tree_list=Tree.tree_list_AND(10),
                name='T17',
                switches=[S8, S9, S10, S11, S12, S13, S14, S15, S16, S17])

    dx = 2
    dy = 1
    ex = 1.5
    ey = 0.5
    eye = (dx+ex)/8
    
    # R0     R0      RE
    # D0     D4     D17
    # R1 D9  R2 D10 R11
    # D1     D5
    # R3 D11 R4 D12 R11
    # D2     D6     
    # R5 D13 R6 D14  R7
    # D3     D7      D8
    # R8 D15 R9 D16 R10
    
    # D1 = D8

    R0 = Room(name='R0',
                position=[0*dx, ey-eye, dx+ex, eye],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7])
    R1 = Room(name='R1',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S8])
    R2 = Room(name='R2',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S9])
    R3 = Room(name='R3',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S10])
    R4 = Room(name='R4',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S11])
    R5 = Room(name='R5',
                position=[0*dx, 3*dy, ex, ey],
                switches_list=[S12])
    R6 = Room(name='R6',
                position=[1*dx, 3*dy, ex, ey],
                switches_list=[S13])
    R7 = Room(name='R7',
                position=[2*dx, 3*dy, ex, ey],
                switches_list=[S14])
    R8 = Room(name='R8',
                position=[0*dx, 4*dy, ex, ey],
                switches_list=[S15])
    R9 = Room(name='R9',
                position=[1*dx, 4*dy, ex, ey],
                switches_list=[S16])
    R10 = Room(name='R10',
                position=[2*dx, 4*dy, ex, ey],
                switches_list=[S17])
    R11 = Room(name='R11',
                position=[2*dx, 1*dy, ex, dy+ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[2*dx, 0*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[ex/2/(dx+ex), 1],
                relative_arrival_coordinates=[1/2, 0])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R3)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R3,
                room_arrival=R5)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R5,
                room_arrival=R8)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R0,
                room_arrival=R2,
                relative_departure_coordinates=[(dx+ex/2)/(dx+ex), 1],
                relative_arrival_coordinates=[1/2, 0])
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R4,
                room_arrival=R2)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R6,
                room_arrival=R4)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R9,
                room_arrival=R6)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R10,
                room_arrival=R7)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R2,
                room_arrival=R1)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R2,
                room_arrival=R11,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, ey/2/(dy+ey)])
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R3,
                room_arrival=R4)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R4,
                room_arrival=R11,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, (dy+ey/2)/(dy+ey)])
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R6,
                room_arrival=R5)
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R7,
                room_arrival=R6)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R8,
                room_arrival=R9)
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R9,
                room_arrival=R10)
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R11,
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[1/2, 1])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17],
                 fastest_solution="S0 S5 D4 S9 D9 S8 D1 S10 D2 S12 D3 S15 D15 S16 D16 S17 D8 S14 D14 S13 D6 S11 D12 D17",
                 level_color=get_color(),
                 name='Herringbone',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.6, sa=0.3, li=0.5)
    lcolor.surrounding_color = Color.color_hls(hu=0.1, sa=0.8, li=0.8)
    lcolor.contour_color = Color.color_hls(hu=0.9, sa=0.8, li=0.8)
    return lcolor