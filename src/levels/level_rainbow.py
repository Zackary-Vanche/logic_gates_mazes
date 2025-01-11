from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import random as rd_random

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
    
    l = [[0, 1],
         [0, 2],
         [0, 4],
         [1, 3],
         [1, 5],
         [2, 3],
         [2, 6],
         [3, 7],
         [4, 5],
         [4, 6],
         [5, 7],
         [6, 7]]

    Vlist = [Tree(tree_list=Tree.tree_list_DIFF(2),
                  name=f'V{i}',
                  switches=[Slist[l[i][0]], Slist[l[i][1]]]) for i in range(len(l))]
    
    Tl = [Tree(tree_list=[None],
               name=f'T{i+1}',
               switches=[Vlist[i]]) for i in range(len(l))]
    
    Tl = [Tree(tree_list=Tree.tree_list_AND(len(l)),
               name='T0',
               switches=Vlist)] + Tl + [Tree(tree_list=[None],
                                             name='T13',
                                             switches=[1])]

    dx = 1
    dy = 1
    ex = 0.4
    ey = 0.4
    
    #    0       1
    #      4   5
    #
    #      6   7
    #    2       3
    #
    
    ax = 0.7
    ay = 0.7

    R0 = Room(name='R0',
                position=[-0.6, 0*dy, 0.3, 2*dy+ay+ey],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[])
    R4 = Room(name='R4',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[])
    R5 = Room(name='R5',
                position=[0*dx+ax, 0*dy+ay, ex, ey],
                switches_list=[])
    R6 = Room(name='R6',
                position=[0*dx+ax, 2*dy+ay, ex, ey],
                switches_list=[])
    R7 = Room(name='R7',
                position=[2*dx+ax, 0*dy+ay, ex, ey],
                switches_list=[])
    R8 = Room(name='R8',
                position=[2*dx+ax, 2*dy+ay, ex, ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[0*dx+2*ax, 0*dy+2*ay, ex, ey],
              is_exit=True)
    
    Rl = [R0, R1, R2, R3, R4, R5, R6, R7, R8, RE]

    Dl = [Door(two_way=True,
                tree=Tl[i+1],
                name=f'D{i+1}',
                room_departure=Rl[l[i][0]+1],
                room_arrival=Rl[l[i][1]+1]) for i in range(len(l))]
    
    Dl = [Door(two_way=False,
                tree=Tl[0],
                name='D0',
                room_departure=Rl[0],
                room_arrival=Rl[1])] + Dl + [Door(two_way=False,
                                                    tree=Tl[13],
                                                    name='D13',
                                                    room_departure=Rl[5],
                                                    room_arrival=Rl[-1])]
                                                  
    for R in Rl:
        R.inside_color = Color.color_hls(hu=rd_random(), li=0.5, sa=0.3)
        R.surrounding_color = Color.color_hls(hu=rd_random(), li=0.8, sa=0.8)
        
    for D in Dl:
        D.inside_color = Color.color_hls(hu=rd_random(), li=0.5, sa=0.3)
        D.surrounding_color = Color.color_hls(hu=rd_random(), li=0.8, sa=0.8)
        
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=Rl,
                 doors_list=Dl,
                 fastest_solution="S0 S3 S5 S6 D0 D3 D13",
                 level_color=get_color(),
                 name='Rainbow',
                 keep_proportions=True,
                 door_window_size=300,
                 uniform_surrounding_colors=False,
                 uniform_inside_room_color=False)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.6, sa=0.4, li=0.5)