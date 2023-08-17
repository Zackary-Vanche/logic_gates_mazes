from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def level_knight():
    v = 0

    S0 = Switch(name='S0')
    S1 = Switch(name='S1', value=v)
    S2 = Switch(name='S2', value=v)
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7', value=v)
    S8 = Switch(name='S8', value=v)
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    S12 = Switch(name='S12', value=v)
    S13 = Switch(name='S13', value=v)
    S14 = Switch(name='S14', value=v)
    S15 = Switch(name='S15')
    S16 = Switch(name='S16', value=v)
    S17 = Switch(name='S17')
    S18 = Switch(name='S18')
    S19 = Switch(name='S19', value=v)
    S20 = Switch(name='S20')
    S21 = Switch(name='S21', value=v)
    S22 = Switch(name='S22')
    S23 = Switch(name='S23')
    S24 = Switch(name='S24', value=v)
    S25 = Switch(name='S25', value=v)
    S26 = Switch(name='S26')
    S27 = Switch(name='S27', value=v)
    S28 = Switch(name='S28', value=v)
    S29 = Switch(name='S29')
    S30 = Switch(name='S30', value=v)
    S31 = Switch(name='S31')
    S32 = Switch(name='S32', value=v)
    S33 = Switch(name='S33', value=v)
    S34 = Switch(name='S34')
    S35 = Switch(name='S35')
    S36 = Switch(name='S36')
    S37 = Switch(name='S37', value=v)
    S38 = Switch(name='S38')
    S39 = Switch(name='S39', value=v)

    V0 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V0',
              switches=[S0, S1])
    V1 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V1',
              switches=[S2, S3])
    V2 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V2',
              switches=[S4, S5])
    V3 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V3',
              switches=[S6, S7])
    V4 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V4',
              switches=[S8, S9])
    V5 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V5',
              switches=[S10, S11])
    V6 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V6',
              switches=[S12, S13])
    V7 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V7',
              switches=[S14, S15])
    V8 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V8',
              switches=[S16, S17])
    V9 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V9',
              switches=[S18, S19])
    V10 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V10',
              switches=[S20, S21])
    V11 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V11',
              switches=[S22, S23])
    V12 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V12',
              switches=[S24, S25])
    V13 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V13',
              switches=[S26, S27])
    V14 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V14',
              switches=[S28, S29])
    V15 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V15',
              switches=[S30, S31])
    V16 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V16',
              switches=[S32, S33])
    V17 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V17',
              switches=[S34, S35])
    V18 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V18',
              switches=[S36, S37])
    V19 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V19',
              switches=[S38, S39])

    tree_list_inf = ['INF', [None], [None]]
    tree_list_minus = ['MINUS', [None]]
    tree_list_diff = ['SUM', [None], tree_list_minus]
    tree_list_abs = ['ABS', tree_list_diff]
    tree_list_equ = ['EQUSET', tree_list_abs, tree_list_abs, [None], [None]]
    tree_list_tot = ['AND', tree_list_inf, tree_list_equ]

    T0 = Tree(tree_list=tree_list_tot,
              name='T0',
              switches=[V1, 3,
                        0, V0,
                        0, V1,
                        1,
                        2],
              cut_expression=False)
    T1 = Tree(tree_list=tree_list_tot,
              name='T1',
              switches=[V3, 3,
                        V0, V2,
                        V1, V3,
                        1,
                        2])
    T2 = Tree(tree_list=tree_list_tot,
              name='T2',
              switches=[V5, 3,
                        V2, V4,
                        V3, V5,
                        1,
                        2])
    T3 = Tree(tree_list=tree_list_tot,
              name='T3',
              switches=[V7, 3,
                        V4, V6,
                        V5, V7,
                        1,
                        2])
    T4 = Tree(tree_list=tree_list_tot,
              name='T4',
              switches=[V9, 3,
                        V6, V8,
                        V7, V9,
                        1,
                        2])
    T5 = Tree(tree_list=tree_list_tot,
              name='T5',
              switches=[V11, 3,
                        V8, V10,
                        V9, V11,
                        1,
                        2])
    T6 = Tree(tree_list=tree_list_tot,
              name='T6',
              switches=[V13, 3,
                        V10, V12,
                        V11, V13,
                        1,
                        2])
    T7 = Tree(tree_list=tree_list_tot,
              name='T7',
              switches=[V15, 3,
                        V12, V14,
                        V13, V15,
                        1,
                        2])
    T8 = Tree(tree_list=tree_list_tot,
              name='T8',
              switches=[V17, 3,
                        V14, V16,
                        V15, V17,
                        1,
                        2])
    T9 = Tree(tree_list=tree_list_tot,
              name='T9',
              switches=[V19, 3,
                        V16, V18,
                        V17, V19,
                        1,
                        2])
    T10 = Tree(tree_list=tree_list_equ,
               name='T10',
               switches=[S36, S37, 1, 1,
                         S38, S39, 0, 1,
                         1,
                         2])
    T11 = Tree(tree_list=['DIFF'] + [Tree.tree_list_BIN(4)] * 12,
               name='T11',
               switches=[0, 0, 0, 0,
                         S0, S1, S2, S3,
                         S4, S5, S6, S7,
                         S8, S9, S10, S11,
                         S12, S13, S14, S15,
                         S16, S17, S18, S19,
                         S20, S21, S22, S23,
                         S24, S25, S26, S27,
                         S28, S29, S30, S31,
                         S32, S33, S34, S35,
                         S36, S37, S38, S39,
                         1, 1, 0, 1],
               cut_expression=True)

    l = 1
    L = 4
    a = L + 1.5
    d = 1.5
    e = d / 2

    R0 = Room(name='R0',
              position=[0, 0, L, l],
              switches_list=[S0, S1, S2, S3])
    R1 = Room(name='R1',
              position=[a, e, L, l],
              switches_list=[S4, S5, S6, S7])
    R2 = Room(name='R2',
              position=[0, d, L, l],
              switches_list=[S8, S9, S10, S11])
    R3 = Room(name='R3',
              position=[a, d + e, L, l],
              switches_list=[S12, S13, S14, S15])
    R4 = Room(name='R4',
              position=[0, 2 * d, L, l],
              switches_list=[S16, S17, S18, S19])
    R5 = Room(name='R5',
              position=[a, 2 * d + e, L, l],
              switches_list=[S20, S21, S22, S23])
    R6 = Room(name='R6',
              position=[0, 3 * d, L, l],
              switches_list=[S24, S25, S26, S27])
    R7 = Room(name='R7',
              position=[a, 3 * d + e, L, l],
              switches_list=[S28, S29, S30, S31])
    R8 = Room(name='R8',
              position=[0, 4 * d, L, l],
              switches_list=[S32, S33, S34, S35])
    R9 = Room(name='R9',
              position=[a, 4 * d + e, L, l],
              switches_list=[S36, S37, S38, S39])
    R10 = Room(name='R10',
               position=[L - l, 5 * d, l, l],
               switches_list=[])
    R11 = Room(name='R11',
               position=[a, 5 * d + e, l, l],
               switches_list=[])
    RE = Room(name='RE',
              position=[L - l, 6 * d, l, l],
              is_exit=True)  # E pour exit ou end

    rp = 0.5
    rc1 = [7 / 8, 1 / 2]
    rc2 = [1 / 8, 1 / 2]

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp,
              relative_departure_coordinates=rc1,
              relative_arrival_coordinates=rc2)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2,
              relative_position=rp,
              relative_departure_coordinates=rc2,
              relative_arrival_coordinates=rc1)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3,
              relative_position=rp,
              relative_departure_coordinates=rc1,
              relative_arrival_coordinates=rc2)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=R4,
              relative_position=rp,
              relative_departure_coordinates=rc2,
              relative_arrival_coordinates=rc1)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R4,
              room_arrival=R5,
              relative_position=rp,
              relative_departure_coordinates=rc1,
              relative_arrival_coordinates=rc2)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R5,
              room_arrival=R6,
              relative_position=rp,
              relative_departure_coordinates=rc2,
              relative_arrival_coordinates=rc1)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R6,
              room_arrival=R7,
              relative_position=rp,
              relative_departure_coordinates=rc1,
              relative_arrival_coordinates=rc2)
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R7,
              room_arrival=R8,
              relative_position=rp,
              relative_departure_coordinates=rc2,
              relative_arrival_coordinates=rc1)
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R8,
              room_arrival=R9,
              relative_position=rp,
              relative_departure_coordinates=rc1,
              relative_arrival_coordinates=rc2)
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R9,
              room_arrival=R10,
              relative_departure_coordinates=[1 / 8, 1 / 2],
              relative_position=rp)
    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R10,
               room_arrival=R11,
               relative_position=rp)
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R11,
               room_arrival=RE,
               relative_position=rp)

    level = Maze(rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11],
                 fastest_solution='S1 S2 D0 S7 D1 S8 D2 S12 S13 S14 D3 S16 S19 D4 S21 D5 S26 D6 S29 S31 D7 S32 S33 D8 S36 S38 D9 D10 D11',
                 level_color=Levels_colors_list.FROM_HUE(0.6, sa=0.12, li=0.45),
                 name='Knight',
                 door_window_size=450,
                 keep_proportions=False)

    return level