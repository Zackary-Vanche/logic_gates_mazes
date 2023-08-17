from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color
from random import shuffle as rd_shuffle

def find(parents, node):
    if parents[node] == -1:
        return node
    parents[node] = find(parents, parents[node])
    return parents[node]

def union(parents, ranks, node1, node2):
    root1 = find(parents, node1)
    root2 = find(parents, node2)
    
    if root1 != root2:
        if ranks[root1] > ranks[root2]:
            root1, root2 = root2, root1
        parents[root1] = root2
        if ranks[root1] == ranks[root2]:
            ranks[root2] += 1

def kruskal(edges):
    node_indices = {}  # Dictionnaire pour mapper les noms de nœuds à des indices numériques
    num_nodes = 0
    parents = []
    ranks = []
    total_weight = 0

    for node1, node2, weight in edges:
        if node1 not in node_indices:
            node_indices[node1] = num_nodes
            num_nodes += 1
            parents.append(-1)
            ranks.append(0)
        if node2 not in node_indices:
            node_indices[node2] = num_nodes
            num_nodes += 1
            parents.append(-1)
            ranks.append(0)

    edges_with_indices = [(node_indices[node1], node_indices[node2], weight) for node1, node2, weight in edges]
    edges_with_indices.sort()

    for node1, node2, weight in edges_with_indices:
        if find(parents, node1) != find(parents, node2):
            union(parents, ranks, node1, node2)
            total_weight += weight

    return total_weight

def level_honeycomb(): 

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
    S30 = Switch(name='S30')
    S31 = Switch(name='S31')
    S32 = Switch(name='S32')
    S33 = Switch(name='S33')
    S34 = Switch(name='S34')
    S35 = Switch(name='S35')
    
    l_weights = [i+1 for i in range(127)]
    rd_shuffle(l_weights)
    l_weights = l_weights[:24]
    
    edges = [('R1', 'R2', l_weights[0]),
             ('R1', 'R3', l_weights[1]),
             ('R1', 'R4', l_weights[2]),
             ('R2', 'R4', l_weights[3]),
             ('R2', 'R5', l_weights[4]),
             ('R3', 'R4', l_weights[5]),
             ('R3', 'R6', l_weights[6]),
             ('R3', 'R7', l_weights[7]),
             ('R4', 'R5', l_weights[8]),
             ('R4', 'R7', l_weights[9]),
             ('R4', 'R8', l_weights[10]),
             ('R5', 'R8', l_weights[11]),
             ('R5', 'R9', l_weights[12]),
             ('R6', 'R7', l_weights[13]),
             ('R6', 'R10', l_weights[14]),
             ('R7', 'R8', l_weights[15]),
             ('R7', 'R10', l_weights[16]),
             ('R7', 'R11', l_weights[17]),
             ('R8', 'R9', l_weights[18]),
             ('R8', 'R11', l_weights[19]),
             ('R8', 'R12', l_weights[20]),
             ('R9', 'R12', l_weights[21]),
             ('R10', 'R11', l_weights[22]),
             ('R11', 'R12', l_weights[23])]
    
    a = kruskal(edges)
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23]
    
    tree_list_0 = ['INF',
                   ['SUM'] + [['PROD', [None], [None]]]*24,
                   [None]]
    
    Slist_0 = []
    
    for i in range(24):
        Slist_0.append(l_weights[i])
        Slist_0.append(Slist[i])
    Slist_0.append(a)
    
    T0 = Tree(tree_list=tree_list_0,
                name='T0',
                switches=Slist_0)
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[S0])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[S1])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[S2])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[S3])
    T5 = Tree(tree_list=[None],
                name='T5',
                switches=[S4])
    T6 = Tree(tree_list=[None],
                name='T6',
                switches=[S5])
    T7 = Tree(tree_list=[None],
                name='T7',
                switches=[S6])
    T8 = Tree(tree_list=[None],
                name='T8',
                switches=[S7])
    T9 = Tree(tree_list=[None],
                name='T9',
                switches=[S8])
    T10 = Tree(tree_list=[None],
                name='T10',
                switches=[S9])
    T11 = Tree(tree_list=[None],
                name='T11',
                switches=[S10])
    T12 = Tree(tree_list=[None],
                name='T12',
                switches=[S11])
    T13 = Tree(tree_list=[None],
                name='T13',
                switches=[S12])
    T14 = Tree(tree_list=[None],
                name='T14',
                switches=[S13])
    T15 = Tree(tree_list=[None],
                name='T15',
                switches=[S14])
    T16 = Tree(tree_list=[None],
                name='T16',
                switches=[S15])
    T17 = Tree(tree_list=[None],
                name='T17',
                switches=[S16])
    T18 = Tree(tree_list=[None],
                name='T18',
                switches=[S17])
    T19 = Tree(tree_list=[None],
                name='T19',
                switches=[S18])
    T20 = Tree(tree_list=[None],
                name='T20',
                switches=[S19])
    T21 = Tree(tree_list=[None],
                name='T21',
                switches=[S20])
    T22 = Tree(tree_list=[None],
                name='T22',
                switches=[S21])
    T23 = Tree(tree_list=[None],
                name='T23',
                switches=[S22])
    T24 = Tree(tree_list=[None],
                name='T24',
                switches=[S23])
    T25 = Tree(tree_list=Tree.tree_list_AND(12),
                name='T25',
                switches=[S24, S25, S26,
                          S27, S28, S29,
                          S30, S31, S32,
                          S33, S34, S35])

    dx = 0.5
    dy = (3)**0.5 / 2
    ex = 0.4
    ey = 0.4
    
    n = 3.5

    R0 = Room(name='R0',
                position=[1*dx-n*ex, 1*dy-n*ey, n*ex, n*ey],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23])

    R1 = Room(name='R1',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[S24])
    R2 = Room(name='R2',
                position=[4*dx, 0*dy, ex, ey],
                switches_list=[S25])
    R3 = Room(name='R3',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S26])
    R4 = Room(name='R4',
                position=[3*dx, 1*dy, ex, ey],
                switches_list=[S27])
    R5 = Room(name='R5',
                position=[5*dx, 1*dy, ex, ey],
                switches_list=[S28])
    R6 = Room(name='R6',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S29])
    R7 = Room(name='R7',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S30])
    R8 = Room(name='R8',
                position=[4*dx, 2*dy, ex, ey],
                switches_list=[S31])
    R9 = Room(name='R9',
                position=[6*dx, 2*dy, ex, ey],
                switches_list=[S32])
    R10 = Room(name='R10',
                position=[1*dx, 3*dy, ex, ey],
                switches_list=[S33])
    R11 = Room(name='R11',
                position=[3*dx, 3*dy, ex, ey],
                switches_list=[S34])
    R12 = Room(name='R12',
                position=[5*dx, 3*dy, ex, ey],
                switches_list=[S35])
    RE = Room(name='RE',
              position=[1*dx-n*ex, 3*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R6,
                relative_departure_coordinates=[1/2, 3/4])
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R3)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R4)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R4)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R2,
                room_arrival=R5)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R3,
                room_arrival=R4)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R3,
                room_arrival=R6)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R3,
                room_arrival=R7)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R4,
                room_arrival=R5)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R4,
                room_arrival=R7)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R4,
                room_arrival=R8)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R5,
                room_arrival=R8)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R5,
                room_arrival=R9)
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R6,
                room_arrival=R7)
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R6,
                room_arrival=R10)
    D16 = Door(two_way=True,
                tree=T16,
                name='D16',
                room_departure=R7,
                room_arrival=R8)
    D17 = Door(two_way=True,
                tree=T17,
                name='D17',
                room_departure=R7,
                room_arrival=R10)
    D18 = Door(two_way=True,
                tree=T18,
                name='D18',
                room_departure=R7,
                room_arrival=R11)
    D19 = Door(two_way=True,
                tree=T19,
                name='D19',
                room_departure=R8,
                room_arrival=R9)
    D20 = Door(two_way=True,
                tree=T20,
                name='D20',
                room_departure=R8,
                room_arrival=R11)
    D21 = Door(two_way=True,
                tree=T21,
                name='D21',
                room_departure=R8,
                room_arrival=R12)
    D22 = Door(two_way=True,
                tree=T22,
                name='D22',
                room_departure=R9,
                room_arrival=R12)
    D23 = Door(two_way=True,
                tree=T23,
                name='D23',
                room_departure=R10,
                room_arrival=R11)
    D24 = Door(two_way=True,
                tree=T24,
                name='D24',
                room_departure=R11,
                room_arrival=R12)
    D25 = Door(two_way=True,
                tree=T25,
                name='D25',
                room_departure=R10,
                room_arrival=RE)
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0.16, sa=0.5, li=0.5)
    lcolor.background_color = Color.ORANGE
    lcolor.surrounding_color = Color.BLACK

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25],
                 fastest_solution=None,
                 level_color=lcolor,
                 name='Honeycomb',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level