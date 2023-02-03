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
    S16 = Switch(name='S16')
    S17 = Switch(name='S17')
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19]

    # These lines were used to create Slisttree for the first time
    # Slisttree = []
    # for i in range(16):
    #     for j in [i-11, i-9, i-7, i-3, i+3, i+7, i+9, i+11]:
    #         if 0 <= j < len(Slist) and i <= j:
    #             Slisttree.append(Slist[i])
    #             Slisttree.append(Slist[j])
    # print([S.name for S in Slisttree])

    Slisttree = [S0, S3, S0, S7, S0, S9, S0, S11, S1, S4, S1, S8, S1, S10, S1, S12, S2, S5, S2, S9, S2, S11, S2, S13,
                 S3, S6, S3, S10, S3, S12, S3, S14, S4, S7, S4, S11, S4, S13, S4, S15, S5, S8, S5, S12, S5, S14, S5,
                 S16, S6, S9, S6, S13, S6, S15, S6, S17, S7, S10, S7, S14, S7, S16, S7, S18, S8, S11, S8, S15, S8, S17,
                 S8, S19, S9, S12, S9, S16, S9, S18, S10, S13, S10, S17, S10, S19, S11, S14, S11, S18, S12, S15, S12,
                 S19, S13, S16, S14, S17, S15, S18]

    d = 4
    ex = 1
    ey = 1

    def y(i):
        return 5 + (i + 1) * 0.525

    n = 7
    tree_list = ['AND'] + [Tree.tree_list_NAND(2)]*n

    def Slist_i(i):
        return Slisttree[i*2*n:(i+1)*2*n]

    def get_tree(i):
        return Tree(tree_list=tree_list,
                    empty=True,
                    name=f'T{i}',
                    switches=Slist_i(i))

    R0 = Room(name='R0',
              position = [d, 2, 5, 4],
              switches_list = Slist)
    R1 = Room(name='R1',
              position=[0, y(0), ex, ey],
              switches_list=[])
    R2 = Room(name='R2',
              position=[d, y(1), ex, ey],
              switches_list=[])
    R3 = Room(name='R3',
              position=[0, y(2), ex, ey],
              switches_list=[])
    R4 = Room(name='R4',
              position=[d, y(3), ex, ey],
              switches_list=[])
    R5 = Room(name='R5',
              position=[0, y(4), ex, ey],
              switches_list=[])
    R6 = Room(name='R6',
              position=[d, y(5), ex, ey],
              switches_list=[])
    R7 = Room(name='R7',
              position=[0, y(6), ex, ey],
              switches_list=[])
    R8 = Room(name='R8',
              position=[d, y(7), ex, ey],
              switches_list=[])
    RE = Room(name='RE',
              position=[0, y(8), ex, ey],
              is_exit=True)   # E pour exit ou end

    D0 = Door(two_way=False,
              tree=get_tree(0),
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1/8, 9/10])
    D1 = Door(two_way=False,
              tree=get_tree(1),
              room_departure=R1,
              room_arrival=R2)
    D2 = Door(two_way=False,
              tree=get_tree(2),
              room_departure=R2,
              room_arrival=R3)
    D3 = Door(two_way=False,
              tree=get_tree(3),
              room_departure=R3,
              room_arrival=R4)
    D4 = Door(two_way=False,
              tree=get_tree(4),
              room_departure=R4,
              room_arrival=R5)
    D5 = Door(two_way=False,
              tree=get_tree(5),
              room_departure=R5,
              room_arrival=R6)
    D6 = Door(two_way=False,
              tree=get_tree(6),
              room_departure=R6,
              room_arrival=R7)
    T7 = Tree(tree_list=['SUPOREQU', ['SUM'] + [[None]] * 20, [None]],
              empty=True,
              name='T7',
              switches=Slist + [10])
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R7,
              room_arrival=R8)
    T8 = Tree(tree_list=['NOT', ['EQU', Tree.tree_list_BIN(20), [None]]],
              empty=True,
              name='T8',
              switches=Slist + [699050])
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R8,
              room_arrival=RE)

    rp = 1/2

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8],
                 fastest_solution='S0 S2 S4 S6 S8 S10 S12 S14 S16 S18 D0 D1 D2 D3 D4 D5 D6 D7 D8',
                 level_color=Levels_colors_list.FROM_HUE(hu=0.55, sa=0.9, li=0.3),
                 name='K',
                 door_window_size=1000,
                 keep_proportions=True,
                 y_separation=40,
                 border=40)

    return level