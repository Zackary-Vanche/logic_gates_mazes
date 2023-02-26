from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def level_pong():
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

    T0 = Tree(tree_list=['EQU', ['SUM'] + [Tree.tree_list_XOR(2)] * 5, [None]],
              empty=True,
              name='T0',
              switches=[S0, S5,
                        S1, S6,
                        S2, S7,
                        S3, S8,
                        S4, S9,
                        Switch(value=3, name='3')])
    T1 = Tree(tree_list=Tree.tree_list_AND(10),
              empty=True,
              name='T1',
              switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9])

    R0 = Room(name='R0',
              position=[0, 0, 1, 5],
              switches_list=[S0, S1, S2, S3, S4])
    R1 = Room(name='R1',
              position=[2, 0, 1, 5],
              switches_list=[S5, S6, S7, S8, S9])
    RE = Room(name='RE',
              position=[0, 6, 3, 1],
              is_exit=True)  # E pour exit ou end
    D0 = Door(two_way=True,
              tree=T0,
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=RE,
              relative_departure_coordinates=[1 / 2, 9 / 10])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, RE],
                 doors_list=[D0, D1],
                 fastest_solution='S0 S1 S2 D0 S5 S8 D0 S3 S4 D0 S6 S7 S9 D1',
                 level_color=Levels_colors_list.FROM_HUE(0.4, sa=0.1, li=0.4),
                 name='Pong',
                 door_window_size=800,
                 keep_proportions=True)

    return level