from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def f():
    v = 0

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3', value=v)
    S4 = Switch(name='S4')
    S5 = Switch(name='S5', value=v)
    S6 = Switch(name='S6')
    S7 = Switch(name='S7', value=v)
    S8 = Switch(name='S8', value=v)
    S9 = Switch(name='S9')
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(5),
              name='V0',
              switches=[S0, S1, S2, S3, S4])
    V1 = Tree(tree_list=Tree.tree_list_BIN(5),
              name='V1',
              switches=[S5, S6, S7, S8, S9])
    
    t_aux = ['DIST', [None], [None], [None], [None]]

    T0 = Tree(tree_list=['AND',
                         ['SUPOREQU', [None], t_aux],
                         ['SUPOREQU', [None], t_aux],
                         ['SUP', [None], t_aux]],
              name='T0',
              switches=[Switch(value=2),
                        V0,
                        V1,
                        Switch(value=7), Switch(value=12),

                        Switch(value=3),
                        V0,
                        V1,
                        Switch(value=7), Switch(value=10),

                        Switch(value=4),
                        V0,
                        V1,
                        Switch(value=9), Switch(value=16),
                        ],
              cut_expression_depth_1=True)

    R0 = Room(name='R0',
              position=[0, 0, 5, 2],
              switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9])
    RE = Room(name='RE',
              position=[2, 3, 1, 1 / 2],
              is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=RE,
              relative_position=1 / 2,
              relative_departure_coordinates=[1 / 2, 1],
              relative_arrival_coordinates=[1 / 2, 0])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution='S0 S1 S2 S5 S7 S8 D0',
                 level_color=get_color(),
                 name='Triangulate',
                 door_window_size=395,
                 keep_proportions=True,
                 y_separation=40,
                 border=70)

    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0, sa=0.3, li=0.7)
    lcolor.contour_color = Color.color_hls(hu=0, sa=1, li=0.5)
    return lcolor