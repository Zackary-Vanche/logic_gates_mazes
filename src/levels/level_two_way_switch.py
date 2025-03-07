from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice

def aux(l): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    
    Slist = [S0, S1]
    
    T0 = Tree(tree_list=Tree.tree_list_from_str(l[0]),
                name='T0',
                switches=[S0])
    T1 = Tree(tree_list=Tree.tree_list_from_str('T' if l[0]=='F' else 'F'),
                name='T1',
                switches=[S0])
    T2 = Tree(tree_list=Tree.tree_list_from_str(l[1]),
                name='T2',
                switches=[S1])
    T3 = Tree(tree_list=Tree.tree_list_from_str('T' if l[1]=='F' else 'F'),
                name='T3',
                switches=[S1])
    
    T4 = Tree(tree_list=Tree.tree_list_from_str(l[2]),
                name='T4',
                switches=[S0])
    T5 = Tree(tree_list=Tree.tree_list_from_str('T' if l[2]=='F' else 'F'),
                name='T5',
                switches=[S0])
    
    T6 = Tree(tree_list=[None],
                name='T6',
                switches=[1])
    T7 = Tree(tree_list=[None],
                name='T7',
                switches=[1])
    T8 = Tree(tree_list=[None],
                name='T8',
                switches=[1])
    
    T9 = Tree(tree_list=Tree.tree_list_from_str(l[3]),
                name='T9',
                switches=[S1])
    T10 = Tree(tree_list=Tree.tree_list_from_str('T' if l[3]=='F' else 'F'),
                name='T10',
                switches=[S1])

    dx = 1.25
    dy = 1.5
    ex = 0.5
    ey = 1.75

    R0 = Room(name='R0',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[])
    R4 = Room(name='R4',
                position=[3*dx, 0*dy, ex, ey],
                switches_list=[])
    R5 = Room(name='R5',
                position=[3*dx, 2*dy, ex, ey],
                switches_list=[])
    R6 = Room(name='R6',
                position=[4*dx, 0*dy, ex, ey],
                switches_list=[])
    R7 = Room(name='R7',
                position=[4*dx, 2*dy, ex, ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[5*dx, 1*dy, ex, ey],
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
                room_departure=R2,
                room_arrival=R3)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R3,
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
                room_arrival=R6)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R4,
                room_arrival=R7)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R5,
                room_arrival=R7)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R6,
                room_arrival=RE)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R7,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Two-way switch',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def f():
    from itertools import product
    chaine = ['F', 'T']
    r = rd_choice([''.join(p) for p in product(chaine, repeat=4)])
    return aux(r)

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.25, sa=0.2, li=0.5)
    lcolor.contour_color = Color.color_hls(hu=0.15, sa=1, li=0.7)
    lcolor.surrounding_color = Color.color_hls(hu=0.1, sa=1, li=0.7)
    return lcolor