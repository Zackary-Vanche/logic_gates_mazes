from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from numpy import sqrt

def f():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')

    T0 = Tree(tree_list=['EQU', ['PROD', [None], Tree.tree_list_BIN(4)], [None]],
              name='T0',
              switches=[7, S0, S1, S2, S3, 42])

    R0 = Room(name='R0',
              position=[0, 0, 1, 1],
              switches_list=[S0, S1, S2, S3])
    RE = Room(name='RE',
              position=[1+(sqrt(2)/2-1)/2, 1+(sqrt(2)/2-1)/2, 1, 1],
              is_exit=True)   # E pour exit ou end
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=RE,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[0, 1/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0] + [RE],
                 doors_list=[D0],
                 fastest_solution='S1 S2 D0',
                 level_color=get_color(),
                 name='Product',
                 door_window_size=400,
                 keep_proportions=True,
                 y_separation=40,
                 border=40)

    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.5, sa=0.6, li=0.7)