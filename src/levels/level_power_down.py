from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def f(): 

    S0 = Switch(name='S0', value=1)
    S1 = Switch(name='S1', value=0)
    S2 = Switch(name='S2', value=1)
    S3 = Switch(name='S3', value=0)
    S4 = Switch(name='S4', value=1)

    Slist = [S0, S1, S2, S3, S4]

    T0 = Tree(tree_list=Tree.tree_list_NAND(2),
                name='T0',
                switches=[S0, S2])
    T1 = Tree(tree_list=Tree.tree_list_NAND(2),
                name='T1',
                switches=[S1, S2])
    T2 = Tree(tree_list=Tree.tree_list_NAND(2),
                name='T2',
                switches=[S2, S4])
    T3 = Tree(tree_list=Tree.tree_list_NAND(2),
                name='T3',
                switches=[S3, S4])
    T4 = Tree(tree_list=Tree.tree_list_AND(5),
                name='T4',
                switches=Slist)

    R0 = Room(name='R0',
                position=[0, 3, 1, 1],
                switches_list=[S0])
    R1 = Room(name='R1',
                position=[0, 1, 1, 1],
                switches_list=[S1])
    R2 = Room(name='R2',
                position=[2, 2, 1, 1],
                switches_list=[S2])
    R3 = Room(name='R3',
                position=[2, 0, 1, 1],
                switches_list=[S3])
    R4 = Room(name='R4',
                position=[4, 1, 1, 1],
                switches_list=[S4])
    RE = Room(name='RE',
              position=[4, 3, 1, 1],
              is_exit=True)

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R2)
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R4)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4],
                 fastest_solution="S0 D0 S2 D0 S0 D0 D1 S1 D1 D2 S4 D2 S2 D2 D3 S3 D3 S4 D4",
                 level_color=Levels_colors_list.FROM_HUE(hu=0.16, sa=0.4, li=0.5),
                 name='Power down',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level