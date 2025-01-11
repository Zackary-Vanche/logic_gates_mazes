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
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')

    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    Slist_3 = [S9, S10, S11]
    Slist_4 = [S12, S13, S14]
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
    V5 = Tree(tree_list=Tree.tree_list_DIFF(5),
              name='V5',
              switches=[V0, V1, V2, V3, V4])
    
    tree_list_INF_BIN = ['INF'] + [Tree.tree_list_BIN(3)]*2

    T0 = Tree(tree_list=Tree.tree_list_NOT,
                name='T0',
                switches=[S15])
    T1 = Tree(tree_list=Tree.tree_list_XNOR(3),
                name='T1',
                switches=Slist_0)
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[1])
    T3 = Tree(tree_list=Tree.tree_list_from_str('TF'),
                name='T3',
                switches=[S15, S16])
    T4 = Tree(tree_list=Tree.tree_list_XNOR(3),
                name='T4',
                switches=Slist_1)
    T5 = Tree(tree_list=tree_list_INF_BIN,
                name='T5',
                switches=Slist_0 + Slist_1)
    T6 = Tree(tree_list=Tree.tree_list_from_str('TTF'),
                name='T6',
                switches=[S15, S16, S17])
    T7 = Tree(tree_list=Tree.tree_list_XNOR(3),
                name='T7',
                switches=Slist_2)
    T8 = Tree(tree_list=tree_list_INF_BIN,
                name='T8',
                switches=Slist_1 + Slist_2)
    T9 = Tree(tree_list=Tree.tree_list_from_str('TTTF'),
                name='T9',
                switches=[S15, S16, S17, S18])
    T10 = Tree(tree_list=Tree.tree_list_XNOR(3),
                name='T10',
                switches=Slist_3)
    T11 = Tree(tree_list=tree_list_INF_BIN,
                name='T11',
                switches=Slist_2 + Slist_3)
    T12 = Tree(tree_list=Tree.tree_list_from_str('TTTTF'),
                name='T12',
                switches=[S15, S16, S17, S18, S19])
    T13 = Tree(tree_list=Tree.tree_list_XNOR(3),
                name='T13',
                switches=Slist_4)
    T14 = Tree(tree_list=tree_list_INF_BIN,
                name='T14',
                switches=Slist_3 + Slist_4)
    T15 = Tree(tree_list=['AND',
                          Tree.tree_list_AND(5),
                          [None]],                          
                name='T15',
                switches=[S15, S16, S17, S18, S19,
                          V5])

    dx = 0.7
    dy = 1
    ex = dx
    ey = 1

    R0 = Room(name='R0',
                position=[0*dx, 6*dy, 10*ex, ey/2],
                switches_list=[])
    R1 = Room(name='R1',
                position=[0*dx, 2*dy, ex, 3*ey],
                switches_list=Slist_0)
    R2 = Room(name='R2',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S15])
    R3 = Room(name='R3',
                position=[2*dx, 2*dy, ex, 3*ey],
                switches_list=Slist_1)
    R4 = Room(name='R4',
                position=[3*dx, 0*dy, ex, ey],
                switches_list=[S16])
    R5 = Room(name='R5',
                position=[4*dx, 2*dy, ex, 3*ey],
                switches_list=Slist_2)
    R6 = Room(name='R6',
                position=[5*dx, 0*dy, ex, ey],
                switches_list=[S17])
    R7 = Room(name='R7',
                position=[6*dx, 2*dy, ex, 3*ey],
                switches_list=Slist_3)
    R8 = Room(name='R8',
                position=[7*dx, 0*dy, ex, ey],
                switches_list=[S18])
    R9 = Room(name='R9',
                position=[8*dx, 2*dy, ex, 3*ey],
                switches_list=Slist_4)
    R10 = Room(name='R10',
                position=[9*dx, 0*dy, ex, ey],
                switches_list=[S19])
    RE = Room(name='RE',
              position=[10*dx, 3*dy, ex, ey],
              is_exit=True)
    
    ra0 = [1/2, 2.5/3]
    rd1 = [1/2, 0.5/3]

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1.5/10, 1/2],
                relative_arrival_coordinates=ra0)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=rd1)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R0,
                relative_arrival_coordinates=[1.5/10, 1/2])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R0,
                room_arrival=R3,
                relative_departure_coordinates=[3.5/10, 1/2],
                relative_arrival_coordinates=ra0)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R3,
                room_arrival=R4,
                relative_departure_coordinates=rd1)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R4,
                room_arrival=R0,
                relative_arrival_coordinates=[3.5/10, 1/2])
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=R5,
                relative_departure_coordinates=[5.5/10, 1/2],
                relative_arrival_coordinates=ra0)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R5,
                room_arrival=R6,
                relative_departure_coordinates=rd1)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R6,
                room_arrival=R0,
                relative_arrival_coordinates=[5.5/10, 1/2])
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R0,
                room_arrival=R7,
                relative_departure_coordinates=[7.5/10, 1/2],
                relative_arrival_coordinates=ra0)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R7,
                room_arrival=R8,
                relative_departure_coordinates=rd1)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R8,
                room_arrival=R0,
                relative_arrival_coordinates=[7.5/10, 1/2])
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R0,
                room_arrival=R9,
                relative_departure_coordinates=[9.5/10, 1/2],
                relative_arrival_coordinates=ra0)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R9,
                room_arrival=R10,
                relative_departure_coordinates=rd1)
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R10,
                room_arrival=R0,
                relative_arrival_coordinates=[9.5/10, 1/2])
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[9.5/10, 1/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15],
                 fastest_solution="D0 D1 S15 D2 D3 S3 S4 D4 S16 D5 D6 S6 S8 D7 S17 D8 D9 S10 S11 D10 S18 D11 D12 S12 S13 S14 D13 S19 D14 D15",
                 level_color=get_color(),
                 name='Jungle',
                 keep_proportions=True,
                 door_window_size=375)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.4, sa=0.3, li=0.4)
    lcolor.surrounding_color = Color.BRIGHT_ORANGE
    lcolor.contour_color = Color.BRIGHT_ORANGE
    return lcolor