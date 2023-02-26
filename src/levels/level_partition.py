from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

# Partition d'un ensemble en deux de sommes égales
def level_partition():
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')

    w_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in range(len(w_list)):
        w_list[i] = Switch(name=str(w_list[i]),
                           value=w_list[i])

    T0 = Tree(tree_list=['EQU',
                         ['SUM'] + [['PROD', [None], [None]]] * 9,
                         ['SUM'] + [['PROD', [None], Tree.tree_list_not]] * 9],
              empty=True,
              name='T0',
              switches=[w_list[0], S0, w_list[1], S1, w_list[2], S2, w_list[3], S3, w_list[4], S4, w_list[5], S5,
                        w_list[6], S6, w_list[7], S7, w_list[8], S8,
                        w_list[0], S0, w_list[1], S1, w_list[2], S2, w_list[3], S3, w_list[4], S4, w_list[5], S5,
                        w_list[6], S6, w_list[7], S7, w_list[8], S8],
              cut_expression=True)
    T1 = Tree(tree_list=['SUP',
                         ['SUM'] + [[None]] * 8,
                         [None]],
              empty=True,
              name='T1',
              switches=[S0, S1, S2, S3, S4, S5, S6, S7, Switch(name='5', value=5)])
    R0 = Room(name='R0',
              position=[0, 0, 3, 3],
              switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8])
    R1 = Room(name='R1',
              position=[1, -2, 1, 1],
              switches_list=[])
    RE = Room(name='RE',
              position=[1, -4, 1, 1],
              is_exit=True)  # E pour exit ou end
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1 / 2, 0.5 / 3])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, RE],
                 doors_list=[D0, D1],
                 fastest_solution="S0 S1 S2 S3 S4 S5 D0 D1",
                 level_color=Levels_colors_list.FROM_HUE(0.5),
                 name='Partition',
                 door_window_size=950,
                 keep_proportions=True)

    return level