from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import randint as rd_randint
from random import choice as rd_choice

def level_arithmetic(): 

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
    
    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8, S9]
    Slist_3 = [S10, S11, S12]
    Slist_4 = [S13, S14, S15, S16,]
    Slist_5 = [S17, S18,]
    Slist_6 = [S19, S20, S21, S22,]
    Slist_7 = [S23, S24,]

    a_plus_b = rd_randint(2, 7)
    a = rd_randint(1, a_plus_b)
    b = a_plus_b - a
    V0 = Tree(tree_list=['SUM', [None], [None]],
              name='V0',
              switches=[a, b],
              is_int=True)
    
    c = rd_randint(2, 7)
    d = rd_randint(2, 7)
    V1 = Tree(tree_list=['SUM', [None], ['MINUS', [None]]],
              name='V1',
              switches=[c+d, c],
              is_int=True)

    l2 = []
    for e in range(5):
        for f in range(5):
            if e*f < 16:
                l2.append([e, f])
    [e, f] = rd_choice(l2)
    V2 = Tree(tree_list=['PROD', [None], [None]],
              name='V2',
              switches=[e, f],
              is_int=True)

    g = rd_randint(2, 7)
    h = rd_randint(2, 7)
    V3 = Tree(tree_list=['DIV', [None], [None]],
              name='V3',
              switches=[g*h, h],
              is_int=True)

    l3 = []
    for i in range(5):
        for j in range(5):
            if i**j < 2**4:
                l3.append([i, j])
    [i, j] = rd_choice(l3)
    V4 = Tree(tree_list=['POW', [None], [None]],
              name='V4',
              switches=[i, j],
              is_int=True)

    k = rd_randint(2, 128)
    l = rd_randint(1, 4)
    V5 = Tree(tree_list=['MOD', [None], [None]],
              name='V5',
              switches=[k, l],
              is_int=True)

    m = rd_randint(0, 2)
    n = rd_randint(0, 3)
    o = rd_randint(0, 2)
    p = rd_randint(0, 3)
    V6 = Tree(tree_list=['POW', ['DIST', [None], [None], [None], [None]], [None]],
              name='V6',
              switches=[m, n, o, p, 2],
              is_int=True)

    q = rd_randint(-3, 3)
    V7 = Tree(tree_list=['ABS', [None]],
              name='V7',
              switches=[q],
              is_int=True)

    T0 = Tree(tree_list=['EQU', [None], Tree.tree_list_BIN(len(Slist_0))],
                name='T0',
                switches=[V0] + Slist_0)
    T1 = Tree(tree_list=['EQU', [None], Tree.tree_list_BIN(len(Slist_1))],
                name='T1',
                switches=[V1] + Slist_1)
    T2 = Tree(tree_list=['EQU', [None], Tree.tree_list_BIN(len(Slist_2))],
                name='T2',
                switches=[V2] + Slist_2)
    T3 = Tree(tree_list=['EQU', [None], Tree.tree_list_BIN(len(Slist_3))],
                name='T3',
                switches=[V3] + Slist_3)
    T4 = Tree(tree_list=['EQU', [None], Tree.tree_list_BIN(len(Slist_4))],
                name='T4',
                switches=[V4] + Slist_4)
    T5 = Tree(tree_list=['EQU', [None], Tree.tree_list_BIN(len(Slist_5))],
                name='T5',
                switches=[V5] + Slist_5)
    T6 = Tree(tree_list=['EQU', [None], Tree.tree_list_BIN(len(Slist_6))],
                name='T6',
                switches=[V6] + Slist_6)
    T7 = Tree(tree_list=['EQU', [None], Tree.tree_list_BIN(len(Slist_7))],
                name='T7',
                switches=[V7] + Slist_7)

    dx = 1
    dy = 1.25
    ex = 1
    ey = 0.5
    
    R0 = Room(name='R0',
                position=[0*dx, 0*dy, 3*ex, ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[4*dx, 0*dy, 3*ex, ey],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[4*dx, 1*dy, 3*ex, ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[0*dx, 1*dy, 3*ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[0*dx, 2*dy, 7*ex, ey],
                switches_list=Slist_4)
    R5 = Room(name='R5',
                position=[0*dx, 3*dy, 2*ex, ey],
                switches_list=Slist_5)
    R6 = Room(name='R6',
                position=[0*dx, 4*dy, 7*ex, ey],
                switches_list=Slist_6)
    R7 = Room(name='R7',
                position=[5*dx, 3*dy, 2*ex, ey],
                switches_list=Slist_7)
    RE = Room(name='RE',
              position=[3*dx, 3*dy, ex, ey],
              is_exit=True)
    
    assert V0.get_value() < 2**len(R0.switches_list), f'{V0.get_value()}, {2**len(R0.switches_list)}'
    assert V1.get_value() < 2**len(R1.switches_list), f'{V1.get_value()}, {2**len(R1.switches_list)}'
    assert V2.get_value() < 2**len(R2.switches_list), f'{V2.get_value()}, {2**len(R2.switches_list)}'
    assert V3.get_value() < 2**len(R3.switches_list), f'{V3.get_value()}, {2**len(R3.switches_list)}'
    assert V4.get_value() < 2**len(R4.switches_list), f'{V4.get_value()}, {2**len(R4.switches_list)}'
    assert V5.get_value() < 2**len(R5.switches_list), f'{V5.get_value()}, {2**len(R5.switches_list)}'
    assert V6.get_value() < 2**len(R6.switches_list), f'{V6.get_value()}, {2**len(R6.switches_list)}'
    assert V7.get_value() < 2**len(R7.switches_list), f'{V7.get_value()}, {2**len(R7.switches_list)}'

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 1/2])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3,
                relative_departure_coordinates=[0, 1/2],
                relative_arrival_coordinates=[1, 1/2])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R5)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R5,
                room_arrival=R6)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R6,
                room_arrival=R7)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R7,
                room_arrival=RE,
                relative_departure_coordinates=[0, 1/2],
                relative_arrival_coordinates=[1, 1/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0.6, sa=0.5, li=0.3),
                 name='Arithmetic',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level