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
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')
    S20 = Switch(name='S20')
    S21 = Switch(name='S21')
    S22 = Switch(name='S22')

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21]

    Slist_0 = [S0, S1]
    Slist_1 = [S2, S3]
    Slist_2 = [S4, S5]
    Slist_3 = [S6, S7]
    Slist_4 = [S8, S9]
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
    
    tree_list = Tree.tree_list_IN(3)

    T0 = Tree(tree_list=Tree.tree_list_INFOREQU(3),
                name='T0',
                switches=[V0, V1, V2])
    
    T1 = Tree(tree_list=tree_list,
                name='T1',
                switches=[1, V0, V1])
    T2 = Tree(tree_list=tree_list,
                name='T2',
                switches=[1, V0, V2])
    T3 = Tree(tree_list=tree_list,
                name='T3',
                switches=[1, V0, V3])
    T4 = Tree(tree_list=tree_list,
                name='T4',
                switches=[1, V1, V2])
    T5 = Tree(tree_list=tree_list,
                name='T5',
                switches=[1, V2, V3])
    T6 = Tree(tree_list=tree_list,
                name='T6',
                switches=[1, V1, V4])
    T7 = Tree(tree_list=tree_list,
                name='T7',
                switches=[1, V2, V4])
    T8 = Tree(tree_list=tree_list,
                name='T8',
                switches=[1, V3, V4])
    
    T9 = Tree(tree_list=tree_list,
                name='T9',
                switches=[2, V0, V1])
    T10 = Tree(tree_list=tree_list,
                name='T10',
                switches=[2, V0, V2])
    T11 = Tree(tree_list=tree_list,
                name='T11',
                switches=[2, V0, V3])
    T12 = Tree(tree_list=tree_list,
                name='T12',
                switches=[2, V1, V2])
    T13 = Tree(tree_list=tree_list,
                name='T13',
                switches=[2, V2, V3])
    T14 = Tree(tree_list=tree_list,
                name='T14',
                switches=[2, V1, V4])
    T15 = Tree(tree_list=tree_list,
                name='T15',
                switches=[2, V2, V4])
    T16 = Tree(tree_list=tree_list,
                name='T16',
                switches=[2, V3, V4])
    
    T17 = Tree(tree_list=tree_list,
                name='T17',
                switches=[3, V3, V4])
    T18 = Tree(tree_list=tree_list,
                name='T18',
                switches=[3, V2, V3])
    T19 = Tree(tree_list=tree_list,
                name='T19',
                switches=[3, V0, V3])
    T20 = Tree(tree_list=tree_list,
                name='T20',
                switches=[3, V2, V4])
    T21 = Tree(tree_list=tree_list,
                name='T21',
                switches=[3, V0, V2])
    T22 = Tree(tree_list=tree_list,
                name='T22',
                switches=[3, V1, V4])
    T23 = Tree(tree_list=tree_list,
                name='T23',
                switches=[3, V1, V2])
    T24 = Tree(tree_list=tree_list,
                name='T24',
                switches=[3, V0, V1])
    
    T25 = Tree(tree_list=Tree.tree_list_AND(13),
                name='T25',
                switches=[S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22])

    dx = 1.5
    dy = -1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[-2*dx, 0*dy, 5*ey, 2*ey],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9])
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S10])
    R2 = Room(name='R2',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S11])
    R3 = Room(name='R3',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S12])
    R4 = Room(name='R4',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S13])
    R5 = Room(name='R5',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S14])
    R6 = Room(name='R6',
                position=[0*dx, 3*dy, ex, ey],
                switches_list=[S15])
    R7 = Room(name='R7',
                position=[1*dx, 3*dy, ex, ey],
                switches_list=[S16])
    R8 = Room(name='R8',
                position=[2*dx, 3*dy, ex, ey],
                switches_list=[S17])
    R9 = Room(name='R9',
                position=[1*dx, 4*dy, ex, ey],
                switches_list=[S18])
    R10 = Room(name='R10',
                position=[-1*dx, 4*dy, ex, ey],
                switches_list=[S19])
    R11 = Room(name='R11',
                position=[-1*dx, 3*dy, ex, ey],
                switches_list=[S20])
    R12 = Room(name='R12',
                position=[-1*dx, 2*dy, ex, ey],
                switches_list=[S21])
    R13 = Room(name='R13',
                position=[-2*dx, 3*dy, ex, ey],
                switches_list=[S22])
    RE = Room(name='RE',
              position=[-1*dx, 1*dy, ex, ey],
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
                room_departure=R6,
                room_arrival=R10)
    D18 = Door(two_way=True,
                tree=T18,
                name='D18',
                room_departure=R6,
                room_arrival=R11)
    D19 = Door(two_way=True,
                tree=T19,
                name='D19',
                room_departure=R6,
                room_arrival=R12)
    D20 = Door(two_way=True,
                tree=T20,
                name='D20',
                room_departure=R10,
                room_arrival=R11)
    D21 = Door(two_way=True,
                tree=T21,
                name='D21',
                room_departure=R11,
                room_arrival=R12)
    D22 = Door(two_way=True,
                tree=T22,
                name='D22',
                room_departure=R10,
                room_arrival=R13)
    D23 = Door(two_way=True,
                tree=T23,
                name='D23',
                room_departure=R11,
                room_arrival=R13)
    D24 = Door(two_way=True,
                tree=T24,
                name='D24',
                room_departure=R12,
                room_arrival=R13)
    D25 = Door(two_way=True,
                tree=T25,
                name='D25',
                room_departure=R12,
                room_arrival=RE)

    Dl0 = [D1, D2, D3, D4, D5, D6, D7]
    Dl1 = [D8, D9, D10, D11, D12, D13, D14, D15]
    Dl2 = [D16, D17, D18, D19, D20, D21, D22, D23, D24,]

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, RE],
                 doors_list=[D0]+Dl0+Dl1+Dl2+[D25],
                 fastest_solution="S0 S3 S4 S5 S7 S8 D0 S10 D1 S11 D1 D2 S12 D2 D3 S13 D8 S14 D9 S15 D12 S16 D13 S17 D16 S18 D14 D18 S20 D20 S19 D20 D23 S22 D23 D21 S21 D25",
                 level_color=get_color(),
                 name='Domatic number',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.3, sa=0.25, li=0.3)
    lcolor.contour_color = Color.color_hls(hu=0.2, sa=1, li=0.7)
    lcolor.surrounding_color = Color.color_hls(hu=0.45, sa=1, li=0.7)
    return lcolor