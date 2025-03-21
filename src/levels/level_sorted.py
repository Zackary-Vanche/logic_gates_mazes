from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
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
    S14 = Switch(name='S14')
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(3),
                name='V0',
                switches=[S0, S1, S2])
    V1 = Tree(tree_list=Tree.tree_list_BIN(3),
                name='V1',
                switches=[S3, S4, S5])
    V2 = Tree(tree_list=Tree.tree_list_BIN(3),
                name='V2',
                switches=[S6, S7, S8])
    V3 = Tree(tree_list=Tree.tree_list_BIN(3),
                name='V3',
                switches=[S9, S10, S11])
    V4 = Tree(tree_list=Tree.tree_list_BIN(3),
                name='V4',
                switches=[S12, S13, S14])
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14]
    Vlist = [V0, V1, V2, V3, V4]

    R0 = Room(name='R0',
                position=[0, 0, 2, 4],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14])
    R1 = Room(name='R1',
                position=[3, 0, 1, 1],
                switches_list=[])
    RE = Room(name='RE',
              position=[3, 2, 1, 1],
              is_exit=True)
    
    i_list = [i for i in range(2**3)]
    rd_shuffle(Slist)
    rd_shuffle(i_list)
    
    T0 = Tree(tree_list=['EQUSET'] + [[None]]*5 + [[None]]*5,
                name='T0',
                switches=Vlist + i_list)
    T1 = Tree(tree_list=['INF'] + [[None]]*5,
                name='T1',
                switches=Vlist)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[3/4, 1/8])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, RE],
                 doors_list=[D0, D1],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Sorted',
                 keep_proportions=True,
                 door_window_size=500,
                 random=True)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.75, sa=0.5, li=0.3)