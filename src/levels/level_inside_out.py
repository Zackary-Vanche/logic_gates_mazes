from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from random import randint as rd_randint

def level_inside_out():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    
    Slist = [S0, S1, S2, S3, S4]
    
    Sa = rd_choice(Slist)
    a = rd_randint(0, 31)
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(5),
              name='V0',
              switches=Slist)
    
    m = 5
    n = 3
    
    lt0 = []
    for i in range(m):
        lt0.append([])
        lt0[-1].append(V0)
        for j in range(n):
            lt0[-1].append(rd_randint(0, 31))
        lt0[-1].append(a)
        lt0[-1][1:] = sorted(lt0[-1][1:])
    lt0 = [S for l in lt0 for S in l]
    
    tree_list_IN = ['IN'] + [[None]]*(n+2)
    tree_list_0 = ['AND'] + [tree_list_IN]*m

    T0 = Tree(tree_list=tree_list_0,
              name='T0',
              switches=lt0,
              cut_expression_depth_1=True)

    dx = 1
    dy = 1
    ex = 1
    ey = 1

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, 5*ey],
                switches_list=Slist)
    RE = Room(name='RE',
              position=[2*dx, 2*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0.6, sa=0.1, li=0.7),
                 name='Inside out',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level