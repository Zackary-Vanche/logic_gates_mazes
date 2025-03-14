from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2') 
    
    Sll = [[ 0, S0, S1],
           [S0,  0, S2],
           [S1, S2,  0]]
    
    n = 3
    
    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[1])
    
    tlE = ["AND"]
    SlE = []
    for j in range(n):
        for i in range(j):
            for k in range(n):
                SlE.extend([Sll[k][i], Sll[k][j]])
            tlE.append(["XOR"]+[Tree.tree_list_AND(2)]*n)
            
    T1 = Tree(tree_list=tlE,
                name='T1',
                switches=SlE,
                cut_expression_depth_1=True)

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5
    a = 0.1

    R0 = Room(name='R0',
                position=[0*dx, 0*dy+a, ex, ey],
                switches_list=[S0])
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, 2*ey],
                switches_list=[S1, S2])
    RE = Room(name='RE',
              position=[0*dx, 1*dy, ex, ey],
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
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, RE],
                 doors_list=[D0, D1],
                 fastest_solution="S0 D0 S1 S2 D1",
                 level_color=get_color(),
                 name='Friendship graph F1 adjacency matrix',
                 keep_proportions=True,
                 door_window_size=340)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.9, sa=0.7, li=0.65)
    lcolor.surrounding_color = Color.color_hls(hu=0.9, sa=1, li=0.9)
    lcolor.contour_color = Color.color_hls(hu=0.9, sa=1, li=0.9)
    return lcolor