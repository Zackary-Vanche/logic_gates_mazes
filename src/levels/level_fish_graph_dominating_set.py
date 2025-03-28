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
    
    tree_list = Tree.tree_list_OR(2)
    
    T0 = Tree(tree_list=["INFOREQU", Tree.tree_list_SUM(6), [None]],
                name='T0',
                switches=[S0, S1, S2, S3, S4, S5, 2])
    T1 = Tree(tree_list=tree_list,
                name='T1',
                switches=[S0, S1])
    T2 = Tree(tree_list=tree_list,
                name='T2',
                switches=[S1, S2])
    T3 = Tree(tree_list=tree_list,
                name='T3',
                switches=[S2, S3])
    T4 = Tree(tree_list=tree_list,
                name='T4',
                switches=[S3, S0])
    T5 = Tree(tree_list=tree_list,
                name='T5',
                switches=[S0, S4])
    T6 = Tree(tree_list=tree_list,
                name='T6',
                switches=[S4, S5])
    T7 = Tree(tree_list=tree_list,
                name='T7',
                switches=[S5, S0])
    T8 = Tree(tree_list=Tree.tree_list_AND(6),
                name='T8',
                switches=[S6, S7, S8, S9, S10, S11])

    dx = 1.5
    dy = 1
    ex = 1
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 3*dy, 3*dx+ex, ey],
                switches_list=[S0, S1, S2, S3, S4, S5])
    R1 = Room(name='R1',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S6])
    R2 = Room(name='R2',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S7])
    R3 = Room(name='R3',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S8])
    R4 = Room(name='R4',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S9])
    R5 = Room(name='R5',
                position=[3*dx, 2*dy, ex, ey],
                switches_list=[S10])
    R6 = Room(name='R6',
                position=[3*dx, 0*dy, ex, ey],
                switches_list=[S11])
    RE = Room(name='RE',
              position=[0*dx, -1*dy, 3*dx+ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R5)
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R1)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R1,
                room_arrival=R5)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R5,
                room_arrival=R6)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R6,
                room_arrival=R1)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R6,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8],
                 fastest_solution="S0 S2 D0 S10 D5 S6 D1 S7 D2 S8 D3 S9 D4 D7 S11 D8",
                 level_color=get_color(),
                 name='Fish graph dominating set',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

get_color = lambda : Levels_colors_list.opposite_hues(1)