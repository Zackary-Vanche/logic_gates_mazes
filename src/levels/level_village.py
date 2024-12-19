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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7]

    tree_list_XOR_2 = Tree.tree_list_XOR(2)
    T0 = Tree(tree_list=tree_list_XOR_2,
                        name='T0',
                        switches=[S0, S1])
    T1 = Tree(tree_list=tree_list_XOR_2,
                        name='T1',
                        switches=[S0, S3])
    T2 = Tree(tree_list=tree_list_XOR_2,
                        name='T2',
                        switches=[S1, S2])
    T3 = Tree(tree_list=tree_list_XOR_2,
                        name='T3',
                        switches=[S1, S4])
    T4 = Tree(tree_list=tree_list_XOR_2,
                        name='T4',
                        switches=[S2, S5])
    T5 = Tree(tree_list=tree_list_XOR_2,
                        name='T5',
                        switches=[S3, S4])
    T6 = Tree(tree_list=tree_list_XOR_2,
                        name='T6',
                        switches=[S3, S6])
    T7 = Tree(tree_list=tree_list_XOR_2,
                        name='T7',
                        switches=[S4, S5])
    T8 = Tree(tree_list=tree_list_XOR_2,
                        name='T8',
                        switches=[S4, S6])
    T9 = Tree(tree_list=tree_list_XOR_2,
                        name='T9',
                        switches=[S4, S7])
    T10 = Tree(tree_list=tree_list_XOR_2,
                        name='T10',
                        switches=[S5, S7])
    T11 = Tree(tree_list=Tree.tree_list_from_str('FTFFFTFT'),
                name='T11',
                switches=Slist)

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S0])
    R1 = Room(name='R1',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S1])
    R2 = Room(name='R2',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S2])
    R3 = Room(name='R3',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S3])
    R4 = Room(name='R4',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S4])
    R5 = Room(name='R5',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S5])
    R6 = Room(name='R6',
                position=[0.5*dx, 0*dy, ex, ey],
                switches_list=[S6])
    R7 = Room(name='R7',
                position=[1.5*dx, 0*dy, ex, ey],
                switches_list=[S7])
    RE = Room(name='RE',
              position=[-0.5*dx, 0*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R3)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R2)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R4)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R5)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R4)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R3,
                room_arrival=R6)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R4,
                room_arrival=R5)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R4,
                room_arrival=R6)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R4,
                room_arrival=R7)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R5,
                room_arrival=R7)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R3,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11],
                 fastest_solution="S0 D0 S1 D3 S4 D7 S5 D10 D9 D5 D1 S0 D0 D2 D4 D10 D9 D5 S3 D6 D8 S4 D7 D10 S7 D9 D5 S3 D11",
                 level_color=Levels_colors_list.FROM_HUE(hu=0.18, sa=0.3, li=0.4),
                 name='Village',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level
