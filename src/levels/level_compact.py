from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def level_compact():
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')

    SN1 = Switch(value=1)
    SN2 = Switch(value=2)
    SN5 = Switch(value=5)

    T0 = Tree(tree_list=['OR', [None], Tree.tree_list_XOR(2)],
              empty=True,
              name='T0',
              switches=[S0, S1, S2])
    T1 = Tree(tree_list=['NAND', [None], Tree.tree_list_XOR(2)],
              empty=True,
              name='T1',
              switches=[S0, S1, S2])
    T2 = Tree(tree_list=['SUP', Tree.tree_list_SUM(3), [None]],
              empty=True,
              name='T2',
              switches=[S0, S1, S2, SN2])
    T3 = Tree(tree_list=Tree.tree_list_NAND(3),
              empty=True,
              name='T3',
              switches=[S0, S1, S2])
    T4 = Tree(tree_list=['SUP', Tree.tree_list_BIN(3), [None]],
              empty=True,
              name='T4',
              switches=[S0, S1, S2, SN1])
    T5 = Tree(tree_list=['INF', Tree.tree_list_BIN(3), [None]],
              empty=True,
              name='T5',
              switches=[S0, S1, S2, SN5])
    T6 = Tree(tree_list=Tree.tree_list_NOR(3),
              empty=True,
              name='T6',
              switches=[S0, S1, S2])

    a = 1

    R0 = Room(name='R0',
              position=[0, 2, a, a],
              switches_list=[S0])
    R1 = Room(name='R1',
              position=[2, 2, a, a],
              switches_list=[S1])
    R2 = Room(name='R2',
              position=[2, 0, a, a],
              switches_list=[S2])
    RE = Room(name='RE',
              position=[0, 0, a, a],
              is_exit=True)  # E pour exit ou end

    rp = 1 / 2

    rp = 0.4

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R0,
              relative_position=rp)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R0,
              room_arrival=R2,
              relative_position=rp)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R2,
              room_arrival=R0,
              relative_position=rp)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R1,
              room_arrival=R2,
              relative_position=rp)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R2,
              room_arrival=R1,
              relative_position=rp)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R2,
              room_arrival=RE,
              relative_position=rp)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution='S0 D0 S1 D4 D3 S0 D0 D4 S2 D3 S0 D0 S1 D4 D3 S0 D0 D4 S2 D6',
                 level_color=Levels_colors_list.FROM_HUE(hu=0.145, sa=0.2, li=0.45),
                 name='Compact',
                 door_window_size=666,
                 keep_proportions=True,
                 y_separation=50,
                 border=66,
                 group='pure maze')

    return level