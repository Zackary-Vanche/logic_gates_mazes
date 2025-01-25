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
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')
    S20 = Switch(name='S20')
    S21 = Switch(name='S21')
    S22 = Switch(name='S22')
    S23 = Switch(name='S23')

    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    Slist_3 = [S9, S10, S11]
    Slist_4 = [S12, S13, S14]
    Slist_5 = [S15, S16, S17]
    Slist_6 = [S18, S19, S20]
    Slist_7 = [S21, S22, S23]
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
    V6 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_6)),
          name='V6',
          switches=Slist_6)
    V7 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_7)),
          name='V7',
          switches=Slist_7)

    Vlist = [V0, V1, V2, V3, V4, V5, V6, V7]

    dx = 1.25
    dy = 1
    ex = dx
    ey = dy

    a = 0.13
    R0 = Room(name='R0',
                position=[0*dx+a, 0*dy+a, ex, ey],
                switches_list=Slist_0+Slist_1)
    R1 = Room(name='R1',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=Slist_2+Slist_3)
    R2 = Room(name='R2',
                position=[2*dx-a, 2*dy-a, ex, ey],
                switches_list=Slist_4+Slist_5)
    R3 = Room(name='R3',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=Slist_6+Slist_7)
    RE = Room(name='RE',
              position=[1*dx+a, 1*dy-a, ex, ey],
              is_exit=True)
    
    vertices = [i for i in range(8)]
    rd_shuffle(vertices)
    edges_solution = [vertices[2*i:2*i+2] for i in range(4)]
    connections_solution = {}
    for edge in edges_solution:
        connections_solution[edge[0]] = [edge[1]]
        connections_solution[edge[1]] = [edge[0]]
    # On relie chaque sommet a deux autres sommets (en plus des liens dans edges_solution)
    all_edges_list = edges_solution[:]
    for i in range(8):
        for _ in range(2):
            choice_list = [j for j in range(8) if j != i and not j in connections_solution[i]]
            if choice_list != []:
                k = rd_choice(choice_list)
                all_edges_list.append([i, k])
                connections_solution[i].append(k)
                connections_solution[k].append(i)
    all_bin_list = [edge[0]+8*edge[1] for edge in all_edges_list]
    all_bin_list.sort()
    
    def get_tree(i):
        Va = Vlist[2*i]
        Vb = Vlist[2*i+1]
        return Tree(tree_list=["AND",
                               ["IN", ["SUM", [None], Tree.tree_list_PROD(2)],]+[[None]]*len(all_bin_list),
                               Tree.tree_list_DIFF(2*(i+1)),
                               ],
                    name=f'T{i}',
                    switches=[Va, 8, Vb]+all_bin_list+Vlist[:2*i+2],
                    cut_expression_depth_1=True)

    D0 = Door(two_way=False,
                tree=get_tree(0),
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=False,
                tree=get_tree(1),
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=False,
                tree=get_tree(2),
                name='D2',
                room_departure=R2,
                room_arrival=R3)
    D3 = Door(two_way=False,
                tree=get_tree(3),
                name='D3',
                room_departure=R3,
                room_arrival=RE,
                relative_position=0.56)
    
    sol_list = []
    for i in range(4):
        edge = edges_solution[i]
        val = edge[0]+8*edge[1]
        for j in range(6):
            if val%2 == 1:
                sol_list.append(f"S{6*i+j}")
            val = val//2
        sol_list.append(f'D{i}')

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, RE],
                 doors_list=[D0, D1, D2, D3],
                 fastest_solution=' '.join(sol_list),
                 level_color=get_color(),
                 name='Perfect matching',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.9, sa=0.5, li=0.6)
    c = Color.color_hls(hu=0.15, sa=0.9, li=0.7)
    lcolor.surrounding_color = c
    lcolor.contour_color = c
    return lcolor