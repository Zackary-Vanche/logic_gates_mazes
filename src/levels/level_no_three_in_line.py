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

    SN1 = Switch(value=1)
    SN2 = Switch(value=2)
    SN3 = Switch(value=3)
    SN8 = Switch(value=8)

    tree_list_SUP_3 = ['SUP', [None], ['SUM'] + [[None]] * 3]
    tree_list_SUP_4 = ['SUP', [None], ['SUM'] + [[None]] * 4]
    tree_list_SUP_5 = ['SUP', [None], ['SUM'] + [[None]] * 5]

    T0 = Tree(tree_list=tree_list_SUP_5,
              name='T0',
              switches=[SN3, S0, S1, S2, S3, S4])
    T1 = Tree(tree_list=tree_list_SUP_5,
              name='T1',
              switches=[SN3, S5, S6, S7, S8, S9])
    T2 = Tree(tree_list=['AND',
                         tree_list_SUP_5,
                         tree_list_SUP_3,
                         tree_list_SUP_3],
              name='T2',
              switches=[SN3, S10, S11, S12, S13, S14,
                        SN3, S0, S7, S14,
                        SN3, S4, S7, S10, ])
    T3 = Tree(tree_list=['AND',
                         tree_list_SUP_5,
                         tree_list_SUP_3,
                         tree_list_SUP_3],
              name='T3',
              switches=[SN3, S15, S16, S17, S18, S19,
                        SN3, S9, S12, S15,
                        SN3, S5, S12, S19, ])
    T4 = Tree(tree_list=['AND',
                         tree_list_SUP_5,

                         tree_list_SUP_3,
                         tree_list_SUP_4,
                         tree_list_SUP_5,
                         tree_list_SUP_4,
                         tree_list_SUP_3,

                         tree_list_SUP_3,
                         tree_list_SUP_4,
                         tree_list_SUP_5,
                         tree_list_SUP_4,
                         tree_list_SUP_3] + [
                            tree_list_SUP_3] * 8 + [
                            tree_list_SUP_5] * 5 + [
                            ['INF', [None], ['SUM'] + [[None]] * 25]] + [
                            ['INF', Tree.tree_list_BIN(4), Tree.tree_list_BIN(4)]] + [
                            Tree.tree_list_NONO(34)],
              name='T4',
              switches=[SN3, S20, S21, S22, S23, S24,

                        SN3, S2, S6, S10,
                        SN3, S3, S7, S11, S15,
                        SN3, S4, S8, S12, S16, S20,
                        SN3, S9, S13, S17, S21,
                        SN3, S14, S18, S22,

                        SN3, S2, S8, S14,
                        SN3, S1, S7, S13, S19,
                        SN3, S0, S6, S12, S18, S24,
                        SN3, S5, S11, S17, S23,
                        SN3, S10, S16, S22,

                        SN3, S10, S17, S24,
                        SN3, S14, S17, S20,
                        SN3, S2, S11, S20,
                        SN3, S3, S12, S21,
                        SN3, S4, S13, S22,
                        SN3, S0, S11, S22,
                        SN3, S1, S12, S23,
                        SN3, S2, S13, S24,

                        SN3, S0, S5, S10, S15, S20,
                        SN3, S1, S6, S11, S16, S21,
                        SN3, S2, S7, S12, S17, S22,
                        SN3, S3, S8, S13, S18, S23,
                        SN3, S4, S9, S14, S19, S24,

                        Switch(value=9), S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17,
                        S18, S19, S20, S21, S22, S23, S24,

                        S3, S4, S8, S9,
                        S15, S16, S20, S21,

                        SN8, SN2, SN1, SN1, SN1, SN1, SN1, SN1, SN2,
                        S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20,
                        S21, S22, S23, S24,
                        ],
              cut_expression=True)

    lx = 1
    ly = 5
    deltax = 2.3 * lx
    deltay = ly + 1.1

    if fast_solution_finding:
        possible_switches_values = [[1, 1, 0, 0, 0],
                                    [1, 0, 1, 0, 0],
                                    [1, 0, 0, 1, 0],
                                    [1, 0, 0, 0, 1],
                                    [0, 1, 1, 0, 0],
                                    [0, 1, 0, 1, 0],
                                    [0, 1, 0, 0, 1],
                                    [0, 0, 1, 1, 0],
                                    [0, 0, 1, 0, 1],
                                    [0, 0, 0, 1, 1]]
    else:
        possible_switches_values = None

    R0 = Room(name='R0',
              position=[0, 0, lx, ly],
              switches_list=[S0, S1, S2, S3, S4],
              possible_switches_values=possible_switches_values)
    R1 = Room(name='R1',
              position=[deltax, 0, lx, ly],
              switches_list=[S5, S6, S7, S8, S9],
              possible_switches_values=possible_switches_values)
    R2 = Room(name='R2',
              position=[2 * deltax, 0, lx, ly],
              switches_list=[S10, S11, S12, S13, S14],
              possible_switches_values=possible_switches_values)
    R3 = Room(name='R3',
              position=[0, deltay, lx, ly],
              switches_list=[S15, S16, S17, S18, S19],
              possible_switches_values=possible_switches_values)
    R4 = Room(name='R4',
              position=[deltax, deltay, lx, ly],
              switches_list=[S20, S21, S22, S23, S24],
              possible_switches_values=possible_switches_values)
    RE = Room(name='RE',
              position=[2 * deltax, deltay, lx, ly],
              is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=[3 / 4, 1],
              relative_arrival_coordinates=[1 / 4, 0],
              relative_position=0.51)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=R4)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R4,
              room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4],
                 fastest_solution="S1 S2 D0 S5 S7 D1 S10 S14 D2 S16 S18 D3 S23 S24 D4",
                 level_color=get_color(),
                 name='No three in line',
                 door_window_size=700,
                 keep_proportions=True,
                 y_separation=45)

    return level

def get_color():
    return Levels_colors_list.FROM_HUE(0.05, sa=1, li=0.6)