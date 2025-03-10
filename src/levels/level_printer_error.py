from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
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
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')
    S15 = Switch(name='S15')

    Slist_0 = [S0, S1, S2, S3]
    Slist_1 = [S4, S5, S6, S7]
    Slist_2 = [S8, S9, S10, S11]
    Slist_3 = [S12, S13, S14, S15]
    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_0)),
          name='V0',
          switches=Slist_0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_1)),
          name='V1',
          switches=Slist_1)
    V2 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_2)),
          name='V2',
          switches=Slist_2)
    V3 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_3)),
          name='V3',
          switches=Slist_3)
    
    V4 = Tree(tree_list=["SUM",
                         [None],
                         Tree.tree_list_PROD(2),
                         Tree.tree_list_PROD(2),
                         Tree.tree_list_PROD(2),
                         ],
          name='V4',
          switches=[V0, 10, V1, 100, V2, 1000, V3,])
    V5 = Tree(tree_list=["PROD",
                         ["POW", [None], [None]],
                         ["POW", [None], [None]],
                         ],
          name='V5',
          switches=[V3, V2, V1, V0,])

    T0 = Tree(tree_list=Tree.tree_list_INF(2),
                name='T0',
                switches=[V0, 10])
    T1 = Tree(tree_list=Tree.tree_list_INF(2),
                name='T1',
                switches=[V1, 10])
    T2 = Tree(tree_list=Tree.tree_list_INF(2),
                name='T2',
                switches=[V2, 10])
    T3 = Tree(tree_list=["AND",
                         Tree.tree_list_INF(2),
                         Tree.tree_list_EQU(2),
                         ],
                name='T3',
                switches=[V3, 10,
                          V4, V5
                          ],
                cut_expression_depth_1=True)

    R0 = Room(name='R0',
                position=[1, 0, 1, 1],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[0, 2, 1, 1],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[2, 2, 1, 1],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[4, 2, 1, 1],
                switches_list=Slist_3)
    RE = Room(name='RE',
              position=[3, 0, 1, 1],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, RE],
                 doors_list=[D0, D1, D2, D3],
                 fastest_solution="S1 D0 S4 S7 D1 S8 S10 D2 S13 D3",
                 level_color=get_color(),
                 name='Printer error',
                 keep_proportions=True,
                 door_window_size=350)
    
    return level

def get_color():
    hu = 0.3
    lcolor = Levels_colors_list.FROM_HUE(hu=hu, sa=0.4, li=0.6)
    lcolor.contour_color = Color.color_hls(hu=1-hu-0.05, sa=1, li=0.8)
    lcolor.surrounding_color = Color.color_hls(hu=1-hu+0.05, sa=1, li=0.5)
    return lcolor