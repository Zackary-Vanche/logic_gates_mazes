from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle

def f():
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    
    Slist0 = [S0, S2, S4, S6]
    Slist1 = [S1, S3, S5, S7]
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(4),
              name='V0',
              switches=Slist0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(4),
              name='V1',
              switches=Slist1)

    Tlist = ['AND'] + [['EQU', [None], [None]]] * 2

    ln = [[i] for i in range(1, 16)]
    rd_shuffle(ln)
    ln = [[0]] + ln

    T0 = Tree(tree_list=[None],
              name='T0',
              switches=[1])
    T1 = Tree(tree_list=[None],
              name='T1',
              switches=[1])
    T2 = Tree(tree_list=[None],
              name='T2',
              switches=[1])
    T3 = Tree(tree_list=[None],
              name='T3',
              switches=[1])
    T4 = Tree(tree_list=Tlist,
              name='T4',
              switches=ln[0] + [V0] + ln[1] + [V1],
              cut_expression=False)
    T5 = Tree(tree_list=Tlist,
              name='T5',
              switches=ln[1] + [V0] + ln[2] + [V1],
              cut_expression=False)
    T6 = Tree(tree_list=Tlist,
              name='T6',
              switches=ln[1] + [V0] + ln[3] + [V1],
              cut_expression=False)
    T7 = Tree(tree_list=Tlist,
              name='T7',
              switches=ln[2] + [V0] + ln[4] + [V1],
              cut_expression=False)
    T8 = Tree(tree_list=Tlist,
              name='T8',
              switches=ln[2] + [V0] + ln[5] + [V1],
              cut_expression=False)
    T9 = Tree(tree_list=Tlist,
              name='T9',
              switches=ln[3] + [V0] + ln[6] + [V1],
              cut_expression=False)
    T10 = Tree(tree_list=Tlist,
               name='T10',
               switches=ln[3] + [V0] + ln[7] + [V1],
               cut_expression=False)
    T11 = Tree(tree_list=Tlist,
               name='T11',
               switches=ln[4] + [V0] + ln[8] + [V1],
               cut_expression=False)
    T12 = Tree(tree_list=Tlist,
               name='T12',
               switches=ln[4] + [V0] + ln[9] + [V1],
               cut_expression=False)
    T13 = Tree(tree_list=Tlist,
               name='T13',
               switches=ln[5] + [V0] + ln[10] + [V1],
               cut_expression=False)
    T14 = Tree(tree_list=Tlist,
               name='T14',
               switches=ln[5] + [V0] + ln[11] + [V1],
               cut_expression=False)
    T15 = Tree(tree_list=Tlist,
               name='T15',
               switches=ln[6] + [V0] + ln[12] + [V1],
               cut_expression=False)
    T16 = Tree(tree_list=Tlist,
               name='T16',
               switches=ln[6] + [V0] + ln[13] + [V1],
               cut_expression=False)
    T17 = Tree(tree_list=Tlist,
               name='T17',
               switches=ln[7] + [V0] + ln[14] + [V1],
               cut_expression=False)
    T18 = Tree(tree_list=Tlist,
               name='T18',
               switches=ln[7] + [V0] + ln[15] + [V1],
               cut_expression=False)
    T19 = Tree(tree_list=['EQU',
                          [None],
                          [None]],
               name='T19',
               switches=[V0, V1])
    T20 = Tree(tree_list=Tlist,
               name='T20',
               switches=ln[15] + [V0] + ln[15] + [V1],
               cut_expression=False)

    R0 = Room(name='R0',
              position=[2, -2, 15, 0.4],
              switches_list=[])
    R1 = Room(name='R1',
              position=[-2, 0.5, 1.5, 5],
              switches_list=Slist0)
    R2 = Room(name='R2',
              position=[0, 0.5, 1.5, 5],
              switches_list=Slist1)
    R3 = Room(name='R3',
              position=[2, 6.6, 15, 0.4],
              switches_list=[])
    RE = Room(name='RE',
              position=[-2, -2, 1.5, 1],
              is_exit=True)  # E pour exit ou end

    tree_list = [T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18]
    rd_shuffle(tree_list)
    for i in range(len(tree_list)):
        tree_list[i].name = f'T{i + 4}'

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[0, 0],
              relative_arrival_coordinates=[1 / 2, 0],
              relative_position=0.8)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R0,
              room_arrival=R2,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[1 / 2, 0],
              relative_position=0.4)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R1,
              room_arrival=R3,
              relative_departure_coordinates=[1 / 2, 1],
              relative_arrival_coordinates=[0, 1],
              relative_position=0.35)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=[1 / 2, 1],
              relative_arrival_coordinates=[0, 0],
              relative_position=0.6)
    n = 17
    D4 = Door(two_way=False,
              tree=tree_list[0],
              room_departure=R3,
              room_arrival=R0,
              relative_departure_coordinates=[1 / n, 0],
              relative_arrival_coordinates=[1 / n, 1],
              relative_position=1 / 9)
    D5 = Door(two_way=False,
              tree=tree_list[1],
              room_departure=R3,
              room_arrival=R0,
              relative_departure_coordinates=[2 / n, 0],
              relative_arrival_coordinates=[2 / n, 1],
              relative_position=2 / 9)
    D6 = Door(two_way=False,
              tree=tree_list[2],
              room_departure=R3,
              room_arrival=R0,
              relative_departure_coordinates=[3 / n, 0],
              relative_arrival_coordinates=[3 / n, 1],
              relative_position=3 / 9)
    D7 = Door(two_way=False,
              tree=tree_list[3],
              room_departure=R3,
              room_arrival=R0,
              relative_departure_coordinates=[4 / n, 0],
              relative_arrival_coordinates=[4 / n, 1],
              relative_position=4 / 9)
    D8 = Door(two_way=False,
              tree=tree_list[4],
              room_departure=R3,
              room_arrival=R0,
              relative_departure_coordinates=[5 / n, 0],
              relative_arrival_coordinates=[5 / n, 1],
              relative_position=5 / 9)
    D9 = Door(two_way=False,
              tree=tree_list[5],
              room_departure=R3,
              room_arrival=R0,
              relative_departure_coordinates=[6 / n, 0],
              relative_arrival_coordinates=[6 / n, 1],
              relative_position=6 / 9)
    D10 = Door(two_way=False,
               tree=tree_list[6],
               room_departure=R3,
               room_arrival=R0,
               relative_departure_coordinates=[7 / n, 0],
               relative_arrival_coordinates=[7 / n, 1],
               relative_position=7 / 9)
    D11 = Door(two_way=False,
               tree=tree_list[7],
               room_departure=R3,
               room_arrival=R0,
               relative_departure_coordinates=[8 / n, 0],
               relative_arrival_coordinates=[8 / n, 1],
               relative_position=8 / 9)
    D12 = Door(two_way=False,
               tree=tree_list[8],
               room_departure=R3,
               room_arrival=R0,
               relative_departure_coordinates=[9 / n, 0],
               relative_arrival_coordinates=[9 / n, 1],
               relative_position=1 / 9)
    D13 = Door(two_way=False,
               tree=tree_list[9],
               room_departure=R3,
               room_arrival=R0,
               relative_departure_coordinates=[10 / n, 0],
               relative_arrival_coordinates=[10 / n, 1],
               relative_position=2 / 9)
    D14 = Door(two_way=False,
               tree=tree_list[10],
               room_departure=R3,
               room_arrival=R0,
               relative_departure_coordinates=[11 / n, 0],
               relative_arrival_coordinates=[11 / n, 1],
               relative_position=3 / 9)
    D15 = Door(two_way=False,
               tree=tree_list[11],
               room_departure=R3,
               room_arrival=R0,
               relative_departure_coordinates=[12 / n, 0],
               relative_arrival_coordinates=[12 / n, 1],
               relative_position=4 / 9)
    D16 = Door(two_way=False,
               tree=tree_list[12],
               room_departure=R3,
               room_arrival=R0,
               relative_departure_coordinates=[13 / n, 0],
               relative_arrival_coordinates=[13 / n, 1],
               relative_position=5 / 9)
    D17 = Door(two_way=False,
               tree=tree_list[13],
               room_departure=R3,
               room_arrival=R0,
               relative_departure_coordinates=[14 / n, 0],
               relative_arrival_coordinates=[14 / n, 1],
               relative_position=6 / 9)
    D18 = Door(two_way=False,
               tree=tree_list[14],
               room_departure=R3,
               room_arrival=R0,
               relative_departure_coordinates=[15 / n, 0],
               relative_arrival_coordinates=[15 / n, 1],
               relative_position=7 / 9)
    D19 = Door(two_way=False,
               tree=T19,
               room_departure=R3,
               room_arrival=R0,
               relative_departure_coordinates=[16 / n, 0],
               relative_arrival_coordinates=[16 / n, 1],
               relative_position=8 / 9)
    D20 = Door(two_way=False,
               tree=T20,
               room_departure=R0,
               room_arrival=RE,
               relative_departure_coordinates=[0, 0],
               relative_arrival_coordinates=[1, 1 / 2],
               relative_position=1 / 2)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19,
                             D20],
                 fastest_solution=None,
                 level_color=Levels_colors_list.RED_AND_YELLOW,
                 name='Tree',
                 random=True,
                 border=40,
                 door_window_size=250)

    return level
