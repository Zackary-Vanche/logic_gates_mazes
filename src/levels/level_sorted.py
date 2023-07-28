from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle

def level_sorted(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7]

    R0 = Room(name='R0',
                position=[0, 0, 2, 4],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7])
    R1 = Room(name='R1',
                position=[3, 0, 1, 1],
                switches_list=[])
    RE = Room(name='RE',
              position=[3, 2, 1, 1],
              is_exit=True)
    
    rd_shuffle(Slist)
    
    T0 = Tree(tree_list=['EQUSET'] + [Tree.tree_list_BIN(2)]*4 + [[None]]*4,
                empty=True,
                name='T0',
                switches=Slist + [0, 1, 2, 3])
    T1 = Tree(tree_list=['INF'] + [Tree.tree_list_BIN(2)]*4,
                empty=True,
                name='T1',
                switches=Slist)

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
                 level_color=Levels_colors_list.FROM_HUE(hu=0.75, sa=0.5, li=0.4),
                 name='Sorted',
                 keep_proportions=True,
                 door_window_size=500)
    
    return level