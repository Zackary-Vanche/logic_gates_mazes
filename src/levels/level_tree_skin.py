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
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11]

    Slist_0 = [S0, S1]
    Slist_1 = [S2, S3]
    Slist_2 = [S4, S5]
    Slist_3 = [S6, S7]
    Slist_4 = [S8, S9]
    Slist_5 = [S10, S11]
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
    V4 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_4)),
          name='V4',
          switches=Slist_4)
    V5 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_5)),
          name='V5',
          switches=Slist_5)
    
    #    0
    # 1 2 3 4
    #    5
    
    V6 = Tree(tree_list=["AND"]+[Tree.tree_list_INF(2)]*6,
              name='V6',
              switches=[V0, 4,
                        V1, 4,
                        V2, 4,
                        V3, 4,
                        V4, 4,
                        V5, 4],
              cut_expression_depth_1=True)
    
    V7 = Tree(tree_list=["AND"]+[Tree.tree_list_DIFF(3)]*8,
              name='V7',
              switches=[V0, V1, V2,
                        V0, V2, V3,
                        V0, V3, V4,
                        V0, V1, V4,
                        V5, V1, V2,
                        V5, V2, V3,
                        V5, V3, V4,
                        V5, V1, V4,
                        ],
              cut_expression_depth_1=True)

    T0 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T0',
                switches=[V6, V7])

    R0 = Room(name='R0',
                position=[0, 0, 2, 6],
                switches_list=Slist)
    RE = Room(name='RE',
              position=[3, 2.5, 1, 1],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 1/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution="S0 S3 S7 S10 D0",
                 level_color=get_color(),
                 name='Tree skin',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.16, sa=0.2, li=0.3)
    lcolor.contour_color = Color.color_hls(hu=0.4, sa=0.7, li=0.5)
    lcolor.surrounding_color = Color.color_hls(hu=0.4, sa=0.7, li=0.5)
    return lcolor