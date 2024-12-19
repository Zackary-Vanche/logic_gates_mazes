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

    V0 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V0',
              switches=[S0, S1, S2])
    V1 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V1',
              switches=[S3, S4, S5])
    V2 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V2',
              switches=[S6, S7, S8])
    V3 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V3',
              switches=[S9, S10, S11])
    V4 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V4',
              switches=[S12, S13, S14])
    V5 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V5',
              switches=[S15, S16, S17])
    V6 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V6',
              switches=[S18, S19, S20])

    for S in [S6,
              S10,
              S12, S13,
              S17,
              S18, S20]:
        S.set_value(1, update_doors=False)

    tree_list_EQU_BIN3 = ['EQU', [None], [None]]
    tree_list_0_IN = ['IN', [None], [None], [None]]

    T0 = Tree(tree_list=['EQUSET'] + [[None]] * 12,
              name='T0',
              switches=[V1, V2, V3, V4, V5, V6,
                        0, 1, 2, 3, 4, 5],
              cut_expression=True)
    T1 = Tree(tree_list=[None],
              name='T1',
              switches=[1])
    T2 = Tree(tree_list=[None],
              name='T2',
              switches=[1])
    T3 = Tree(tree_list=['AND',
                         ['EQU', [None], [None]],
                         ['EQU', Tree.tree_list_BIN(18), [None]]],
              name='T3',
              switches=[0, V0,
                        S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20,
                        69987],
              cut_expression=True)
    T4 = Tree(tree_list=tree_list_EQU_BIN3,
              name='T4',
              switches=[V0, 1])
    T5 = Tree(tree_list=tree_list_EQU_BIN3,
              name='T5',
              switches=[V0, 1])
    T6 = Tree(tree_list=tree_list_EQU_BIN3,
              name='T6',
              switches=[V0, 2])
    T7 = Tree(tree_list=['AND', tree_list_EQU_BIN3, tree_list_0_IN],
              name='T7',
              switches=[V0, 2,
                        0,
                        V2, V3])
    T8 = Tree(tree_list=tree_list_EQU_BIN3,
              name='T8',
              switches=[V0, 3])
    T9 = Tree(tree_list=tree_list_EQU_BIN3,
              name='T9',
              switches=[V0, 3])
    T10 = Tree(tree_list=tree_list_EQU_BIN3,
               name='T10',
               switches=[V0, 4])
    T11 = Tree(tree_list=['AND', tree_list_EQU_BIN3, tree_list_0_IN],
               name='T11',
               switches=[V0, 4,
                         0,
                         V5, V6])
    T12 = Tree(tree_list=tree_list_EQU_BIN3,
               name='T12',
               switches=[V0, 5])
    T13 = Tree(tree_list=tree_list_EQU_BIN3,
               name='T13',
               switches=[V0, 5])
    T14 = Tree(tree_list=['AND', tree_list_EQU_BIN3, tree_list_0_IN],
               name='T14',
               switches=[V0, 5,
                         0,
                         V1, V4])
    T15 = Tree(tree_list=tree_list_EQU_BIN3,
               name='T15',
               switches=[V0, 6])
    T16 = Tree(tree_list=tree_list_EQU_BIN3,
               name='T16',
               switches=[V0, 6])
    T17 = Tree(tree_list=['AND', tree_list_EQU_BIN3, tree_list_0_IN],
               name='T17',
               switches=[V0, 6,
                         0,
                         V2, V5])
    T18 = Tree(tree_list=tree_list_EQU_BIN3,
               name='T18',
               switches=[V0, 7])
    T19 = Tree(tree_list=tree_list_EQU_BIN3,
               name='T19',
               switches=[V0, 7])
    T20 = Tree(tree_list=['AND', tree_list_EQU_BIN3, tree_list_0_IN],
               name='T20',
               switches=[V0, 7,
                         0,
                         V3, V6])
    T21 = Tree(tree_list=tree_list_EQU_BIN3,
               name='T21',
               switches=[V0, 2])
    T22 = Tree(tree_list=['AND', tree_list_EQU_BIN3, tree_list_0_IN],
               name='T22',
               switches=[V0, 1,
                         0,
                         V1, V2])
    T23 = Tree(tree_list=tree_list_EQU_BIN3,
               name='T23',
               switches=[V0, 4])
    T24 = Tree(tree_list=['AND', tree_list_EQU_BIN3, tree_list_0_IN],
               name='T24',
               switches=[V0, 3,
                         0,
                         V4, V5])
    

    ex = 0.8
    ey = 0.8

    R0 = Room(name='R0',
              position=[1, ey + 1, ex, 1 + 6 * ey],
              switches_list=[S0, S1, S2, ])
    R1 = Room(name='R1',
              position=[2 + ex, ey / 2, 2 + ex * 3, ey / 2],
              switches_list=[])
    R2 = Room(name='R2',
              position=[5 + 4 * ex, ey + 1, 0.57 * ex, 1 + 6 * ey],
              switches_list=[])
    R3 = Room(name='R3',
              position=[2 + ex, 3 + 7 * ey, 2 + ex * 3, ey / 2],
              switches_list=[])
    R4 = Room(name='R4',
              position=[2 + ex, ey + 1, ex, ey * 3],
              switches_list=[S3, S4, S5])
    R5 = Room(name='R5',
              position=[3 + 2 * ex, ey + 1, ex, ey * 3],
              switches_list=[S6, S7, S8, ])
    R6 = Room(name='R6',
              position=[4 + 3 * ex, ey + 1, ex, ey * 3],
              switches_list=[S9, S10, S11, ])
    R7 = Room(name='R7',
              position=[2 + ex, 2 + 4 * ey, ex, ey * 3],
              switches_list=[S12, S13, S14, ])
    R8 = Room(name='R8',
              position=[3 + 2 * ex, 2 + 4 * ey, ex, ey * 3],
              switches_list=[S15, S16, S17, ])
    R9 = Room(name='R9',
              position=[4 + 3 * ex, 2 + 4 * ey, ex, ey * 3],
              switches_list=[S18, S19, S20, ])
    RE = Room(name='RE',
              position=[1, 3 + 6 * ey, ex, 1.5 * ey],
              is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=True,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1, 0],
              relative_arrival_coordinates=[0, 1])
    D1 = Door(two_way=True,
              tree=T1,
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=[1, 1],
              relative_arrival_coordinates=[0, 0])
    D2 = Door(two_way=True,
              tree=T2,
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[1, 0])
    D3 = Door(two_way=True,
              tree=T3,
              room_departure=R3,
              room_arrival=RE,
              relative_departure_coordinates=[0, 1 / 2],
              relative_arrival_coordinates=[0.85, 53 / 64])

    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R0,
              room_arrival=R4,
              relative_departure_coordinates=[1 / 2, 1.5 * ex / (1 + 6 * ex)])
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R4,
              room_arrival=R5)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R5,
              room_arrival=R6)
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R6,
              room_arrival=R2,
              relative_departure_coordinates=[1, 1 / 2],
              relative_arrival_coordinates=[0, 1.5 * ey / (1 + 6 * ey)])

    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R0,
              room_arrival=R7,
              relative_departure_coordinates=[1 / 2, (1 + 4.5 * ex) / (1 + 6 * ex)])
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R7,
              room_arrival=R8)
    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R8,
               room_arrival=R9)
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R9,
               room_arrival=R2,
               relative_departure_coordinates=[1, 1 / 2],
               relative_arrival_coordinates=[0, (1 + 4.5 * ey) / (1 + 6 * ey)])

    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R1,
               room_arrival=R4,
               relative_departure_coordinates=[0.5 * ex / (2 + ex * 3), 1],
               relative_arrival_coordinates=[1 / 2, 0])
    D13 = Door(two_way=False,
               tree=T13,
               room_departure=R4,
               room_arrival=R7)
    D14 = Door(two_way=False,
               tree=T14,
               room_departure=R7,
               room_arrival=R3,
               relative_departure_coordinates=[1 / 2, 1],
               relative_arrival_coordinates=[0.5 * ex / (2 + ex * 3), 0])

    D15 = Door(two_way=False,
               tree=T15,
               room_departure=R1,
               room_arrival=R5,
               relative_departure_coordinates=[(1 + 1.5 * ex) / (2 + ex * 3), 1],
               relative_arrival_coordinates=[1 / 2, 0])
    D16 = Door(two_way=False,
               tree=T16,
               room_departure=R5,
               room_arrival=R8)
    D17 = Door(two_way=False,
               tree=T17,
               room_departure=R8,
               room_arrival=R3,
               relative_departure_coordinates=[1 / 2, 1],
               relative_arrival_coordinates=[(1 + 1.5 * ex) / (2 + ex * 3), 0])

    D18 = Door(two_way=False,
               tree=T18,
               room_departure=R1,
               room_arrival=R6,
               relative_departure_coordinates=[(2 + 2.5 * ex) / (2 + ex * 3), 1],
               relative_arrival_coordinates=[1 / 2, 0])
    D19 = Door(two_way=False,
               tree=T19,
               room_departure=R6,
               room_arrival=R9)
    D20 = Door(two_way=False,
               tree=T20,
               room_departure=R9,
               room_arrival=R3,
               relative_departure_coordinates=[1 / 2, 1],
               relative_arrival_coordinates=[(2 + 2.5 * ex) / (2 + ex * 3), 0])

    D21 = Door(two_way=False,
               tree=T21,
               room_departure=R1,
               room_arrival=R5,
               relative_departure_coordinates=[ex / (2 + ex * 3), 1],
               relative_arrival_coordinates=[0, 0],
               relative_position=0.6)
    D22 = Door(two_way=False,
               tree=T22,
               room_departure=R5,
               room_arrival=R1,
               relative_departure_coordinates=[1, 0],
               relative_arrival_coordinates=[(2 + 2 * ex) / (2 + ex * 3), 1])
    D23 = Door(two_way=False,
               tree=T23,
               room_departure=R3,
               room_arrival=R8,
               relative_departure_coordinates=[ex / (2 + ex * 3), 0],
               relative_arrival_coordinates=[0, 1],
               relative_position=0.6)
    D24 = Door(two_way=False,
               tree=T24,
               room_departure=R8,
               room_arrival=R3,
               relative_departure_coordinates=[1, 1],
               relative_arrival_coordinates=[(2 + 2 * ex) / (2 + ex * 3), 0],
               relative_position=0.55)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, RE],
                 doors_list=[D0, D1, D2, D3,
                             D4, D5, D6, D7,
                             D8, D9, D10, D11,
                             D12, D13, D14,
                             D15, D16, D17,
                             D18, D19, D20,
                             D21, D22, D23, D24, ],
                 fastest_solution="S0 D4 S3 D5 S6 D22 D0 S0 S1 D0 D21 S7 D6 S10 D7 D1 D0 S0 S2 D0 D18 S9 S11 D19 S18 S20 D20 D2 D1 D0 S0 S1 D0 D1 D2 D23 S17 D10 S20 D11 D1 D0 S1 D0 D15 S7 D16 S16 D17 D2 D1 D0 S0 S1 S2 D4 S3 D5 S6 D22 D0 S2 D0 D12 S3 S4 D13 S12 S13 D14 D2 D1 D0 S1 S2 D8 S13 D9 S16 D24 D2 D1 D0 S0 S1 S2 D0 D1 D2 D23 S17 D10 S20 D11 D1 D0 S0 S1 D0 D18 S9 S11 D19 S18 S20 D20 D2 D1 D0 S0 S2 D0 D21 S6 D6 S9 D7 D1 D0 S2 D0 D15 S8 D16 S17 D17 D2 D1 D0 S0 S2 D8 S13 D9 S16 D24 D2 D1 D0 S1 S2 D0 D12 S3 S4 D13 S12 S13 D14 D2 D1 D0 S2 D4 S5 D5 S8 D22 D0 S0 S1 D0 D21 S6 D6 S9 D7 D1 D0 S0 S2 D0 D18 S9 S11 D19 S18 S20 D20 D2 D1 D0 S0 S1 D0 D1 D2 D23 S16 D10 S19 D11 D1 D0 S1 D0 D15 S6 D16 S15 D17 D2 D1 D0 S0 S1 S2 D4 S5 D5 S8 D22 D0 S2 D0 D12 S3 S4 D13 S12 S13 D14 D2 D1 D0 S0 S2 D0 D1 D2 D3",
                 level_color=Levels_colors_list.FROM_HUE(0.4, sa=1, li=0.95),
                 name='Puzzle',
                 door_window_size=444,
                 keep_proportions=True,
                 border=20)

    return level