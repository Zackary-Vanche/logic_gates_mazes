from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8]

    Slist_0 = [S0, S1, S2, 1]
    Slist_1 = [S3, S4, S5, 1]
    Slist_2 = [S6, S7, S8, 1]
    tree_list_V0 = ["SUM", Tree.tree_list_BIN(3), [None]]
    V0 = Tree(tree_list=tree_list_V0,
          name='V0',
          switches=Slist_0)
    V1 = Tree(tree_list=tree_list_V0,
          name='V1',
          switches=Slist_1)
    V2 = Tree(tree_list=tree_list_V0,
          name='V2',
          switches=Slist_2)
    V3 = Tree(tree_list=Tree.tree_list_PROD(3),
          name='V3',
          switches=[V0, V1, V2])
    V4 = Tree(tree_list=Tree.tree_list_INF(3),
              name='V4',
              switches=[V0, V1, V2])
    V5 = Tree(tree_list=["EQU", ["SUM"] + [Tree.tree_list_DIVINT]*3 + [[None]], [None]],
              name='V5',
              switches=[V3, V0, V3, V1, V3, V2, 1, V3])

    T0 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T0',
                switches=[V4, V5],
                cut_expression_depth_1=True)

    dx = 0.75
    dy = 0.5
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=Slist)
    RE = Room(name='RE',
              position=[0, 0, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution="S0 S4 S7 S8 D0",
                 level_color=Levels_colors_list.FROM_HUE(hu=0.65, sa=0.45, li=0.35),
                 name='The answer',
                 keep_proportions=True,
                 door_window_size=325)
    
    return level