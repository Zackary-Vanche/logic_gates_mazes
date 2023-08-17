from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def level_egyptian_fractions():
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
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')

    SN1 = Switch(value=1)

    T0 = Tree(tree_list=['EQU',
                         ['DIV', [None], [None]],
                         ['SUM',
                          ['DIV', [None], ['SUM', [None], Tree.tree_list_BIN(3)]],
                          ['DIV', [None], ['SUM', [None], Tree.tree_list_BIN(4)]],
                          ['DIV', [None], ['SUM', [None], Tree.tree_list_BIN(8)]]], ],
              name='T0',
              switches=[Switch(value=7), Switch(value=22),
                        SN1, SN1,
                        S0, S1, S2,
                        SN1, SN1,
                        S3, S4, S5, S6,
                        SN1, SN1,
                        S7, S8, S9, S10, S11, S12, S13, S14,
                        ],
              cut_expression=True)
    R0 = Room(name='R0',
              position=[0, 2, 3, 5],
              switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14])
    RE = Room(name='RE',
              position=[0, 0, 3, 1],
              is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=RE,
              relative_position=1 / 2,
              relative_departure_coordinates=[1 / 2, 0],
              relative_arrival_coordinates=[1 / 2, 1])
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0] + [RE],
                 doors_list=[D0],
                 fastest_solution='S0 S1 S3 S4 S5 S6 S7 S8 S9 S10 S12 S14 D0',
                 level_color=Levels_colors_list.FROM_HUE(hu=0.15, sa=0.8, li=0.51),
                 name='Egyptian fractions',
                 door_window_size=350,
                 keep_proportions=True,
                 y_separation=40,
                 border=40)

    return level