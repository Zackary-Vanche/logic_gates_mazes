from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import randint as rd_randint


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
    a = rd_randint(0, 128)
    Sa = Switch(name='?', value=a)

    Slist0 = [S0, S1, S2, S3, S4, S5, S6, S7]
    Slist1 = [S8, S9, S10]
    Slist2 = [S11, S12, S13]
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist0)),
              name='V0',
              switches = Slist0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(len(Slist1)),
              name='V1',
              switches = Slist1)
    V2 = Tree(tree_list=Tree.tree_list_BIN(len(Slist2)),
              name='V2',
              switches = Slist2)

    T0 = Tree(tree_list=[None],
              name='T0',
              switches=[1])
    T1 = Tree(tree_list=['AND',
                         ['INF', [None], [None]],
                         ['EQU', [None], ['SUM', [None], [None]]]],
              name='T1',
              switches=[Sa, V0, V1, 1, V2])
    T2 = Tree(tree_list=['AND',
                         ['EQU', [None], [None]],
                         ['EQU', [None], ['SUM', [None], [None]]]],
              name='T2',
              switches=[Sa, V0, V1, 1, V2])
    T3 = Tree(tree_list=['AND',
                         ['SUP', [None], [None]],
                         ['EQU', [None], ['SUM', [None], [None]]]],
              name='T3',
              switches=[Sa, V0, V1, 1, V2])
    T4 = Tree(tree_list=['EQU', [None], [None]],
              name='T4',
              switches=[V1, V2])
    T5 = Tree(tree_list=['DIFF', [None], [None]],
              name='T5',
              switches=[Sa, 0])
    T6 = Tree(tree_list=['AND',
                         [None],
                         ['EQU', [None], [None]]],
              name='T6',
              switches=[S14, V0, Sa])

    d = 1.5

    R0 = Room(name='R0',
              position=[2 + d, 5, 1, 3],
              switches_list=Slist2)
    R1 = Room(name='R1',
              position=[0, 0, 1, 8],
              switches_list=Slist0)
    R2 = Room(name='R2',
              position=[2 + d, 0, 1, 3],
              switches_list=Slist1)
    R3 = Room(name='R3',
              position=[(2 + d) / 2 + 0.1, 3.5, 0.5, 1],
              switches_list=[S14])
    RE = Room(name='RE',
              position=[2.3 + d, 3, 1.7, 2],
              is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=[1, 3 / 8],
              relative_arrival_coordinates=[0, 1])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R2,
              room_arrival=R0,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[0, 0],
              relative_position=0.2)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R0,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[0, 0],
              relative_position=0.525)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R2,
              room_arrival=R0,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[0, 0],
              relative_position=0.85)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[0, 0],
              relative_arrival_coordinates=[1, 5 / 8])
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R1,
              room_arrival=R3,
              relative_departure_coordinates=[1, 1 / 2],
              relative_arrival_coordinates=[0, 1 / 2])
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R3,
              room_arrival=RE,
              relative_departure_coordinates=[1, 1 / 2],
              relative_arrival_coordinates=[0, 1 / 2],
              relative_position=0.3)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Dichotomy',
                 random=True,
                 door_window_size=300,
                 keep_proportions=True,
                 y_separation=40,
                 border=40)

    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.75, sa=0.5, li=0.6)
    lcolor.room_color = Color.color_hls(hu=0, sa=0.2, li=0.7)
    lcolor.surrounding_color = Color.color_hls(hu=0.75, sa=1, li=0.8)
    lcolor.contour_color = Color.color_hls(hu=0.75, sa=1, li=0.8)
    return lcolor