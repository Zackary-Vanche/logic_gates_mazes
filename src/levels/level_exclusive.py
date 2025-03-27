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
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    Slist = [S0, S1, S2, S3]
    
    
    T0 = Tree(tree_list=[["XOR", "XNOR"][l[0]], Tree.tree_list_XOR(2), Tree.tree_list_XOR(2)],
                name='T0',
                switches=Slist)
    T1 = Tree(tree_list=[["XOR", "XNOR"][l[1]], [None], [None]],
                name='T1',
                switches=[S0, S1])
    T2 = Tree(tree_list=[["XOR", "XNOR"][l[2]], [None], [None]],
                name='T2',
                switches=[S1, S2])
    T3 = Tree(tree_list=[["XOR", "XNOR"][l[3]], [None], [None]],
                name='T3',
                switches=[S2, S3])
    # T2 = Tree(tree_list=[None],
    #             name='T2',
    #             switches=[1])
    # T3 = Tree(tree_list=[None],
    #             name='T3',
    #             switches=[1])
    
    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 1*dy-ey/2, ex, ey],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[0*dx, 1*dy+ey/2, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, RE],
                 doors_list=[D0, D1, D2, D3],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Exclusive',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def f():
    
    l = rd_choice([(0, 0, 0, 1),
                   (0, 0, 1, 1),
                   (0, 1, 0, 0),
                   (0, 1, 1, 0),
                   (1, 0, 0, 0),
                   (1, 0, 1, 0),
                   (1, 1, 0, 1),
                   (1, 1, 1, 1)])
    return aux(l)

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.975, sa=0.4)