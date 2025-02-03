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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11]
    
    V0 = Tree(tree_list=["AND",
                         ["IN", Tree.tree_list_SUM(3), [None], [None]],
                         ["IN", Tree.tree_list_SUM(2), [None], [None]],
                         ["IN", Tree.tree_list_SUM(4), [None], [None]],
                         ["IN", Tree.tree_list_SUM(3), [None], [None]],
                         ["IN", Tree.tree_list_SUM(3), [None], [None]],
                         ["IN", Tree.tree_list_SUM(3), [None], [None]],
                         ["IN", Tree.tree_list_SUM(2), [None], [None]]
                         ],
              name='V0',
              switches=[S0, S1, S8, 0, 2,
                        S1, S10, 0, 2,
                        S2, S3, S8, S9, 0, 2,
                        S2, S6, S7, 0, 2,
                        S3, S10, S11, 0, 2,
                        S4, S5, S9, 0, 2,
                        S4, S7, 0, 2,
                        ],
              cut_expression_depth_1=True)
    
    possibles_solutions = ["S0 S1 S10 S11 D0 D1 D10 D11",
                           "S0 S3 S8 S11 D0 D8 D3 D11",
                           "S0 S5 S8 S9 D0 D8 D9 D5",
                           "S2 S3 S6 S11 D6 D2 D3 D11",
                           "S2 S5 S6 S9 D6 D2 D9 D5",
                           "S4 S5 S6 S7 D6 D7 D4 D5",
                           "S0 S1 S2 S4 S7 S9 S10 S11 D0 D1 D10 D11",
                           "S0 S1 S2 S5 S6 S9 S10 S11 D0 D1 D10 D11",
                           "S0 S1 S2 S5 S6 S9 S10 S11 D6 D2 D9 D5",
                           "S0 S1 S4 S5 S6 S7 S10 S11 D0 D1 D10 D11",
                           "S0 S1 S4 S5 S6 S7 S10 S11 D6 D7 D4 D5",
                           "S0 S3 S4 S5 S6 S7 S8 S11 D0 D8 D3 D11",
                           "S0 S3 S4 S5 S6 S7 S8 S11 D6 D7 D4 D5",
                           "S1 S3 S4 S5 S6 S7 S8 S10 D6 D7 D4 D5",
                           "S0 S1 S3 S5 S9 S10 D0 D1 D10 D3 D9 D5",
                           "S0 S2 S4 S5 S7 S8 D0 D8 D2 D7 D4 D5",
                           "S1 S2 S6 S8 S10 S11 D6 D2 D8 D1 D10 D11",
                           "S3 S4 S6 S7 S9 S11 D6 D7 D4 D9 D3 D11",
                           "S0 S1 S2 S3 S4 S5 S7 S10 D0 D1 D10 D3 D2 D7 D4 D5",
                           "S1 S4 S6 S7 S8 S9 S10 S11 D6 D7 D4 D9 D8 D1 D10 D11"]
    l = [rd_randint(1, 31) for i in range(len(Slist))]
    i_min_sol = 0
    Spath_min = float('inf')
    for isol, sol in enumerate(possibles_solutions):
        Spath = 0
        for i, S in enumerate(Slist):
            if S.name in sol:
                Spath += l[i]
        if Spath < Spath_min:
            Spath_min = Spath
            i_min_sol = isol
    
    Slist_V1 = []
    for i in range(len(l)):
        Slist_V1.extend([l[i], Slist[i]])
    
    V1 = Tree(tree_list=["INFOREQU",
                         ["SUM"]+[Tree.tree_list_PROD(2)]*len(l),
                         [None]],
              name='V1',
              switches=Slist_V1+[Spath_min])

    T0 = Tree(tree_list=Tree.tree_list_AND(3),
                name='T0',
                switches=[S0, V0, V1])
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[S1])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[S2])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[S3])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[S4])
    T5 = Tree(tree_list=[None],
                name='T5',
                switches=[S5])
    T6 = Tree(tree_list=Tree.tree_list_AND(3),
                name='T6',
                switches=[S6, V0, V1])
    T7 = Tree(tree_list=[None],
                name='T7',
                switches=[S7])
    T8 = Tree(tree_list=[None],
                name='T8',
                switches=[S8])
    T9 = Tree(tree_list=[None],
                name='T9',
                switches=[S9])
    T10 = Tree(tree_list=[None],
                name='T10',
                switches=[S10])
    T11 = Tree(tree_list=[None],
                name='T11',
                switches=[S11])

    dx = 1
    dy = 1
    ex = 0.6
    ey = 0.6
    
    a = 0.75
    exe = 4*ex*a
    eye = 3*ey*a

    R0 = Room(name='R0',
                position=[0*dx-exe+ex, 0*dy-eye+ey, exe, eye],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[])
    R4 = Room(name='R4',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[])
    R5 = Room(name='R5',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[])
    R6 = Room(name='R6',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[])
    R7 = Room(name='R7',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[2*dx, 2*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[(exe-ex/2)/exe, (eye-ey/2)/eye])
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R3,
                room_arrival=R4)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R4,
                room_arrival=R5)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R6,
                room_arrival=R7)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R7,
                room_arrival=RE)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=R3,
                relative_departure_coordinates=[(exe-ex/2)/exe, (eye-ey/2)/eye])
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R3,
                room_arrival=R6)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R1,
                room_arrival=R4)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R4,
                room_arrival=R7)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R2,
                room_arrival=R5)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R5,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11],
                 fastest_solution=possibles_solutions[i_min_sol],
                 level_color=get_color(),
                 name='Maximize',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def get_color():
    return Levels_colors_list.WHITE