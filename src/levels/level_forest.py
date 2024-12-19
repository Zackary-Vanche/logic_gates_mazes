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

    Slist = [S0, S1, S2]

    T0 = Tree(tree_list=Tree.tree_list_NOR(3),
                name='T0',
                switches=Slist)
    T1 = Tree(tree_list=Tree.tree_list_XOR(3),
                name='T1',
                switches=Slist)
    T2 = Tree(tree_list=['XOR'] + [Tree.tree_list_NOT]*3,
                name='T2',
                switches=Slist)
    T3 = Tree(tree_list=Tree.tree_list_AND(3),
                name='T3',
                switches=Slist)
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[S0])
    T5 = Tree(tree_list=[None],
                name='T5',
                switches=[S1])
    T6 = Tree(tree_list=[None],
                name='T6',
                switches=[S2])
    T7 = Tree(tree_list=Tree.tree_list_NOT,
                name='T7',
                switches=[S0])
    T8 = Tree(tree_list=Tree.tree_list_NOT,
                name='T8',
                switches=[S1])
    T9 = Tree(tree_list=Tree.tree_list_NOT,
                name='T9',
                switches=[S2])
    T10 = Tree(tree_list=Tree.tree_list_AND(11),
                name='T10',
                switches=[S0, S1, S2,
                          S3, S4,
                          S5, S6, S7, S8, S9, S10])

    dx = 1
    dy = 1.5
    ex = 1
    ey = 1

    R0 = Room(name='R0',
                position=[4*dx, 4*dy, 3*ex, ey],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S3])
    R2 = Room(name='R2',
                position=[3*dx, 2*dy, ex, ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[7*dx, 2*dy, ex, ey],
                switches_list=[])
    R4 = Room(name='R4',
                position=[9*dx, 2*dy, ex, ey],
                switches_list=[S4])
    R5 = Room(name='R5',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S5])
    R6 = Room(name='R6',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[S6])
    R7 = Room(name='R7',
                position=[4*dx, 0*dy, ex, ey],
                switches_list=[S7])
    R8 = Room(name='R8',
                position=[6*dx, 0*dy, ex, ey],
                switches_list=[S8])
    R9 = Room(name='R9',
                position=[8*dx, 0*dy, ex, ey],
                switches_list=[S9])
    R10 = Room(name='R10',
                position=[10*dx, 0*dy, ex, ey],
                switches_list=[S10])
    RE = Room(name='RE',
              position=[5*dx, 2*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[0.5/3, 1/2])
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R2,
                relative_departure_coordinates=[0.5/3, 1/2])
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=R3,
                relative_departure_coordinates=[2.5/3, 1/2])
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R0,
                room_arrival=R4,
                relative_departure_coordinates=[2.5/3, 1/2])
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R5)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R2,
                room_arrival=R6)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R2,
                room_arrival=R7)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R3,
                room_arrival=R8)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R3,
                room_arrival=R9)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R3,
                room_arrival=R10)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R0,
                room_arrival=RE)
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0.25, sa=0.2, li=0.5)
    lcolor.background_color = Color.DARK_BROWN

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10],
                 fastest_solution="D0 S3 D0 S0 D1 D4 S5 D4 D1 S1 D2 D9 S10 D9 D2 S0 D1 D5 S6 D5 D1 S2 D2 D7 S8 D7 D2 S1 D1 D6 S7 D6 D1 S0 D2 D8 S9 D8 D2 S1 D3 S4 D3 D10",
                 level_color=lcolor,
                 name='Forest',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level