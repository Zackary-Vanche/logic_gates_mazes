from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from itertools import permutations
from math import ceil

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
    S24 = Switch(name='S24')
    S25 = Switch(name='S25')
    S26 = Switch(name='S26')
    S27 = Switch(name='S27')
    S28 = Switch(name='S28')
    S29 = Switch(name='S29')
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29]

    Slist_0 = [S0, S1, S2, S3, S4, S5]
    Slist_1 = [S6, S7, S8, S9, S10, S11]
    Slist_2 = [S12, S13, S14, S15, S16, S17]
    Slist_3 = [S18, S19, S20, S21, S22, S23]
    Slist_4 = [S24, S25, S26, S27, S28, S29]
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

    Vlist_size6 = [V0, V1, V2, V3, V4]
    
    bin_list = [[rd_choice([0, 1]) for j in range(6)] for i in range(5)]
    p_list = [[l[0]+l[1]*2+l[2]*4, l[3]+l[4]*2+l[5]*4] for l in bin_list]
    values_list = [sum([l[i]*2**i for i in range(len(l))]) for l in bin_list]
    
    index_permutations_list = list(permutations(range(5)))
    min_length = float('inf')
    for index_permutation in index_permutations_list:
        length_max = 0
        for k in range(5):
            i = index_permutation[k]
            j = index_permutation[(k+1)%5]
            a = p_list[i]
            b = p_list[j]
            dx = a[0] - b[0]
            dy = a[1] - b[1]
            length_max = max(length_max, (dx**2 + dy**2)**(1/2))
        if length_max < min_length:
            min_length = length_max
            solution_permutation = index_permutation
            
    old_min_length = min_length
    min_length = ceil(min_length*100)/100
    assert old_min_length <= min_length, f"{old_min_length} !<= {min_length}"
            
    # solution_p_list = [p_list[k] for k in solution_permutation]
    # import matplotlib.pyplot as plt
    # plt.plot([p[0] for p in solution_p_list]+[solution_p_list[0][0]],
    #          [p[1] for p in solution_p_list]+[solution_p_list[0][1]])
    # plt.scatter([p[0] for p in solution_p_list],
    #             [p[1] for p in solution_p_list])
    # plt.show()
    
    Vlist_size3 = [Tree(tree_list=Tree.tree_list_BIN(3),
                        name=f'V{5+i}',
                        switches=Slist[3*i:3*i+3]) for i in range(10)]
    
    tree_list_DIST = ['DIST'] + [[None]] * 4
    tree_list_SUM = ['MAX'] + [tree_list_DIST] * 5
    
    Slist_V15 = []
    for i in range(5):
        j = (i+1)%5
        Slist_V15.extend(Vlist_size3[2*i:2*i+2])
        Slist_V15.extend(Vlist_size3[2*j:2*j+2])
    
    V15=Tree(tree_list=tree_list_SUM,
             name='V15',
             switches=Slist_V15,
             cut_expression_depth_1=True)
    
    values_list = sorted(values_list)

    def get_tree(i):
        if i == 0:
            return Tree(tree_list=Tree.tree_list_IN(1+5),
                        name=f'T{i}',
                        switches=[V0]+values_list)
        elif i < 4:
            return Tree(tree_list=Tree.tree_list_IN(1+5),
                        name=f'T{i}',
                        switches=[Vlist_size6[i]]+values_list)
        else:
            return Tree(tree_list=["AND",
                                   Tree.tree_list_IN(1+5),
                                   Tree.tree_list_EQUSET(10),
                                   Tree.tree_list_INFOREQU(2)],
                        name=f'T{i}',
                        switches=[Vlist_size6[i]]+values_list+Vlist_size6+values_list+[V15, min_length],
                        cut_expression_depth_1=True)

    dx = -4
    dy = -3
    ex = 3
    ey = 2

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=Slist_4)
    RE = Room(name='RE',
              position=[1*dx, 0*dy, ex, ey],
              is_exit=True)

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
                room_arrival=R4)
    D4 = Door(two_way=False,
                tree=get_tree(4),
                name='D4',
                room_departure=R4,
                room_arrival=RE)
    
    sol_list = []
    for ik, k in enumerate(solution_permutation):
        for ibit, bit in enumerate(bin_list[k]):
            if bit:
                sol_list.append(f"S{ik*6+ibit}")
        sol_list.append(f'D{ik}')

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4],
                 fastest_solution=' '.join(sol_list),
                 level_color=get_color(),
                 name='Random bottleneck travelling salesman',
                 keep_proportions=True,
                 door_window_size=400,
                 random=True)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.25, sa=0.2, li=0.4)
    lcolor.surrounding_color = Color.color_hls(hu=0.75, sa=1, li=0.6)
    lcolor.contour_color = Color.color_hls(hu=0.75, sa=1, li=0.6)
    return lcolor