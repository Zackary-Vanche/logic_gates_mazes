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

    Slist = [S0, S1, S2, S3, S4, S5]

    Slist_0 = [S0, S1]
    Slist_1 = [S2, S3]
    Slist_2 = [S4, S5]
    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_0)),
          name='V0',
          switches=Slist_0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_1)),
          name='V1',
          switches=Slist_1)
    V2 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_2)),
          name='V2',
          switches=Slist_2)
    
    tree_list_V = ["SUM", Tree.tree_list_PROD(2), [None]]
    
    V3 = Tree(tree_list=tree_list_V,
          name='V3',
          switches=[2, V0, 1])
    V4 = Tree(tree_list=tree_list_V,
          name='V4',
          switches=[2, V1, 1])
    V5 = Tree(tree_list=tree_list_V,
          name='V5',
          switches=[2, V2, 1])
    
    tree_list_minus = ["SUM", Tree.tree_list_MAX(2), ["MINUS", Tree.tree_list_MIN(2)]]
    
    V6 = Tree(tree_list=tree_list_minus,
          name='V6',
          switches=[V3, V4, V3, V4])
    V7 = Tree(tree_list=tree_list_minus,
          name='V7',
          switches=[V4, V5, V4, V5])

    T0 = Tree(tree_list=Tree.tree_list_EQUSET(5*2),
                name='T0',
                switches=[V3, V4, V5, V6, V7, 1, 2, 3, 4, 5])

    dx = 0.8
    dy = 0.8
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, 1*ex, 1.5*ey],
                switches_list=Slist)
    RE = Room(name='RE',
              position=[1*dx, 1*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE,
                relative_position=0.6)
    
    color=Color.color_hls(hu=0.6, li=0.7, sa=0.8)
    lcolor=Levels_colors_list.FROM_HUE(hu=0.6, sa=0.2, li=0.4)
    lcolor.surrounding_color=color
    lcolor.contour_color=color

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution="S0 S3 D0",
                 level_color=lcolor,
                 name='Substract',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level