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
    
    # 1
    S4 = Switch(name='S4', value=1)
    S5 = Switch(name='S5')
    # 2
    S6 = Switch(name='S6')
    S7 = Switch(name='S7', value=1)
    # 3
    S8 = Switch(name='S8', value=1)
    S9 = Switch(name='S9', value=1)
    # 1
    S10 = Switch(name='S10', value=1)
    S11 = Switch(name='S11')
    # 3
    S12 = Switch(name='S12', value=1)
    S13 = Switch(name='S13', value=1)

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13]

    Slist_0 = [S0, S1]
    Slist_1 = [S2, S3]
    Slist_2 = [S4, S5]
    Slist_3 = [S6, S7]
    Slist_4 = [S8, S9]
    Slist_5 = [S10, S11]
    Slist_6 = [S12, S13]
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
    V5 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_5)),
          name='V5',
          switches=Slist_5)
    V6 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_6)),
          name='V6',
          switches=Slist_6)
    
    V7 = Tree(tree_list=Tree.tree_list_EQU(2),
          name='V7',
          switches=[V0, 0])
    V8 = Tree(tree_list=Tree.tree_list_EQU(2),
          name='V8',
          switches=[V0, 1])
    V9 = Tree(tree_list=Tree.tree_list_EQU(2),
          name='V9',
          switches=[V0, 2])
    V10 = Tree(tree_list=Tree.tree_list_EQU(2),
          name='V10',
          switches=[V0, 3])
    
    V11 = Tree(tree_list=Tree.tree_list_EQUSET(3*2),
          name='V11',
          switches=[V1, V2, V3, 1, 2, 3])
    V12 = Tree(tree_list=Tree.tree_list_EQUSET(3*2),
          name='V12',
          switches=[V1, V3, V4, 1, 2, 3])
    V13 = Tree(tree_list=Tree.tree_list_EQUSET(3*2),
          name='V13',
          switches=[V1, V4, V5, 1, 2, 3])
    V14 = Tree(tree_list=Tree.tree_list_EQUSET(3*2),
          name='V14',
          switches=[V1, V5, V6, 1, 2, 3])
    
    V15 = Tree(tree_list=Tree.tree_list_EQU(3),
          name='V15',
          switches=[V1, V2, V3])
    V16 = Tree(tree_list=Tree.tree_list_EQU(3),
          name='V16',
          switches=[V1, V3, V4])
    V17 = Tree(tree_list=Tree.tree_list_EQU(3),
          name='V17',
          switches=[V1, V4, V5])
    V18 = Tree(tree_list=Tree.tree_list_EQU(3),
          name='V18',
          switches=[V1, V5, V6])

    Vlist = [V0, V1, V2, V3, V4, V5, V6]

    T0 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T0',
                switches=[V7, V11])
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[V7])
    T2 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T2',
                switches=[V7, V15])
    
    T3 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T3',
                switches=[V8, V12])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[V8])
    T5 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T5',
                switches=[V8, V16])
    
    T6 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T6',
                switches=[V9, V13])
    T7 = Tree(tree_list=[None],
                name='T7',
                switches=[V9])
    T8 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T8',
                switches=[V9, V17])
    
    T9 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T9',
                switches=[V10, V14])
    T10 = Tree(tree_list=[None],
                name='T10',
                switches=[V10])
    T11 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T11',
                switches=[V10, V18])
    
    T12 = Tree(tree_list=Tree.tree_list_EQU(7),
                name='T12',
                switches=[V0, V1, V2, V3, V4, V5, V6])

    dx = 1.5
    dy = 2
    ex = 2
    ey = 1
    
    exe = 4*dx+ex

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, exe, ey],
                switches_list=[S0, S1, S2, S3])
    R1 = Room(name='R1',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S4, S5,])
    R2 = Room(name='R2',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S6, S7,])
    R3 = Room(name='R3',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S8, S9,])
    R4 = Room(name='R4',
                position=[3*dx, 2*dy, ex, ey],
                switches_list=[S10, S11,])
    R5 = Room(name='R5',
                position=[4*dx, 1*dy, ex, ey],
                switches_list=[S12, S13,])
    RE = Room(name='RE',
              position=[2*dx, -1*dy+0.5, ex, 0.7],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[ex/2/exe, 1],
                relative_arrival_coordinates=[1/2, 0])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R0,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[(dx+ex/2)/exe, 0],
                relative_position=0.4)
    
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R0,
                room_arrival=R2,
                relative_departure_coordinates=[(dx+ex/2)/exe, 0],
                relative_arrival_coordinates=[1/2, 1],
                relative_position=0.4)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R3)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R0,
                relative_departure_coordinates=[1/4, 0],
                relative_arrival_coordinates=[(2*dx+ex/4)/exe, 1])
    
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=R3,
                relative_departure_coordinates=[(2*dx+3*ex/4)/exe, 1],
                relative_arrival_coordinates=[3/4, 0])
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R3,
                room_arrival=R4)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R4,
                room_arrival=R0,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[(3*dx+ex/2)/exe, 0],
                relative_position=0.4)
    
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R0,
                room_arrival=R4,
                relative_departure_coordinates=[(3*dx+ex/2)/exe, 0],
                relative_arrival_coordinates=[1/2, 1],
                relative_position=0.4)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R4,
                room_arrival=R5)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R5,
                room_arrival=R0,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[(4*dx+ex/2)/exe, 1])
    
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[1/2, 1])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12],
                 fastest_solution="S0 S1 S3 D9 S10 S11 D10 S12 D11 S0 S2 S3 D6 S9 D7 S10 S11 D8 S0 S1 S3 D3 S6 D4 S9 D5 S0 S2 D0 S4 S5 D1 S6 D2 S1 D6 S8 D7 S10 S11 D8 D12",
                 level_color=get_color(),
                 name='Flip',
                 keep_proportions=True,
                 door_window_size=400)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE_light_background(hu=0.3, sa=0.2, li=0.1)