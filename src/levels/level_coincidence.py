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
    S16 = Switch(name='S16')
    S17 = Switch(name='S17')
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')
    S20 = Switch(name='S20')
    S21 = Switch(name='S21')
    S22 = Switch(name='S22')
    S23 = Switch(name='S23')

    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    Slist_3 = [S9, S10, S11]
    Slist_4 = [S12, S13, S14]
    Slist_5 = [S15, S16, S17]
    Slist_6 = [S18, S19, S20]
    Slist_7 = [S21, S22, S23]
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
    V6 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_6)),
          name='V6',
          switches=Slist_6)
    V7 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_7)),
          name='V7',
          switches=Slist_7)
    
    # 
    #         V4   V5
    #         V6   V7
    # V0 V1 V0V4 V0V5
    # V2 V3 V2V4 V3V7
    
    tree_list_aux = ["EQU",
                         ["SUM",
                          Tree.tree_list_PROD(2),
                          Tree.tree_list_PROD(2)],
                         Tree.tree_list_PROD(2)]

    T0 = Tree(tree_list=["AND",
                         tree_list_aux,
                         Tree.tree_list_DIFF(3),
                         Tree.tree_list_INF(2)],
                name='T0',
                switches=[V0, V4,
                          V1, V6,
                          V0, V4,
                          V0, V1, V4,
                          V0, V4],
                cut_expression_depth_1=True)
    T1 = Tree(tree_list=["AND",
                         tree_list_aux,
                         Tree.tree_list_DIFF(4),
                         Tree.tree_list_INF(2)],
                name='T1',
                switches=[V2, V4,
                          V3, V6,
                          V2, V6,
                          V0, V1, V3, V4,
                          V0, V3],
                cut_expression_depth_1=True)
    T2 = Tree(tree_list=["AND",
                         tree_list_aux,
                         tree_list_aux,
                         Tree.tree_list_EQUSET(6*2)],
                name='T2',
                switches=[V0, V5,
                          V1, V7,
                          V1, V5,
                          #######
                          V2, V5,
                          V3, V7,
                          V3, V7,
                          V0, V1, V3, V4, V5, V7, 1, 2, 3, 4, 5, 6],
                cut_expression_depth_1=True)

    dx = 2
    ey = 0.5
    ex = 1.5
    
    R0 = Room(name='R0',
                position=[0, 0, ex, 4*ey],
                switches_list=Slist_0+Slist_1+Slist_4+Slist_6)
    R1 = Room(name='R1',
                position=[1*dx, 0, ex, 2*ey],
                switches_list=Slist_2+Slist_3)
    R2 = Room(name='R2',
                position=[1*dx, 3*ey, ex, 2*ey],
                switches_list=Slist_5+Slist_7)
    RE = Room(name='RE',
              position=[0, 5*ey, ex, ey],
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
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, RE],
                 doors_list=[D0, D1, D2],
                 fastest_solution="S0 S4 S14 D0 S9 S11 D1 S16 S17 S21 S22 D2",
                 level_color=get_color(),
                 name='Coincidence',
                 keep_proportions=True,
                 door_window_size=375)
    
    return level

def get_color():
    hu = 0.4
    lcolor = Levels_colors_list.FROM_HUE(hu=hu, sa=0.4, li=0.6)
    lcolor.contour_color = Color.color_hls(hu=1-hu-0.05, sa=1, li=0.5)
    lcolor.surrounding_color = Color.color_hls(hu=1-hu+0.05, sa=1, li=0.5)
    return lcolor