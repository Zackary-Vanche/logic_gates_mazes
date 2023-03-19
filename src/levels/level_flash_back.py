from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle

def level_flash_back():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')

    Slist0 = [S0, S1, S2]
    Slist1 = [S3, S4, S5]

    vlist = [1, 2, 3, 4, 5, 6, 7]
    rd_shuffle(vlist)
    vlist = [0] + vlist

    def tree_list_IN(k):
        if k == 1:
            return ['EQU', Tree.tree_list_BIN(3), [None]]
        else:
            return ['IN', Tree.tree_list_BIN(3)] + [[None]]*k

    tree_list_1 = ['OR']
    Slist_tree1 = []
    for i in range(8):
        tree_list_1.append(['AND',
                            tree_list_IN(1),
                            tree_list_IN(min(i+2, 8))])
        Slist_tree1.extend(Slist0 + [vlist[i]] + Slist1 + sorted(vlist[:i+2]))

    T1 = Tree(tree_list=tree_list_1,
              empty=True,
              name='T1',
              switches=Slist_tree1,
              cut_expression=True,
              cut_expression_separator=']')
    T0 = Tree(tree_list=['EQU'] + [Tree.tree_list_BIN(3)]*2,
              empty=True,
              name='T0',
              switches=[S0, S1, S2, S3, S4, S5])
    T2 = Tree(tree_list=['AND', tree_list_IN(1), tree_list_IN(1)],
              empty=True,
              name='T2',
              switches=Slist0 + [vlist[-1]] + Slist1 + [vlist[-1]])

    ex = 1/2
    ey = 1/2
    dx = 6

    R0 = Room(name='R0',
              position=[0, 0, ex, 5],
              switches_list=Slist0)
    R1 = Room(name='R1',
              position=[dx, 0, ex, 5],
              switches_list=Slist1)
    RE = Room(name='RE',
              position=[0, 6, dx+ex, ey],
              is_exit=True)  # E pour exit ou end
    n = 12
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1, 1 / n],
              relative_arrival_coordinates=[0, 1 / 2])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R0,
              relative_departure_coordinates=[0, (n-1) / n],
              relative_arrival_coordinates=[1, 1 / 2])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R1,
              room_arrival=RE,
              relative_departure_coordinates=[1 / 2, 1],
              relative_arrival_coordinates=[1 / 2, 0])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, RE],
                 doors_list=[D0, D1, D2],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(0.95, sa=0.2, li=0.4),
                 name='Flash-back',
                 door_window_size=800,
                 keep_proportions=True)

    return level