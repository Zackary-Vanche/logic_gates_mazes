from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_hut(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')

    Slist = [S0, S1, S2, S3, S4]
    
    tl = Tree.tree_list_XOR(2)

    T0 = Tree(tree_list=tl,
                name='T0',
                switches=[S0, S1])
    T1 = Tree(tree_list=tl,
                name='T1',
                switches=[S0, S2])
    T2 = Tree(tree_list=tl,
                name='T2',
                switches=[S1, S3])
    T3 = Tree(tree_list=tl,
                name='T3',
                switches=[S2, S3])
    T4 = Tree(tree_list=tl,
                name='T4',
                switches=[S2, S4])
    T5 = Tree(tree_list=tl,
                name='T5',
                switches=[S3, S4])
    T6 = Tree(tree_list=Tree.tree_list_from_str('TTTFF'),
                name='T6',
                switches=Slist)

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 3*dy, ex, ey],
                switches_list=[S0])
    R1 = Room(name='R1',
                position=[3*dx, 3*dy, ex, ey],
                switches_list=[S1])
    R2 = Room(name='R2',
                position=[0.5*dx, 2*dy, ex, ey],
                switches_list=[S2])
    R3 = Room(name='R3',
                position=[2.5*dx, 2*dy, ex, ey],
                switches_list=[S3])
    R4 = Room(name='R4',
                position=[1.5*dx, 1*dy, ex, ey],
                switches_list=[S4])
    RE = Room(name='RE',
              position=[0*dx, 0.5*dy, ex, ey],
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
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R3)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R3)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R4)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R4)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution="S0 D1 S2 D3 S3 D2 D0 S0 D1 D4 D5 D2 S1 D0 D1 D4 D5 S3 D2 D0 S0 D6",
                 level_color=Levels_colors_list.FROM_HUE(hu=0.05, sa=0.2, li=0.5),
                 name='Hut',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level