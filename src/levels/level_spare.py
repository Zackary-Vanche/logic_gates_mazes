from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def f():

    v = 1
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3', value=v)
    S4 = Switch(name='S4')
    S5 = Switch(name='S5', value=v)
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    S12 = Switch(name='S12', value=v)
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')

    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4]
    Slist_2 = [S5, S6]
    Slist_3 = [S7, S8]
    Slist_4 = [S9, S10]
    Slist_5 = [S11, S12]
    Slist_6 = [S13, S14]
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14]
    
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

    tree_list_0 = ['AND',
                   ['OR'] + [['EQU', [None], [None]]]*2,
                   ['EQU', [None], [None]]]
    tree_list_1 = ['AND',
                   ['EQU'] + [[None]]*2,
                   ['EQU', [None], [None]]]
    tree_list_2 = ['AND',
                   ['EQUSET'] + [[None]]*6 + [[None]]*6,
                   ['EQU', [None], [None]]]
    Slist2 = [V1, V2, V3, V4, V5, V6, 0, 0, 0, 1, 1, 2,]

    T0 = Tree(tree_list=tree_list_0,
              name='T0',
              switches=[V1] + [0] + [V2] + [0] + [V0] + [1])
    T1 = Tree(tree_list=tree_list_1,
              name='T1',
              switches=[V1] + [V2] + [V0] + [1])
    T2 = Tree(tree_list=tree_list_2,
              name='T2',
              switches=Slist2 + [V0] + [1])

    T3 = Tree(tree_list=tree_list_0,
              name='T3',
              switches=[V2] + [0] + [V3] + [0] + [V0] + [2])
    T4 = Tree(tree_list=tree_list_1,
              name='T4',
              switches=[V2] + [V3] + [V0] + [2])
    T5 = Tree(tree_list=['AND',
                         ['EQUSET'] + [[None]]*6 + [[None]]*6,
                         ['IN', [None], [None], [None]]],
              name='T5',
              switches=Slist2 + [V0] + [2, 5])

    T6 = Tree(tree_list=tree_list_0,
              name='T6',
              switches=[V3] + [0] + [V4] + [0] + [V0] + [3])
    T7 = Tree(tree_list=tree_list_1,
              name='T7',
              switches=[V3] + [V4] + [V0] + [3])
    T8 = Tree(tree_list=tree_list_2,
              name='T8',
              switches=Slist2 + [V0] + [3])

    T9 = Tree(tree_list=tree_list_0,
              name='T9',
              switches=[V4] + [0] + [V5] + [0] + [V0] + [4])
    T10 = Tree(tree_list=tree_list_1,
              name='T10',
              switches=[V4] + [V5] + [V0] + [4])
    T11 = Tree(tree_list=tree_list_2,
              name='T11',
              switches=Slist2 + [V0] + [4])

    T12 = Tree(tree_list=tree_list_0,
               name='T12',
               switches=[V6] + [0] + [V3] + [0] + [V0] + [5])
    T13 = Tree(tree_list=tree_list_1,
               name='T13',
               switches=[V6] + [V3] + [V0] + [5])

    T14 = Tree(tree_list=Tree.tree_list_from_str('TTTFTFFFFTFTFFF'),
               name='T14',
               switches=Slist)

    ex = 0.2
    ey = 0.5
    ex0 = 0.2
    ey0 = 0.7
    ey3 = 0.45
    ex4 = 0.125
    ex6 = 0.3
    ey6 = 0.6
    exe = 0.8
    eye = 0.4
    dx = 1

    R0 = Room(name='R0',
              position = [dx+(ex-ex0)/2, 1+(ey-ey0)/2, ex0, ey0],
              switches_list = Slist_0)
    R1 = Room(name='R1',
              position = [0, 0, ex, ey],
              switches_list = Slist_1)
    R2 = Room(name='R2',
              position = [ex-ex4, 1, ex4, ey],
              switches_list = Slist_2)
    R3 = Room(name='R3',
              position = [0, 2, ex, ey3],
              switches_list = Slist_3)
    R4 = Room(name='R4',
              position = [2*dx-ex+ex4, 1, ex4, ey],
              switches_list = Slist_4)
    R5 = Room(name='R5',
              position = [2*dx, ey-ey3, ex, ey3],
              switches_list = Slist_5)
    R6 = Room(name='R6',
              position = [2*dx+(ex-ex6), 2+(ex-ex6), ex6, ey6],
              switches_list = Slist_6)
    RE = Room(name='RE',
              position=[dx+(ex-exe)/2, 0, exe, eye],
              is_exit=True)   # E pour exit ou end

    epsilon = 1/6

    D0 = Door(two_way=False,
                tree=T0,
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=False,
                tree=T1,
                room_departure=R1,
                room_arrival=R2,
              relative_departure_coordinates=[epsilon, 1-epsilon],
              relative_arrival_coordinates=[1-epsilon, epsilon])
    D2 = Door(two_way=False,
                tree=T2,
                room_departure=R2,
                room_arrival=R0,
              relative_departure_coordinates=[1/2, 1/8],
              relative_arrival_coordinates=[1/2, 1/3])
    D3 = Door(two_way=False,
                tree=T3,
                room_departure=R0,
                room_arrival=R2,
              relative_departure_coordinates=[1/2, 1-1/3],
              relative_arrival_coordinates=[1/2, 1-1/8])
    D4 = Door(two_way=False,
                tree=T4,
                room_departure=R2,
                room_arrival=R3,
              relative_departure_coordinates=[1-epsilon, epsilon],
              relative_arrival_coordinates=[epsilon, 1-epsilon])
    D5 = Door(two_way=False,
                tree=T5,
                room_departure=R3,
                room_arrival=R0,
              relative_position=0.4)
    D6 = Door(two_way=False,
                tree=T6,
                room_departure=R0,
                room_arrival=R3,
              relative_position=0.4)
    D7 = Door(two_way=False,
                tree=T7,
                room_departure=R3,
                room_arrival=R4,
              relative_departure_coordinates=[1, 1/4],
              relative_arrival_coordinates=[0, 1])
    D8 = Door(two_way=False,
                tree=T8,
                room_departure=R4,
                room_arrival=R0,
              relative_departure_coordinates=[1/2, 1-1/8],
              relative_arrival_coordinates=[1/2, 1-1/3])
    D9 = Door(two_way=False,
                tree=T9,
                room_departure=R0,
                room_arrival=R4,
              relative_departure_coordinates=[1/2, 1/3],
              relative_arrival_coordinates=[1/2, 1/8])
    D10 = Door(two_way=False,
                tree=T10,
                room_departure=R4,
                room_arrival=R5,
              relative_departure_coordinates=[epsilon, epsilon],
              relative_arrival_coordinates=[1-epsilon, 1-epsilon])
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R5,
               room_arrival=R0)
    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R0,
               room_arrival=R6,
               relative_position=0.4)
    D13 = Door(two_way=False,
               tree=T13,
               room_departure=R6,
               room_arrival=R3)
    D14 = Door(two_way=False,
               tree=T14,
               room_departure=R0,
               room_arrival=RE,
               relative_departure_coordinates=[1/2, 0],
               relative_arrival_coordinates=[1/2, 1])

    lcolor = Levels_colors_list.FROM_HUE(hu=0.15, sa=1, li=0.4)
    lcolor.inside_room_color = Color.BLACK_RED
    lcolor.background_color = Color.ORANGE
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14],
                 fastest_solution='S2 D9 S10 D10 S12 D11 S0 S1 S2 D6 S8 D7 S10 D8 S1 S2 D12 S14 D13 S8 D5 S0 S1 S2 D3 S5 D4 S7 D5 S0 D6 S7 D7 S9 D8 S1 D0 S3 D1 S5 D2 S0 S1 D3 S5 D4 S7 D5 S1 S2 D9 S9 D10 S11 D11 S0 S1 S2 D6 S7 D7 S9 D8 S1 S2 D12 S14 D13 S8 D5 S0 S1 S2 D3 S6 D4 S8 D5 S0 S1 D0 S4 D1 S6 D2 S1 S2 D14',
                 level_color=lcolor,
                 name='Spare',
                 door_window_size=400,
                 keep_proportions=True,
                 y_separation=40,
                 border=40)

    return level