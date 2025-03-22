from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def f():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')

    T0 = Tree(tree_list=[None],
              name='T0',
              switches=[S0])
    T1 = Tree(tree_list=[None],
              name='T1',
              switches=[S1])
    T2 = Tree(tree_list=[None],
              name='T2',
              switches=[S2])
    T3 = Tree(tree_list=Tree.tree_list_from_str('FT'),
              name='T3',
              switches=[S0, S3])

    R0 = Room(name='R0',
              position=[1, 0, 2, 2],
              switches_list=[S0])
    R1 = Room(name='R1',
              position=[4, 1, 2, 2],
              switches_list=[S1])
    R2 = Room(name='R2',
              position=[3, 4, 2, 2],
              switches_list=[S2, S3])
    RE = Room(name='RE',
              position=[0, 3, 2, 2],
              is_exit=True)  # E pour exit ou end

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
              room_arrival=R0)
    D3 = Door(two_way=False,
              tree=T3,
              name='D3',
              room_departure=R0,
              room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, RE],
                 doors_list=[D0, D1, D2, D3],
                 fastest_solution='S0 D0 S1 D1 S2 S3 D2 S0 D3',
                 level_color=get_color(),
                 name='Loop',
                 door_window_size=400,
                 border=60,
                 keep_proportions=True)

    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE_light_background(hu=0, sa=0.5, li=0.2)
    lcolor.contour_color = Color.color_hls(hu=0, li=0.6, sa=1)
    return lcolor