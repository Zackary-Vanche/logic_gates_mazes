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
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6', value=1)
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
    
    Slist0 = [S0, S1, S2]
    Slist1 = [S3, S4, S5, S6]
    Slist2 = [S11, S12, S13]
    Slist3 = [S17, S18]
    Slist4 = [S21, S22, S23]
    Slist5 = [S24, S25, S26]
    Slist6 = [S19, S20]
    Slist7 = [S14, S15, S16]
    Slist8 = [S7, S8, S9, S10]

    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist0)),
          name='V0',
          switches=Slist0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(len(Slist1)),
          name='V1',
          switches=Slist1)
    V2 = Tree(tree_list=Tree.tree_list_BIN(len(Slist2)),
          name='V2',
          switches=Slist2)
    V3 = Tree(tree_list=Tree.tree_list_BIN(len(Slist3)),
          name='V3',
          switches=Slist3)
    V4 = Tree(tree_list=Tree.tree_list_BIN(len(Slist4)),
          name='V4',
          switches=Slist4)
    V5 = Tree(tree_list=Tree.tree_list_BIN(len(Slist5)),
          name='V5',
          switches=Slist5)
    V6 = Tree(tree_list=Tree.tree_list_BIN(len(Slist6)),
          name='V6',
          switches=Slist6)
    V7 = Tree(tree_list=Tree.tree_list_BIN(len(Slist7)),
          name='V7',
          switches=Slist7)
    V8 = Tree(tree_list=Tree.tree_list_BIN(len(Slist8)),
          name='V8',
          switches=Slist8)
    
    V9 = Tree(tree_list=['EQU', [None], ['SUM', [None], [None]]],
          name='V9',
          switches=[V4, V5, 1])

    tree_list_EQU_plus1_BIN3 = ['EQU', Tree.tree_list_BIN(3), ['SUM', Tree.tree_list_BIN(3), [None]]]

    # 17 18 3 4 5 6 S0
    # 11 12 13 3 4 5 6 S1
    T0 = Tree(tree_list=['AND',
                         ['OR',
                          Tree.tree_list_NOT,
                          Tree.tree_list_EQU(2),
                          Tree.tree_list_EQU(2),
                          Tree.tree_list_EQU(2),
                          Tree.tree_list_EQU(2),],
                         ['OR',
                          Tree.tree_list_NOT,
                          Tree.tree_list_EQU(2),
                          Tree.tree_list_EQU(2),
                          Tree.tree_list_EQU(2),
                          Tree.tree_list_EQU(2),
                          ],
                         Tree.tree_list_OR(2), ],
              name='T0',
              switches=[
                  S0,
                  V3, 3,
                  V1, 15,
                  V3, 0,
                  V1, 0,
                  S1,
                  V2, 5,
                  V1, 15,
                  V2, 0,
                  V1, 0,
                  S0, S1,
              ],
              cut_expression_depth_1=True)

    T1 = Tree(tree_list=['AND',
                         [None],
                         ['OR'] + [Tree.tree_list_EQU(2)]*4
                         ],
              name='T1',
              switches=[S2,
                        V3, 3, 
                        V2, 5, 
                        V3, 0, 
                        V2, 0, 
                        ])
    T2 = Tree(tree_list=[None],
              name='T2',
              switches=[S1])

    T3 = Tree(tree_list=[None],
              name='T3',
              switches=[S0])

    T4 = Tree(tree_list=Tree.tree_list_AND(2),
              name='T4',
              switches=[S1, V9])

    T5 = Tree(tree_list=[None],
              name='T5',
              switches=[S2])

    T6 = Tree(tree_list=['AND', Tree.tree_list_OR(2), [None]],
              name='T6',
              switches=[S0, S2, V9])

    T7 = Tree(tree_list=['AND',
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', [None], [None]],
                         ['EQU', [None], [None]],
                         ['EQU', [None], [None]]
                         ],
              name='T7',
              switches=[V6, V7, V8, 8,
                        V3, V6,
                        V2, V7,
                        V1, V8,
                        ])
    T8 = Tree(tree_list=['EQU', Tree.tree_list_SUM(3), [None]],
              name='T8',
              switches=[V1, V2, V3, 8])
    T9 = Tree(tree_list=Tree.tree_list_EQU(2),
              name='T9',
              switches=[V4, V5])
    T10 = Tree(tree_list=Tree.tree_list_EQU(2),
               name='T10',
               switches=[V3, V6])
    T11 = Tree(tree_list=Tree.tree_list_EQU(2),
               name='T11',
               switches=[V2, V7])
    T12 = Tree(tree_list=Tree.tree_list_EQU(2),
               name='T12',
               switches=[V1, V8])
    T13 = Tree(tree_list=['AND'] + [Tree.tree_list_EQU(2)]*9,
               name='T13',
               switches=[V0, 0,
                         V1, 4,
                         V2, 4,
                         V3, 0,
                         V4, 7,
                         V5, 7,
                         V6, 0,
                         V7, 4,
                         V8, 4,
                         ])

    ex = 0.9
    ey = 1.5
    dy = 2.8
    a = 0.3

    symetric = 0
    if symetric:
        d3 = 3
    else:
        d3 = 3.2

    epsilonx = 0.1

    R0 = Room(name='R0',
              position=[5 + a - epsilonx, 2 * dy, ex, 2 * dy + ey],
              switches_list=Slist0)
    R1 = Room(name='R1',
              position=[0, 4 * dy, 4, ey],
              switches_list=Slist1)
    R2 = Room(name='R2',
              position=[symetric, 3 * dy, d3, ey],
              switches_list=Slist2)
    R3 = Room(name='R3',
              position=[1 - symetric, 2 * dy, d3, ey],
              switches_list=Slist3)
    R4 = Room(name='R4',
              position=[symetric, 1 * dy, d3, ey],
              switches_list=Slist4)
    R5 = Room(name='R5',
              position=[7.1 + a + ex, 1 * dy, 3 * ex, ey],
              switches_list=Slist5)
    R6 = Room(name='R6',
              position=[7.1 + a + ex, 2 * dy, 3 * ex, ey],
              switches_list=Slist6)
    R7 = Room(name='R7',
              position=[7.1 + a + ex, 3 * dy, 3 * ex, ey],
              switches_list=Slist7)
    R8 = Room(name='R8',
              position=[7.1 + a, 4 * dy, 4 * ex, ey],
              switches_list=Slist8)
    le = 1
    position_RE = [5 + a - epsilonx - le / 2, 1 * dy, ex + le, ey]
    RE = Room(name='RE',
              position=position_RE,
              is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R1,
              room_arrival=R0,
              relative_departure_coordinates=[1, 1 / 2],
              relative_arrival_coordinates=[0, (2 * dy + ey / 2) / (2 * dy + ey)])
    if symetric:
        rp2 = 1 / 2
    else:
        rp2 = 0.725
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R2,
              room_arrival=R0,
              relative_departure_coordinates=[1, 1 / 2],
              relative_arrival_coordinates=[0, (1 * dy + ey / 2) / (2 * dy + ey)],
              relative_position=rp2)
    if symetric:
        rdc4 = [(d3 - 1.5) / d3, 1 / 2]
        rac4 = [(4 - 1.5) / 4, 1 / 2]
    else:
        rdc4 = [1.5 / d3, 1 / 2]
        rac4 = [1.5 / 4, 1 / 2]
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R1,
              relative_departure_coordinates=rdc4,
              relative_arrival_coordinates=rac4)
    if symetric:
        rdc6 = [(d3 - 2.75) / d3, 1 / 2]
        rac6 = [(4 - 3.75) / 4, 1 / 2]
    else:
        rdc6 = [2.7 / d3, 1 / 2]
        rac6 = [3.7 / 4, 1 / 2]
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=R1,
              relative_departure_coordinates=rdc6,
              relative_arrival_coordinates=rac6)
    if symetric:
        rdc8 = [(d3 - 0.5) / d3, 1 / 2]
        rac8 = [(d3 - 0.5) / d3, 1 / 2]
    else:
        rdc8 = [0.5 / d3, 1 / 2]
        rac8 = [0.5 / d3, 1 / 2]
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R4,
              room_arrival=R2,
              relative_departure_coordinates=rdc8,
              relative_arrival_coordinates=rac8)
    if symetric:
        rdc10 = [(d3 - 1) / d3, 1 / 2]
        rac10 = [(d3 - 2) / d3, 1 / 2]
    else:
        rdc10 = [1 / d3, 1 / 2]
        rac10 = [2 / d3, 1 / 2]
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R3,
              room_arrival=R2,
              relative_departure_coordinates=rdc10,
              relative_arrival_coordinates=rac10)
    if symetric:
        rdc12 = [(d3 - 2.5) / d3, 1 / 2]
        rac12 = [(d3 - 1.5) / d3, 1 / 2]
    else:
        rdc12 = [2.5 / d3, 1 / 2]
        rac12 = [1.5 / d3, 1 / 2]
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R4,
              room_arrival=R3,
              relative_departure_coordinates=rdc12,
              relative_arrival_coordinates=rac12)
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R0,
              room_arrival=R4,
              relative_departure_coordinates=[0, 0],
              relative_arrival_coordinates=[1, 1])
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R0,
              room_arrival=R5,
              relative_departure_coordinates=[1, 0],
              relative_arrival_coordinates=[0, 1])
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R5,
              room_arrival=R6,
              relative_departure_coordinates=[1 / 2, 1 / 2],
              relative_arrival_coordinates=[1 / 2, 1 / 2])
    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R6,
               room_arrival=R7)
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R7,
               room_arrival=R8,
               relative_arrival_coordinates=[2.5 / 4, 1 / 2])
    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R8,
               room_arrival=R0,
               relative_departure_coordinates=[0, 1 / 2],
               relative_arrival_coordinates=[1, (2 * dy + ey / 2) / (2 * dy + ey)])
    D13 = Door(two_way=False,
               tree=T13,
               room_departure=R0,
               room_arrival=RE,
               relative_departure_coordinates=[1 / 2, 0],
               relative_arrival_coordinates=[1 / 2, 1],
               relative_position=1 / 2)

    solution = """D8
D9
D10
D11
S10 D12
S1 D7
S21 D4
S11 S13 D2
S3 S4 S6 D0
D8
S24 D9
D10
S14 S16 D11
S7 S8 S10 D12
S1 S2 D7
S22 S21 D6
S17 S18 D5
S11 S12 S13 D1
D8
S24 S25 D9
S19 S20 D10
S14 S15 S16 D11
D12
S0 S2 D7
S21 D6
S17 S18 D3
S3 S5 D0
D8
S24 D9
S19 S20 D10
D11
S7 S9 D12
S0 S2 D7
S23 S21 S22 D6
S18 D5
S12 D1
D8
S24 S25 S26 D9
S20 D10
S15 D11
D12
S1 S2 D7
S21 D4
S11 S13 D2
S3 S4 S5 D0
D8
S24 D9
D10
S14 S16 D11
S7 S8 S9 D12
S1 S2 D7
S21 S22 D6
S17 D5
S11 D1
D8
S24 S25 D9
S19 D10
S14 D11
D12
S0 S2 D7
S21 D6
S17 S18 D3
S3 S5 D0
S0 D8
S24 D9
S19 S20 D10
D11
S7 S9 D12
D13
""".replace('\n', ' ')

    solution = '''D8
D9
D10
D11
S10 D12
S1 S2 D7
S21 D4
D1
D8
S24 D9
D10
D11
D12
D7
S21 S22 D4
D1
D8
S24 S25 D9
D10
D11
D12
D7
S21 D4
D1
D8
S24 D9
D10
D11
D12
D7
S21 S22 S23 D4
D1
D8
S24 S25 S26 D9
D10
D11
D12
D7
S21 D6
S18 D5
S11 S13 D2
S3 S6 D0
D8
S24 D9
S20
D10
S14 S16 D11
S7 S10 D12
D7
S21 S22 D6
S17 D5
S11 D1
D8
S24 S25 D9
S19 D10
S14 D11
D12
S0 S1 D7
S21 D6
S17 S18
D3
S3 S5 D0
D8
S24 D9
S19 S20 D10
D11
S7 S9 D12
S0 S2 D13'''.replace('\n', ' ')

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13],
                 fastest_solution='S1 S2 D8 D9 D10 D11 S10 D12 D7 S21 D4 D1 D8 S24 D9 D10 D11 D12 D7 S21 S22 D4 D1 D8 S24 S25 D9 D10 D11 D12 D7 S21 D4 D1 D8 S24 D9 D10 D11 D12 D7 S21 S22 S23 D4 D1 D8 S24 S25 S26 D9 D10 D11 D12 D7 S21 D6 S18 D5 S11 S13 D2 S3 S6 D0 S0 S1 D8 S24 D9 S20 D10 S14 S16 D11 S7 S10 D12 D7 S21 S22 D6 S17 D5 S11 D1 D8 S24 S25 D9 S19 D10 S14 D11 D12 D7 S21 D6 S17 S18 D3 S3 S5 D0 S0 S2 D8 S24 D9 S19 S20 D10 D11 S7 S9 D12 D13',
                 level_color=get_color(),
                 name='Water pouring',
                 door_window_size=350,
                 keep_proportions=True)

    return level

def get_color():
    return Levels_colors_list.FROM_HUE(0.58, sa=0.8, li=0.35)