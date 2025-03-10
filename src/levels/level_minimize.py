from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import randint as rd_randint

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')

    Slist = [S0, S1, S2, S3, S4, S5, S6]
    
    #  A S0  B S2  C
    # S1    S3    S4
    #  D S5  C S6  D
    
    ll = [[0, 2, 4],
          [0, 3, 6],
          [1, 5, 6],
          [1, 5, 3, 2, 4]]
    
    lv = [rd_randint(0, 15) for i in range(len(Slist))]
    
    i_min = 0
    S_min = float('inf')
    sum_list = []
    for i in range(len(ll)):
        S = 0
        for j in ll[i]:
            S += lv[j]
        sum_list.append(S)
        if S < S_min:
            S_min = S
            i_min = i
    sum_list = list(set(sum_list)) # On retire les doublons
    sum_list.sort()
    if len(sum_list) == 1:
        sum_list.append(sum_list[0]+1)
    sol = ["S0 S2 S4 D0 D2 D4",
           "S0 S3 S6 D0 D3 D6",
           "S1 S5 S6 D1 D5 D6",
           "S1 S5 S3 S2 S4 D1 D5 D3 D2 D4"][i_min]
    
    V0 = Tree(tree_list=["INF", ["SUM"]+[Tree.tree_list_PROD(2)]*len(Slist), [None]],
              name='V0',
              switches=[lv[0], S0,
                        lv[1], S1,
                        lv[2], S2,
                        lv[3], S3,
                        lv[4], S4,
                        lv[5], S5,
                        lv[6], S6,]+[sum_list[1]])
    
    T0 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T0',
                switches=[S0, V0])
    T1 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T1',
                switches=[S1, V0])
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

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S0, S1, S2, S3, S4, S5, S6])
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[])
    R4 = Room(name='R4',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[2*dx, 1*dy, ex, ey],
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
                room_arrival=R3)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R2)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R4)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=RE)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R4)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R4,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution=sol,
                 level_color=get_color(),
                 name='Minimize',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.875, sa=0.2, li=0.7)
    lcolor.surrounding_color = Color.color_hls(hu=0.875, sa=1, li=0.7)
    lcolor.contour_color = Color.color_hls(hu=0.875, sa=1, li=0.7)
    return lcolor