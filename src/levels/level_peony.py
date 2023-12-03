from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def level_peony(): 

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

    Slist_0 = [S0, S1, S4]
    Slist_1 = [S1, S2, S5]
    Slist_2 = [S2, S3, S6]
    Slist_3 = [S3, S0, S7]

    V0 = Tree(tree_list=Tree.tree_list_SUM(3),
          name='V0',
          switches=Slist_0)
    V1 = Tree(tree_list=Tree.tree_list_SUM(3),
          name='V1',
          switches=Slist_1)
    V2 = Tree(tree_list=Tree.tree_list_SUM(3),
          name='V2',
          switches=Slist_2)
    V3 = Tree(tree_list=Tree.tree_list_SUM(3),
          name='V3',
          switches=Slist_3)

    T0 = Tree(tree_list=['AND',
                         ['EQU', [None], [None]],
                         ['EQU', [None], [None]],
                         ['EQU', [None], [None]],
                         ['EQU', [None], [None]],
                         ['EQU', [None], Tree.tree_list_SUM(8)],
                         ['INF', Tree.tree_list_BIN(3), Tree.tree_list_BIN(3)]],
                name='T0',
                switches=[V0, 1,
                          V1, 2,
                          V2, 1,
                          V3, 2,
                          4, S0, S1, S2, S3, S4, S5, S6, S7,
                          S0, S1, S4, S3, S2, S6],
                cut_expression_depth_1=True)
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[S0])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[S1])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[S2])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[S3])
    T5 = Tree(tree_list=[None],
                name='T5',
                switches=[S4])
    T6 = Tree(tree_list=[None],
                name='T6',
                switches=[S5])
    T7 = Tree(tree_list=[None],
                name='T7',
                switches=[S6])
    T8 = Tree(tree_list=[None],
                name='T8',
                switches=[S7])
    T9 = Tree(tree_list=Tree.tree_list_AND(5),
                name='T9',
                switches=[S8, S9, S10, S11, S12])

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5
    ax = 1

    R0 = Room(name='R0',
                position=[0*dx-ax, 4*dy, 2*dx+ex+ax, ey*0.5],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7])
    R1 = Room(name='R1',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S8])
    R2 = Room(name='R2',
                position=[1*dx, 3*dy, ex, ey],
                switches_list=[S9])
    R3 = Room(name='R3',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S10])
    R4 = Room(name='R4',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S11])
    R5 = Room(name='R5',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S12])
    RE = Room(name='RE',
              position=[0*dx-ax, 3*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R2)
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R3)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R4)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R1,
                room_arrival=R5)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R2,
                room_arrival=R3)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R3,
                room_arrival=R4)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R4,
                room_arrival=R5)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R5,
                room_arrival=R2)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R5,
                room_arrival=RE)
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0.85, sa=0.3, li=0.7)
    lcolor.contour_color = Color.GREEN
    lcolor.surrounding_color = Color.GREEN

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9],
                 fastest_solution="S0 S2 S5 S7 D0 S9 D1 S8 D3 S11 D6 S10 D6 D3 D1 D8 S12 D9",
                 level_color=lcolor,
                 name='Peony',
                 keep_proportions=True,
                 door_window_size=315)
    
    return level

