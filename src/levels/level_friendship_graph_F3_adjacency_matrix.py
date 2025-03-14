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
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')
    S15 = Switch(name='S15')
    S16 = Switch(name='S16')
    S17 = Switch(name='S17')
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')
    S20 = Switch(name='S20')
    
    Sll = [[  0,  S0,  S1,  S3,  S6, S10, S15],
           [ S0,   0,  S2,  S4,  S7, S11, S16],
           [ S1,  S2,   0,  S5,  S8, S12, S17],
           [ S3,  S4,  S5,   0,  S9, S13, S18],
           [ S6,  S7,  S8,  S9,   0, S14, S19],
           [S10, S11, S12, S13, S14,   0, S20],
           [S15, S16, S17, S18, S19, S20,   0],
           ]
    
    n = 7
    
    Vl = []
    for j in range(n):
        for i in range(j):
            SlV = []
            for k in range(n):
                SlV.extend([Sll[k][i], Sll[k][j]])
            Vl.append(Tree(tree_list=["XOR"]+[Tree.tree_list_AND(2)]*n,
                           name=f'V{len(Vl)}',
                           switches=SlV,
                           cut_expression_depth_1=True))
            
    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[1])
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[1])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[1])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[1])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[1])
    T5 = Tree(tree_list=Tree.tree_list_AND(len(Vl)),
                name='T5',
                switches=Vl)

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.7
    a = 0.05

    R0 = Room(name='R0',
                position=[0*dx, 0*dy+5*a, ex, ey],
                switches_list=[S0])
    R1 = Room(name='R1',
                position=[1*dx, 0*dy+4*a, ex, 2*ey],
                switches_list=[S1, S2])
    R2 = Room(name='R2',
                position=[2*dx, 0*dy+3*a, ex, 3*ey],
                switches_list=[S3, S4, S5])
    R3 = Room(name='R3',
                position=[3*dx, 0*dy+2*a, ex, 4*ey],
                switches_list=[S6, S7, S8, S9])
    R4 = Room(name='R4',
                position=[4*dx, 0*dy+a, ex, 5*ey],
                switches_list=[S10, S11, S12, S13, S14])
    R5 = Room(name='R5',
                position=[5*dx, 0*dy, ex, 6*ey],
                switches_list=[S15, S16, S17, S18, S19, S20])
    RE = Room(name='RE',
              position=[0*dx, 5*ey, ex, ey],
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
                room_arrival=R4)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R5)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R5,
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 5.5/6])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5],
                 fastest_solution="S0 D0 D1 S5 D2 D3 S14 D4 S15 S16 S17 S18 S19 S20 D5",
                 level_color=get_color(),
                 name='Friendship graph F3 adjacency matrix',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.9, sa=0.7, li=0.65)
    lcolor.surrounding_color = Color.color_hls(hu=0.9, sa=1, li=0.9)
    lcolor.contour_color = Color.color_hls(hu=0.9, sa=1, li=0.9)
    return lcolor