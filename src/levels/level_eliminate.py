from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list

from random import shuffle as rd_shuffle

def f():

    l = []
    for i in range(2):
        for j in range(2):
            a = [None] if i else Tree.tree_list_NOT
            b = Tree.tree_list_NOT if i else [None]
            c = [None] if j else Tree.tree_list_NOT
            d = Tree.tree_list_NOT if j else [None]
            l.append([a, b, c, d])
    rd_shuffle(l)

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')

    T0 = Tree(tree_list=l[0][0],
                name='T0',
                switches=[S0])
    T1 = Tree(tree_list=l[0][1],
                name='T1',
                switches=[S0])
    T5 = Tree(tree_list=l[0][2],
                name='T5',
                switches=[S1])
    T6 = Tree(tree_list=l[0][3],
                name='T6',
                switches=[S1])
    
    T7 = Tree(tree_list=l[1][0],
                name='T7',
                switches=[S0])
    T8 = Tree(tree_list=l[1][1],
                name='T8',
                switches=[S0])
    T12 = Tree(tree_list=l[1][2],
                name='T12',
                switches=[S1])
    T13 = Tree(tree_list=l[1][3],
                name='T13',
                switches=[S1])
    
    T14 = Tree(tree_list=l[2][0],
                name='T14',
                switches=[S0])
    T15 = Tree(tree_list=l[2][1],
                name='T15',
                switches=[S0])
    T19 = Tree(tree_list=l[2][2],
                name='T19',
                switches=[S1])
    T20 = Tree(tree_list=l[2][3],
                name='T20',
                switches=[S1])
    
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[1])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[1])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[1])
    T9 = Tree(tree_list=[None],
                name='T9',
                switches=[1])
    T10 = Tree(tree_list=[None],
                name='T10',
                switches=[1])
    T11 = Tree(tree_list=[None],
                name='T11',
                switches=[1])
    T16 = Tree(tree_list=[None],
                name='T16',
                switches=[1])
    T17 = Tree(tree_list=[None],
                name='T17',
                switches=[1])
    T18 = Tree(tree_list=[None],
                name='T18',
                switches=[1])

    dx = 1
    dy = 1
    ex = 0.6
    ey = 0.6
    
    #R0 D0 R1 D2 R3 D5 R5
    #R0       D3       R5
    #R0 D1 R2 D4 R4 D6 R5
    
    #R5 D7 R6 D9  R8 D12 R10
    #R5       D10        R10
    #R5 D8 R7 D11 R9 D13 R10
    
    #R10 D14 R11 D16 R13 D19 RE
    #R10         D17         RE
    #R10 D15 R12 D18 R14 D20 RE
    
    ax = 0.4
    ay = 0.4

    R0 = Room(name='R0',
              position=[0*dx-ax, 0*dy, ex, dy+ey],
              switches_list=[S0, S1])
    R1 = Room(name='R1',
              position=[1*dx, 0*dy, ex, ey],
              switches_list=[])
    R2 = Room(name='R2',
              position=[1*dx, 1*dy, ex, ey],
              switches_list=[])
    R3 = Room(name='R3',
                position=[2*dx+ax, 0*dy, ex, ey],
                switches_list=[])
    R4 = Room(name='R4',
                position=[2*dx+ax, 1*dy, ex, ey],
                switches_list=[])
    
    R5 = Room(name='R5',
                position=[4*dx, 0*dy, ex, ey],
                switches_list=[])
    R6 = Room(name='R6',
                position=[4*dx, 2*dy-ay, ex, ey],
                switches_list=[])
    R7 = Room(name='R7',
                position=[3*dx, 2*dy-ay, ex, ey],
                switches_list=[])
    R8 = Room(name='R8',
                position=[4*dx, 3*dy+ay, ex, ey],
                switches_list=[])
    R9 = Room(name='R9',
                position=[3*dx, 3*dy+ay, ex, ey],
                switches_list=[])
    
    R10 = Room(name='R10',
                position=[4*dx, 5*dy, ex, ey],
                switches_list=[])
    R11 = Room(name='R11',
                position=[2*dx+ax, 5*dy, ex, ey],
                switches_list=[])
    R12 = Room(name='R12',
                position=[2*dx+ax, 4*dy, ex, ey],
                switches_list=[])
    R13 = Room(name='R13',
                position=[1*dx, 5*dy, ex, ey],
                switches_list=[])
    R14 = Room(name='R14',
                position=[1*dx, 4*dy, ex, ey],
                switches_list=[])
    
    RE = Room(name='RE',
              position=[0*dx-ax, 4*dy, ex, dy+ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R2)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R3)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R4)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R4)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R5)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R4,
                room_arrival=R5)
    
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R5,
                room_arrival=R6)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R5,
                room_arrival=R7)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R6,
                room_arrival=R8)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R6,
                room_arrival=R9)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R7,
                room_arrival=R9)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R8,
                room_arrival=R10)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R9,
                room_arrival=R10)
    
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R10,
                room_arrival=R11)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R10,
                room_arrival=R12)
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R11,
                room_arrival=R13)
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R11,
                room_arrival=R14)
    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=R12,
                room_arrival=R14)
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R13,
                room_arrival=RE)
    D20 = Door(two_way=False,
                tree=T20,
                name='D20',
                room_departure=R14,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Eliminate',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    sol_list = level.find_all_solutions()[0]
    assert len(sol_list) == 1
    level.fastest_solution = ' '.join(sol_list[0])
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.05, sa=0.2, li=0.5)
    lcolor.contour_color = Color.color_hls(hu=0.95, sa=1, li=0.7)
    lcolor.surrounding_color = Color.color_hls(hu=0.9, sa=1, li=0.7)
    return lcolor