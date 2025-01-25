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
    
    l_room_doors = [[] for i in range(8)]
    for i, x in enumerate(l):
        a, b = x
        l_room_doors[a].append(i)
        l_room_doors[b].append(i)
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19]

    Sl_T0 = []
    for x in l_room_doors:
        for i in x:
            Sl_T0.append(Slist[i])
    
    T0 = Tree(tree_list=["AND"] + [Tree.tree_list_XOR(3)]*8,
              name='T0',
              switches=Sl_T0,
              cut_expression_depth_1=True)
    
    Tl = [Tree(tree_list=Tree.tree_list_NOT,
                name=f'T{i+1}',
                switches=[Slist[i]]) for i in range(12)]
    
    T13 = Tree(tree_list=Tree.tree_list_AND(8),
                name='T13',
                switches=[S12, S13, S14, S15, S16, S17, S18, S19])
    
    Tl = [T0] + Tl + [T13]

    dx = 1
    dy = 1
    ex = 0.4
    ey = 0.4
    ax = 0.7
    ay = 0.7

    R0 = Room(name='R0',
                position=[-1, 0*dy, 0.5, 2*dy+ay+ey],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11,])
    R1 = Room(name='R1',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S12])
    R2 = Room(name='R2',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S13])
    R3 = Room(name='R3',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[S14])
    R4 = Room(name='R4',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S15])
    R5 = Room(name='R5',
                position=[0*dx+ax, 0*dy+ay, ex, ey],
                switches_list=[S16])
    R6 = Room(name='R6',
                position=[0*dx+ax, 2*dy+ay, ex, ey],
                switches_list=[S17])
    R7 = Room(name='R7',
                position=[2*dx+ax, 0*dy+ay, ex, ey],
                switches_list=[S18])
    R8 = Room(name='R8',
                position=[2*dx+ax, 2*dy+ay, ex, ey],
                switches_list=[S19])
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

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=Rl,
                 doors_list=Dl,
                 fastest_solution="S0 S5 S9 S10 D0 S12 D2 S14 D7 S18 D12 S19 D8 S15 D4 S13 D5 S17 D9 S16 D13",
                 level_color=get_color(),
                 name='Cube maximum matching',
                 keep_proportions=True,
                 door_window_size=280)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.6, sa=0.4, li=0.5)
    lcolor.surrounding_color = Color.color_hls(hu=0.14, sa=1, li=0.6)
    lcolor.contour_color = Color.color_hls(hu=0.14, sa=0.8, li=0.4)
    return lcolor