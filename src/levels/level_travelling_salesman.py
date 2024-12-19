from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def f(fast_solution_finding=False):
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
    S28 = Switch(name='S28')
    S29 = Switch(name='S29')
    S30 = Switch(name='S30')
    S31 = Switch(name='S31')
    S32 = Switch(name='S32')
    S33 = Switch(name='S33')
    S34 = Switch(name='S34')
    S35 = Switch(name='S35')
    S36 = Switch(name='S36')
    S37 = Switch(name='S37')
    S38 = Switch(name='S38')
    S39 = Switch(name='S39')
    S40 = Switch(name='S40')
    S41 = Switch(name='S41')

    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    Slist_3 = [S9, S10, S11]
    Slist_4 = [S12, S13, S14]
    Slist_5 = [S15, S16, S17]
    Slist_6 = [S18, S19, S20]
    Slist_7 = [S21, S22, S23]
    Slist_8 = [S24, S25, S26]
    Slist_9 = [S27, S28, S29]
    Slist_10 = [S30, S31, S32]
    Slist_11 = [S33, S34, S35]
    Slist_12 = [S36, S37, S38]
    Slist_13 = [S39, S40, S41]
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_0)),
              name='V0',
              switches=Slist_0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_1)),
              name='V1',
              switches=Slist_1)
    V2 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_2)),
              name='V2',
              switches=Slist_2)
    V3 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_3)),
              name='V3',
              switches=Slist_3)
    V4 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_4)),
              name='V4',
              switches=Slist_4)
    V5 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_5)),
              name='V5',
              switches=Slist_5)
    V6 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_6)),
              name='V6',
              switches=Slist_6)
    V7 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_7)),
              name='V7',
              switches=Slist_7)
    V8 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_8)),
              name='V8',
              switches=Slist_8)
    V9 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_9)),
              name='V9',
              switches=Slist_9)
    V10 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_10)),
              name='V10',
              switches=Slist_10)
    V11 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_11)),
              name='V11',
              switches=Slist_11)
    V12 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_12)),
              name='V12',
              switches=Slist_12)
    V13 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_13)),
              name='V13',
              switches=Slist_13)

    tree_list_IN = ['IN', Tree.tree_list_BIN(6)] + [[None]] * 7

    tree_list_DIST = ['DIST'] + [[None]] * 4  # 12

    tree_list_SUM = ['SUM'] + [tree_list_DIST] * 7  # 72

    tree_list_INF = ['INF', tree_list_SUM, [None]]  # 73

    if fast_solution_finding:
        T0 = Tree(tree_list=[None],
                  name='T0',
                  switches=[1])
        T1 = Tree(tree_list=['DIFF'] + [Tree.tree_list_BIN(6)] * 2,
                  name='T1',
                  switches=[S0, S1, S2, S3, S4, S5,
                            S6, S7, S8, S9, S10, S11],
                  cut_expression=True,
                  cut_expression_separator=']')
        T2 = Tree(tree_list=['DIFF'] + [Tree.tree_list_BIN(6)] * 3,
                  name='T2',
                  switches=[S0, S1, S2, S3, S4, S5,
                            S6, S7, S8, S9, S10, S11,
                            S12, S13, S14, S15, S16, S17],
                  cut_expression=True,
                  cut_expression_separator=')')
        T3 = Tree(tree_list=['DIFF'] + [Tree.tree_list_BIN(6)] * 4,
                  name='T3',
                  switches=[S0, S1, S2, S3, S4, S5,
                            S6, S7, S8, S9, S10, S11,
                            S12, S13, S14, S15, S16, S17,
                            S18, S19, S20, S21, S22, S23],
                  cut_expression=True,
                  cut_expression_separator=')')
        T4 = Tree(tree_list=['DIFF'] + [Tree.tree_list_BIN(6)] * 5,
                  name='T4',
                  switches=[S0, S1, S2, S3, S4, S5,
                            S6, S7, S8, S9, S10, S11,
                            S12, S13, S14, S15, S16, S17,
                            S18, S19, S20, S21, S22, S23,
                            S24, S25, S26, S27, S28, S29],
                  cut_expression=True,
                  cut_expression_separator=')')
        T5 = Tree(tree_list=['DIFF'] + [Tree.tree_list_BIN(6)] * 6,
                  name='T5',
                  switches=[S0, S1, S2, S3, S4, S5,
                            S6, S7, S8, S9, S10, S11,
                            S12, S13, S14, S15, S16, S17,
                            S18, S19, S20, S21, S22, S23,
                            S24, S25, S26, S27, S28, S29,
                            S30, S31, S32, S33, S34, S35],
                  cut_expression=True,
                  cut_expression_separator=')')
        T6 = Tree(tree_list=['DIFF'] + [Tree.tree_list_BIN(6)] * 7,
                  name='T6',
                  switches=[S0, S1, S2, S3, S4, S5,
                            S6, S7, S8, S9, S10, S11,
                            S12, S13, S14, S15, S16, S17,
                            S18, S19, S20, S21, S22, S23,
                            S24, S25, S26, S27, S28, S29,
                            S30, S31, S32, S33, S34, S35,
                            S36, S37, S38, S39, S40, S41],
                  cut_expression=True,
                  cut_expression_separator=')')
    else:
        T0 = Tree(tree_list=[None],
                  name='T0',
                  switches=[1])
        T1 = Tree(tree_list=[None],
                  name='T1',
                  switches=[1])
        T2 = Tree(tree_list=[None],
                  name='T2',
                  switches=[1])
        T3 = Tree(tree_list=[None],
                  name='T3',
                  switches=[1])
        T4 = Tree(tree_list=[None],
                  name='T4',
                  switches=[1])
        T5 = Tree(tree_list=[None],
                  name='T5',
                  switches=[1])
        T6 = Tree(tree_list=['EQUSET'] + [Tree.tree_list_BIN(6)] * 7 + [[None]] * 7,
                  name='T6',
                  switches=[S0, S1, S2, S3, S4, S5,
                            S6, S7, S8, S9, S10, S11,
                            S12, S13, S14, S15, S16, S17,
                            S18, S19, S20, S21, S22, S23,
                            S24, S25, S26, S27, S28, S29,
                            S30, S31, S32, S33, S34, S35,
                            S36, S37, S38, S39, S40, S41,
                            4, 6, 12, 18, 30, 42, 60],
                  cut_expression=True,
                  cut_expression_separator=')')
    T7 = Tree(tree_list=['AND',
                         tree_list_INF,
                         Tree.tree_list_OR(2),
                         Tree.tree_list_OR(2)],
              name='T7',
              switches=[V0, V1, V2, V3,
                        V2, V3, V4, V5,
                        V4, V5, V6, V7,
                        V6, V7, V8, V9,
                        V8, V9, V10, V11,
                        V10, V11, V12, V13,
                        V12, V13, V0, V1,
                        Switch(name='19', value=19),
                        S23, S30, S3, S36],
              cut_expression=True,
              cut_expression_separator=']')

    a = 3
    e = 1 / 100
    l = 0.75

    if fast_solution_finding:
        possible_switches_values = [[0, 0, 1, 0, 0, 0],
                                    [0, 1, 1, 0, 0, 0],
                                    [0, 0, 1, 1, 0, 0],
                                    [0, 1, 0, 0, 1, 0],
                                    [0, 1, 1, 1, 1, 0],
                                    [0, 1, 0, 1, 0, 1],
                                    [0, 0, 1, 1, 1, 1]]
    else:
        possible_switches_values = None

    R0 = Room(name='R0',
              position=[l, 1.5 * a, 6, 1],
              switches_list=[S0, S1, S2, S3, S4, S5],
              possible_switches_values=possible_switches_values)
    R1 = Room(name='R1',
              position=[l, 0.5 * a, 6, 1],
              switches_list=[S6, S7, S8, S9, S10, S11],
              possible_switches_values=possible_switches_values)
    R2 = Room(name='R2',
              position=[0, 0, 6, 1],
              switches_list=[S12, S13, S14, S15, S16, S17],
              possible_switches_values=possible_switches_values)
    R3 = Room(name='R3',
              position=[0, a, 6, 1],
              switches_list=[S18, S19, S20, S21, S22, S23],
              possible_switches_values=possible_switches_values)
    R4 = Room(name='R4',
              position=[0, 2 * a, 6, 1],
              switches_list=[S24, S25, S26, S27, S28, S29],
              possible_switches_values=possible_switches_values)
    R5 = Room(name='R5',
              position=[0, 3 * a, 6, 1],
              switches_list=[S30, S31, S32, S33, S34, S35],
              possible_switches_values=possible_switches_values)
    R6 = Room(name='R6',
              position=[l, 3.5 * a, 6, 1],
              switches_list=[S36, S37, S38, S39, S40, S41],
              possible_switches_values=possible_switches_values)
    R7 = Room(name='R7',
              position=[l + 4, 2.5 * a, 2, 1],
              switches_list=[])
    RE = Room(name='RE',
              position=[l, 2.5 * a, 3, 1],
              is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1 - e, 1 / 2],
              relative_arrival_coordinates=[1 - e, 1 / 2])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=[1, 0],
              relative_arrival_coordinates=[1, 0])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=[e, 1 / 2],
              relative_arrival_coordinates=[e, 1 / 2])
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=R4,
              relative_departure_coordinates=[e, 1 / 2],
              relative_arrival_coordinates=[e, 1 / 2])
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R4,
              room_arrival=R5,
              relative_departure_coordinates=[e, 1 / 2],
              relative_arrival_coordinates=[e, 1 / 2])
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R5,
              room_arrival=R6,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[0, 1])
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R6,
              room_arrival=R7,
              relative_departure_coordinates=[1 - e, 1 / 2],
              relative_arrival_coordinates=[1 - e, 1 / 2])
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R7,
              room_arrival=RE,
              relative_departure_coordinates=[0, 1 / 2],
              relative_arrival_coordinates=[1, 1 / 2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7],
                 fastest_solution='S2 S3 D0 S7 S10 D1 S13 S15 S17 D2 S20 S21 S22 S23 D3 S25 S26 S27 S28 D4 S31 S32 D5 S38 D6 D7',
                 level_color=Levels_colors_list.FROM_HUE(0.2, sa=0.5, li=0.4),
                 name='Travelling salesman',
                 door_window_size=425,
                 keep_proportions=False)

    return level