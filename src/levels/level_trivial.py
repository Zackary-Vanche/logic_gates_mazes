from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def f():

    T0 = Tree(tree_list=[None],
              name='T0',
              switches=[1])

    R0 = Room(name='R0',
              position=[1.5, 0, 1, 1],
              switches_list=[])
    RE = Room(name='RE',
              position=[0, 0, 1, 1],
              is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0] + [RE],
                 doors_list=[D0],
                 fastest_solution='D0',
                 level_color=get_color(),
                 name='Trivial',
                 door_window_size=380,
                 keep_proportions=True,
                 y_separation=40,
                 border=40)

    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.6, sa=0.4, li=0.3)
    lcolor.surrounding_color = Color.color_hls(hu=0.5, sa=1, li=0.8)
    lcolor.contour_color = Color.color_hls(hu=0.5, sa=1, li=0.8)
    return lcolor