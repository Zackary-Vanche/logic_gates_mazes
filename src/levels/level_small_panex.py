from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def level_small_panex(): 
    
    v = 1

    S0 = Switch(name='S0', value=v)
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4', value=v)
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
    S18 = Switch(name='S18', value=v)
    S19 = Switch(name='S19')
    S20 = Switch(name='S20', value=v)
    S21 = Switch(name='S21')
    S22 = Switch(name='S22', value=v)
    S23 = Switch(name='S23', value=v)
    S24 = Switch(name='S24')
    S25 = Switch(name='S25')
    S26 = Switch(name='S26')
    
    tree_list_0 = ['AND',
                   ['EQU', Tree.tree_list_BIN(3), [None]],
                   ['INF0'] + [Tree.tree_list_BIN(3)]*3]
    tree_list_12 = ['EQU', Tree.tree_list_BIN(3), Tree.tree_list_BIN(3)]
    
    Slist0 = [S0, S1, S2, S3, S4, S5, S6, S7, S8]
    Slist1 = [S9, S10, S11, S12, S13, S14, S15, S16, S17]
    Slist2 = [S18, S19, S20, S21, S22, S23, S24, S25, S26]

    T0 = Tree(tree_list=tree_list_0,
                name='T0',
                switches=[S0, S1, S2, 0] + Slist0)
    T1 = Tree(tree_list=tree_list_0,
                name='T1',
                switches=[S3, S4, S5, 0] + Slist0)
    T2 = Tree(tree_list=tree_list_0,
                name='T2',
                switches=[S6, S7, S8, 0] + Slist0)
    T3 = Tree(tree_list=tree_list_0,
                name='T3',
                switches=[S9, S10, S11, 0] + Slist1)
    T4 = Tree(tree_list=tree_list_0,
                name='T4',
                switches=[S12, S13, S14, 0] + Slist1)
    T5 = Tree(tree_list=tree_list_0,
                name='T5',
                switches=[S15, S16, S17, 0] + Slist1)
    T6 = Tree(tree_list=tree_list_0,
                name='T6',
                switches=[S18, S19, S20, 0] + Slist2)
    T7 = Tree(tree_list=tree_list_0,
                name='T7',
                switches=[S21, S22, S23, 0] + Slist2)
    T8 = Tree(tree_list=tree_list_0,
                name='T8',
                switches=[S24, S25, S26, 0] + Slist2)
    T9 = Tree(tree_list=tree_list_0,
                name='T9',
                switches=[S9, S10, S11, 0] + Slist1)
    T10 = Tree(tree_list=tree_list_0,
                name='T10',
                switches=[S12, S13, S14, 0] + Slist1)
    T11 = Tree(tree_list=tree_list_0,
                name='T11',
                switches=[S15, S16, S17, 0] + Slist1)
    T12 = Tree(tree_list=tree_list_12,
                name='T12',
                switches=[S0, S1, S2, S3, S4, S5])
    T13 = Tree(tree_list=tree_list_12,
                name='T13',
                switches=[S3, S4, S5, S6, S7, S8])
    T14 = Tree(tree_list=tree_list_12,
                name='T14',
                switches=[S6, S7, S8, S15, S16, S17])
    T15 = Tree(tree_list=tree_list_12,
                name='T15',
                switches=[S9, S10, S11, S12, S13, S14])
    T16 = Tree(tree_list=tree_list_12,
                name='T16',
                switches=[S12, S13, S14, S15, S16, S17])
    T17 = Tree(tree_list=tree_list_12,
                name='T17',
                switches=[S6, S7, S8, S24, S25, S26])
    T18 = Tree(tree_list=tree_list_12,
                name='T18',
                switches=[S18, S19, S20, S21, S22, S23])
    T19 = Tree(tree_list=tree_list_12,
                name='T19',
                switches=[S21, S22, S23, S24, S25, S26])
    T20 = Tree(tree_list=tree_list_12,
                name='T20',
                switches=[S15, S16, S17, S24, S25, S26])
    T21 = Tree(tree_list=[None],
                name='T21',
                switches=[1])
    T22 = Tree(tree_list=Tree.tree_list_from_str('101011100010'),
                name='T22',
                switches=[S0, S1, S2,
                          S3, S4, S5,
                          S18, S19, S20,
                          S21, S22, S23,],
                cut_expression=True)
    ex = 0.4
    ey = 0.95
    
    epsilonx = 0.1

    R0 = Room(name='R0',
                position=[2.1, 2+ey, ex, 5.25],
                switches_list=[])
    R1 = Room(name='R1',
                position=[8.5, 2+ey, ex, 5.25],
                switches_list=[])
    R2 = Room(name='R2',
                position=[3+2*epsilonx, 6, 2, ey],
                switches_list=[S0, S1, S2])
    R3 = Room(name='R3',
                position=[3+epsilonx, 4, 2, ey],
                switches_list=[S3, S4, S5])
    R4 = Room(name='R4',
                position=[3, 2, 2, ey],
                switches_list=[S6, S7, S8])
    R5 = Room(name='R5',
                position=[4+2*epsilonx, 7, 3-4*epsilonx, ey],
                switches_list=[S9, S10, S11])
    R6 = Room(name='R6',
                position=[4+epsilonx, 5, 3-2*epsilonx, ey],
                switches_list=[S12, S13, S14])
    R7 = Room(name='R7',
                position=[4, 3, 3, ey],
                switches_list=[S15, S16, S17])
    R8 = Room(name='R8',
                position=[6-2*epsilonx, 6, 2, ey],
                switches_list=[S18, S19, S20])
    R9 = Room(name='R9',
                position=[6-epsilonx, 4, 2, ey],
                switches_list=[S21, S22, S23])
    R10 = Room(name='R10',
                position=[6, 2, 2, ey],
                switches_list=[S24, S25, S26])
    RE = Room(name='RE',
              position=[2, 1.9, ex+0.2, ey/2],
              is_exit=True)
    
    r = 1/30

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R2,
                relative_departure_coordinates=[1, 4/5.5],
                relative_arrival_coordinates=[0, 1/2])
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R3,
                relative_departure_coordinates=[1, 2/5.5],
                relative_arrival_coordinates=[0, 1/2])
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=R4,
                relative_departure_coordinates=[1, 0/5.5],
                relative_arrival_coordinates=[0, 1/2])
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R0,
                room_arrival=R5,
                relative_departure_coordinates=[1, 5/5.5],
                relative_arrival_coordinates=[0, 1/2],
                relative_position=1/3)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R0,
                room_arrival=R6,
                relative_departure_coordinates=[1, 3/5.5],
                relative_arrival_coordinates=[0, 1/2],
                relative_position=1/3)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R0,
                room_arrival=R7,
                relative_departure_coordinates=[1, 1/5.5],
                relative_arrival_coordinates=[0, 1/2],
                relative_position=1/3)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R1,
                room_arrival=R8,
                relative_departure_coordinates=[0, 4/5.5],
                relative_arrival_coordinates=[1, 1/2])
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R1,
                room_arrival=R9,
                relative_departure_coordinates=[0, 2/5.5],
                relative_arrival_coordinates=[1, 1/2])
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R1,
                room_arrival=R10,
                relative_departure_coordinates=[0, 0/5.5],
                relative_arrival_coordinates=[1, 1/2])
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R1,
                room_arrival=R5,
                relative_departure_coordinates=[0, 5/5.5],
                relative_arrival_coordinates=[1, 1/2],
                relative_position=1/3)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R1,
                room_arrival=R6,
                relative_departure_coordinates=[0, 3/5.5],
                relative_arrival_coordinates=[1, 1/2],
                relative_position=1/3)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R1,
                room_arrival=R7,
                relative_departure_coordinates=[0, 1/5.5],
                relative_arrival_coordinates=[1, 1/2],
                relative_position=1/3)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R2,
                room_arrival=R3,
                relative_departure_coordinates=[1/3, 1/2],
                relative_arrival_coordinates=[1/6, 1/2])
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R3,
                room_arrival=R4,
                relative_departure_coordinates=[1/3, 1/2],
                relative_arrival_coordinates=[1/6, 1/2])
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R4,
                room_arrival=R7,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[1/2, 0],
                relative_position=0.5-r)
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R5,
                room_arrival=R6)
    D16 = Door(two_way=True,
                tree=T16,
                name='D16',
                room_departure=R6,
                room_arrival=R7)
    D17 = Door(two_way=True,
                tree=T17,
                name='D17',
                room_departure=R4,
                room_arrival=R10,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[0, 0])
    D18 = Door(two_way=True,
                tree=T18,
                name='D18',
                room_departure=R8,
                room_arrival=R9,
                relative_departure_coordinates=[2/3, 1/2],
                relative_arrival_coordinates=[5/6, 1/2])
    D19 = Door(two_way=True,
                tree=T19,
                name='D19',
                room_departure=R9,
                room_arrival=R10,
                relative_departure_coordinates=[2/3, 1/2],
                relative_arrival_coordinates=[5/6, 1/2])
    D20 = Door(two_way=True,
                tree=T20,
                name='D20',
                room_departure=R10,
                room_arrival=R7,
                relative_departure_coordinates=[0, 0],
                relative_arrival_coordinates=[1/2, 0],
                relative_position=0.5-r)
    D21 = Door(two_way=True,
                tree=T21,
                name='D21',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1, 1],
                relative_arrival_coordinates=[0, 1])
    D22 = Door(two_way=True,
                tree=T22,
                name='D22',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[1/2, 1])

    lcolor = Levels_colors_list.FROM_HUE(hu=0, sa=0.2, li=0.4)
    lcolor.surrounding_color = Color.TOTAL_YELLOW
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22],
                 fastest_solution='D2 S7 D13 S3 S4 D12 S0 D0 D5 S16 D14 S6 S7 D13 S3 D1 D21 D8 S25 S26 D19 S21 S22 D18 S18 S20 D6 D10 S13 D16 S17 D20 S24 S25 D19 S21 S23 D7 D9 S10 D15 S14 D16 S15 S16 D20 S26 D17 S8 D14 S15 S16 D16 S14 D15 S10 D3 D1 S3 S5 D13 S6 S7 D14 S17 D16 S13 D10 D7 S21 D19 S24 S25 D20 S16 D11 D6 S18 D18 S21 S22 D19 S25 D8 D21 D0 S0 S2 D12 S3 S4 D13 S7 S8 D2 D22',
                 level_color=lcolor,
                 name='Small panex',
                 keep_proportions=True,
                 door_window_size=525)
    
    return level