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

    T0 = Tree(tree_list=Tree.tree_list_XOR(2),
                name='T0',
                switches=[S0, S1])
    T1 = Tree(tree_list=Tree.tree_list_XNOR(2),
                name='T1',
                switches=[S0, S1])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[S0])
    T3 = Tree(tree_list=Tree.tree_list_NOT,
                name='T3',
                switches=[S0])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[S0])
    T5 = Tree(tree_list=Tree.tree_list_NOT,
                name='T5',
                switches=[S0])
    T6 = Tree(tree_list=Tree.tree_list_AND(6),
                name='T6',
                switches=[S0, S1, S2, S3, S4, S5])
    
    dx = 1
    dy = 1
    ex = 1
    ey = 1

    R0 = Room(name='R0',
                position=[2.5*dx, 4*dy, 2*ex, ey],
                switches_list=[S0, S1])
    R1 = Room(name='R1',
                position=[0.5*dx, 2*dy, ex, 2*ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[5.5*dx, 2*dy, ex, 2*ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[-0.5*dx, 0*dy, ex, ey],
                switches_list=[S2])
    R4 = Room(name='R4',
                position=[1.5*dx, 0*dy, ex, ey],
                switches_list=[S3])
    R5 = Room(name='R5',
                position=[4.5*dx, 0*dy, ex, ey],
                switches_list=[S4])
    R6 = Room(name='R6',
                position=[6.5*dx, 0*dy, ex, ey],
                switches_list=[S5])
    RE = Room(name='RE',
              position=[3*dx, 2*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1/4, 1/2],
                relative_arrival_coordinates=[1/2, 3/4])
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R2,
                relative_departure_coordinates=[3/4, 1/2],
                relative_arrival_coordinates=[1/2, 3/4])
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R3,
                relative_departure_coordinates=[1/2, 1/4])
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R4,
                relative_departure_coordinates=[1/2, 1/4])
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R5,
                relative_departure_coordinates=[1/2, 1/4])
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R2,
                room_arrival=R6,
                relative_departure_coordinates=[1/2, 1/4])
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=RE)
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0.1, sa=0.5, li=0.7)
    lcolor.room_color = Color.BRIGHT_GREEN
    lcolor.surrounding_color = Color.IVORY

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution="D1 D5 S5 D5 D1 S0 D0 D2 S2 D2 D0 S0 S1 D0 D3 S3 D3 D0 S0 D1 D4 S4 D4 D1 D6",
                 level_color=lcolor,
                 name='Orchard',
                 keep_proportions=False,
                 door_window_size=350)
    
    return level