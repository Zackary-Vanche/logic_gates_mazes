from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
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
    
    Slist = [S0, S1, S2, S3, S4, S5, S6,]

    T0 = Tree(tree_list=[None],
              name='T0',
              switches=[1])
    T1 = Tree(tree_list=[None],
              name='T1',
              switches=[1])
    T2 = Tree(tree_list=[None],
              name='T2',
              switches=[S0])
    T3 = Tree(tree_list=[None],
              name='T3',
              switches=[S0])
    T4 = Tree(tree_list=[None],
              name='T4',
              switches=[S1])
    T5 = Tree(tree_list=[None],
              name='T5',
              switches=[S1])
    T6 = Tree(tree_list=[None],
              name='T6',
              switches=[S2])
    T7 = Tree(tree_list=[None],
              name='T7',
              switches=[S3])
    T8 = Tree(tree_list=[None],
              name='T8',
              switches=[S3])
    T9 = Tree(tree_list=[None],
              name='T9',
              switches=[S4])
    T10 = Tree(tree_list=[None],
               name='T10',
               switches=[S5])
    T11 = Tree(tree_list=[None],
               name='T11',
               switches=[S6])
    
    possibles_solutions = ["D0 S0 D2 S2 D6 S5 D10 D12",
                           "D0 S0 D3 S3 D7 S5 D10 D12",
                           "D0 S0 D3 S3 D8 S6 D11 D12",
                           "D1 S1 D4 S3 D7 S5 D10 D12",
                           "D1 S1 D4 S3 D8 S6 D11 D12",
                           "D1 S1 D5 S4 D9 S6 D11 D12"]
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
    
    Slist_T12 = []
    for i in range(len(l)):
        Slist_T12.extend([l[i], Slist[i]])
    
    T12 = Tree(tree_list=["INFOREQU",
                          ["SUM"]+[Tree.tree_list_PROD(2)]*len(l),
                          [None]],
               name='T12',
               switches=Slist_T12+[Spath_min])
    
    a = 1.5

    R0 = Room(name='R0',
              position=[0, 2 * a, 1, 1],
              switches_list=[])
    R1 = Room(name='R1',
              position=[2, 1 * a, 1, 1],
              switches_list=[S0])
    R2 = Room(name='R2',
              position=[2, 3 * a, 1, 1],
              switches_list=[S1])
    R3 = Room(name='R3',
              position=[4, 0, 1, 1],
              switches_list=[S2])
    R4 = Room(name='R4',
              position=[4, 2 * a, 1, 1],
              switches_list=[S3])
    R5 = Room(name='R5',
              position=[4, 4 * a, 1, 1],
              switches_list=[S4])
    R6 = Room(name='R6',
              position=[6, 1 * a, 1, 1],
              switches_list=[S5])
    R7 = Room(name='R7',
              position=[6, 3 * a, 1, 1],
              switches_list=[S6])
    R8 = Room(name='R8',
              position=[8, 2 * a, 1, 1],
              switches_list=[])
    RE = Room(name='RE',
              position=[8, 4 * a, 1, 1],
              is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R0,
              room_arrival=R2)

    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R1,
              room_arrival=R3)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R1,
              room_arrival=R4)

    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R2,
              room_arrival=R4)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R2,
              room_arrival=R5)

    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R3,
              room_arrival=R6)

    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R4,
              room_arrival=R6)
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R4,
              room_arrival=R7)

    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R5,
              room_arrival=R7)

    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R6,
               room_arrival=R8)

    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R7,
               room_arrival=R8)

    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R8,
               room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12],
                 fastest_solution=possibles_solutions[i_min_sol],
                 level_color=get_color(),
                 name='Longest path',
                 door_window_size=300,
                 keep_proportions=True,
                 random=True)

    return level

def get_color():
    return Levels_colors_list.FROM_HUE_light_background(hu=0.9, sa=0.2, li=0.2)