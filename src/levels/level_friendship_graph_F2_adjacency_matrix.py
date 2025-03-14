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
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    S9 = Switch(name='S9') 
    
    Sll = [[  0,  S0,  S1,  S3,  S6],
           [ S0,   0,  S2,  S4,  S7],
           [ S1,  S2,   0,  S5,  S8],
           [ S3,  S4,  S5,   0,  S9],
           [ S6,  S7,  S8,  S9,   0]
           ]
    
    n = 5
    
    tlE = ["AND"]
    SlE = []
    for j in range(n):
        for i in range(j):
            for k in range(n):
                SlE.extend([Sll[k][i], Sll[k][j]])
            tlE.append(["XOR"]+[Tree.tree_list_AND(2)]*n)
            
    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[1])
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[1])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[1])
    T3 = Tree(tree_list=tlE,
                name='T3',
                switches=SlE,
                cut_expression_depth_1=True)

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.7
    a = 0.05
    
    #    A B C D E
    #    
    # A  x 1 0 0 1
    # B  1 x 0 0 1
    # C  0 0 x 1 1
    # D  0 0 1 x 1
    # E  1 1 1 1 x

    R0 = Room(name='R0',
                position=[0*dx, 0*dy+3*a, ex, ey],
                switches_list=[S0])
    R1 = Room(name='R1',
                position=[1*dx, 0*dy+2*a, ex, 2*ey],
                switches_list=[S1, S2])
    R2 = Room(name='R2',
                position=[2*dx, 0*dy+a, ex, 3*ey],
                switches_list=[S3, S4, S5])
    R3 = Room(name='R3',
                position=[3*dx, 0*dy, ex, 4*ey],
                switches_list=[S6, S7, S8, S9])
    RE = Room(name='RE',
              position=[0*dx, 3*ey, ex, ey],
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
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 3.5/4])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, RE],
                 doors_list=[D0, D1, D2, D3],
                 fastest_solution="S0 D0 D1 S5 D2 S6 S7 S8 S9 D3",
                 level_color=get_color(),
                 name='Friendship graph F2 adjacency matrix',
                 keep_proportions=True,
                 door_window_size=420)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.9, sa=0.7, li=0.65)
    lcolor.surrounding_color = Color.color_hls(hu=0.9, sa=1, li=0.9)
    lcolor.contour_color = Color.color_hls(hu=0.9, sa=1, li=0.9)
    return lcolor