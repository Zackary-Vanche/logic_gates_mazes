from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color
from random import shuffle as rd_shuffle
from Graph import Graph

def level_small_honeycomb(): 

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
    
    l_weights = [i+1 for i in range(127)]
    rd_shuffle(l_weights)
    l_weights = l_weights[:24]
    
    edges = [('R1', 'R2', l_weights[0]),
             ('R1', 'R3', l_weights[1]),
             ('R1', 'R4', l_weights[2]),
             ('R2', 'R4', l_weights[3]),
             ('R2', 'R5', l_weights[4]),
             ('R3', 'R4', l_weights[5]),
             ('R4', 'R5', l_weights[6]),
             ('R3', 'R6', l_weights[7]),
             ('R6', 'R4', l_weights[8]),
             ('R4', 'R7', l_weights[9]),
             ('R7', 'R5', l_weights[10]),
             ('R6', 'R7', l_weights[11])]
    
    g = Graph()
    g.add_edge_list(edges)
    dico = g.kruskals_mst()
    a = dico['total_weight']
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11]
    
    tree_list_0 = ['INFOREQU',
                   ['SUM'] + [['PROD', [None], [None]]]*len(Slist),
                   [None]]
    
    Slist_0 = []
    
    S_weight_list = []
    
    for i in range(len(Slist)):
        S_weight_list.append([Slist[i], l_weights[i]])
    S_weight_list.sort(key = lambda x : x[1])
    for i in range(len(S_weight_list)):
        S, weight = S_weight_list[i]
        Slist_0.append(weight)
        Slist_0.append(S)
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
    T13 = Tree(tree_list=Tree.tree_list_AND(7),
                name='T13',
                switches=[S12, S13, S14, S15, S16, S17, S18])

    dx = 0.5
    dy = (3)**0.5 / 2
    ex = 0.4
    ey = 0.4
    
    nx = 3
    ny = 3

    R0 = Room(name='R0',
                position=[1*dx-nx*ex, 1*dy-ny*ey, nx*ex, ny*ey],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11])

    R1 = Room(name='R1',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[S12])
    R2 = Room(name='R2',
                position=[4*dx, 0*dy, ex, ey],
                switches_list=[S13])
    R3 = Room(name='R3',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S14])
    R4 = Room(name='R4',
                position=[3*dx, 1*dy, ex, ey],
                switches_list=[S15])
    R5 = Room(name='R5',
                position=[5*dx, 1*dy, ex, ey],
                switches_list=[S16])
    R6 = Room(name='R6',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S17])
    R7 = Room(name='R7',
                position=[4*dx, 2*dy, ex, ey],
                switches_list=[S18])
    RE = Room(name='RE',
              position=[1*dx-nx*ex, 2*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[0, 0])
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
                room_departure=R4,
                room_arrival=R5)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R3,
                room_arrival=R6)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R6,
                room_arrival=R4)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R4,
                room_arrival=R7)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R7,
                room_arrival=R5)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R6,
                room_arrival=R7)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R6,
                room_arrival=RE)
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0.16, sa=0.5, li=0.5)
    lcolor.background_color = Color.ORANGE
    lcolor.surrounding_color = Color.BLACK

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13],
                 fastest_solution=None,
                 level_color=lcolor,
                 name='Small honeycomb',
                 keep_proportions=True,
                 door_window_size=325,
                 random=True)
    
    return level