from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import randint as rd_randint

def level_numeration():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')

    Slist = [S0, S1, S2, S3, S4]

    T0 = Tree(tree_list=['EQU', Tree.tree_list_BIN(len(Slist)), [None]],
              name='T0',
              switches = Slist + [rd_randint(0, 31)])

    R0 = Room(name='R0',
              position = [0, 0, 5, 1],
              switches_list = Slist)
    RE = Room(name='RE',
              position=[2, 2, 1, 1],
              is_exit=True)   # E pour exit ou end
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=RE,
              relative_departure_coordinates=[1/2, 1],
              relative_arrival_coordinates=[1/2, 0])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0] + [RE],
                 doors_list=[D0],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0.1, sa=0.8, li=0.35),
                 name='Numeration',
                 door_window_size=450,
                 keep_proportions=True,
                 y_separation=40,
                 border=40,
                 random=True)

    return level