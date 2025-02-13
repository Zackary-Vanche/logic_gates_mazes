from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle
from random import choice as rd_choice

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
    S15 = Switch(name='S15')
    S16 = Switch(name='S16')
    S17 = Switch(name='S17')
    # S18 = Switch(name='S18')
    # S19 = Switch(name='S19')
    # S20 = Switch(name='S20')
    # S21 = Switch(name='S21')
    # S22 = Switch(name='S22')
    # S23 = Switch(name='S23')

    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    Slist_3 = [S9, S10, S11]
    Slist_4 = [S12, S13, S14]
    Slist_5 = [S15, S16, S17]
    
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
    
    Vlist_bin = [V0, V1, V2, V3, V4, V5]
    
    value_list = [i for i in range(36) if i//6<i%6]
    rd_shuffle(value_list)
    value_list = value_list[:rd_choice([i for i in range(5, len(value_list))])]
    value_list = sorted(value_list)
    
    Vlist_edge = []
    for i, value in enumerate(value_list):
        Va = Vlist_bin[value//6]
        Vb = Vlist_bin[value%6]
        Vlist_edge.append(Tree(tree_list=["SUM", Tree.tree_list_MAX(2), ["PROD", [None], Tree.tree_list_MIN(2)]],
                               name=f'V{i+6}',
                               switches=[Va, Vb, 6, Va, Vb]))
    
    V = Tree(tree_list=Tree.tree_list_EQUSET(len(Vlist_edge)*2),
             name=f'V{len(Vlist_edge)+6}',
             switches=value_list+Vlist_edge)

    T0 = Tree(tree_list=Tree.tree_list_INF(2),
                name='T0',
                switches=[V0, 6])
    T1 = Tree(tree_list=["AND", Tree.tree_list_INF(2), Tree.tree_list_DIFF(2)],
                name='T1',
                switches=[V1, 6, V0, V1])
    T2 = Tree(tree_list=["AND", Tree.tree_list_INF(2), Tree.tree_list_DIFF(3)],
                name='T2',
                switches=[V2, 6, V0, V1, V2])
    T3 = Tree(tree_list=["AND", Tree.tree_list_INF(2), Tree.tree_list_DIFF(4)],
                name='T3',
                switches=[V3, 6, V0, V1, V2, V3])
    T4 = Tree(tree_list=["AND", Tree.tree_list_INF(2), Tree.tree_list_DIFF(5)],
                name='T4',
                switches=[V4, 6, V0, V1, V2, V3, V4])
    T5 = Tree(tree_list=["AND", Tree.tree_list_INF(2), Tree.tree_list_DIFF(6), [None]],
                name='T5',
                switches=[V5, 6, V0, V1, V2, V3, V4, V5, V])

    dx = 1
    dy = 1
    ex = 0.5
    ey = 3

    R0 = Room(name='R0',
                position=[0, dy, ex, ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[dx, dy, ex, ey],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[2*dx, dy, ex, ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[3*dx, dy, ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[4*dx, dy, ex, ey],
                switches_list=Slist_4)
    R5 = Room(name='R5',
                position=[5*dx, dy, ex, ey],
                switches_list=Slist_5)
    RE = Room(name='RE',
              position=[5*dx, 0, ex, ex],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R5)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R5,
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[1/2, 1])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Isomorphism',
                 keep_proportions=True,
                 door_window_size=340,
                 random=True)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.9, sa=0.2, li=0.25)