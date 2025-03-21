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

    T0 = Tree(tree_list=Tree.tree_list_OR(2),
              name='T0',
              switches=[S0, S1])
    T1 = Tree(tree_list=Tree.tree_list_OR(2),
              name='T1',
              switches=[S1, S2])
    T2 = Tree(tree_list=Tree.tree_list_from_str('FFF'),
              name='T2',
              switches=[S0, S1, S2])

    d = 5
    e = 1.75

    position_R0 = [0, 0, e, e]
    position_R1 = [d, 0, e, e]
    position_R2 = [2 * d, 0, e, e]
    position_RE = [3 * d, 0, e, e]

    R0 = Room(name='R0', position=position_R0, switches_list=[S0])
    R1 = Room(name='R1', position=position_R1, switches_list=[S1])
    R2 = Room(name='R2', position=position_R2, switches_list=[S2])
    RE = Room(name='RE', position=position_RE, is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=True,
              tree=T0,
              name='D0',
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=True,
              tree=T1,
              name='D1',
              room_departure=R1,
              room_arrival=R2)
    D2 = Door(two_way=False,
              tree=T2,
              name='D2',
              room_departure=R2,
              room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, RE],
                 doors_list=[D0, D1, D2],
                 fastest_solution="S0 D0 S1 D0 S0 D0 D1 S2 D1 S1 D1 S2 D2",
                 level_color=get_color(),
                 name='Yoyo',
                 door_window_size=250,
                 keep_proportions=True)

    return level

def get_color():
    return Levels_colors_list.FROM_HUE(0.9)