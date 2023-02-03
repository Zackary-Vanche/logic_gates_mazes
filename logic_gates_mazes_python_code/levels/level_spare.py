from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_spare():

    v = 1

    S0 = Switch(name='S0', value=v)
    S1 = Switch(name='S1')
    S2 = Switch(name='S2', value=v)
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7', value=v)
    S8 = Switch(name='S8')
    S9 = Switch(name='S9', value=v)
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11]

    T0 = Tree(tree_list=[None],
              empty=True,
              name='T0',
              switches = [1])
    T1 = Tree(tree_list=[None],
              empty=True,
              name='T1',
              switches = [1])
    T2 = Tree(tree_list=[None],
              empty=True,
              name='T2',
              switches = [1])
    T3 = Tree(tree_list=[None],
              empty=True,
              name='T3',
              switches = [1])
    T4 = Tree(tree_list=[None],
              empty=True,
              name='T4',
              switches = [1])
    T5 = Tree(tree_list=[None],
              empty=True,
              name='T5',
              switches = [1])
    T6 = Tree(tree_list=[None],
              empty=True,
              name='T6',
              switches = [1])
    T7 = Tree(tree_list=[None],
              empty=True,
              name='T7',
              switches = [1])
    T8 = Tree(tree_list=[None],
              empty=True,
              name='T8',
              switches = [1])
    T9 = Tree(tree_list=[None],
              empty=True,
              name='T9',
              switches = [1])
    T10 = Tree(tree_list=[None],
              empty=True,
              name='T10',
              switches = [1])
    T11 = Tree(tree_list=[None],
               empty=True,
               name='T11',
               switches=[1])
    T12 = Tree(tree_list=[None],
               empty=True,
               name='T12',
               switches=[1])
    T13 = Tree(tree_list=[None],
               empty=True,
               name='T13',
               switches=[1])
    T14 = Tree(tree_list=['EQU', Tree.tree_list_BIN(12), Tree.tree_list_BIN(12)],
               empty=True,
               name='T14',
               switches=Slist + [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0])

    ex = 0.15
    ey = 0.5
    ex0 = 0.1
    ey0 = 0.4
    ey3 = 0.45
    ex4 = 0.125
    ex6 = ex + 0.2
    ey6 = ey + 0.2
    exe = 0.6
    eye = 0.6
    dx = 0.4

    R0 = Room(name='R0',
              position = [dx+(ex-ex0)/2, 1+(ey-ey0)/2, ex0, ey0],
              switches_list = [])
    R1 = Room(name='R1',
              position = [0, 0, ex, ey],
              switches_list = [S0, S1])
    R2 = Room(name='R2',
              position = [ex-ex4, 1, ex4, ey],
              switches_list = [S2, S3])
    R3 = Room(name='R3',
              position = [0, 2, ex, ey3],
              switches_list = [S4, S5])
    R4 = Room(name='R4',
              position = [2*dx-ex+ex4, 1, ex4, ey],
              switches_list = [S6, S7])
    R5 = Room(name='R5',
              position = [2*dx, ey-ey3, ex, ey3],
              switches_list = [S8, S9])
    R6 = Room(name='R6',
              position = [2*dx+(ex-ex6), 2+(ex-ex6), ex6, ey6],
              switches_list = [S10, S11])
    RE = Room(name='RE',
              position=[dx+(ex-exe)/2, 0, exe, eye],
              is_exit=True)   # E pour exit ou end

    rp = 0.375

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
               room_departure=R3,
               room_arrival=R6)
    D13 = Door(two_way=False,
               tree=T13,
               room_departure=R6,
               room_arrival=R0,
               relative_position=0.55)
    D14 = Door(two_way=False,
               tree=T14,
               room_departure=R0,
               room_arrival=RE)

    rp = 1/2


    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0.15, sa=1, li=0.9),
                 name='Spare',
                 door_window_size=1400,
                 keep_proportions=True,
                 y_separation=40,
                 border=40)

    return level