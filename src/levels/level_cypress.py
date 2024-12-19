from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from numpy import cos, sin, pi
from random import shuffle as rd_shuffle
from Graph import Graph
from Color import Color

def f():
    
    l_weights = [i+1 for i in range(127)]
    rd_shuffle(l_weights)
    l_weights = l_weights[:24]
    
    edges = [['R2', 'R1', l_weights[1]],
             ['R4', 'R1', l_weights[2]],
             ['R5', 'R1', l_weights[3]],
             ['R6', 'R1', l_weights[4]],
             ['R7', 'R1', l_weights[5]],
             ['R3', 'R2', l_weights[6]],
             ['R4', 'R2', l_weights[7]],
             ['R7', 'R2', l_weights[8]],
             ['R8', 'R2', l_weights[9]],
             ['R4', 'R3', l_weights[10]],
             ['R5', 'R4', l_weights[11]],
             ['R6', 'R5', l_weights[12]],
             ['R7', 'R6', l_weights[13]],
             ['R8', 'R7', l_weights[14]],
             ['R3', 'R8', l_weights[15]]]
    
    g = Graph()
    g.add_edge_list(edges)
    dico = g.kruskals_mst()
    
    open_list = []
    for i in range(len(edges)):
        open_list.append(int(edges[i] in dico['mst']))
            
    x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, = open_list
    partial_sol = []
    for i in range(len(open_list)):
        if open_list[i]:
            partial_sol.append('S'+str(i))
    partial_sol = ' '.join(partial_sol)

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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14]

    T0 = Tree(tree_list=['AND',
                         ['EQU', Tree.tree_list_SUM(15), [None]],
                         ['EQU', Tree.tree_list_SUM(5), [None]],
                         ['EQU', Tree.tree_list_SUM(5), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(4), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(4), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]]],
                name='T0',
                switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, 7,
                          S0, S1, S2, S3, S4, x0+x1+x2+x3+x4,
                          S0, S5, S6, S7, S8, x0+x5+x6+x7+x8,
                          S5, S9, S14, x5+x9+x14,
                          S1, S6, S9, S10, x1+x6+x9+x10,
                          S2, S10, S11, x2+x10+x11,
                          S3, S11, S12, x3+x11+x12,
                          S4, S7, S12, S13, x4+x7+x12+x13,
                          S8, S13, S14, x8+x13+x14,],
                cut_expression_depth_1=True)
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
    T16 = Tree(tree_list=Tree.tree_list_AND(8),
                name='T16',
                switches=[S15, S16, S17, S18,
                          S19, S20, S21, S22])

    dx = 1
    dy = 0.75
    ex = 0.6
    ey = 0.25
    
    alpha = 0.4*pi
    ax = 2*abs(cos(alpha))
    ay = 2*abs(sin(alpha))
    
    a = 2

    R0 = Room(name='R0',
                position=[0*dx-a, 3*dy, ex+2*a, ey],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S15])
    R2 = Room(name='R2',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S16])
    R3 = Room(name='R3',
                position=[ax*dx, 1*dy-ay*dy, ex, ey],
                switches_list=[S17])
    R4 = Room(name='R4',
                position=[1*dx, 0.5*dy, ex, ey],
                switches_list=[S18])
    R5 = Room(name='R5',
                position=[ax*dx, ay*dy, ex, ey],
                switches_list=[S19])
    R6 = Room(name='R6',
                position=[-ax*dx, ay*dy, ex, ey],
                switches_list=[S20])
    R7 = Room(name='R7',
                position=[-1*dx, 0.5*dy, ex, ey],
                switches_list=[S21])
    R8 = Room(name='R8',
                position=[-ax*dx, 1*dy-ay*dy, ex, ey],
                switches_list=[S22])
    RE = Room(name='RE',
              position=[0*dx, -1.5*dy-ey, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R5)
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R4)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R5)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R1,
                room_arrival=R6)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R1,
                room_arrival=R7)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R2,
                room_arrival=R3)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R2,
                room_arrival=R4)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R2,
                room_arrival=R7)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R2,
                room_arrival=R8)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R3,
                room_arrival=R4)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R4,
                room_arrival=R5)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R5,
                room_arrival=R6)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R6,
                room_arrival=R7)
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R7,
                room_arrival=R8)
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R8,
                room_arrival=R3)
    D16 = Door(two_way=True,
                tree=T16,
                name='D16',
                room_departure=R8,
                room_arrival=RE)
    
    Rlist = [R0, R1, R2, R3, R4, R5, R6, R7, R8]
    Dlist = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16]
    
    # for l in [Rlist,
    #           [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22],
    #           Dlist]:
    #     names = [x.name for x in l]
    #     rd_shuffle(names)
    #     for i in range(len(l)):
    #         l[i].name = names[i]
            
    R0.switches_list.sort(key=lambda x: [len(x.name), x.name])
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0.5, sa=0.2, li=0.3)
    lcolor.contour_color = Color.GREY
    lcolor.surrounding_color = Color.GREY

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=Rlist + [RE],
                 doors_list=Dlist,
                 partial_solution=partial_sol,
                 level_color=lcolor,
                 name='Cypress',
                 keep_proportions=True,
                 door_window_size=350,
                 random=True)
    
    return level