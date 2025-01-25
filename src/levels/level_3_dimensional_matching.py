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

    nbin = 2
    ns = nbin*3*4
    
    Slist = [Switch(name=f'S{i}') for i in range(ns)]
    
    X = [i for i in range(4)]
    Y = X[:]
    Z = Y[:]
    rd_shuffle(X)
    rd_shuffle(Y)
    rd_shuffle(Z)
    
    edges_solution = [[X[i], Y[i], Z[i]] for i in range(4)]
    # On relie chaque sommet a deux autres sommets (en plus des liens dans edges_solution)
    all_edges_list = edges_solution[:]
    for _ in range(8):
        all_edges_list.append([rd_choice([i for i in range(4)]) for _ in range(3)])
    all_bin_list = [edge[0]+4*edge[1]+16*edge[2] for edge in all_edges_list]
    all_bin_list = list(set(all_bin_list))
    all_bin_list.sort()
    
    Vlist = [Tree(tree_list=Tree.tree_list_BIN(2),
                  name=f'V{i}',
                  switches=Slist[2*i:2*i+2]) for i in range(12)]
    
    tree_list_V = ['SUM',
                   [None],
                   Tree.tree_list_PROD(2),
                   Tree.tree_list_PROD(2)]
    
    V12 = Tree(tree_list=tree_list_V,
          name='V12',
          switches=[Vlist[0], 4, Vlist[1], 16, Vlist[2]])
    V13 = Tree(tree_list=tree_list_V,
          name='V13',
          switches=[Vlist[3], 4, Vlist[4], 16, Vlist[5]])
    V14 = Tree(tree_list=tree_list_V,
          name='V14',
          switches=[Vlist[6], 4, Vlist[7], 16, Vlist[8]])
    V15 = Tree(tree_list=tree_list_V,
          name='V15',
          switches=[Vlist[9], 4, Vlist[10], 16, Vlist[11]])
    
    T0 = Tree(tree_list=["AND"] + [Tree.tree_list_IN(1+len(all_bin_list))]*4,
              name='T0',
              switches=[V12]+all_bin_list+[V13]+all_bin_list+[V14]+all_bin_list+[V15]+all_bin_list,
              cut_expression_depth_1=True)

    dx = 6
    dy = 4
    ex = 1
    ey = 1

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, dx, dy],
                switches_list=Slist)
    RE = Room(name='RE',
              position=[0*dx+ex, 1*dy+ey, dx-2*ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[1/2, 0])
    
    sol_list = []
    for i in range(4):
        edge = edges_solution[i]
        val = edge[0]+4*edge[1]+16*edge[2]
        for j in range(6):
            if val%2 == 1:
                sol_list.append(f"S{6*i+j}")
            val = val//2
    sol_list.append('D0')

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution=' '.join(sol_list),
                 level_color=get_color(),
                 name='3-dimensional matching',
                 keep_proportions=True,
                 door_window_size=400,
                 random=True)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.1, sa=0.3, li=0.7)