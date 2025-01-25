from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import randint as rd_randint
from numpy import array as np_array

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    
    A = np_array([[rd_randint(0, 7) for j in range(3)] for i in range(3)])
    X = np_array([rd_randint(0, 7) for j in range(3)]).T
    B = A @ X

    Slist = [S0, S1, S2,
             S3, S4, S5,
             S6, S7, S8]
    
    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_0)),
          name='V0',
          switches=Slist_0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_1)),
          name='V1',
          switches=Slist_1)
    V2 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_2)),
          name='V2',
          switches=Slist_2)
    Vlist = [V0, V1, V2]
    
    Slist_T0 = []
    for i in range(3):
        Slist_T0.append(int(B[i]))
        for j in range(3):
            Slist_T0.extend([int(A[i, j]), Vlist[j]])

    T0 = Tree(tree_list=["AND"] + [["EQU", [None], ["SUM"]+[Tree.tree_list_PROD(2)]*3]]*3,
                name='T0',
                switches=Slist_T0,
                cut_expression_depth_1=True)

    R0 = Room(name='R0',
                position=[0, 0, 3, 3],
                switches_list=Slist)
    RE = Room(name='RE',
              position=[3, 1, 1, 2],
              is_exit=True)

    e = 0.01

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[1-e, e],
                relative_arrival_coordinates=[1/2, e])
    
    sol_list = []
    for i in range(3):
        a = X[i]
        for j in range(3):
            if a%2:
                sol_list.append(f"S{3*i+j}")
            a = a//2
    sol_list.append('D0')

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution=' '.join(sol_list),
                 level_color=get_color(),
                 name='Matrix inversion',
                 keep_proportions=True,
                 door_window_size=350,
                 random=True)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.2, sa=0.4, li=0.6)
    lcolor.contour_color = Color.color_hls(hu=0.75, sa=0.8, li=0.4)
    lcolor.surrounding_color = Color.color_hls(hu=0.85, sa=0.8, li=0.4)
    return lcolor