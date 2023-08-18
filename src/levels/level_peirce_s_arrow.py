from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def level_peirce_s_arrow(): 

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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12]

    Slist_0 = []
    Slist_1 = []
    Slist_2 = []
    Slist_3 = []
    Slist_4 = []
    Slist_5 = []
    Slist_6 = []
    Slist_7 = []
    Slist_8 = []
    Slist_9 = []
    Slist_10 = []
    Slist_11 = []
    Slist_12 = []
    Slist_13 = []
    Slist_14 = []
    Slist_15 = []
    Slist_16 = []
    Slist_17 = []
    Slist_18 = []
    Slist_19 = []

    tree_list = Tree.tree_list_NOR(2)

    V13 = Tree(tree_list=tree_list,
              name='V13',
              switches=[1, 1])
    V14 = Tree(tree_list=tree_list,
              name='V14',
              switches=[1, 1])
    V15 = Tree(tree_list=tree_list,
              name='V15',
              switches=[1, 1])
    V16 = Tree(tree_list=tree_list,
              name='V16',
              switches=[1, 1])
    V17 = Tree(tree_list=tree_list,
              name='V17',
              switches=[1, 1])
    V18 = Tree(tree_list=tree_list,
              name='V18',
              switches=[1, 1])
    V19 = Tree(tree_list=tree_list,
              name='V19',
          switches=[1, 1])

    # NOT
    T0 = Tree(tree_list=tree_list,
                name='T0',
                switches=[S0, S0])

    # AND
    V0 = Tree(tree_list=tree_list,
              name='V0',
              switches=[S1, S1])
    V1 = Tree(tree_list=tree_list,
              name='V1',
              switches=[S2, S2])
    T1 = Tree(tree_list=tree_list,
                name='T1',
                switches=[V0, V1])

    # NAND
    V2 = Tree(tree_list=tree_list,
              name='V2',
              switches=[S3, S3])
    V3 = Tree(tree_list=tree_list,
              name='V3',
              switches=[S4, S4])
    V4 = Tree(tree_list=tree_list,
              name='V4',
              switches=[V2, V3])
    T2 = Tree(tree_list=tree_list,
                name='T2',
                switches=[V4, V4])

    # OR
    V5 = Tree(tree_list=tree_list,
              name='V5',
              switches=[S5, S6])
    T3 = Tree(tree_list=tree_list,
                name='T3',
                switches=[V5, V5])

    # NOR
    T4 = Tree(tree_list=tree_list,
                name='T4',
                switches=[S7, S8])

    # XOR
    V6 = Tree(tree_list=tree_list,
              name='V6',
              switches=[S9, S9])
    V7 = Tree(tree_list=tree_list,
              name='V7',
              switches=[S9, S10])
    V8 = Tree(tree_list=tree_list,
              name='V8',
              switches=[S10, S10])
    V9 = Tree(tree_list=tree_list,
              name='V9',
              switches=[V6, V8])
    T5 = Tree(tree_list=tree_list,
                name='T5',
                switches=[V7, V9])

    # XNOR
    V10 = Tree(tree_list=tree_list,
              name='V10',
              switches=[S11, S12])
    V11 = Tree(tree_list=tree_list,
              name='V11',
              switches=[S11, V10])
    V12 = Tree(tree_list=tree_list,
              name='V12',
              switches=[V10, S12])
    T6 = Tree(tree_list=tree_list,
                name='T6',
                switches=[V11, V12])

    dx = 1
    dy = 1
    ex = 1
    ey = 0.5

    R0 = Room(name='R0',
                position=[2*dx, 3*dy, ex, ey],
                switches_list=[S0])
    R1 = Room(name='R1',
                position=[1.55*dx, 2*dy, ex, ey],
                switches_list=[S1, S2])
    R2 = Room(name='R2',
                position=[1.55*dx, 1*dy, ex, ey],
                switches_list=[S3, S4])
    R3 = Room(name='R3',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[S5, S6])
    R4 = Room(name='R4',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S7, S8])
    R5 = Room(name='R5',
                position=[0.45*dx, 1*dy, ex, ey],
                switches_list=[S9, S10])
    R6 = Room(name='R6',
                position=[0.45*dx, 2*dy, ex, ey],
                switches_list=[S11, S12])
    RE = Room(name='RE',
              position=[0*dx, 3*dy, ex, ey],
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
                room_arrival=R6)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R6,
                room_arrival=RE)

    lcolor = Levels_colors_list.FROM_HUE(hu=0, sa=0.4, li=0.5)
    lcolor.background_color = Color.BLACK
    lcolor.contour_color = Color.BLACK
    lcolor.inside_room_surrounding_color = Color.BLACK

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution="D0 S1 S2 D1 D2 S5 D3 D4 S9 D5 D6",
                 level_color=lcolor,
                 name="Peirce's arrow",
                 keep_proportions=True,
                 door_window_size=300)
    
    return level