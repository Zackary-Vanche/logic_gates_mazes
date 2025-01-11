from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

# Théorème des 4 couleurs
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

    tree_list_0 = ['INF',
                   ['SUM',
                    [None],
                    ['PROD',
                     [None],
                     [None]],
                    [None],
                    ['PROD',
                     [None],
                     [None]]],
                   [None]]
    tree_list_1 = ['OR',
                   Tree.tree_list_XOR(2),
                   Tree.tree_list_XOR(2)]

    SN2 = Switch(value=2, name='2')
    SN3 = Switch(value=3, name='3')
    SN9 = Switch(value=10, name='10')

    if fast_solution_finding:
        T0 = Tree(
            tree_list=['AND'] + [tree_list_0] * 2 + [tree_list_1] * 17 + [['SUPOREQU', Tree.tree_list_SUM(16), [None]]],
            name='T0',
            switches=[S0, SN2, S1, S4, SN2, S5, SN2,
                      S0, SN2, S1, S8, SN2, S9, SN3,
                      S0, S2, S1, S3,
                      S0, S4, S1, S5,
                      S0, S8, S1, S9,
                      S0, S10, S1, S11,
                      S0, S12, S1, S13,
                      S0, S14, S1, S15,
                      S2, S4, S3, S5,
                      S2, S12, S3, S13,
                      S4, S6, S5, S7,
                      S4, S12, S5, S13,
                      S4, S14, S5, S15,
                      S6, S8, S7, S9,
                      S6, S12, S7, S13,
                      S6, S14, S7, S15,
                      S8, S10, S9, S11,
                      S8, S12, S9, S13,
                      S10, S12, S11, S13,
                      S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, SN9],
            cut_expression=True)
        R0 = Room(name='R0',
                  position=[1.5, 1.5, 5.5, 5.5],
                  switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15])
        RE = Room(name='RE',
                  position=[10 - 0.2, 6, 1, 1],
                  is_exit=True)  # E pour exit ou end
        D0 = Door(two_way=False,
                  tree=T0,
                  room_departure=R0,
                  room_arrival=RE,
                  relative_departure_coordinates=[1, 0.8 / 5.5],
                  relative_arrival_coordinates=[0, 1 / 2])

        level = Maze(start_room_index=0,
                     exit_room_index=-1,
                     rooms_list=[R0, RE],
                     doors_list=[D0],
                     fastest_solution='S2 S3 S4 S6 S7 S8 S10 S11 S13 S15 D0',
                     level_color=Levels_colors_list.FOUR_COLORS,
                     name='4 colors theorem',
                     door_window_size=550,
                     keep_proportions=True)

        return level
    else:
        T0 = Tree(tree_list=tree_list_0,
                  name='T0',
                  switches=[S0, SN2, S1, S4, SN2, S5, SN2])
        T1 = Tree(tree_list=tree_list_0,
                  name='T1',
                  switches=[S0, SN2, S1, S8, SN2, S9, SN3])
        T2 = Tree(tree_list=tree_list_1,
                  name='T2',
                  switches=[S0, S2, S1, S3])
        T3 = Tree(tree_list=tree_list_1,
                  name='T3',
                  switches=[S0, S4, S1, S5])
        T4 = Tree(tree_list=tree_list_1,
                  name='T4',
                  switches=[S0, S8, S1, S9])
        T5 = Tree(tree_list=tree_list_1,
                  name='T5',
                  switches=[S0, S10, S1, S11])
        T6 = Tree(tree_list=tree_list_1,
                  name='T6',
                  switches=[S0, S12, S1, S13])
        T7 = Tree(tree_list=tree_list_1,
                  name='T7',
                  switches=[S0, S14, S1, S15])
        T8 = Tree(tree_list=tree_list_1,
                  name='T8',
                  switches=[S2, S4, S3, S5])
        T9 = Tree(tree_list=tree_list_1,
                  name='T9',
                  switches=[S2, S12, S3, S13])
        T10 = Tree(tree_list=tree_list_1,
                   name='T10',
                   switches=[S4, S6, S5, S7])
        T11 = Tree(tree_list=tree_list_1,
                   name='T11',
                   switches=[S4, S12, S5, S13])
        T12 = Tree(tree_list=tree_list_1,
                   name='T12',
                   switches=[S4, S14, S5, S15])
        T13 = Tree(tree_list=tree_list_1,
                   name='T13',
                   switches=[S6, S8, S7, S9])
        T14 = Tree(tree_list=tree_list_1,
                   name='T14',
                   switches=[S6, S12, S7, S13])
        T15 = Tree(tree_list=tree_list_1,
                   name='T15',
                   switches=[S6, S14, S7, S15])
        T16 = Tree(tree_list=tree_list_1,
                   name='T16',
                   switches=[S8, S10, S9, S11])
        T17 = Tree(tree_list=tree_list_1,
                   name='T17',
                   switches=[S8, S12, S9, S13])
        T18 = Tree(tree_list=tree_list_1,
                   name='T18',
                   switches=[S10, S12, S11, S13])
        T19 = Tree(tree_list=['SUPOREQU', Tree.tree_list_SUM(16), [None]],
                   name='T19',
                   switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, SN9])
        R0 = Room(name='R0',
                  position=[1.5, 1.5, 5.5, 5.5],
                  switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15])
        R1 = Room(name='R1',
                  position=[8, 2, 0.6, 0.6],
                  switches_list=[])
        R2 = Room(name='R2',
                  position=[8, 4, 0.6, 0.6],
                  switches_list=[])
        R3 = Room(name='R3',
                  position=[8, 6, 0.6, 0.6],
                  switches_list=[])
        R4 = Room(name='R4',
                  position=[8, 8, 0.6, 0.6],
                  switches_list=[])
        R5 = Room(name='R5',
                  position=[6, 8, 0.6, 0.6],
                  switches_list=[])
        R6 = Room(name='R6',
                  position=[4, 8, 0.6, 0.6],
                  switches_list=[])
        R7 = Room(name='R7',
                  position=[2, 8, 0.6, 0.6],
                  switches_list=[])
        R8 = Room(name='R8',
                  position=[0, 8, 0.6, 0.6],
                  switches_list=[])
        R9 = Room(name='R9',
                  position=[0, 6, 0.6, 0.6],
                  switches_list=[])
        R10 = Room(name='R10',
                   position=[0, 4, 0.6, 0.6],
                   switches_list=[])
        R11 = Room(name='R11',
                   position=[0, 2, 0.6, 0.6],
                   switches_list=[])
        R12 = Room(name='R12',
                   position=[0, 0, 0.6, 0.6],
                   switches_list=[])
        R13 = Room(name='R13',
                   position=[2, 0, 0.6, 0.6],
                   switches_list=[])
        R14 = Room(name='R14',
                   position=[4, 0, 0.6, 0.6],
                   switches_list=[])
        R15 = Room(name='R15',
                   position=[6, 0, 0.6, 0.6],
                   switches_list=[])
        R16 = Room(name='R16',
                   position=[8, 0, 0.6, 0.6],
                   switches_list=[])
        R17 = Room(name='R17',
                   position=[10, 0, 0.6, 0.6],
                   switches_list=[])
        R18 = Room(name='R18',
                   position=[10, 2, 0.6, 0.6],
                   switches_list=[])
        R19 = Room(name='R19',
                   position=[10, 4, 0.6, 0.6],
                   switches_list=[])
        RE = Room(name='RE',
                  position=[10 - 0.2, 6, 1, 1],
                  is_exit=True)  # E pour exit ou end
        D0 = Door(two_way=False,
                  tree=T0,
                  room_departure=R0,
                  room_arrival=R1,
                  relative_departure_coordinates=[1, 0.8 / 5.5],
                  relative_arrival_coordinates=[0, 1 / 2])
        D1 = Door(two_way=False,
                  tree=T1,
                  room_departure=R1,
                  room_arrival=R2)
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
                  room_arrival=R7)
        D7 = Door(two_way=False,
                  tree=T7,
                  room_departure=R7,
                  room_arrival=R8)
        D8 = Door(two_way=False,
                  tree=T8,
                  room_departure=R8,
                  room_arrival=R9)
        D9 = Door(two_way=False,
                  tree=T9,
                  room_departure=R9,
                  room_arrival=R10)
        D10 = Door(two_way=False,
                   tree=T10,
                   room_departure=R10,
                   room_arrival=R11)
        D11 = Door(two_way=False,
                   tree=T11,
                   room_departure=R11,
                   room_arrival=R12)
        D12 = Door(two_way=False,
                   tree=T12,
                   room_departure=R12,
                   room_arrival=R13)
        D13 = Door(two_way=False,
                   tree=T13,
                   room_departure=R13,
                   room_arrival=R14)
        D14 = Door(two_way=False,
                   tree=T14,
                   room_departure=R14,
                   room_arrival=R15)
        D15 = Door(two_way=False,
                   tree=T15,
                   room_departure=R15,
                   room_arrival=R16)
        D16 = Door(two_way=False,
                   tree=T16,
                   room_departure=R16,
                   room_arrival=R17)
        D17 = Door(two_way=False,
                   tree=T17,
                   room_departure=R17,
                   room_arrival=R18)
        D18 = Door(two_way=False,
                   tree=T18,
                   room_departure=R18,
                   room_arrival=R19)
        D19 = Door(two_way=False,
                   tree=T19,
                   room_departure=R19,
                   room_arrival=RE)

        level = Maze(start_room_index=0,
                     exit_room_index=-1,
                     rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18,
                                 R19, RE],
                     doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18,
                                 D19],
                     fastest_solution='S2 S3 S4 S6 S7 S8 S10 S11 S13 S15 D0 D1 D2 D3 D4 D5 D6 D7 D8 D9 D10 D11 D12 D13 D14 D15 D16 D17 D18 D19',
                     level_color=get_color(),
                     name='4 colors theorem',
                     door_window_size=400,
                     keep_proportions=True)

        return level
    
def get_color():
    return Levels_colors_list.FOUR_COLORS