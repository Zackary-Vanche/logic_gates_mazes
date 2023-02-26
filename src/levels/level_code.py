from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def level_code():
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')

    SN1 = Switch(value=1)

    T0 = Tree(tree_list=['EQU', Tree.tree_list_BIN(4), Tree.tree_list_BIN(4)],
              empty=True,
              name='T0',
              switches=[S0, S2, S4, S6,
                        S1, S3, S5, S7, ])
    tree_gray = ['BIN'] + [Tree.tree_list_XOR(2)] * 3 + [[None]]
    T1 = Tree(tree_list=['EQU',
                         tree_gray,
                         ['SUM', [None], tree_gray]],
              empty=True,
              name='T1',
              switches=[S1, S3,
                        S3, S5,
                        S5, S7,
                        S7,
                        SN1,
                        S0, S2,
                        S2, S4,
                        S4, S6,
                        S6,
                        ],
              cut_expression=True)
    T2 = Tree(tree_list=Tree.tree_list_from_str('00011001'),
              empty=True,
              name='T2',
              switches=[S0, S1, S2, S3, S4, S5, S6, S7])
    # T2 = Tree(tree_list=Tree.tree_list_from_str('T'),
    #           empty=True,
    #           name='T2',
    #           switches = [Switch(value=1)])

    R0 = Room(name='R0',
              position=[3, 3, 2, 2],
              switches_list=[S0, S2, S4, S6])
    R1 = Room(name='R1',
              position=[3, 0, 2, 2],
              switches_list=[S1, S3, S5, S7])
    RE = Room(name='RE',
              position=[0, 3, 2, 2],
              is_exit=True)  # E pour exit ou end

    rp = 1 / 2

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp,
              relative_departure_coordinates=[1, 0],
              relative_arrival_coordinates=[1, 1])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R0,
              relative_position=rp,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[0, 0])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R0,
              room_arrival=RE,
              relative_position=rp)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1] + [RE],
                 doors_list=[D0, D1, D2],
                 fastest_solution="D0 S1 D1 S0 D0 S3 D1 S2 D0 S1 D1 S0 D0 S1 S5 D1 S0 S4 D0 S1 D1 S0 D0 S3 D1 S2 D0 S1 D1 S0 D0 S3 S7 D1 S2 S6 D0 S1 D1 S0 D0 S3 D1 S2 D0 S1 D1 S0 D0 S1 S5 D1 S0 S4 D0 S1 D1 S0 D0 S3 D1 S2 D0 S1 D1 S0 S2 S4 S6 D2",
                 level_color=Levels_colors_list.FROM_HUE(hu=0.5, sa=0.25, li=0.9),
                 name='Code',
                 door_window_size=500,
                 keep_proportions=True,
                 y_separation=40,
                 border=40)

    return level