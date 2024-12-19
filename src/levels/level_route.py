from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
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
    
    tx = Tree.tree_list_XOR(2)

    V0 = Tree(tree_list=tx,
          name='V0',
          switches=[S0, S1])
    V1 = Tree(tree_list=tx,
          name='V1',
          switches=[S0, S2])
    V2 = Tree(tree_list=tx,
          name='V2',
          switches=[S1, S3])
    V3 = Tree(tree_list=tx,
          name='V3',
          switches=[S2, S3])
    
    tree_list_1 = ['AND',
                   ['EQU', Tree.tree_list_SUM(2), [None]],
                   ['IN', Tree.tree_list_SUM(3), [None], [None]],
                   ['IN', Tree.tree_list_SUM(2), [None], [None]],
                   ['IN', Tree.tree_list_SUM(4), [None], [None]],
                   ['IN', Tree.tree_list_SUM(2), [None], [None]],
                   ['IN', Tree.tree_list_SUM(3), [None], [None]],
                   ['EQU', Tree.tree_list_SUM(2), [None]],
                   ['SUP', Tree.tree_list_SUM(6), [None]],]

    T0 = Tree(tree_list=['INF', Tree.tree_list_BIN(2), Tree.tree_list_BIN(2)],
                name='T0',
                switches=[S0, S1, S2, S3])
    T1 = Tree(tree_list=tree_list_1,
                name='T1',
                switches=[S4, S5, 2,
                          S4, S6, V0, 0, 2,
                          S6, S8, 0, 2,
                          V0, V1, V2, V3, 0, 2,
                          S7, S9, 0, 2,
                          S9, S11, V3, 0, 2,
                          S10, S11, 2,
                          S5, S7, V1, S8, S10, V2, 5,
                          ],
                cut_expression_depth_1=True)
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[S4])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[S5])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[S6])
    T5 = Tree(tree_list=[None],
                name='T5',
                switches=[V0])
    T6 = Tree(tree_list=[None],
                name='T6',
                switches=[V1])
    T7 = Tree(tree_list=[None],
                name='T7',
                switches=[S7])
    T8 = Tree(tree_list=[None],
                name='T8',
                switches=[S8])
    T9 = Tree(tree_list=[None],
                name='T9',
                switches=[V2])
    T10 = Tree(tree_list=[None],
                name='T10',
                switches=[V3])
    T11 = Tree(tree_list=[None],
                name='T11',
                switches=[S9])
    T12 = Tree(tree_list=[None],
                name='T12',
                switches=[S10])
    T13 = Tree(tree_list=[None],
                name='T13',
                switches=[S11])
    T14 = Tree(tree_list=[None],
                name='T14',
                switches=[1])

    dx = 1
    dy = 1
    ex = 1
    ey = 1

    R0 = Room(name='R0',
                position=[0.5*dx, 0*dy, 3.5*ex, ey],
                switches_list=[S0, S1, S2, S3])
    R1 = Room(name='R1',
                position=[0.5*dx, 2*dy, 1.5*ex, 4*dy+ey],
                switches_list=[S4, S5, S6, S7, S8, S9, S10, S11])
    R2 = Room(name='R2',
                position=[3*dx, 6*dy, ex, ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[3*dx, 4*dy, ex, ey],
                switches_list=[])
    R4 = Room(name='R4',
                position=[5*dx, 6*dy, ex, ey],
                switches_list=[])
    R5 = Room(name='R5',
                position=[3*dx, 2*dy, ex, ey],
                switches_list=[])
    R6 = Room(name='R6',
                position=[5*dx, 4*dy, ex, ey],
                switches_list=[])
    R7 = Room(name='R7',
                position=[7*dx, 6*dy, ex, ey],
                switches_list=[])
    R8 = Room(name='R8',
                position=[5*dx, 2*dy, ex, ey],
                switches_list=[])
    R9 = Room(name='R9',
                position=[7*dx, 4*dy, ex, ey],
                switches_list=[])
    R10 = Room(name='R10',
                position=[7*dx, 2*dy, ex, ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[5*dx, 0*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_arrival_coordinates=[1/2, 1/9])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=[2/3, 3.5/5])
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R4)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R3,
                room_arrival=R5)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R6)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R4,
                room_arrival=R6)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R4,
                room_arrival=R7)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R5,
                room_arrival=R8)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R6,
                room_arrival=R8)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R6,
                room_arrival=R9)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R7,
                room_arrival=R9)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R8,
                room_arrival=R10)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R9,
                room_arrival=R10)
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R10,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14],
                 fastest_solution="S2 S3 D0 S4 S5 S6 S7 S8 S9 S10 S11 D1 D2 D4 D8 D12 D14",
                 level_color=Levels_colors_list.FROM_HUE(hu=0, sa=0.3, li=0.5),
                 name='Route',
                 keep_proportions=True,
                 door_window_size=315)
    
    return level