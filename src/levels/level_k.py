from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_k(fast_solution_finding=False):

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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15]#, S16, S17, S18, S19]

    Slisttree = [S0, S3, S0, S7, S0, S9, S0, S11, S1, S4, S1, S8, S1, S10, S1, S12, S2, S5, S2, S9, S2, S11, S2, S13,
                 S3, S6, S3, S10, S3, S12, S3, S14, S4, S7, S4, S11, S4, S13, S4, S15, S5, S8, S5, S12, S5, S14, S6, S9,
                 S6, S13, S6, S15, S7, S10, S7, S14, S8, S11, S8, S15, S9, S12, S10, S13, S11, S14, S12, S15]

    d = 4
    ex = 1
    ey = 1

    def y(i):
        return 5 + (i + 1) * 0.525

    def pos(i):
        j = i-1
        return [(j%2)*d, y(j), ex, ey]

    rp = 0.4

    if fast_solution_finding:

        T0 = Tree(tree_list=['AND'] + [Tree.tree_list_NAND(2)]*34 + [['SUPOREQU', ['SUM'] + [[None]] * 16, [None]],
                                                                     ['NOT', ['EQU', Tree.tree_list_BIN(16), [None]]]],
                    empty=True,
                    name='T0',
                    switches=Slisttree + Slist + [8] + Slist + [43690])
        R0 = Room(name='R0',
                  position=[0, 0, 4, 4],
                  switches_list=Slist)
        RE = Room(name='RE',
                  position=[0, 5, 4, 4],
                  is_exit=True)  # E pour exit ou end

        D0 = Door(two_way=False,
                  tree=T0,
                  room_departure=R0,
                  room_arrival=RE,
                  relative_departure_coordinates=[1 / 8, 9 / 10],
                  relative_position=rp)

        level = Maze(start_room_index=0,
                     exit_room_index=-1,
                     rooms_list=[R0] + [RE],
                     doors_list=[D0],
                     fastest_solution='S0 S2 S4 S6 S8 S10 S12 S14 D0',
                     level_color=Levels_colors_list.FROM_HUE(hu=0.55, sa=0.9, li=0.3),
                     name='K',
                     door_window_size=1000,
                     keep_proportions=True,
                     y_separation=40,
                     border=40)

        return level

    else:

        n = 2
        tree_list = ['AND'] + [Tree.tree_list_NAND(2)]*n

        def Slist_i(i):
            if Slisttree[i*2*n:(i+1)*2*n] == []:
                print(i)
            return Slisttree[i*2*n:(i+1)*2*n]

        def get_tree(i):
            return Tree(tree_list=tree_list,
                        empty=True,
                        name=f'T{i}',
                        switches=Slist_i(i))

        R0 = Room(name='R0',
                  position = [d, 2, 4, 4],
                  switches_list = Slist)
        R1 = Room(name='R1',
                  position=pos(1),
                  switches_list=[])
        R2 = Room(name='R2',
                  position=pos(2),
                  switches_list=[])
        R3 = Room(name='R3',
                  position=pos(3),
                  switches_list=[])
        R4 = Room(name='R4',
                  position=pos(4),
                  switches_list=[])
        R5 = Room(name='R5',
                  position=pos(5),
                  switches_list=[])
        R6 = Room(name='R6',
                  position=pos(6),
                  switches_list=[])
        R7 = Room(name='R7',
                  position=pos(7),
                  switches_list=[])
        R8 = Room(name='R8',
                  position=pos(8),
                  switches_list=[])
        R9 = Room(name='R9',
                  position=pos(9),
                  switches_list=[])
        R10 = Room(name='R10',
                   position=pos(10),
                   switches_list=[])
        R11 = Room(name='R11',
                   position=pos(11),
                   switches_list=[])
        R12 = Room(name='R12',
                   position=pos(12),
                   switches_list=[])
        R13 = Room(name='R13',
                   position=pos(13),
                   switches_list=[])
        R14 = Room(name='R14',
                   position=pos(14),
                   switches_list=[])
        R15 = Room(name='R15',
                   position=pos(15),
                   switches_list=[])
        R16 = Room(name='R16',
                   position=pos(16),
                   switches_list=[])
        R17 = Room(name='R17',
                   position=pos(17),
                   switches_list=[])
        R18 = Room(name='R18',
                   position=pos(18),
                   switches_list=[])
        RE = Room(name='RE',
                  position=pos(19),
                  is_exit=True)   # E pour exit ou end

        D0 = Door(two_way=False,
                  tree=get_tree(0),
                  room_departure=R0,
                  room_arrival=R1,
                  relative_departure_coordinates=[1/8, 9/10],
                  relative_position=rp)
        D1 = Door(two_way=False,
                  tree=get_tree(1),
                  room_departure=R1,
                  room_arrival=R2,
                  relative_position=rp)
        D2 = Door(two_way=False,
                  tree=get_tree(2),
                  room_departure=R2,
                  room_arrival=R3,
                  relative_position=rp)
        D3 = Door(two_way=False,
                  tree=get_tree(3),
                  room_departure=R3,
                  room_arrival=R4,
                  relative_position=rp)
        D4 = Door(two_way=False,
                  tree=get_tree(4),
                  room_departure=R4,
                  room_arrival=R5,
                  relative_position=rp)
        D5 = Door(two_way=False,
                  tree=get_tree(5),
                  room_departure=R5,
                  room_arrival=R6,
                  relative_position=rp)
        D6 = Door(two_way=False,
                  tree=get_tree(6),
                  room_departure=R6,
                  room_arrival=R7,
                  relative_position=rp)
        D7 = Door(two_way=False,
                  tree=get_tree(7),
                  room_departure=R7,
                  room_arrival=R8,
                  relative_position=rp)
        D8 = Door(two_way=False,
                  tree=get_tree(8),
                  room_departure=R8,
                  room_arrival=R9,
                  relative_position=rp)
        D9 = Door(two_way=False,
                  tree=get_tree(9),
                  room_departure=R9,
                  room_arrival=R10,
                  relative_position=rp)
        D10 = Door(two_way=False,
                   tree=get_tree(10),
                   room_departure=R10,
                   room_arrival=R11,
                  relative_position=rp)
        D11 = Door(two_way=False,
                   tree=get_tree(11),
                   room_departure=R11,
                   room_arrival=R12,
                  relative_position=rp)
        D12 = Door(two_way=False,
                   tree=get_tree(12),
                   room_departure=R12,
                   room_arrival=R13,
                  relative_position=rp)
        D13 = Door(two_way=False,
                   tree=get_tree(13),
                   room_departure=R13,
                   room_arrival=R14,
                  relative_position=rp)
        D14 = Door(two_way=False,
                   tree=get_tree(14),
                   room_departure=R14,
                   room_arrival=R15,
                  relative_position=rp)
        D15 = Door(two_way=False,
                   tree=get_tree(15),
                   room_departure=R15,
                   room_arrival=R16,
                  relative_position=rp)
        D16 = Door(two_way=False,
                   tree=get_tree(16),
                   room_departure=R16,
                   room_arrival=R17,
                  relative_position=rp)
        D17 = Door(two_way=False,
                  tree=Tree(tree_list=['SUPOREQU', ['SUM'] + [[None]] * 16, [None]],
                            empty=True,
                            name='T17',
                            switches=Slist + [8]),
                  room_departure=R17,
                  room_arrival=R18,
                  relative_position=rp)
        D18 = Door(two_way=False,
                  tree=Tree(tree_list=['NOT', ['EQU', Tree.tree_list_BIN(16), [None]]],
                            empty=True,
                            name='T18',
                            switches=Slist + [43690]),  # TODO
                  room_departure=R18,
                  room_arrival=RE,
                  relative_position=rp)

        rp = 1/2

        level = Maze(start_room_index=0,
                     exit_room_index=-1,
                     rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18] + [RE],
                     doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18],
                     fastest_solution='S0 S2 S4 S6 S8 S10 S12 S14 D0 D1 D2 D3 D4 D5 D6 D7 D8 D9 D10 D11 D12 D13 D14 D15 D16 D17 D18',
                     level_color=Levels_colors_list.FROM_HUE(hu=0.55, sa=0.9, li=0.3),
                     name='K',
                     door_window_size=1000,
                     keep_proportions=True,
                     y_separation=40,
                     border=40)

        return level