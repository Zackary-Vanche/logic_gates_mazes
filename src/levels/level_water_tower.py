from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle

def level_water_tower(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    
    values = [i+1 for i in range(128)]
    rd_shuffle(values)

    Slist = [S0, S1, S2, S3, S4, S5]

    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_0)),
              name='V0',
              switches=Slist_0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_1)),
              name='V1',
              switches=Slist_1)
    tree_list_2 = ["SUM"] + [["PROD", Tree.tree_list_EQU(2), [None]]]*8
    Slist_2 = []
    Slist_3 = []
    for i in range(8):
        Slist_2.extend([V0, i, values[i]])
        Slist_3.extend([V1, i, values[i]])
    V2 = Tree(tree_list=tree_list_2,
              name='V2',
              switches=Slist_2,
              cut_expression_depth_1=True)
    V3 = Tree(tree_list=tree_list_2,
              name='V3',
              switches=Slist_3,
              cut_expression_depth_1=True)
    V4 = Tree(tree_list=["MIN", [None], [None]],
              name='V4',
              switches=[V2, V3])
    
    threshold = 0
    for i in range(8):
        for j in range(8):
            new_threshold = min(values[i], values[j])*abs(i-j)
            threshold = max(threshold, new_threshold)
    
    T0 = Tree(tree_list=["AND",
                         Tree.tree_list_INF(2),
                         ["INFOREQU",
                         [None],
                         ["PROD",
                          ["ABS", ["SUM", [None], ["MINUS", [None]]]],
                          ["MIN", [None], [None]],
                          ]]],
                name='T0',
                switches=[V0, V1, threshold, V0, V1, V2, V3],
                cut_expression_depth_1=True)

    R0 = Room(name='R0',
                position=[3, 0, 2, 3],
                switches_list=Slist)
    RE = Room(name='RE',
              position=[0.75, 2, 1, 1],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[0.25, 0.5])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0.57, sa=0.4, li=0.5),
                 name='Water tower',
                 keep_proportions=True,
                 door_window_size=400,
                 random=True)
    
    return level