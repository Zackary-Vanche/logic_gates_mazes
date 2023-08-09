from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def level_magic_square(fast_solution_finding=False):
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
    S15 = Switch(name='S15')
    S16 = Switch(name='S16')
    S17 = Switch(name='S17')
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')
    S20 = Switch(name='S20')
    S21 = Switch(name='S21')
    S22 = Switch(name='S22')
    S23 = Switch(name='S23')
    S24 = Switch(name='S24')
    S25 = Switch(name='S25')
    S26 = Switch(name='S26')
    S27 = Switch(name='S27')

    SN12 = Switch(value=12, name='12')

    tree_list_SUM = ['SUM',
                     Tree.tree_list_BIN(3),
                     Tree.tree_list_BIN(3),
                     Tree.tree_list_BIN(3)]

    tree_list_EQU = ['EQU', tree_list_SUM, [None]]

    if fast_solution_finding:
        tree_list_0 = ['AND',
                       tree_list_EQU,
                       ['DIFF'] + [Tree.tree_list_BIN(3)] * 3]
        tree_list_1 = ['AND',
                       tree_list_EQU,
                       ['DIFF'] + [Tree.tree_list_BIN(3)] * 6]
        tree_list_2 = ['AND',
                       ['EQU',
                        ['SUM',
                         Tree.tree_list_BIN(3),
                         Tree.tree_list_BIN(4),
                         Tree.tree_list_BIN(3)],
                        [None]],
                       ['DIFF',
                        Tree.tree_list_BIN(3),
                        Tree.tree_list_BIN(3),
                        Tree.tree_list_BIN(3),
                        Tree.tree_list_BIN(3),
                        Tree.tree_list_BIN(3),
                        Tree.tree_list_BIN(3),
                        Tree.tree_list_BIN(3),
                        Tree.tree_list_BIN(4),
                        Tree.tree_list_BIN(3)]]
    else:
        tree_list_0 = tree_list_EQU
        tree_list_1 = tree_list_EQU
        tree_list_2 = ['EQU',
                       ['SUM',
                        Tree.tree_list_BIN(3),
                        Tree.tree_list_BIN(4),
                        Tree.tree_list_BIN(3)],
                       [None]]

    T0 = Tree(tree_list=tree_list_0,
              empty=True,
              name='T0',
              switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, SN12] + [S0, S1, S2, S3, S4, S5, S6, S7,
                                                                     S8] * fast_solution_finding)
    T1 = Tree(tree_list=tree_list_1,
              empty=True,
              name='T1',
              switches=[S9, S10, S11, S12, S13, S14, S15, S16, S17, SN12] + [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9,
                                                                             S10, S11, S12, S13, S14, S15, S16,
                                                                             S17] * fast_solution_finding,
              cut_expression=True,
              cut_expression_separator=']')
    T2 = Tree(tree_list=tree_list_2,
              empty=True,
              name='T2',
              switches=[S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, SN12] + [S0, S1, S2, S3, S4, S5, S6, S7, S8,
                                                                                   S9, S10, S11, S12, S13, S14, S15,
                                                                                   S16, S17, S18, S19, S20, S21, S22,
                                                                                   S23, S24, S25, S26,
                                                                                   S27] * fast_solution_finding,
              cut_expression=True,
              cut_expression_separator=']')
    T3 = Tree(tree_list=['EQU',
                         tree_list_SUM,
                         ['SUM',
                          Tree.tree_list_BIN(3),
                          Tree.tree_list_BIN(3),
                          Tree.tree_list_BIN(4)],
                         tree_list_SUM],
              empty=True,
              name='T3',
              switches=[S0, S1, S2,
                        S9, S10, S11,
                        S18, S19, S20,

                        S3, S4, S5,
                        S12, S13, S14,
                        S21, S22, S23, S24,

                        S6, S7, S8,
                        S15, S16, S17,
                        S25, S26, S27,
                        ],
              cut_expression=True,
              cut_expression_separator=']')
    T4 = Tree(tree_list=['EQU',
                         tree_list_SUM,
                         tree_list_SUM],
              empty=True,
              name='T4',
              switches=[S0, S1, S2,
                        S12, S13, S14,
                        S25, S26, S27,

                        S6, S7, S8,
                        S12, S13, S14,
                        S18, S19, S20],
              cut_expression=True,
              cut_expression_separator=']')
    T5 = Tree(tree_list=['AND',
                         ['DIFF'] + [Tree.tree_list_BIN(3)] * 7 + [Tree.tree_list_BIN(4)] + [Tree.tree_list_BIN(3)],
                         ['INF', Tree.tree_list_BIN(3), Tree.tree_list_BIN(3)]],
              empty=True,
              name='T5',
              switches=[S0, S1, S2,
                        S3, S4, S5,
                        S6, S7, S8,
                        S9, S10, S11,
                        S12, S13, S14,
                        S15, S16, S17,
                        S18, S19, S20,
                        S21, S22, S23, S24,
                        S25, S26, S27,
                        S0, S1, S2, S6, S7, S8],
              cut_expression=True,
              cut_expression_separator=')')

    R0 = Room(name='R0',
              position=[8, 4, 6, 6],
              switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8])
    R1 = Room(name='R1',
              position=[8, 12, 6, 6],
              switches_list=[S9, S10, S11, S12, S13, S14, S15, S16, S17])
    R2 = Room(name='R2',
              position=[2, 8, 4, 10],
              switches_list=[S18, S19, S20, S21, S22, S23, S24, S25, S26, S27])
    R3 = Room(name='R3',
              position=[2, 5, 1, 1],
              switches_list=[])
    R4 = Room(name='R4',
              position=[2, 2, 1, 1],
              switches_list=[])
    R5 = Room(name='R5',
              position=[5, 2, 1, 1],
              switches_list=[])
    RE = Room(name='RE',
              position=[8.25, 1.5, 2, 2],
              is_exit=True)  # E pour exit ou end
    R_useless = Room(name='',
                     position=[4, 4, 3, 3])

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=[0, 1 / 2],
              relative_arrival_coordinates=[1, 7 / 10])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=[1 / 8, 0],
              relative_arrival_coordinates=[1 / 2, 1])
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=R4)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R4,
              room_arrival=R5)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R5,
              room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-2,
                 rooms_list=[R0, R1, R2, R3, R4, R5, RE, R_useless],
                 doors_list=[D0, D1, D2, D3, D4, D5],
                 fastest_solution="S0 S2 S6 S7 S8 D0 S10 S11 S14 S16 D1 S18 S24 S25 S26 D2 D3 D4 D5",
                 level_color=Levels_colors_list.PINK_AND_WHITE,
                 name='Magic square',
                 door_window_size=600,
                 keep_proportions=True,
                 border=20)

    return level