
from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle
from random import randint as rd_randint

def DFS(g, n):
    dist_dict = {}
    l_to_visit = [[n, []]]
    while l_to_visit != []:
        couple = l_to_visit.pop(0)
        n, path = couple
        path.append(n)
        dist_dict[n] = path[:]
        for child in g[n]:
            if not child in dist_dict.keys():
                l_to_visit.append([child, path[:]])
    return dist_dict

def longest_path(g):
    # On applique deux recherches DFS, en partant d'un noeud au hasard (0)
    # puis en partant du noeur le plus loin du noeud 0
    # Le plus long chemin trouvé lors de la deuxième recherche est le plus long chemin possible dans l'arbre
    # (On suppose que g est le graphe d'un arbre)
    def aux_longest_path(dist_dict):
        paths_list = list(dist_dict.values())
        paths_list.sort(key=len)
        return paths_list[-1]
    path = aux_longest_path(DFS(g, 0))
    n = path[-1]
    path = aux_longest_path(DFS(g, n))
    return path

def f():
    
    Nlist = [i for i in range(16)]
    rd_shuffle(Nlist)
    
    g = {i:[] for i in range(16)}
    g[Nlist[0]].append(Nlist[1])
    g[Nlist[0]].append(Nlist[2])
    g[Nlist[0]].append(Nlist[3])
    g[Nlist[1]].append(Nlist[0])
    g[Nlist[2]].append(Nlist[0])
    g[Nlist[3]].append(Nlist[0])
    for i in range(4, 16):
        n = Nlist[i]
        a = Nlist[rd_randint(0, i-1)]
        g[a].append(n)
        g[n].append(a)
        
    path = longest_path(g)
    
    nbin = 4
    nR = len(path)+1
    # nR = 16

    Slist = [Switch(name=f'S{i}') for i in range(nbin*nR-1)]

    Sl_list = [Slist[nbin*i:nbin*i+nbin] for i in range(nR-1)]
    
    Vlist_S = [Tree(tree_list=Tree.tree_list_BIN(len(Sl_list[i])),
                    name=f'V{i}',
                    switches=Sl_list[i]) for i in range(nR-1)]
    
    tree_list_V = ["SUM", Tree.tree_list_PROD(2), [None]]
    
    Vlist_D = [Tree(tree_list=tree_list_V,
                    name=f'V{len(Vlist_S)+i}',
                    switches=[Vlist_S[i], 16, Vlist_S[i+1]]) for i in range(nR-2)]
        
    Vlist_v = []
    for k in g.keys():
        for a in g[k]:
            Vlist_v.append(Tree(tree_list=tree_list_V,
                                name=f'V{2*nR-3+len(Vlist_v)}',
                                switches=[16, k, a]))
            
    dx = 1
    dy = 1
    ex = 0.6
    ey = 0.6
    ax = 0.225
    ay = 0.225
    
    pos_list = [[   0*dx, 0*dy+ay, ex, ey],
                [1*dx+ax,    0*dy, ex, ey],
                [1*dx+ax, 1*dy+ay, ex, ey],
                [   0*dx,    1*dy, ex, ey],
                [   0*dx, 2*dy+ay, ex, ey],
                [   1*dx, 2*dy-ay/2, ex, ey],
                [2*dx+ax, 2*dy+ay, ex, ey],
                [2*dx+ax/2,    1*dy, ex, ey],
                [   2*dx,    0*dy, ex, ey],
                [   3*dx,    0*dy, ex, ey],
                [   3*dx-ax/2,    1*dy, ex, ey],
                [   3*dx,    2*dy, ex, ey],
                [   3*dx,    3*dy, ex, ey],
                [   2*dx,    3*dy, ex, ey],
                [   1*dx,    3*dy-ay/2, ex, ey],
                [   0*dx,    3*dy, ex, ey],]
    
    Rlist = [Room(name=f'R{i}',
                  position=pos_list[i],
                  switches_list=Sl_list[i]) for i in range(nR-1)]
    Rlist.append(Room(name='RE',
                      is_exit = True,
                      position=pos_list[nR-1],
                      switches_list=[]))
    
    T0 = Tree(tree_list=Tree.tree_list_INLIST(2+len(Vlist_v)),
                         name='T0',
                         switches=[1, Vlist_D[0]]+Vlist_v)
    T0 = Tree(tree_list=[None],
                         name='T0',
                         switches=[1])
    
    Tlist = [T0] + [Tree(tree_list=["AND",
                                    Tree.tree_list_INLIST(2+len(Vlist_v)),
                                    Tree.tree_list_DIFF(i+1),
                                    ],
                         name=f'T{i}',
                         switches=[1, Vlist_D[i-1]]+Vlist_v+Vlist_S[:i+1],
                         cut_expression_depth_1=True) for i in range(1, nR-2)]
    
    Tlist.append(Tree(tree_list=["AND",
                                 Tree.tree_list_INLIST(2+len(Vlist_v)),
                                 Tree.tree_list_DIFF(len(Vlist_S)),
                                 ],
                      name=f'T{len(Tlist)}',
                      switches=[1, Vlist_D[-1]]+Vlist_v+Vlist_S,
                      cut_expression_depth_1=True))
    
    Dlist = [Door(two_way=False,
                  tree=Tlist[i],
                  name=f'D{i}',
                  room_departure=Rlist[i],
                  room_arrival=Rlist[i+1]) for i in range(nR-1)]
    
    for R in Rlist:
        assert isinstance(R, Room), str(R)
    for D in Dlist:
        assert isinstance(D, Door), str(D)
        
    bin_list = []
    for n in path:
        for i in range(4):
            bin_list.append(n%2)
            n = n//2
    sol_list = []
    for i in range(len(bin_list)):
        if bin_list[i]:
            sol_list.append(f'S{i}')
        if (i+1)%nbin == 0:
            sol_list.append(f'D{i//4}')
    sol = ' '.join(sol_list)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=Rlist,
                 doors_list=Dlist,
                 fastest_solution=sol,
                 level_color=get_color(),
                 name='Tree diameter',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.14, sa=0.35, li=0.4)
    lcolor.surrounding_color = Color.color_hls(hu=0.4, sa=0.35, li=0.75)
    lcolor.contour_color = Color.color_hls(hu=0.4, sa=0.35, li=0.75)
    return lcolor