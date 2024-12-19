from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def f(fast_solution_finding=False):

    a = 7
    b = 2

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
    
    Slist_0 = [S0, S1]
    Slist_1 = [S2, S3]
    Slist_2 = [S4, S5]
    Slist_3 = [S6, S7]
    Slist_4 = [S8, S9]
    Slist_5 = [S10, S11]
    Slist_6 = [S12, S13]
    Slist_7 = [S14, S15]
    Slist_8 = [S16, S17]
    Slist_9 = [S18, S19]
    Slist_10 = [S20, S21]
    Slist_11 = [S22, S23]
    Slist_12 = [S24, S25]
    Slist_13 = [S26, S27]
    Slist_14 = [S28, S29]
    Slist_15 = [S30, S31]

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
    V14 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_14)),
              name='V14',
              switches=Slist_14)
    V15 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_15)),
              name='V15',
              switches=Slist_15)

    SNlist = [0, 1, 2, 3]
    Slist0 = [S0, S1,
              S10, S11,
              S20, S21,
              S30, S31]
    Slist1 = [S6, S7,
              S12, S13,
              S18, S19,
              S24, S25]
    Slist2 = [S2, S3, S4, S5]
    Slist3 = [S26, S27, S28, S29]
    Slist4 = [S8, S9, S16, S17]
    Slist5 = [S14, S15, S22, S23]

    def tree_list(n):
        return ['EQUSET'] + [[None]] * n + [[None]] * 4

    T0 = Tree(tree_list=tree_list(4),
              name='T0',
              switches=[V0, V5, V10, V15] + SNlist)
    T1 = Tree(tree_list=tree_list(4),
              name='T1',
              switches=[V3, V6, V9, V12] + SNlist)
    T2 = Tree(tree_list=tree_list(4),
              name='T2',
              switches=[V0, V1, V2, V3] + SNlist)
    T3 = Tree(tree_list=['AND'] + [tree_list(4)] * 3,
              name='T3',
              switches=[V1, V5, V9, V13] + SNlist + [V2, V6, V10, V14] + SNlist + [V12, V13, V14, V15] + SNlist,
              cut_expression=True)
    T4 = Tree(tree_list=tree_list(4),
              name='T4',
              switches=[V0, V4, V8, V12] + SNlist)
    T5 = Tree(tree_list=['AND'] + [tree_list(4)] * 3,
              name='T5',
              switches=[V4, V5, V6, V7] + SNlist + [V3, V7, V11, V15] + SNlist + [V8, V9, V10, V11] + SNlist,
              cut_expression=True)
    T6 = Tree(tree_list=['AND',
                         ['EQU',
                          ['MOD',
                           Tree.tree_list_BIN(11),
                           [None]],
                          [None]],
                         Tree.tree_list_XOR(2)],
              name='T6',
              switches=[S2, S3, S5, S7, S11, S13, S17, S19, S23, S29, S31, a, b, S0, S31])

    if fast_solution_finding:
        possible_switches_values = [[0, 0, 1, 0, 0, 1, 1, 1],
                                    [0, 0, 1, 0, 1, 1, 0, 1],
                                    [0, 0, 0, 1, 1, 0, 1, 1],
                                    [0, 0, 0, 1, 1, 1, 1, 0],
                                    [0, 0, 1, 1, 1, 0, 0, 1],
                                    [0, 0, 1, 1, 0, 1, 1, 0],
                                    [1, 0, 0, 0, 0, 1, 1, 1],
                                    [1, 0, 0, 0, 1, 1, 0, 1],
                                    [1, 0, 0, 1, 0, 0, 1, 1],
                                    [1, 0, 0, 1, 1, 1, 0, 0],
                                    [1, 0, 1, 1, 0, 0, 0, 1],
                                    [0, 0, 1, 1, 0, 1, 0, 0],
                                    [0, 1, 0, 0, 1, 0, 1, 1],
                                    [0, 1, 0, 0, 1, 1, 1, 0],
                                    [0, 1, 1, 0, 0, 0, 1, 1],
                                    [0, 1, 1, 0, 1, 1, 0, 0],
                                    [0, 1, 1, 1, 0, 0, 1, 0],
                                    [0, 1, 1, 1, 1, 0, 0, 0],
                                    [1, 1, 0, 0, 1, 0, 0, 1],
                                    [1, 1, 0, 0, 0, 1, 1, 0],
                                    [1, 1, 1, 0, 0, 0, 0, 1],
                                    [1, 1, 1, 0, 0, 1, 0, 0],
                                    [1, 1, 0, 1, 0, 0, 1, 0],
                                    [1, 1, 0, 1, 1, 0, 0, 0]]
    else:
        possible_switches_values = None

    R0 = Room(name='R0',
              position=[0, 8, 9, 1],
              switches_list=Slist0,
              possible_switches_values=possible_switches_values)
    R1 = Room(name='R1',
              position=[0, 6, 9, 1],
              switches_list=Slist1,
              possible_switches_values=possible_switches_values)
    R2 = Room(name='R2',
              position=[5, 4, 4, 1],
              switches_list=Slist2)
    R3 = Room(name='R3',
              position=[0, 4, 4, 1],
              switches_list=Slist3)
    R4 = Room(name='R4',
              position=[0, 2, 4, 1],
              switches_list=Slist4)
    R5 = Room(name='R5',
              position=[5, 2, 4, 1],
              switches_list=Slist5)
    R6 = Room(name='R6',
              position=[5, 0, 4, 1],
              switches_list=[])
    RE = Room(name='RE',
              position=[0, 0, 4, 1],
              is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=[7 / 9, 1 / 2])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3)
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
              room_arrival=R6)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R6,
              room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution='S1 S10 S30 S31 D0 S6 S13 S18 S19 D1 S4 S5 D2 S27 S28 D3 S8 S9 S16 D4 S23 D5 D6',
                 level_color=Levels_colors_list.FROM_HUE(0.5, sa=0.2, li=0.9),
                 name='Diagonal',
                 door_window_size=600,
                 keep_proportions=True)

    return level