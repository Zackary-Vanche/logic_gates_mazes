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
    Sl0 = [S0, S1, S2, S3, S4, S5]
    rd_shuffle(Sl0)
        
    edges = [
        (0, 1),
        (0, 3),
        (0, 5),
        (2, 1),
        (2, 3),
        (2, 5),
        (4, 1),
        (4, 3),
        (4, 5),
    ]

    
    Sl = []
    for e in edges:
        Sl.append(Sl0[e[0]])
        Sl.append(Sl0[e[1]])
    
    T0 = Tree(tree_list=["AND"]+[Tree.tree_list_XOR(2)]*len(edges),
                name='T0',
                switches=Sl)

    n = 3

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
    
    sol_list = [Sl0[0].name,
                Sl0[2].name,
                Sl0[4].name,
                "D0"]
    sol = ' '.join(sol_list)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution=sol,
                 level_color=get_color(),
                 name='Utility graph Graph 2-coloring',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.4, sa=0.25, li=0.5)
    lcolor.contour_color = Color.color_hls(hu=0.06, sa=1, li=0.6)
    lcolor.surrounding_color = Color.color_hls(hu=0.06, sa=1, li=0.6)
    return lcolor