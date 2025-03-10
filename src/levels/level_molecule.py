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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9]
    
    Slist_T0 = []
    tree_list = ["AND"]
    for l in [[S9, S0, S1],
              [S0, S1, S2],
              [S1, S2, S3, S7],
              [S2, S3, S4],
              [S3, S4, S5],
              [S4, S5, S6],
              [S5, S6, S7],
              [S6, S7, S8, S2],
              [S7, S8, S9],
              [S8, S9, S0]]:
        Slist_T0.extend(l)
        tree_list.append(Tree.tree_list_OR(len(l)))

    T0 = Tree(tree_list=tree_list+[["INFOREQU", Tree.tree_list_SUM(10), [None]]],
                name='T0',
                switches=Slist_T0+Slist+[3],
                cut_expression_depth_1=True)

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, 5*ex, 2*ey],
                switches_list=Slist)
    RE = Room(name='RE',
              position=[1*dx, 2*dy, ex, ey],
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
                 fastest_solution="S0 S4 S7 D0",
                 level_color=get_color(),
                 name='Molecule',
                 keep_proportions=True,
                 door_window_size=340)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.7)
    lcolor.contour_color = Color.color_hls(hu=0, sa=0.2, li=0.7)
    return lcolor