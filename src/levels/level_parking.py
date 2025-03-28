from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def f():
    v = 1
    # 0
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    # 3
    S3 = Switch(name='S3', value=v)
    S4 = Switch(name='S4', value=v)
    S5 = Switch(name='S5')
    # 4
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8', value=v)
    # 1
    S9 = Switch(name='S9', value=v)
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    # 3
    S12 = Switch(name='S12', value=v)
    S13 = Switch(name='S13', value=v)
    S14 = Switch(name='S14')
    # 0
    S15 = Switch(name='S15')
    S16 = Switch(name='S16')
    S17 = Switch(name='S17')
    # 3
    S18 = Switch(name='S18', value=v)
    S19 = Switch(name='S19', value=v)
    S20 = Switch(name='S20')
    # 2
    S21 = Switch(name='S21')
    S22 = Switch(name='S22', value=v)
    S23 = Switch(name='S23')
    # 3
    S24 = Switch(name='S24', value=v)
    S25 = Switch(name='S25', value=v)
    S26 = Switch(name='S26')
    # 1
    S27 = Switch(name='S27', value=v)
    S28 = Switch(name='S28')
    S29 = Switch(name='S29')
    # 2
    S30 = Switch(name='S30')
    S31 = Switch(name='S31', value=v)
    S32 = Switch(name='S32')
    # 0
    S33 = Switch(name='S33')
    S34 = Switch(name='S34')
    S35 = Switch(name='S35')
    # 3
    S36 = Switch(name='S36', value=v)
    S37 = Switch(name='S37', value=v)
    S38 = Switch(name='S38')
    # 4
    S39 = Switch(name='S39')
    S40 = Switch(name='S40')
    S41 = Switch(name='S41', value=v)
    # 1
    S42 = Switch(name='S42', value=v)
    S43 = Switch(name='S43')
    S44 = Switch(name='S44')
    # 3
    S45 = Switch(name='S45', value=v)
    S46 = Switch(name='S46', value=v)
    S47 = Switch(name='S47')
    # 0
    S48 = Switch(name='S48')
    S49 = Switch(name='S49')
    S50 = Switch(name='S50')
    # 3
    S51 = Switch(name='S51', value=v)
    S52 = Switch(name='S52', value=v)
    S53 = Switch(name='S53')
    # 2
    S54 = Switch(name='S54')
    S55 = Switch(name='S55', value=v)
    S56 = Switch(name='S56')
    # 3
    S57 = Switch(name='S57', value=v)
    S58 = Switch(name='S58', value=v)
    S59 = Switch(name='S59')
    # 1
    S60 = Switch(name='S60', value=v)
    S61 = Switch(name='S61')
    S62 = Switch(name='S62')
    # 2
    S63 = Switch(name='S63')
    S64 = Switch(name='S64', value=v)
    S65 = Switch(name='S65')
    
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
    V7 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V7',
              switches=[S21, S22, S23])
    V8 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V8',
              switches=[S24, S25, S26])
    V9 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V9',
              switches=[S27, S28, S29])
    V10 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V10',
              switches=[S30, S31, S32])
    V11 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V11',
              switches=[S33, S34, S35])
    V12 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V12',
              switches=[S36, S37, S38])
    V13 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V13',
              switches=[S39, S40, S41])
    V14 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V14',
              switches=[S42, S43, S44])
    V15 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V15',
              switches=[S45, S46, S47])
    V16 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V16',
              switches=[S48, S49, S50])
    V17 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V17',
              switches=[S51, S52, S53])
    V18 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V18',
              switches=[S54, S55, S56])
    V19 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V19',
              switches=[S57, S58, S59])
    V20 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V20',
              switches=[S60, S61, S62])
    V21 = Tree(tree_list=Tree.tree_list_BIN(3),
              name='V21',
              switches=[S63, S64, S65])

    tree_list_INF_BIN_ABS = ['AND',
                             ['INFOREQU',
                              [None],
                              [None]],
                             ['EQU',
                              [None],
                              ['ABS',
                               ['SUM',
                                [None],
                                ['MINUS',
                                 [None]]]]]]
    tree_list_EQU = ['EQU',
                     [None],
                     [None]]

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
    T6 = Tree(tree_list=[None],
              name='T6',
              switches=[1])
    T7 = Tree(tree_list=[None],
              name='T7',
              switches=[1])
    T8 = Tree(tree_list=[None],
              name='T8',
              switches=[1])
    T9 = Tree(tree_list=[None],
              name='T9',
              switches=[1])
    T10 = Tree(tree_list=[None],
               name='T10',
               switches=[1])
    T11 = Tree(tree_list=tree_list_INF_BIN_ABS,
               name='T11',
               switches=[V0, 4,
                         1,
                         V0, V11])
    T12 = Tree(tree_list=tree_list_INF_BIN_ABS,
               name='T12',
               switches=[V1, 3,
                         1,
                         V1, V12])
    T13 = Tree(tree_list=tree_list_INF_BIN_ABS,
               name='T13',
               switches=[V2, 4,
                         1,
                         V2, V13, ])
    T14 = Tree(tree_list=tree_list_INF_BIN_ABS,
               name='T14',
               switches=[V3, 4,
                         1,
                         V3, V14, ])
    T15 = Tree(tree_list=tree_list_INF_BIN_ABS,
               name='T15',
               switches=[V4, 4,
                         1,
                         V4, V15, ])
    T16 = Tree(tree_list=tree_list_INF_BIN_ABS,
               name='T16',
               switches=[V5, 4,
                         1,
                         V5, V16, ])
    T17 = Tree(tree_list=tree_list_INF_BIN_ABS,
               name='T17',
               switches=[V6, 3,
                         1,
                         V6, V17, ])
    T18 = Tree(tree_list=tree_list_INF_BIN_ABS,
               name='T18',
               switches=[V7, 4,
                         1,
                         V7, V18, ])
    T19 = Tree(tree_list=tree_list_INF_BIN_ABS,
               name='T19',
               switches=[V8, 3,
                         1,
                         V8, V19, ])
    T20 = Tree(tree_list=tree_list_INF_BIN_ABS,
               name='T20',
               switches=[V9, 4,
                         1,
                         V9, V20, ])
    T21 = Tree(tree_list=tree_list_INF_BIN_ABS,
               name='T21',
               switches=[V10, 3,
                         1,
                         V10, V21, ])

    T22 = Tree(tree_list=tree_list_EQU,
               name='T22',
               switches=[V0, V11])

    T23 = Tree(tree_list=tree_list_EQU,
               name='T23',
               switches=[V1, V12, ])
    T24 = Tree(tree_list=tree_list_EQU,
               name='T24',
               switches=[V2, V13, ])
    T25 = Tree(tree_list=tree_list_EQU,
               name='T25',
               switches=[V3, V14, ])
    T26 = Tree(tree_list=tree_list_EQU,
               name='T26',
               switches=[V4, V15, ])
    T27 = Tree(tree_list=tree_list_EQU,
               name='T27',
               switches=[V5, V16, ])
    T28 = Tree(tree_list=tree_list_EQU,
               name='T28',
               switches=[V6, V17, ])
    T29 = Tree(tree_list=tree_list_EQU,
               name='T29',
               switches=[V7, V18, ])
    T30 = Tree(tree_list=tree_list_EQU,
               name='T30',
               switches=[V8, V19, ])
    T31 = Tree(tree_list=tree_list_EQU,
               name='T31',
               switches=[V9, V20, ])
    T32 = Tree(tree_list=tree_list_EQU,
               name='T32',
               switches=[V10, V21, ])
    tree_list_aux_1 = ['SUM', [None], [None]]
    tree_list_aux_2 = ['SUM', [None], ['PROD', [None], [None]]]
    T33 = Tree(tree_list=['DIFF',
                          # Horizontal
                          [None],
                          tree_list_aux_1,
                          [None],
                          tree_list_aux_1,
                          tree_list_aux_1,
                          tree_list_aux_1,
                          tree_list_aux_1,
                          tree_list_aux_1,
                          tree_list_aux_1,
                          tree_list_aux_1,
                          tree_list_aux_1,
                          tree_list_aux_1,
                          tree_list_aux_1,
                          tree_list_aux_1,
                          tree_list_aux_1,
                          tree_list_aux_1,
                          # Vertical
                          ['PROD', [None], [None]],
                          tree_list_aux_2,
                          tree_list_aux_2,
                          tree_list_aux_2,
                          tree_list_aux_2,
                          tree_list_aux_2,
                          tree_list_aux_2,
                          tree_list_aux_2,
                          tree_list_aux_2,
                          tree_list_aux_2,
                          ],
               name='T33',
               switches=[  # Line 0
                   V0,
                   1, V0,
                   V1,
                   1, V1,
                   2, V1,
                   # Line 1
                   6, V2,
                   7, V2,
                   # Line 2
                   12, V3,
                   13, V3,
                   # Line 3
                   18, V4,
                   19, V4,
                   # Line 4
                   24, V5,
                   25, V5,
                   # Line 5
                   30, V6,
                   31, V6,
                   32, V6,
                   # Column 0
                   6, V7,
                   6, 6, V7,
                   # Column 2
                   2, 6, V8,
                   8, 6, V8,
                   14, 6, V8,
                   # Column 3
                   3, 6, V9,
                   9, 6, V9,
                   # Column 5
                   5, 6, V10,
                   11, 6, V10,
                   17, 6, V10,
               ],
               cut_expression=True)
    T34 = Tree(tree_list=['EQU', [None], Tree.tree_list_BIN(3)],
               name='T34',
               switches=[4, S9, S10, S11])
    T34 = Tree(tree_list=['AND', ['EQU', [None], Tree.tree_list_BIN(15)], ['EQU', [None], Tree.tree_list_BIN(18)]],
               name='T34',
               switches=[Switch(value=12377),
                         S0, S1, S2,
                         S3, S4, S5,
                         S6, S7, S8,
                         S9, S10, S11,
                         S12, S13, S14,
                         Switch(value=103424),
                         S15, S16, S17,
                         S18, S19, S20,
                         S21, S22, S23,
                         S24, S25, S26,
                         S27, S28, S29,
                         S30, S31, S32])  # 3389010009

    dx = 0.5
    a = 1.3
    ey = 0.7
    lx = 4

    R0 = Room(name='R0',
              position=[0, 0, dx, 12],
              switches_list=[])

    R1 = Room(name='R1',
              position=[dx + a, 0, lx, ey],
              switches_list=[S0, S1, S2, ])
    R2 = Room(name='R2',
              position=[dx + a, 1, lx, ey],
              switches_list=[S3, S4, S5, ])
    R3 = Room(name='R3',
              position=[dx + a, 2, lx, ey],
              switches_list=[S6, S7, S8, ])
    R4 = Room(name='R4',
              position=[dx + a, 3, lx, ey],
              switches_list=[S9, S10, S11, ])
    R5 = Room(name='R5',
              position=[dx + a, 4, lx, ey],
              switches_list=[S12, S13, S14, ])
    R6 = Room(name='R6',
              position=[dx + a, 5, lx, ey],
              switches_list=[S15, S16, S17, ])
    R7 = Room(name='R7',
              position=[dx + a, 6, lx, ey],
              switches_list=[S18, S19, S20, ])
    R8 = Room(name='R8',
              position=[dx + a, 7, lx, ey],
              switches_list=[S21, S22, S23, ])
    R9 = Room(name='R9',
              position=[dx + a, 8, lx, ey],
              switches_list=[S24, S25, S26, ])
    R10 = Room(name='R10',
               position=[dx + a, 9, lx, ey],
               switches_list=[S27, S28, S29, ])
    R11 = Room(name='R11',
               position=[dx + a, 10, lx, ey],
               switches_list=[S30, S31, S32, ])

    R12 = Room(name='R12',
               position=[dx + 2 * a + lx, 0, lx, ey],
               switches_list=[S33, S34, S35, ])
    R13 = Room(name='R13',
               position=[dx + 2 * a + lx, 1, lx, ey],
               switches_list=[S36, S37, S38, ])
    R14 = Room(name='R14',
               position=[dx + 2 * a + lx, 2, lx, ey],
               switches_list=[S39, S40, S41, ])
    R15 = Room(name='R15',
               position=[dx + 2 * a + lx, 3, lx, ey],
               switches_list=[S42, S43, S44, ])
    R16 = Room(name='R16',
               position=[dx + 2 * a + lx, 4, lx, ey],
               switches_list=[S45, S46, S47, ])
    R17 = Room(name='R17',
               position=[dx + 2 * a + lx, 5, lx, ey],
               switches_list=[S48, S49, S50, ])
    R18 = Room(name='R18',
               position=[dx + 2 * a + lx, 6, lx, ey],
               switches_list=[S51, S52, S53, ])
    R19 = Room(name='R19',
               position=[dx + 2 * a + lx, 7, lx, ey],
               switches_list=[S54, S55, S56, ])
    R20 = Room(name='R20',
               position=[dx + 2 * a + lx, 8, lx, ey],
               switches_list=[S57, S58, S59, ])
    R21 = Room(name='R21',
               position=[dx + 2 * a + lx, 9, lx, ey],
               switches_list=[S60, S61, S62, ])
    R22 = Room(name='R22',
               position=[dx + 2 * a + lx, 10, lx, ey],
               switches_list=[S63, S64, S65, ])

    R23 = Room(name='R23',
               position=[dx + 3 * a + 2 * lx, 0, dx*1.25, 12],
               switches_list=[])
    RE = Room(name='RE',
              position=[dx + a, 12 - ey, 1, ey],
              is_exit=True)  # E pour exit ou end

    rp = 1 / 2
    rdc1 = [1, 1 / 2]
    rac1 = [0, 1 / 2]

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp,
              relative_departure_coordinates=[1, ey / 2 / 12],
              relative_arrival_coordinates=rac1)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R0,
              room_arrival=R2,
              relative_position=rp,
              relative_departure_coordinates=[1, (1 + ey / 2) / 12],
              relative_arrival_coordinates=rac1)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R0,
              room_arrival=R3,
              relative_position=rp,
              relative_departure_coordinates=[1, (2 + ey / 2) / 12],
              relative_arrival_coordinates=rac1)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R0,
              room_arrival=R4,
              relative_position=rp,
              relative_departure_coordinates=[1, (3 + ey / 2) / 12],
              relative_arrival_coordinates=rac1)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R0,
              room_arrival=R5,
              relative_position=rp,
              relative_departure_coordinates=[1, (4 + ey / 2) / 12],
              relative_arrival_coordinates=rac1)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R0,
              room_arrival=R6,
              relative_position=rp,
              relative_departure_coordinates=[1, (5 + ey / 2) / 12],
              relative_arrival_coordinates=rac1)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R0,
              room_arrival=R7,
              relative_position=rp,
              relative_departure_coordinates=[1, (6 + ey / 2) / 12],
              relative_arrival_coordinates=rac1)
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R0,
              room_arrival=R8,
              relative_position=rp,
              relative_departure_coordinates=[1, (7 + ey / 2) / 12],
              relative_arrival_coordinates=rac1)
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R0,
              room_arrival=R9,
              relative_position=rp,
              relative_departure_coordinates=[1, (8 + ey / 2) / 12],
              relative_arrival_coordinates=rac1)
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R0,
              room_arrival=R10,
              relative_position=rp,
              relative_departure_coordinates=[1, (9 + ey / 2) / 12],
              relative_arrival_coordinates=rac1)
    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R0,
               room_arrival=R11,
               relative_position=rp,
               relative_departure_coordinates=[1, (10 + ey / 2) / 12],
               relative_arrival_coordinates=rac1)

    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R1,
               room_arrival=R12,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=rac1)
    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R2,
               room_arrival=R13,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=rac1)
    D13 = Door(two_way=False,
               tree=T13,
               room_departure=R3,
               room_arrival=R14,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=rac1)
    D14 = Door(two_way=False,
               tree=T14,
               room_departure=R4,
               room_arrival=R15,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=rac1)
    D15 = Door(two_way=False,
               tree=T15,
               room_departure=R5,
               room_arrival=R16,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=rac1)
    D16 = Door(two_way=False,
               tree=T16,
               room_departure=R6,
               room_arrival=R17,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=rac1)
    D17 = Door(two_way=False,
               tree=T17,
               room_departure=R7,
               room_arrival=R18,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=rac1)
    D18 = Door(two_way=False,
               tree=T18,
               room_departure=R8,
               room_arrival=R19,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=rac1)
    D19 = Door(two_way=False,
               tree=T19,
               room_departure=R9,
               room_arrival=R20,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=rac1)
    D20 = Door(two_way=False,
               tree=T20,
               room_departure=R10,
               room_arrival=R21,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=rac1)
    D21 = Door(two_way=False,
               tree=T21,
               room_departure=R11,
               room_arrival=R22,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=rac1)

    D22 = Door(two_way=False,
               tree=T22,
               room_departure=R12,
               room_arrival=R23,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=[0, ey / 2 / 12])
    D23 = Door(two_way=False,
               tree=T23,
               room_departure=R13,
               room_arrival=R23,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=[0, (1 + ey / 2) / 12])
    D24 = Door(two_way=False,
               tree=T24,
               room_departure=R14,
               room_arrival=R23,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=[0, (2 + ey / 2) / 12])
    D25 = Door(two_way=False,
               tree=T25,
               room_departure=R15,
               room_arrival=R23,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=[0, (3 + ey / 2) / 12])
    D26 = Door(two_way=False,
               tree=T26,
               room_departure=R16,
               room_arrival=R23,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=[0, (4 + ey / 2) / 12])
    D27 = Door(two_way=False,
               tree=T27,
               room_departure=R17,
               room_arrival=R23,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=[0, (5 + ey / 2) / 12])
    D28 = Door(two_way=False,
               tree=T28,
               room_departure=R18,
               room_arrival=R23,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=[0, (6 + ey / 2) / 12])
    D29 = Door(two_way=False,
               tree=T29,
               room_departure=R19,
               room_arrival=R23,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=[0, (7 + ey / 2) / 12])
    D30 = Door(two_way=False,
               tree=T30,
               room_departure=R20,
               room_arrival=R23,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=[0, (8 + ey / 2) / 12])
    D31 = Door(two_way=False,
               tree=T31,
               room_departure=R21,
               room_arrival=R23,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=[0, (9 + ey / 2) / 12])
    D32 = Door(two_way=False,
               tree=T32,
               room_departure=R22,
               room_arrival=R23,
               relative_position=rp,
               relative_departure_coordinates=rdc1,
               relative_arrival_coordinates=[0, (10 + ey / 2) / 12])

    D33 = Door(two_way=False,
               tree=T33,
               room_departure=R23,
               room_arrival=R0,
               relative_position=rp,
               relative_departure_coordinates=[0, (11 + ey / 4) / 12],
               relative_arrival_coordinates=[1, (11 + ey / 4) / 12])
    D34 = Door(two_way=False,
               tree=T34,
               room_departure=R0,
               room_arrival=RE,
               relative_position=rp,
               relative_departure_coordinates=[1, (12 - ey / 2) / 12],
               relative_arrival_coordinates=[0, 1 / 2])

    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19,
                             R20, R21, R22, R23] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19,
                             D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30, D31, D32, D33, D34],
                 fastest_solution="D0 S0 D11 S33 D22 D33 D7 S21 S22 D18 S54 S55 D29 D33 D7 S21 D18 S54 D29 D33 D3 S9 D14 S42 D25 D33 D8 S24 D19 S57 D30 D33 D8 S24 S25 D19 S57 S58 D30 D33 D5 S15 D16 S48 D27 D33 D5 S15 S16 D16 S48 S49 D27 D33 D5 S15 D16 S48 D27 D33 D8 S24 S25 D19 S57 S58 D30 D33 D8 S24 D19 S57 D30 D33 D3 S9 D14 S42 D25 D33 D7 S21 D18 S54 D29 D33 D0 S0 D11 S33 D22 D33 D7 S21 S22 D18 S54 S55 D29 D33 D7 S21 D18 S54 D29 D33 D3 S9 D14 S42 D25 D33 D7 S21 S22 S23 D18 S54 S55 S56 D29 D33 D8 S24 D19 S57 D30 D33 D8 S24 S25 D19 S57 S58 D30 D33 D8 S24 D19 S57 D30 D33 D4 S12 D15 S45 D26 D33 D4 S12 S13 D15 S45 S46 D26 D33 D4 S12 D15 S45 D26 D33 D8 S24 D19 S57 D30 D33 D8 S24 S25 D19 S57 S58 D30 D33 D8 S24 D19 S57 D30 D33 D3 S9 D14 S42 D25 D33 D9 S27 S28 D20 S60 S61 D31 D33 D2 S6 S7 S8 D13 S39 S40 S41 D24 D33 D10 S30 S31 D21 S63 S64 D32 D33 D5 S15 S16 S17 D16 S48 S49 S50 D27 D33 D9 S27 D20 S60 D31 D33 D3 S9 S10 D14 S42 S43 D25 D33 D3 S9 D14 S42 D25 D33 D8 S24 D19 S57 D30 D33 D8 S24 S25 D19 S57 S58 D30 D33 D8 S24 D19 S57 D30 D33 D4 S12 D15 S45 D26 D33 D7 S21 S22 S23 D18 S54 S55 S56 D29 D33 D7 S21 D18 S54 D29 D33 D7 S21 S22 D18 S54 S55 D29 D33 D4 S12 D15 S45 D26 D33 D8 S24 D19 S57 D30 D33 D0 S0 D11 S33 D22 D33 D7 S21 D18 S54 D29 D33 D8 S24 S25 D19 S57 S58 D30 D33 D8 S24 D19 S57 D30 D33 D3 S9 D14 S42 D25 D33 D3 S9 S10 D14 S42 S43 D25 D33 D3 S9 D14 S42 D25 D33 D8 S24 D19 S57 D30 D33 D8 S24 S25 D19 S57 S58 D30 D33 D9 S27 D20 S60 D31 D33 D5 S15 S16 S17 D16 S48 S49 S50 D27 D33 D5 S15 D16 S48 D27 D33 D5 S15 S16 D16 S48 S49 D27 D33 D5 S15 D16 S48 D27 D33 D8 S24 S25 D19 S57 S58 D30 D33 D8 S24 D19 S57 D30 D33 D3 S9 D14 S42 D25 D33 D7 S21 D18 S54 D29 D33 D0 S0 D11 S33 D22 D33 D9 S27 D20 S60 D31 D33 D3 S9 S10 D14 S42 S43 D25 D33 D3 S9 D14 S42 D25 D33 D8 S24 D19 S57 D30 D33 D6 S18 D17 S51 D28 D33 D6 S18 S19 D17 S51 S52 D28 D33 D6 S18 D17 S51 D28 D33 D8 S24 S25 D19 S57 S58 D30 D33 D8 S24 D19 S57 D30 D33 D4 S12 D15 S45 D26 D33 D9 S27 S28 S29 D20 S60 S61 S62 D31 D33 D4 S12 S13 D15 S45 S46 D26 D33 D4 S12 D15 S45 D26 D33 D8 S24 D19 S57 D30 D33 D1 S3 D12 S36 D23 D33 D8 S24 S25 D19 S57 S58 D30 D33 D2 S6 D13 S39 D24 D33 D2 S6 S7 D13 S39 S40 D24 D33 D10 S30 D21 S63 D32 D33 D4 S12 S13 S14 D15 S45 S46 S47 D26 D33 D9 S27 S28 S29 D20 S60 S61 S62 D31 D33 D6 S18 D17 S51 D28 D33 D6 S18 S19 D17 S51 S52 D28 D33 D6 S18 D17 S51 D28 D33 D8 S24 D19 S57 D30 D33 D3 S9 D14 S42 D25 D33 D3 S9 S10 D14 S42 S43 D25 D33 D9 S27 D20 S60 D31 D33 D9 S27 S28 D20 S60 S61 D31 D33 D4 S12 S13 S14 D15 S45 S46 S47 D26 D33 D10 S30 D21 S63 D32 D33 D1 S3 D12 S36 D23 D33 D0 S0 D11 S33 D22 D33 D7 S21 D18 S54 D29 D33 D3 S9 D14 S42 D25 D33 D8 S24 D19 S57 D30 D33 D6 S18 D17 S51 D28 D33 D6 S18 S19 D17 S51 S52 D28 D33 D6 S18 D17 S51 D28 D33 D10 S30 S31 D21 S63 S64 D32 D33 D10 S30 D21 S63 D32 D33 D34",
                 level_color=get_color(),
                 name='Parking',
                 door_window_size=375,
                 keep_proportions=True,
                 y_separation=27,
                 border=40)
                 #do_not_write_trees_always_open=True)

    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.1, sa=0.15, li=0.6)
    lcolor.surrounding_color = [255, 255, 255]
    lcolor.contour_color = [255, 255, 255]
    return lcolor