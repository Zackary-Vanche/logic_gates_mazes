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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14]

    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    Slist_3 = [S9, S10, S11]
    Slist_4 = [S12, S13, S14]
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
    
    #   4
    #
    # 2   3
    #
    # 0   1
    
    #   0
    #
    # 1   2
    #
    # 3   4
    
    tree_list_V = ["MOD", Tree.tree_list_SUM(2), [None]]
    V5 = Tree(tree_list=tree_list_V,
              name='V5',
              switches=[V0, V1, 7])
    V6 = Tree(tree_list=tree_list_V,
              name='V6',
              switches=[V0, V2, 7])
    V7 = Tree(tree_list=tree_list_V,
              name='V7',
              switches=[V0, V3, 7])
    V8 = Tree(tree_list=tree_list_V,
              name='V8',
              switches=[V1, V3, 7])
    V9 = Tree(tree_list=tree_list_V,
              name='V9',
              switches=[V2, V3, 7])
    V10 = Tree(tree_list=tree_list_V,
              name='V10',
              switches=[V2, V4, 7])
    V11 = Tree(tree_list=tree_list_V,
              name='V11',
              switches=[V3, V4, 7])

    T0 = Tree(tree_list=["AND",
                         Tree.tree_list_EQUSET(10),
                         Tree.tree_list_DIFF(7),
                         ],
               name='T0',
               switches=[V0, V1, V2, V3, V4, 0, 1, 2, 3, 4,
                         V5, V6, V7, V8, V9, V10, V11])

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

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution="S0 S1 S5 S6 S10 D0",
                 level_color=get_color(),
                 name='Harmonious house',
                 keep_proportions=True,
                 door_window_size=360)
    
    return level

def get_color():
    color=Color.color_hls(hu=0.3, li=0.6, sa=0.9)
    lcolor=Levels_colors_list.FROM_HUE(hu=0.3, sa=0.2, li=0.7)
    lcolor.surrounding_color=color
    lcolor.contour_color=color
    return lcolor