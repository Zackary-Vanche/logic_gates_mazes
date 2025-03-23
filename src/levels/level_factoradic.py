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
    Slist_0 = [S0,]
    Slist_1 = [S1, S2,]
    Slist_2 = [S3, S4,]
    Slist_3 = [S5, S6, S7]
    Slist_4 = [S8, S9, S10]
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
    V5 = Tree(tree_list=["SUM", [None], # V0
                         ["PROD", [None], # 2
                          ["SUM", [None], # V1
                           ["PROD", [None], # 3
                            ["SUM", [None], # V2
                             ["PROD", [None], # 4
                              ["SUM", [None], # V3
                               ["PROD", [None], # 5
                                [None]] # V4
                               ]
                              ]
                             ]
                            ]
                           ]
                          ]
                         ],
          name='V5',
          switches=[V0,
                    2, V1,
                    3, V2,
                    4, V3,
                    5, V4]
                   )

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[1])
    T1 = Tree(tree_list=Tree.tree_list_INFOREQU(2),
                name='T1',
                switches=[V1, 2])
    T2 = Tree(tree_list=Tree.tree_list_INFOREQU(2),
                name='T2',
                switches=[V2, 3])
    T3 = Tree(tree_list=Tree.tree_list_INFOREQU(2),
                name='T3',
                switches=[V3, 4])
    T4 = Tree(tree_list=Tree.tree_list_INFOREQU(2),
                name='T4',
                switches=[V4, 5])
    T5 = Tree(tree_list=Tree.tree_list_EQU(2),
                name='T5',
                switches=[V5, rd_randint(0, 2*3*4*5*6-1)])

    dx = 0.75
    ex = 0.4
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 0, ex, ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[1*dx, 0, ex, 2*ey],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[2*dx, 0, ex, 2*ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[3*dx, 0, ex, 3*ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[4*dx, 0, ex, 3*ey],
                switches_list=Slist_4)
    R5 = Room(name='R5',
                position=[4*dx, -2*ey, ex, ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[3*dx, -2*ey, ex, ey],
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
                room_arrival=R5,
                relative_departure_coordinates=[1/2, 0.5/3])
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R5,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Factoradic',
                 keep_proportions=True,
                 door_window_size=425,
                 random=True)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.15, sa=0.15, li=0.7)
    lcolor.surrounding_color = Color.IVORY
    lcolor.contour_color = Color.IVORY
    return lcolor