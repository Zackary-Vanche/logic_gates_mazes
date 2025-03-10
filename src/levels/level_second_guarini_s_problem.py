from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list

def f(fast_solution_finding=False): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6', value=1)
    S7 = Switch(name='S7')
    
    S8 = Switch(name='S8')
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11', value=1)
    
    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14', value=1)
    S15 = Switch(name='S15', value=1)
    
    S16 = Switch(name='S16', value=1)
    S17 = Switch(name='S17', value=1)
    S18 = Switch(name='S18', value=1)
    S19 = Switch(name='S19')
    
    S20 = Switch(name='S20', value=1)
    S21 = Switch(name='S21', value=1)
    S22 = Switch(name='S22')
    S23 = Switch(name='S23', value=1)
    
    S24 = Switch(name='S24', value=1)
    S25 = Switch(name='S25', value=1)
    S26 = Switch(name='S26', value=1)
    S27 = Switch(name='S27', value=1)

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27]
    
    tree_list_BIN_4 = Tree.tree_list_BIN(4)

    Slist_0 = [S0, S1, S2, S3]
    Slist_1 = [S4, S5, S6, S7]
    Slist_2 = [S8, S9, S10, S11]
    Slist_3 = [S12, S13, S14, S15]
    Slist_4 = [S16, S17, S18, S19]
    Slist_5 = [S20, S21, S22, S23]
    Slist_6 = [S24, S25, S26, S27]
    Slist = Slist_0 + Slist_1 + Slist_2 + Slist_3 + Slist_4 + Slist_5 + Slist_6
    V0 = Tree(tree_list=tree_list_BIN_4,
          name='V0',
          switches=Slist_0)
    V1 = Tree(tree_list=tree_list_BIN_4,
          name='V1',
          switches=Slist_1)
    V2 = Tree(tree_list=tree_list_BIN_4,
          name='V2',
          switches=Slist_2)
    V3 = Tree(tree_list=tree_list_BIN_4,
          name='V3',
          switches=Slist_3)
    V4 = Tree(tree_list=tree_list_BIN_4,
          name='V4',
          switches=Slist_4)
    V5 = Tree(tree_list=tree_list_BIN_4,
          name='V5',
          switches=Slist_5)
    V6 = Tree(tree_list=tree_list_BIN_4,
          name='V6',
          switches=Slist_6)

    V7 = Tree(tree_list=['AND'] + [Tree.tree_list_OR(2)]*7,
          name='V7',
          switches=[S2, S3,
                    S6, S7,
                    S10, S11,
                    S14, S15,
                    S18, S19,
                    S22, S23,
                    S26, S27])
    
    V8 = Tree(tree_list=['DIFF'] + [[None]]*6,
          name='V8',
          switches=[V1, V2, V3, V4, V5, V6])
    
    tree_list_0 = ['AND',
                   [None],
                   [None],
                   ['EQUSET',
                    ['ABS', ['SUM', Tree.tree_list_BIN(2), ['MINUS', Tree.tree_list_BIN(2)]]],
                    ['ABS', ['SUM', Tree.tree_list_BIN(2), ['MINUS', Tree.tree_list_BIN(2)]]],
                    [None],
                    [None],
                   ]]
    tree_list_1 = ['EQU', [None], [None]]
    
    SlistOR5 = [S2, S3,
                S6, S7,
                S10, S11,
                S14, S15,
                S18, S19,
                S22, S23,
                S26, S27]

    T0 = Tree(tree_list=tree_list_0,
                name='T0',
                switches=[V7, V8,
                          S0, S1,
                          S4, S5,
                          S2, S3,
                          S6, S7,
                          1, 2
                          ])
    T1 = Tree(tree_list=tree_list_1,
                name='T1',
                switches=[V0, V1])
    T2 = Tree(tree_list=tree_list_0,
                name='T2',
                switches=[V7, V8,
                          S0, S1,
                          S8, S9,
                          S2, S3,
                          S10, S11,
                          1, 2
                          ])
    T3 = Tree(tree_list=tree_list_1,
                name='T3',
                switches=[V0, V2])
    T4 = Tree(tree_list=tree_list_0,
                name='T4',
                switches=[V7, V8,
                          S0, S1,
                          S12, S13,
                          S2, S3,
                          S14, S15,
                          1, 2
                          ])
    T5 = Tree(tree_list=tree_list_1,
                name='T5',
                switches=[V0, V3])
    T6 = Tree(tree_list=tree_list_0,
                name='T6',
                switches=[V7, V8,
                          S0, S1,
                          S16, S17,
                          S2, S3,
                          S18, S19,
                          1, 2
                          ])
    T7 = Tree(tree_list=tree_list_1,
                name='T7',
                switches=[V0, V4])
    T8 = Tree(tree_list=tree_list_0,
                name='T8',
                switches=[V7, V8,
                          S0, S1,
                          S20, S21,
                          S2, S3,
                          S22, S23,
                          1, 2
                          ])
    T9 = Tree(tree_list=tree_list_1,
                name='T9',
                switches=[V0, V5])
    T10 = Tree(tree_list=tree_list_0,
                name='T10',
                switches=[V7, V8,
                          S0, S1,
                          S24, S25,
                          S2, S3,
                          S26, S27,
                          1, 2
                          ])
    T11 = Tree(tree_list=tree_list_1,
                name='T11',
                switches=[V0, V6])
    T12 = Tree(tree_list=['AND',
                          Tree.tree_list_NOR(4),
                          Tree.tree_list_AND(6),
                          Tree.tree_list_NOR(6),
                          ]+[Tree.tree_list_OR(2)]*6,
                name='T12',
                switches=[S0, S1, S2, S3,
                          S4, S5,
                          S8, S9,
                          S12, S13,
                          S16, S17,
                          S20, S21,
                          S24, S25,
                          S6, S7,
                          S10, S11,
                          S14, S15,
                          S18, S19,
                          S22, S23,
                          S26, S27])
    
    dx = 1
    dy = 1
    ex = 4
    ey = 1

    R0 = Room(name='R0',
              position=[4*dx, 4*dy, ex, ey],
              switches_list=Slist_0)
    if fast_solution_finding:
        room_of_possible_switches = R0
    else:
        room_of_possible_switches = None
    R1 = Room(name='R1',
              position=[0*dx, 2*dy, ex, ey],
              switches_list=Slist_1,
              room_of_possible_switches=room_of_possible_switches)
    R5 = Room(name='R5',
              position=[4*dx, 1*dy, ex, ey],
              switches_list=Slist_2,
              room_of_possible_switches=room_of_possible_switches)
    R9 = Room(name='R9',
                position=[8*dx, 2*dy, ex, ey],
                switches_list=Slist_3,
                room_of_possible_switches=room_of_possible_switches)
    R13 = Room(name='R13',
                position=[0*dx, 6*dy, ex, ey],
                switches_list=Slist_4,
                room_of_possible_switches=room_of_possible_switches)
    R17 = Room(name='R17',
                position=[4*dx, 7*dy, ex, ey],
                switches_list=Slist_5,
                room_of_possible_switches=room_of_possible_switches)
    R21 = Room(name='R21',
                position=[8*dx, 6*dy, ex, ey],
                switches_list=Slist_6,
                room_of_possible_switches=room_of_possible_switches)
    RE = Room(name='RE',
              position=[10, 4, 2, ey],
              is_exit=True)
    
    coorda = [1.5/4, 1/2]
    coordb = [2.5/4, 1/2]

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=coorda,
                relative_arrival_coordinates=coorda,)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R0,
                relative_departure_coordinates=coordb,
                relative_arrival_coordinates=coordb,)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=R5,
                relative_departure_coordinates=coorda,
                relative_arrival_coordinates=coorda,)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R5,
                room_arrival=R0,
                relative_departure_coordinates=coordb,
                relative_arrival_coordinates=coordb,)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R0,
                room_arrival=R9,
                relative_departure_coordinates=coorda,
                relative_arrival_coordinates=coorda,)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R9,
                room_arrival=R0,
                relative_departure_coordinates=coordb,
                relative_arrival_coordinates=coordb,)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=R13,
                relative_departure_coordinates=coorda,
                relative_arrival_coordinates=coorda,)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R13,
                room_arrival=R0,
                relative_departure_coordinates=coordb,
                relative_arrival_coordinates=coordb,)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R0,
                room_arrival=R17,
                relative_departure_coordinates=coorda,
                relative_arrival_coordinates=coorda,)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R17,
                room_arrival=R0,
                relative_departure_coordinates=coordb,
                relative_arrival_coordinates=coordb,)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R0,
                room_arrival=R21,
                relative_departure_coordinates=coorda,
                relative_arrival_coordinates=coorda,)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R21,
                room_arrival=R0,
                relative_departure_coordinates=coordb,
                relative_arrival_coordinates=coordb,)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 1/2],)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0,
                             R1,
                             R5,
                             R9,
                             R13,
                             R17,
                             R21,
                             RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12],
                 fastest_solution="S1 S2 D10 S24 S27 D11 S3 D6 S16 S19 D7 S0 S1 D0 S4 S7 D1 S3 D6 S16 S17 S19 D7 S0 S1 S3 D2 S9 S10 D3 S1 S2 D10 S25 S26 S27 D11 S1 S2 S3 D0 S4 S5 S7 D1 S0 S3 D0 S4 S7 D1 S1 D8 S21 S22 D9 S0 S3 D8 S20 S23 D9 S0 S1 S2 S3 D6 S17 S18 S19 D7 S1 S2 D6 S17 S18 D7 S3 D2 S8 S9 S11 D3 S1 S2 S3 D2 S9 S10 S11 D3 S1 S2 S3 D4 S12 S15 D5 S0 S1 S3 D4 S12 S13 S15 D5 S0 S3 D4 S12 S15 D5 S0 S1 D6 S16 S19 D7 S2 D12",
                 level_color=get_color(),
                 name="Second Guarini's puzzle",
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    lcolor =  Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.5)
    lcolor.contour_color = Color.color_hls(hu=0.1, sa=1, li=0.85)
    return lcolor