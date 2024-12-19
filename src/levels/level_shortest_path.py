from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle

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

    Slist = [S0, S1, S2,
             S3, S4, S5, S6, S7, S8, S9, S10, S11,
             S12, S13, S14]
    
    l_weight = [i for i in range(128)]
    rd_shuffle(l_weight)
    l_weight = l_weight[:15]
    l_weight_0 = l_weight[:3]
    l_weight_1 = l_weight[3:12]
    l_weight_2 = l_weight[12:15]
    assert l_weight_0 + l_weight_1 + l_weight_2 == l_weight
    assert len(l_weight_0) == 3
    assert len(l_weight_1) == 9
    assert len(l_weight_2) == 3
    
    l_sum = []
    sum_dico = {}
    for i in range(len(l_weight_0)):
        Si = [S0, S1, S2][i]
        wi = l_weight_0[i]
        for j in range(len(l_weight_1)):
            Sj = [S3, S4, S5, S6, S7, S8, S9, S10, S11][j]
            wj = l_weight_1[j]
            for k in range(len(l_weight_2)):
                Sk = [S12, S13, S14][k]
                wk = l_weight_2[k]
                w = wi+wj+wk
                l_sum.append(w)
                sum_dico[w] = [Si, Sj, Sk]
                
    solution_list = sum_dico[min(l_sum)]
    solution_list = [S.name for S in solution_list]
                
    Slist_E = []
    for i in range(len(Slist)):
        Slist_E.append(Slist[i])
        Slist_E.append(l_weight[i])
    Slist_E.append(min(l_sum))

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[S0])
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
    T6 = Tree(tree_list=[None],
                name='T6',
                switches=[S6])
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
    T12 = Tree(tree_list=[None],
                name='T12',
                switches=[S12])
    T13 = Tree(tree_list=[None],
                name='T13',
                switches=[S13])
    T14 = Tree(tree_list=[None],
                name='T14',
                switches=[S14])
    T15 = Tree(tree_list=['INFOREQU',
                          ['SUM'] + [['PROD', [None], [None]]]*15,
                          [None]],
                name='T15',
                switches=Slist_E)

    dx = 1
    dy = 1.5
    ex = 0.35
    ey = 1.5
    
    a = 3
    b = 1
    
    R0 = Room(name='R0',
                position=[4*a-4*b, 0*dy, 1.5*dx, 5*ey],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[3*a-3*b, 0*dy, ex, 5*ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[2*a-2*b, 0*dy, ex, 5*ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[a-b, 0*dy, ex, 5*ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[0, 2*dy, 2*ex, ey],
              is_exit=True)
    
    rp0 = 0.55
    rp1 = 0.525
    rp3 = 0.3
    rp4 = 0.4
    rp5 = 0.6
    rp12 = 0.35
    rp13 = 0.4
    
    rc1 = [1/2, 0.5/5]
    rc3 = [1/2, 4.5/5]

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_position=rp0,
                relative_arrival_coordinates=rc1)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R1,
                relative_position=rp1)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=R1,
                relative_position=rp0,
                relative_arrival_coordinates=rc3)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R2,
                relative_position=rp3,
                relative_departure_coordinates=rc1,
                relative_arrival_coordinates=rc1)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R1,
                room_arrival=R2,
                relative_position=rp4,
                relative_departure_coordinates=rc1)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R1,
                room_arrival=R2,
                relative_position=rp5,
                relative_departure_coordinates=rc1,
                relative_arrival_coordinates=rc3)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R1,
                room_arrival=R2,
                relative_position=rp4,
                relative_arrival_coordinates=rc1)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R1,
                room_arrival=R2)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R1,
                room_arrival=R2,
                relative_position=rp4,
                relative_arrival_coordinates=rc3)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R1,
                room_arrival=R2,
                relative_position=rp5,
                relative_departure_coordinates=rc3,
                relative_arrival_coordinates=rc1)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=rc3,
                relative_position=rp4)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R1,
                room_arrival=R2,
                relative_position=rp3,
                relative_departure_coordinates=rc3,
                relative_arrival_coordinates=rc3)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R2,
                room_arrival=R3,
                relative_position=rp12,
                relative_departure_coordinates=rc1)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R2,
                room_arrival=R3,
                relative_position=rp13)
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R2,
                room_arrival=R3,
                relative_position=rp12,
                relative_departure_coordinates=rc3)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R3,
                room_arrival=RE)
    
    solution = ' '.join(solution_list)
    for S in solution_list:
        solution = solution + ' ' + S.replace('S', 'D')
    solution = solution + ' ' + 'D15'

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15],
                 fastest_solution=solution,
                 level_color=Levels_colors_list.FROM_HUE(hu=0.875, sa=0.4, li=0.4),
                 name='Shortest path',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level