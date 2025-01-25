from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def f():
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')

    T0 = Tree(tree_list=['INF',
                         ['ABS',
                          ['SUM',
                           ['MINUS',
                            Tree.tree_list_BIN(3)],
                           Tree.tree_list_BIN(3)]],
                         [None]],
              name='T0',
              switches=[S0, S2, S4, S1, S3, S5,
                        Switch(value=2, name='2')])
    T1 = Tree(tree_list=Tree.tree_list_AND(6),
              name='T1',
              switches=[S0, S1, S2, S3, S4, S5])

    R0 = Room(name='R0',
              position=[0, 0, 4, 1],
              switches_list=[S0, S2, S4,])
    R1 = Room(name='R1',
              position=[0, 4, 4, 1],
              switches_list=[S1, S3, S5,])
    RE = Room(name='RE',
              position=[2, 2, 2, 1],
              is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=True,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[0, 0])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=RE,
              relative_departure_coordinates=[3 / 4, 0],
              relative_arrival_coordinates=[1 / 2, 1])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, RE],
                 doors_list=[D0, D1],
                 fastest_solution='S0 D0 S3 D0 S2 D0 S3 S5 D0 S2 S4 D0 S3 D0 S2 D0 S1 D1',
                 level_color=get_color(),
                 name='Naturals',
                 door_window_size=450,
                 keep_proportions=True)

    return level

def get_color():
    return Levels_colors_list.FROM_HUE(0.3)