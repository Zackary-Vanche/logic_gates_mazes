from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import randint as rd_randint
from random import choice as rd_choice
from random import shuffle as rd_shuffle

def f():

    Slist_0 = [Switch(name=f'S{i}') for i in range(4)]
    Slist_1 = [Switch(name=f'S{i}') for i in range(4, 16+4)]
    rd_shuffle(Slist_1)
    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_0)),
              name='V0',
              switches=Slist_0)

    connections_index_list = [sorted([0, 1]),
                        sorted([14, 15])]
    n = rd_randint(4, 16-4-1)
    for i in range(0, n):
        for j in range(0, i):
            assert j < i < n
            if rd_choice([0, 1]):
                connections_index_list.append(sorted([i, j]))
    for i in range(n+1, 16):
        for j in range(i+1, 16):
            assert n < i < j
            if rd_choice([0, 1]):
                connections_index_list.append(sorted([i, j]))
    for i in range(16):
        if i != n and rd_choice([0, 1]):
            connections_index_list.append(sorted([i, n]))
    connections_index_list = list(set([tuple(c) for c in connections_index_list]))
            
    values_list = [i for i in range(16)]
    rd_shuffle(values_list)
    
    tree_list_aux = ["OR"] + [Tree.tree_list_EQU(2)]*3
    tree_list_1 = ["AND"]
    Slist_tree_1 = []
    for c in connections_index_list:
        i, j = c
        Slist_tree_1.extend([Slist_1[i], Slist_1[j],
                             V0, values_list[i],
                             V0, values_list[j]])
        tree_list_1.append(tree_list_aux)
    Slist_tree_1.extend(Slist_1+[2, 1])
    tree_list_1.append(["EQU", ["MOD", Tree.tree_list_SUM(16), [None]], [None]])

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[1])
    T1 = Tree(tree_list=tree_list_1,
                name='T1',
                switches=Slist_tree_1,
                cut_expression_depth_1=False)

    dx = 1
    dy = 1
    ex = 0.7
    ey = 0.7

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=Slist_1)
    RE = Room(name='RE',
              position=[1*dx, 1*dy, ex, ey],
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
                room_arrival=RE)
    
    sol = []
    nbin = values_list[n]
    for i in range(4):
        if nbin%2 == 1:
            sol.append(Slist_0[i].name)
        nbin = nbin // 2
    sol.append('D0')
    sol_R1 = []
    for i in range(0, n):
        sol_R1.append(Slist_1[i].name)
    if len(sol_R1)%2 == 0:
        sol_R1.append(Slist_1[n].name)
    sol_R1.sort(key = lambda x : int(x.replace('S', '')))
    sol.extend(sol_R1)
    sol.append("D1")
    sol = ' '.join(sol)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, RE],
                 doors_list=[D0, D1],
                 fastest_solution=sol,
                 level_color=get_color(),
                 name='Articulation point',
                 keep_proportions=True,
                 door_window_size=400)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.025, sa=0.4, li=0.2)