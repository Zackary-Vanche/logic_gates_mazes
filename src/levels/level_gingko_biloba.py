from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import random as rd_random
from random import uniform as rd_uniform
from Color import Color
from random import shuffle as rd_shuffle
from Graph import Graph

def level_gingko_biloba(fast_solution_finding=False):
    
    l_weights = [i+1 for i in range(127)]
    rd_shuffle(l_weights)
    l_weights = l_weights[:24]
    
    edges = [['R1', 'R2', l_weights[1]],
             ['R2', 'R3', l_weights[2]],
             ['R3', 'R4', l_weights[3]],
             ['R5', 'R6', l_weights[4]],
             ['R6', 'R7', l_weights[5]],
             ['R7', 'R8', l_weights[6]],
             ['R9', 'R10', l_weights[7]],
             ['R10', 'R11', l_weights[8]],
             ['R11', 'R12', l_weights[9]],
             ['R1', 'R5', l_weights[10]],
             ['R5', 'R9', l_weights[11]],
             ['R2', 'R6', l_weights[12]],
             ['R6', 'R10', l_weights[13]],
             ['R3', 'R7', l_weights[14]],
             ['R7', 'R11', l_weights[15]],
             ['R4', 'R8', l_weights[16]],
             ['R8', 'R12', l_weights[17]]]
    
    g = Graph()
    g.add_edge_list(edges)
    dico = g.kruskals_mst()
    
    open_list = []
    for i in range(len(edges)):
        open_list.append(int(edges[i] in dico['mst']))
            
    x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16 = open_list

    # for l in [[0, 3, 9, 11],
    #           [1, 4, 11, 13],
    #           [2, 5, 13, 15],
    #           [3, 6, 10, 12],
    #           [4, 7, 12, 14],
    #           [5, 8, 14, 16],]:
    #     [a, b, c, d] = l
    #     print(f'S{a}, S{b}, S{c}, S{d}, x{a} + x{b} + x{c} + x{d}')

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
    
    tree_list_aux_0 = ['EQU', Tree.tree_list_SUM(4), [None]]

    T0 = Tree(tree_list=['AND',
                         ['EQU', Tree.tree_list_SUM(17), [None]]] + [tree_list_aux_0]*6,
              name='T0',
              switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, 11,
                        S0, S3, S9, S11, x0 + x3 + x9 + x11,
                        S1, S4, S11, S13, x1 + x4 + x11 + x13,
                        S2, S5, S13, S15, x2 + x5 + x13 + x15,
                        S3, S6, S10, S12, x3 + x6 + x10 + x12,
                        S4, S7, S12, S14, x4 + x7 + x12 + x14,
                        S5, S8, S14, S16, x5 + x8 + x14 + x16,],
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
    T16 = Tree(tree_list=[None],
               name='T16',
               switches=[S15])
    T17 = Tree(tree_list=[None],
               name='T17',
               switches=[S16])
    T18 = Tree(tree_list=Tree.tree_list_AND(12),
               name='T18',
               switches=[S17, S18, S19, S20,
                         S21, S22, S23, S24,
                         S25, S26, S27, S28])

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5
    ax = 0.25
    bx = 0.075
    cx = 0.2
    
    ex0 = 3*dx+ex+2*ax
    ey0 = ex0/18
    
    a = 0.75

    R0 = Room(name='R0',
                position=[0*dx-ax, 3*dy, ex0, ey0],
                switches_list=[S0, S1, S2, S3, S4, S5,
                               S6, S7, S8, S9, S10, S11,
                               S12, S13, S14, S15, S16])
    R1 = Room(name='R1',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S17])
    R2 = Room(name='R2',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S18])
    R3 = Room(name='R3',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S19])
    R4 = Room(name='R4',
                position=[3*dx, 2*dy, ex, ey],
                switches_list=[S20])
    R5 = Room(name='R5',
                position=[0*dx-bx, 1*dy, ex, ey],
                switches_list=[S21])
    R6 = Room(name='R6',
                position=[1*dx-bx, 1*dy, ex, ey],
                switches_list=[S22])
    R7 = Room(name='R7',
                position=[2*dx+bx, 1*dy, ex, ey],
                switches_list=[S23])
    R8 = Room(name='R8',
                position=[3*dx+bx, 1*dy, ex, ey],
                switches_list=[S24])
    R9 = Room(name='R9',
                position=[0*dx-cx, 0*dy, ex, ey],
                switches_list=[S25])
    R10 = Room(name='R10',
                position=[1*dx-cx, 0*dy, ex, ey],
                switches_list=[S26])
    R11 = Room(name='R11',
                position=[2*dx+cx, 0*dy, ex, ey],
                switches_list=[S27])
    R12 = Room(name='R12',
                position=[3*dx+cx, 0*dy, ex, ey],
                switches_list=[S28])
    RE = Room(name='RE',
              position=[0*dx-ax-ex-0.1, 3*dy, ex, ey0],
              is_exit=True)
    if fast_solution_finding:
        for room in [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12]:
            room.possible_switches_values = [[1]]

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R2,
                relative_position=0.45)
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R5,
                room_arrival=R6)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R6,
                room_arrival=R7)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R7,
                room_arrival=R8)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R9,
                room_arrival=R10)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R10,
                room_arrival=R11)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R11,
                room_arrival=R12)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R1,
                room_arrival=R5)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R5,
                room_arrival=R9)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R2,
                room_arrival=R6)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R6,
                room_arrival=R10)
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R3,
                room_arrival=R7)
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R7,
                room_arrival=R11)
    D16 = Door(two_way=True,
                tree=T16,
                name='D16',
                room_departure=R4,
                room_arrival=R8)
    D17 = Door(two_way=True,
                tree=T17,
                name='D17',
                room_departure=R8,
                room_arrival=R12)
    D18 = Door(two_way=True,
                tree=T18,
                name='D18',
                room_departure=R1,
                room_arrival=RE)
    
    lcolor = Levels_colors_list.FROM_HUE(hu=rd_uniform(0.16, 0.4), sa=0.4, li=0.55)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18],
                 fastest_solution=None,
                 level_color=lcolor,
                 name='Gingko biloba',
                 keep_proportions=True,
                 door_window_size=280,
                 random=True)
    
    return level