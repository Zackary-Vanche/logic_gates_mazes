from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from os.path import exists as os_path_exists
from Color import Color

def level_wasted(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    
    tl1 = [None]
    tl0 = Tree.tree_list_not

    T0 = Tree(tree_list=['IN',
                         Tree.tree_list_BIN(3),
                         
                         #['BIN', tl1, tl0, tl1],
                         ['BIN', tl1, tl1, tl0],
                         
                         #['BIN', tl0, tl1, tl1],
                         ['BIN', tl1, tl1, tl0],
                         
                         #['BIN', tl0, tl1, tl1],
                         ['BIN', tl1, tl0, tl1]],
                empty=True,
                name='T0',
                switches=[S0, S1, S2,
                          #S3, S5, S4,
                          S3, S5, S4,
                          #S5, S4, S3,
                          S5, S4, S3,
                          #S4, S3, S5,
                          S4, S3, S5],
                cut_expression=True)
    T1 = Tree(tree_list=['EQU'] + [Tree.tree_list_BIN(3)]*2,
                empty=True,
                name='T1',
                switches=[S0, S1, S2, S3, S4, S5])
    filename = 'levels/Wasted_random_exits.txt'
    if os_path_exists(filename):
        with open(filename, 'r') as fr:
            lines = fr.readlines()
            l = rd_choice(lines)
        T2 = Tree(tree_list=Tree.tree_list_from_str(l),
                    empty=True,
                    name='T2',
                    switches=[S0, S1, S2, S3, S4, S5])
    else:
        T2 = Tree(tree_list=['EQU'] + [Tree.tree_list_BIN(3)]*2,
                    empty=True,
                    name='T2',
                    switches=[S0, S1, S2, S3, S4, S5])

    R0 = Room(name='R0',
              position=[0, 2, 3, 0.25],
              switches_list=[S0, S1, S2])
    R1 = Room(name='R1',
              position=[0, 3, 3, 0.25],
              switches_list=[S3, S4, S5])
    RE = Room(name='RE',
              position=[0, 1.5, 3, 0.25],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[0, 0],
                relative_arrival_coordinates=[1, 1],
                relative_position=0.35)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R0,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[1, 0],
                relative_position=0.35)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[1/2, 1])

    lcolor = Levels_colors_list.FROM_HUE(hu=0.6, sa=0.6, li=0.3)
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, RE],
                 doors_list=[D0, D1, D2],
                 fastest_solution=None,
                 level_color=lcolor,
                 name='Wasted',
                 keep_proportions=True,
                 door_window_size=500,
                 random=True)
    
    return level

