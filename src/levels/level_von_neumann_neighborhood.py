from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def level_von_neumann_neighborhood(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')

    Slist = [S0, S1, S2,
             S3, S4, S5,
             S6, S7, S8]
    Slist_T0 = [S0, S1,
                S0, S3,
                S1, S2,
                S1, S4,
                S2, S5,
                S3, S4,
                S3, S6,
                S4, S5,
                S4, S7,
                S5, S8,
                S7, S8]

    T0 = Tree(tree_list=['AND',
                         ['INF', Tree.tree_list_SUM(9), [None]]] + [Tree.tree_list_XOR(2)]*(len(Slist_T0)//2),
                name='T0',
                switches=Slist + [5] + Slist_T0,
                cut_expression_depth_1=True)

    R0 = Room(name='R0',
              position=[0, 0, 3, 3],
              switches_list=Slist)
    RE = Room(name='RE',
              position=[2, 4, 1, 1],
              is_exit=True)

    D0 = Door(two_way=False,
              tree=T0,
              name='D0',
              room_departure=R0,
              room_arrival=RE,
              relative_departure_coordinates=[1/2, 2.5/3])

    lcolor = Levels_colors_list.FROM_HUE(hu=0.2, sa=0.4, li=0.8)
    lcolor.background_color = Color.GREY_100
    lcolor.surrounding_color = Color.WHITE
    lcolor.contour_color = Color.WHITE
    lcolor.letters_color = Color.WHITE

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution='S1 S3 S5 S7 D0',
                 level_color=lcolor,
                 name='von Neumann neighborhood',
                 keep_proportions=True,
                 door_window_size=380)
    
    return level