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
    
    Slist_0 = [S0, S1, S2, S3, S4, S5, S6, S7,]

    T0 = Tree(tree_list=["AND",
                         ['EQU', Tree.tree_list_SUM(8), [None]],
                         ['EQU', Tree.tree_list_SUM(4), [None]],
                         Tree.tree_list_DIFF(2)],
                name='T0',
                switches=Slist_0+[4]+[S1, S3, S4, S6, 2]+[S1, S6])
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[S0])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[S1])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[S2])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[S3])
    T5 = Tree(tree_list=[None],
                name='T5',
                switches=[S4])
    T6 = Tree(tree_list=[None],
                name='T6',
                switches=[S5])
    T7 = Tree(tree_list=[None],
                name='T7',
                switches=[S6])
    T8 = Tree(tree_list=[None],
                name='T8',
                switches=[S7])
    T9 = Tree(tree_list=Tree.tree_list_NOT,
                name='T9',
                switches=[S0])
    T10 = Tree(tree_list=Tree.tree_list_NOT,
                name='T10',
                switches=[S1])
    T11 = Tree(tree_list=Tree.tree_list_NOT,
                name='T11',
                switches=[S2])
    T12 = Tree(tree_list=Tree.tree_list_NOT,
                name='T12',
                switches=[S3])
    T13 = Tree(tree_list=Tree.tree_list_NOT,
                name='T13',
                switches=[S4])
    T14 = Tree(tree_list=Tree.tree_list_NOT,
                name='T14',
                switches=[S5])
    T15 = Tree(tree_list=Tree.tree_list_NOT,
                name='T15',
                switches=[S6])
    T16 = Tree(tree_list=Tree.tree_list_NOT,
                name='T16',
                switches=[S7])
    T17 = Tree(tree_list=Tree.tree_list_AND(9),
                name='T17',
                switches=[S8, S9, S10, S11, S12, S13, S14, S15, S16,])

    dx = 1.5
    dy = -1
    ex = 0.75
    ey = 0.5

    R0 = Room(name='R0',
                position=[-1*dx, 0*dy, 4*ey, 2*ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S8])
    R2 = Room(name='R2',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S9])
    R3 = Room(name='R3',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S10])
    R4 = Room(name='R4',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S11])
    R5 = Room(name='R5',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S12])
    R6 = Room(name='R6',
                position=[0*dx, 3*dy, ex, ey],
                switches_list=[S13])
    R7 = Room(name='R7',
                position=[1*dx, 3*dy, ex, ey],
                switches_list=[S14])
    R8 = Room(name='R8',
                position=[2*dx, 3*dy, ex, ey],
                switches_list=[S15])
    R9 = Room(name='R9',
                position=[1*dx, 4*dy, ex, ey],
                switches_list=[S16])
    RE = Room(name='RE',
              position=[-1*dx, 2*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1, 1/4],
                relative_arrival_coordinates=[0, 1/2])
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R3)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R4)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R3)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R4)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R2,
                room_arrival=R5)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R3,
                room_arrival=R5)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R4,
                room_arrival=R5)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R5,
                room_arrival=R6)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R5,
                room_arrival=R7)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R5,
                room_arrival=R8)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R6,
                room_arrival=R7)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R7,
                room_arrival=R8)
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R6,
                room_arrival=R9)
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R7,
                room_arrival=R9)
    D16 = Door(two_way=True,
                tree=T16,
                name='D16',
                room_departure=R8,
                room_arrival=R9)
    D17 = Door(two_way=True,
                tree=T17,
                name='D17',
                room_departure=R5,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17],
                 fastest_solution="S0 S2 S3 S6 D0 S8 D3 S11 D3 D1 S9 D4 S10 D7 S12 D10 S14 D13 S15 D16 S16 D14 S13 D14 D16 D13 D10 D17",
                 level_color=get_color(),
                 name='Arboricity',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.4, sa=0.25, li=0.3)
    lcolor.contour_color = Color.color_hls(hu=0.15, sa=1, li=0.7)
    lcolor.surrounding_color = Color.color_hls(hu=0.4, sa=1, li=0.7)
    return lcolor