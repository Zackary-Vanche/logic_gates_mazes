from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle

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
    T0 = Tree(tree_list=["INFOREQU", Tree.tree_list_SUM(9), [None]],
                name='T0',
                switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, 5])
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
    T10 = Tree(tree_list=Tree.tree_list_AND(5),
                name='T10',
                switches=[S9, S10, S11, S12, S13])

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[-1*dx-ex, 0*dy, 3*dx+3*ex, ey],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8])
    R1 = Room(name='R1',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S9])
    R2 = Room(name='R2',
                position=[-1*dx, 2*dy, ex, ey],
                switches_list=[S10])
    R3 = Room(name='R3',
                position=[0*dx, 3*dy, ex, ey],
                switches_list=[S11])
    R4 = Room(name='R4',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S12])
    R5 = Room(name='R5',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S13])
    RE = Room(name='RE',
              position=[-1*dx, 1*dy, ex, ey],
              is_exit=True)
    
    Rlist = [R2, R3, R4, R5]
    Rpos_list = [R.position for R in Rlist]
    rd_shuffle(Rpos_list)
    for i, R in enumerate(Rlist):
        R.position = Rpos_list[i]

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R3)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R4)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R3,
                room_arrival=R4)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R5)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R4,
                room_arrival=R1)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R4,
                room_arrival=R5)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R5,
                room_arrival=R1)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R5,
                room_arrival=R2)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R1,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10],
                 fastest_solution="S0 S2 S4 S5 S8 D0 S9 D1 S11 D5 S13 D9 S10 D3 S12 D6 D10",
                 level_color=get_color(),
                 name='Hamiltonian path',
                 keep_proportions=True,
                 door_window_size=330)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.95, sa=0.2, li=0.25)
    lcolor.background_color, lcolor.room_color = lcolor.room_color, lcolor.background_color
    return lcolor