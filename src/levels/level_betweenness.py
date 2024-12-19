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

    SN2 = Switch(value=2)

    SN3 = Switch(value=3)
    SN5 = Switch(value=5)
    SN6 = Switch(value=6)
    SN9 = Switch(value=9)
    SN10 = Switch(value=10)
    SN12 = Switch(value=12)

    tree_list_0 = ['EQU', [None], ['SUM'] + [[None]] * 4, ]

    Slist = [S0, S1, S2, S3,
             S4, S5, S6, S7,
             S8, S9, S10, S11,
             S12, S13, S14, S15,
             S16, S17, S18, S19,
             S20, S21, S22, S23]

    T0 = Tree(tree_list=tree_list_0,
              name='T0',
              switches=[SN2, S0, S1, S2, S3, ])
    T1 = Tree(tree_list=tree_list_0,              
              name='T1',
              switches=[SN2, S4, S5, S6, S7, ])
    T2 = Tree(tree_list=tree_list_0,
              name='T2',
              switches=[SN2, S8, S9, S10, S11, ])
    T3 = Tree(tree_list=tree_list_0,
              name='T3',
              switches=[SN2, S12, S13, S14, S15, ])
    T4 = Tree(tree_list=tree_list_0,
              name='T4',
              switches=[SN2, S16, S17, S18, S19, ])
    n = 5
    T5 = Tree(tree_list=['AND', tree_list_0, ['BETWEEN'] + [[None]] * (3 * n + 1) + [Tree.tree_list_BIN(4)] * 6,
                         ['INF', Tree.tree_list_BIN(4), Tree.tree_list_BIN(4)]],
              name='T5',
              switches=[SN2, S20, S21, S22, S23, ] + [Switch(value=n),
                                                      SN3, SN6, SN9,
                                                      SN12, SN10, SN6,
                                                      SN6, SN12, SN5,
                                                      SN3, SN12, SN6,
                                                      SN5, SN3, SN9, ] + Slist + [S0, S1, S2, S3,
                                                                                  S16, S17, S18, S19, ],
              cut_expression=True,
              cut_expression_separator=')')

    ex = 0.9
    ey = 0.15
    a = 2

    R0 = Room(name='R0',
              position=[0, 0, a, 3 + ey],
              switches_list=[S0, S1, S2, S3, ])
    R1 = Room(name='R1',
              position=[0, 4, a, 3 + ey],
              switches_list=[S4, S5, S6, S7, ])
    R2 = Room(name='R2',
              position=[3 - ex, 5, 2, 2 + ey],
              switches_list=[S8, S9, S10, S11, ])
    R3 = Room(name='R3',
              position=[6 - 2 * ex, 4, a, 3 + ey],
              switches_list=[S12, S13, S14, S15, ])
    R4 = Room(name='R4',
              position=[6 - 2 * ex, 0, a, 3 + ey],
              switches_list=[S16, S17, S18, S19, ])
    R5 = Room(name='R5',
              position=[3 - ex, 0, 2, 2 + ey],
              switches_list=[S20, S21, S22, S23, ])
    dE = 0.35
    RE = Room(name='RE',
              position=[3 - ex, 3 + dE / 2, 2, 1 + ey - dE],
              is_exit=True)  # E pour exit ou end

    p = 0.3

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=[1, 0],
              relative_arrival_coordinates=[1, 0],
              relative_position=p)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=[0, 0],
              relative_arrival_coordinates=[0, 0],
              relative_position=1 - p)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=R4)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R4,
              room_arrival=R5,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[0, 1],
              relative_position=p)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R5,
              room_arrival=RE,
              relative_departure_coordinates=[0.15, 1],
              relative_arrival_coordinates=[0.15, 1 / 2],
              relative_position=0.5)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5],
                 fastest_solution='S0 S2 D0 S4 S5 D1 S10 S11 D2 S13 S15 D3 S17 S18 D4 S20 S23 D5',
                 level_color=Levels_colors_list.FROM_HUE(0.57, sa=0.3, li=0.5),
                 name='Betweenness',
                 door_window_size=333,
                 keep_proportions=True)

    return level