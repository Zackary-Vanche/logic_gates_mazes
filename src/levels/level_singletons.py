from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_singletons(): 

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
    
    tree_list_SUM_MOD = ['EQU', ['MOD', Tree.tree_list_SUM(3), [None]], [None]]

    T0 = Tree(tree_list=['AND'] + [tree_list_SUM_MOD]*2,
                name='T0',
                switches=[S2, S6, S7, 2, 0,
                          S2, S10, S11, 2, 0])
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
    T9 = Tree(tree_list=[None],
                name='T9',
                switches=[S8])
    T10 = Tree(tree_list=[None],
                name='T10',
                switches=[S9])
    T11 = Tree(tree_list=[None],
                name='T11',
                switches=[S10])
    T12 = Tree(tree_list=[None],
                name='T12',
                switches=[S11])
    T13 = Tree(tree_list=[None],
                name='T13',
                switches=[S12])
    T14 = Tree(tree_list=['INFOREQU',
                          Tree.tree_list_SUM(8),
                          [None]],
                name='T14',
                switches=[S0, S1, S3, S4, S5, S8, S9, S12, 2])
    
    ex = 1
    ey = 1
    dx = 1
    dy = 1
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12]

    R0 = Room(name='R0',
                position=[0*dx, 7*dy, 7*ex , ex/2],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[2*dx, 5*dy, ex ,ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[4*dx, 5*dy, ex ,ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[0*dx, 4*dy, ex ,ey],
                switches_list=[])
    R4 = Room(name='R4',
                position=[6*dx, 4*dy, ex ,ey],
                switches_list=[])
    R5 = Room(name='R5',
                position=[2*dx, 3*dy, ex ,ey],
                switches_list=[])
    R6 = Room(name='R6',
                position=[4*dx, 3*dy, ex ,ey],
                switches_list=[])
    R7 = Room(name='R7',
                position=[0*dx, 2*dy, ex ,ey],
                switches_list=[])
    R8 = Room(name='R8',
                position=[6*dx, 2*dy, ex ,ey],
                switches_list=[])
    R9 = Room(name='R9',
                position=[2*dx, 1*dy, ex ,ey],
                switches_list=[])
    R10 = Room(name='R10',
                position=[4*dx, 1*dy, ex ,ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[3*dx, -1*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R3,
                room_arrival=R4)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R5,
                room_arrival=R6)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R7,
                room_arrival=R8)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R9,
                room_arrival=R10)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R1,
                room_arrival=R3)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R3,
                room_arrival=R5)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R5,
                room_arrival=R7)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R7,
                room_arrival=R9)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R2,
                room_arrival=R4)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R4,
                room_arrival=R6)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R6,
                room_arrival=R8)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R8,
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
                 fastest_solution="S2 S5 S6 S11 S12 D0 D6 D7 D3 D12 D13 D14",
                 level_color=Levels_colors_list.FROM_HUE(hu=0, sa=0.1, li=0.5),
                 name='singletons',
                 keep_proportions=True,
                 door_window_size=480)
    
    return level