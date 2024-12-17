from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list

def level_remove(): 

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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17]

    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    Slist_3 = [S9, S10, S11]
    Slist_4 = [S12, S13, S14]
    Slist_5 = [S15, S16, S17]
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
    
    tree_list_V = ["SUM", Tree.tree_list_PROD(2), [None]]
    
    V6 = Tree(tree_list=tree_list_V,
          name='V6',
          switches=[2, V0, 1])
    V7 = Tree(tree_list=tree_list_V,
          name='V7',
          switches=[2, V1, 1])
    V8 = Tree(tree_list=tree_list_V,
          name='V8',
          switches=[2, V2, 1])
    V9 = Tree(tree_list=tree_list_V,
          name='V9',
          switches=[2, V3, 1])
    V10 = Tree(tree_list=tree_list_V,
          name='V10',
          switches=[2, V4, 1])
    V11 = Tree(tree_list=tree_list_V,
          name='V11',
          switches=[2, V5, 1])
    
    tree_list_minus = ["SUM", Tree.tree_list_MAX(2), ["MINUS", Tree.tree_list_MIN(2)]]
    
    V12 = Tree(tree_list=tree_list_minus,
          name='V12',
          switches=[V6, V7]*2)
    V13 = Tree(tree_list=tree_list_minus,
          name='V13',
          switches=[V6, V8]*2)
    V14 = Tree(tree_list=tree_list_minus,
          name='V14',
          switches=[V6, V9]*2)
    V15 = Tree(tree_list=tree_list_minus,
          name='V15',
          switches=[V6, V10]*2)
    V16 = Tree(tree_list=tree_list_minus,
          name='V16',
          switches=[V6, V11]*2)

    Vlist = [V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16]

    T0 = Tree(tree_list=["AND", Tree.tree_list_INF(5), Tree.tree_list_EQUSET(11*2)],
              name='T0',
              switches=[V12, V13, V14, V15, V16]+Vlist+[i for i in range(1, 12)],
              cut_expression_depth_1=True)

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, 1*ex, 2*ey],
                switches_list=Slist)
    RE = Room(name='RE',
              position=[1*dx, 1*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE)
    
    color=Color.color_hls(hu=0.5, li=0.7, sa=0.8)
    lcolor=Levels_colors_list.FROM_HUE(hu=0.5, sa=0.2, li=0.4)
    lcolor.surrounding_color=color
    lcolor.contour_color=color

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution="S3 S7 S9 S10 S14 S15 S17 D0",
                 level_color=lcolor,
                 name='Remove',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level