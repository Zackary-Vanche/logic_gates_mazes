from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import randint as rd_randint
from random import shuffle as rd_shuffle

def level_second():

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

    a = rd_randint(1, 15)
    b = rd_randint(0, 15)
    c = rd_randint(0, 15)

    Sa = Switch(name='?a', value=a)
    Sb = Switch(name='?b', value=b)
    Sc = Switch(name='?c', value=c)
    lint = [i for i in range(-63, 64)]
    rd_shuffle(lint)

    Slist = [S0, S1, S2, S3,
             S4, S5, S6, S7,
             S8, S9, S10, S11]

    tree_list = ['EQU',
                  ['SUM',
                   ['PROD', Tree.tree_list_BIN(4), ['POW', [None], [None]]],
                   ['PROD', Tree.tree_list_BIN(4), [None]],
                   Tree.tree_list_BIN(4)],
                 [None],]

    def Slist_i(i):
        x = lint[i]
        return [S0, S1, S2, S3, x, 2,
                S4, S5, S6, S7, x,
                S8, S9, S10, S11,
                a * x ** 2 + b * x + c,]

    T0 = Tree(tree_list=tree_list,
              empty=True,
              name='T0',
              switches=Slist_i(0))
    T1 = Tree(tree_list=tree_list,
              empty=True,
              name='T1',
              switches=Slist_i(1))
    T2 = Tree(tree_list=tree_list,
              empty=True,
              name='T2',
              switches=Slist_i(2))

    ex = 1
    ey = 3/4

    R0 = Room(name='R0',
              position = [0, 6, 4, 3],
              switches_list = Slist)
    R1 = Room(name='R1',
              position = [0, 4, ex, ey],
              switches_list = [])
    R2 = Room(name='R2',
              position = [1, 2, ex, ey],
              switches_list = [])
    RE = Room(name='RE',
              position=[3, 0.75, ex, ey],
              is_exit=True)   # E pour exit ou end
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1.5 / 4, 3 / 4 * 0.5 / 3])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=RE)

    rp = 1/2

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2] + [RE],
                 doors_list=[D0, D1, D2],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0, sa=0.2, li=0.4),
                 name='Second',
                 door_window_size=900,
                 keep_proportions=True,
                 y_separation=40,
                 border=40,
                 random=True)

    return level