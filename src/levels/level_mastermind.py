from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import randint as rd_randint
from random import random


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
    nmax = 1
    a0 = rd_randint(0, nmax)
    a1 = rd_randint(0, nmax)
    a2 = rd_randint(0, nmax)
    a3 = rd_randint(0, nmax)
    a4 = rd_randint(0, nmax)
    a5 = rd_randint(0, nmax)
    a6 = rd_randint(0, nmax)
    a7 = rd_randint(0, nmax)
    Sa0 = Switch(name='?0', value=a0)
    Sa1 = Switch(name='?1', value=a1)
    Sa2 = Switch(name='?2', value=a2)
    Sa3 = Switch(name='?3', value=a3)
    Sa4 = Switch(name='?4', value=a4)
    Sa5 = Switch(name='?5', value=a5)
    Sa6 = Switch(name='?6', value=a6)
    Sa7 = Switch(name='?7', value=a7)
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V0',
              switches=[S0, S1])
    V1 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V1',
              switches=[S2, S3])
    V2 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V2',
              switches=[S4, S5])
    V3 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V3',
              switches=[S6, S7])
    V4 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V4',
              switches=[Sa0, Sa1])
    V5 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V5',
              switches=[Sa2, Sa3])
    V6 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V6',
              switches=[Sa4, Sa5])
    V7 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V7',
              switches=[Sa6, Sa7])
    V8 = Tree(tree_list=Tree.tree_list_XOR(2),
              name='V8',
              switches=[S8, S9])

    Slist = [V0, V1, V2, V3]
    Slista = [V4, V5, V6, V7]
    Slist_1 = [V8,
               V0, V4,
               V1, V5,
               V2, V6,
               V3, V7]
    Slist_2 = [V8] + Slist + Slista

    tree_list1 = ['AND',
                  [None],
                  ['EQU',
                   ['SUM'] + [['EQU', [None], [None]]] * 4,
                   [None]]]
    tree_list2 = ['AND',
                  [None],
                  ['EQU',
                   ['MAS'] + [[None]] * 8,
                   [None]]]

    T0 = Tree(tree_list=[None],
              name='T0',
              switches=[1])
    T1 = Tree(tree_list=tree_list1,
              name='T1',
              switches=Slist_1 + [0])
    T2 = Tree(tree_list=tree_list1,
              name='T2',
              switches=Slist_1 + [1])
    T3 = Tree(tree_list=tree_list1,
              name='T3',
              switches=Slist_1 + [2])
    T4 = Tree(tree_list=tree_list1,
              name='T4',
              switches=Slist_1 + [3])
    T5 = Tree(tree_list=tree_list1,
              name='T5',
              switches=Slist_1 + [4])
    T6 = Tree(tree_list=tree_list2,
              name='T6',
              switches=Slist_2 + [0])
    T7 = Tree(tree_list=tree_list2,
              name='T7',
              switches=Slist_2 + [1])
    T8 = Tree(tree_list=tree_list2,
              name='T8',
              switches=Slist_2 + [2])
    T11 = Tree(tree_list=tree_list2,
               name='T11',
               switches=Slist_2 + [3])
    T12 = Tree(tree_list=tree_list2,
               name='T12',
               switches=Slist_2 + [4])
    T13 = Tree(tree_list=Tree.tree_list_not,
               name='T13',
               switches=[V8])
    T14 = Tree(tree_list=[None],
               name='T14',
               switches=[1])
    T15 = Tree(tree_list=['AND'] + [['EQU', [None], [None]]] * 9,
               name='T15',
               switches=[S0, Sa0,
                         S1, Sa1,
                         S2, Sa2,
                         S3, Sa3,
                         S4, Sa4,
                         S5, Sa5,
                         S6, Sa6,
                         S7, Sa7,
                         S10, 1
                         ])

    def rp(k):
        return (k + 0.6) / 10

    R0 = Room(name='R0',
              position=[2, 0, 0.5, 8],
              switches_list=[S0, S1, S2, S3, S4, S5, S6, S7])
    R1 = Room(name='R1',
              position=[3.5, 0, 1.25, 0.5],
              switches_list=[S8])
    R2 = Room(name='R2',
              position=[3.5, 7.5, 1.25, 0.5],
              switches_list=[S9])
    R3 = Room(name='R3',
              position=[0.5, 4.5, 0.5, 1],
              switches_list=[S10])
    RE = Room(name='RE',
              position=[0.5, 2.5, 0.5, 1],
              is_exit=True)  # E pour exit ou end
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1, 1/2],
              relative_arrival_coordinates=[0, 1])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2,
              relative_position=rp(0),
              relative_departure_coordinates=[1 / 2, 1],
              relative_arrival_coordinates=[1 / 2, 0])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R1,
              room_arrival=R2,
              relative_position=rp(1),
              relative_departure_coordinates=[1 / 2, 1],
              relative_arrival_coordinates=[1 / 2, 0])
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R1,
              room_arrival=R2,
              relative_position=rp(2),
              relative_departure_coordinates=[1 / 2, 1],
              relative_arrival_coordinates=[1 / 2, 0])
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R1,
              room_arrival=R2,
              relative_position=rp(3),
              relative_departure_coordinates=[1 / 2, 1],
              relative_arrival_coordinates=[1 / 2, 0])
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R1,
              room_arrival=R2,
              relative_position=rp(4),
              relative_departure_coordinates=[1 / 2, 1],
              relative_arrival_coordinates=[1 / 2, 0])
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R1,
              room_arrival=R2,
              relative_position=rp(5),
              relative_departure_coordinates=[1 / 2, 1],
              relative_arrival_coordinates=[1 / 2, 0])
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R1,
              room_arrival=R2,
              relative_position=rp(6),
              relative_departure_coordinates=[1 / 2, 1],
              relative_arrival_coordinates=[1 / 2, 0])
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R1,
              room_arrival=R2,
              relative_position=rp(7),
              relative_departure_coordinates=[1 / 2, 1],
              relative_arrival_coordinates=[1 / 2, 0])
    D9 = Door(two_way=False,
               tree=T11,
               room_departure=R1,
               room_arrival=R2,
               relative_position=rp(8),
               relative_departure_coordinates=[1 / 2, 1],
               relative_arrival_coordinates=[1 / 2, 0])
    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R1,
               room_arrival=R2,
               relative_position=rp(9),
               relative_departure_coordinates=[1 / 2, 1],
               relative_arrival_coordinates=[1 / 2, 0])
    D13 = Door(two_way=False,
               tree=T13,
               room_departure=R2,
               room_arrival=R0,
               relative_departure_coordinates=[0, 0],
               relative_arrival_coordinates=[1, 1/2])
    D14 = Door(two_way=False,
               tree=T14,
               room_departure=R0,
               room_arrival=R3)
    D15 = Door(two_way=False,
               tree=T15,
               room_departure=R3,
               room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D12, D13, D14, D15],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Mastermind',
                 random=True,
                 door_window_size=620,
                 keep_proportions=True,
                 y_separation=40,
                 border=40)

    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=random(), sa=1, li=0.3)