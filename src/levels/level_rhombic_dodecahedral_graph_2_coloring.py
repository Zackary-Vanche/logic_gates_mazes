from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle

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
    Sl0 = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13]
    rd_shuffle(Sl0)
    
    assert len(Sl0) == 14
    
    # 1: 9 10 11
    # 2: 9 10 12
    # 3: 9 11 13
    # 4: 10 11 14
    # 5: 10 12 14
    # 6: 9 12 13
    # 7: 11 13 14
    # 8: 12 13 14
    # 9: 1 2 3 6
    # 10: 1 2 4 5
    # 11: 1 3 4 7
    # 12: 2 5 6 8
    # 13: 3 6 7 8
    # 14: 4 5 7 8
    
    edges = [
        (1, 9), (1, 10), (1, 11),
        (2, 9), (2, 10), (2, 12),
        (3, 9), (3, 11), (3, 13),
        (4, 10), (4, 11), (4, 14),
        (5, 10), (5, 12), (5, 14),
        (6, 9), (6, 12), (6, 13),
        (7, 11), (7, 13), (7, 14),
        (8, 12), (8, 13), (8, 14),
    ]

    
    Sl = []
    for e in edges:
        Sl.append(Sl0[e[0]-1])
        Sl.append(Sl0[e[1]-1])
    
    T0 = Tree(tree_list=["AND"]+[Tree.tree_list_XOR(2)]*len(edges)+[["INF", Tree.tree_list_SUM(14), [None]]],
                name='T0',
                switches=Sl+[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, 7])

    n = 5

    R0 = Room(name='R0',
                position=[0, 0, n, n],
                switches_list=Sl0)
    RE = Room(name='RE',
              position=[n+1, n+1, 1, 1],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[(n-1/2)/n, (n-1/2)/n])
    
    sol_list = [Sl0[8].name,
                Sl0[9].name,
                Sl0[10].name,
                Sl0[11].name,
                Sl0[12].name,
                Sl0[13].name,
                "D0"]
    sol = ' '.join(sol_list)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution=sol,
                 level_color=get_color(),
                 name='Rhombic Dodecahedral Graph 2-coloring',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.4, sa=0.25, li=0.5)
    lcolor.contour_color = Color.color_hls(hu=0.12, sa=1, li=0.6)
    lcolor.surrounding_color = Color.color_hls(hu=0.12, sa=1, li=0.6)
    return lcolor