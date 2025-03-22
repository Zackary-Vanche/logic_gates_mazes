from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle
from random import choice as rd_choice

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7]
    S8 = Switch(name='S8')
    
    T0 = Tree(tree_list=["AND",
                         [None],
                         ["INF", Tree.tree_list_SUM(8), [None]]],
                name='T0',
                switches=[S0]+Slist+[5])
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
    T7 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T7',
                switches=[S7, S8])

    dx = 1
    dy = 1
    ex = 0.6
    ey = 0.6
    ex0 = 1.3
    ey0 = 1.3

    R0 = Room(name='R0',
                position=[dx+ex-ex0, dy+ey-ey0, ex0, ey0],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[3*dx, 1*dy, ex, ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[1*dx, 3*dy, ex, ey],
                switches_list=[])
    R4 = Room(name='R4',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[])
    R5 = Room(name='R5',
                position=[4*dx, 2*dy, ex, ey],
                switches_list=[])
    R6 = Room(name='R6',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[])
    R7 = Room(name='R7',
                position=[2*dx, 4*dy, ex, ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[3*dx, 3*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1, 1],
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
                room_departure=R2,
                room_arrival=R4)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R5)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R6)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R3,
                room_arrival=R7)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R1,
                room_arrival=RE)
    
    R = rd_choice([R4, R5, R6, R7])
    R.switches_list = [S8]
    S8.room = R

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Again',
                 keep_proportions=True,
                 door_window_size=400,
                 random=True)
    
    return level

def get_color():
    hu = 0.8
    lcolor = Levels_colors_list.FROM_HUE(hu, sa=0.3, li=0.2)
    lcolor.surrounding_color = Color.color_hls(hu, sa=0.7, li=0.7)
    lcolor.contour_color = Color.color_hls(hu, sa=0.7, li=0.7)
    return lcolor