from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list

def f(): 

    Slist = [Switch(name=f'S{i}') for i in range(12)]

    #    
    #         A
    #   0   1    2    3
    # 4 B 5 C 6  D  7 E 4
    #   8   9   10   11
    #         F
    
    S_indexes = [0, 1, 2, 3,
                 0, 4, 5, 8,
                 1, 5, 6, 9,
                 2, 6, 7, 10,
                 3, 4, 7, 11,
                 8, 9, 10, 11,]

    T0 = Tree(tree_list=["AND"]+[Tree.tree_list_XOR(4)]*6,
                name='T0',
                switches=[Slist[i] for i in S_indexes],
                cut_expression_depth_1=True)

    dx = 1
    dy = 1
    ex = 0.2
    ey = 0.4

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, dx, dy],
                switches_list=Slist)
    RE = Room(name='RE',
              position=[-2*ex, (dy-ey)/2, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[0, 1/2],
                relative_arrival_coordinates=[1, 1/2])
    
    sol_list = [Slist[0].name, Slist[6].name, Slist[11].name, 'D0']

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution=" ".join(sol_list),
                 level_color=get_color(),
                 name='Octahedron maximum matching',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.7, sa=0.4, li=0.5)
    lcolor.surrounding_color = Color.color_hls(hu=0.24, sa=1, li=0.6)
    lcolor.contour_color = Color.color_hls(hu=0.24, sa=0.8, li=0.4)
    return lcolor