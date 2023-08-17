from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from os.path import exists as os_path_exists
from Color import Color

def level_rotation():
    
    v = 1

    S0 = Switch(name='S0', value=v)
    S1 = Switch(name='S1', value=v)
    S2 = Switch(name='S2', value=v)
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6', value=v)
    S7 = Switch(name='S7', value=v)
    S8 = Switch(name='S8', value=v)
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11]

    T0 = Tree(tree_list=['IN'] + [Tree.tree_list_BIN(6)]*4,
                name='T0',
                switches=[S0, S1, S2, S3, S4,  S5,
                         #S6   S7   S8   S9  S10  S11
                          S6, S11,  S7,  S9,  S8, S10,   # 7 8 10 11 7
                          S8,  S7,  S9, S11, S10,  S6,   # 8 6 11  9 8
                          S10, S6,  S8,  S7,  S9, S11],  # 6 7  9 10 6
                cut_expression=True)
    T1 = Tree(tree_list=['EQU'] + [Tree.tree_list_BIN(6)]*2,
                name='T1',
                switches=Slist)
    filename = 'levels/Rotation_random_exits.txt'
    if os_path_exists(filename):
        with open(filename, 'r') as fr:
            lines = fr.readlines()
            l = rd_choice(lines)
        T2 = Tree(tree_list=Tree.tree_list_from_str(l),
                    name='T2',
                    switches=Slist)
    else:
        T2 = Tree(tree_list=['EQU'] + [Tree.tree_list_BIN(6)]*2,
                    name='T2',
                    switches=Slist)

    R0 = Room(name='R0',
                position=[2, 3, 2, 3],
                switches_list=[S0, S1, S2, S3, S4, S5])
    R1 = Room(name='R1',
                position=[1, 0, 3, 2],
                switches_list=[S6, S7, S8, S9, S10, S11])
    RE = Room(name='RE',
              position=[0.5, 3, 0.5, 3],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[0.5/2, 0],
                relative_arrival_coordinates=[1.5/3, 1])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R0,
                relative_departure_coordinates=[2.5/3, 1],
                relative_arrival_coordinates=[1.5/2, 0])
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[0, 1/2],
                relative_arrival_coordinates=[1, 1/2])

    lcolor = Levels_colors_list.FROM_HUE(hu=0.9, sa=0.8, li=0.6)
    lcolor.room_color = Color.BRIGHT_ORANGE
    lcolor.inside_room_color = Color.BLACK
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, RE],
                 doors_list=[D0, D1, D2],
                 fastest_solution=None,
                 level_color=lcolor,
                 name='Rotation',
                 keep_proportions=True,
                 door_window_size=425,
                 random=True)
    
    return level