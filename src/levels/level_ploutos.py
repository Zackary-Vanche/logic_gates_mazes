from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color
from Color import Color

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
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')
    S20 = Switch(name='S20')

    Slist_0 = [S0, S1, S2, S3, S4, S5]
    Slist_1 = [S6, S7, S8]
    Slist_2 = [S9, S10, S11]
    Slist_3 = [S12, S13, S14]
    Slist_4 = [S15, S16, S17]
    Slist_5 = [S18, S19, S20]
    V0 = Tree(tree_list=["SUM", Tree.tree_list_BIN(len(Slist_0)), [None]],
          name='V0',
          switches=Slist_0+[1])
    V1 = Tree(tree_list=["SUM", Tree.tree_list_BIN(len(Slist_1)), [None]],
          name='V1',
          switches=Slist_1+[1])
    V2 = Tree(tree_list=["SUM", Tree.tree_list_BIN(len(Slist_2)), [None]],
          name='V2',
          switches=Slist_2+[1])
    V3 = Tree(tree_list=["SUM", Tree.tree_list_BIN(len(Slist_3)), [None]],
          name='V3',
          switches=Slist_3+[1])
    V4 = Tree(tree_list=["SUM", Tree.tree_list_BIN(len(Slist_4)), [None]],
          name='V4',
          switches=Slist_4+[1])
    V5 = Tree(tree_list=["SUM", Tree.tree_list_BIN(len(Slist_5)), [None]],
          name='V5',
          switches=Slist_5+[1])
    
    tree_list_EQU_MOD = ["EQU", ["MOD", [None], [None]], [None]]
    
    V6 = Tree(tree_list=tree_list_EQU_MOD,
              name='V6',
              switches=[V0, V1, 0])
    V7 = Tree(tree_list=tree_list_EQU_MOD,
              name='V7',
              switches=[V0, V2, 0])
    V8 = Tree(tree_list=tree_list_EQU_MOD,
              name='V8',
              switches=[V0, V3, 0])
    V9 = Tree(tree_list=tree_list_EQU_MOD,
              name='V9',
              switches=[V0, V4, 0])
    V10 = Tree(tree_list=tree_list_EQU_MOD,
              name='V10',
              switches=[V0, V5, 0])

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[1])
    T1 = Tree(tree_list=["AND", [None], Tree.tree_list_INF(2)],
                name='T1',
                switches=[V6, 1, V1])
    T2 = Tree(tree_list=["AND", [None], Tree.tree_list_INF(2)],
                name='T2',
                switches=[V7, V1, V2])
    T3 = Tree(tree_list=["AND", [None], Tree.tree_list_INF(2)],
                name='T3',
                switches=[V8, V2, V3])
    T4 = Tree(tree_list=["AND", [None], Tree.tree_list_INF(2)],
                name='T4',
                switches=[V9, V3, V4])
    T5 = Tree(tree_list=["AND",
                         [None],
                         Tree.tree_list_INF(2),
                         ["INF", ["POW", [None], [None]], [None]]],
                name='T5',
                switches=[V10,
                          V4, V5,
                          V5, 2, V0])

    dx = 1.05
    dy = 2
    ex = 1
    ey = 1

    R0 = Room(name='R0',
                position=[2*dx, 0*dy, 5*dx+ex, ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[0*dx, 1*dy, 3*dx+ex, ey],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[1*dx, 2*dy, 3*dx+ex, ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[3*dx, 3*dy, 3*dx+ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[5*dx, 2*dy, 3*dx+ex, ey],
                switches_list=Slist_4)
    R5 = Room(name='R5',
                position=[6*dx, 1*dy, 3*dx+ex, ey],
                switches_list=Slist_5)
    RE = Room(name='RE',
              position=[4*dx, 1*dy, ex, ey],
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
                relative_departure_coordinates=[0, 1/2],
                relative_arrival_coordinates=[1, 1/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5],
                 fastest_solution="S0 S1 S3 S4 S5 D0 S6 D1 S10 D2 S12 S13 D3 S17 D4 S18 S20 D5",
                 level_color=get_color(),
                 name='Ploutos',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    return Level_color(background_color=Color.color_hls(0.6, 0.1, 0.25),
                       room_color=Color.color_hls(0.1, 0.7, 0.2),
                       letters_color=Color.WHITE,
                       contour_color=Color.WHITE,
                       inside_room_color=Color.BLACK,
                       surrounding_color=Color.WHITE)