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

    Slist = [S0, S1, S2, S3, S4, S5]
    
    #    R0 R1 R2 R3
    # R0     0  1  2
    # R1  0     3  4
    # R2  1  3     5
    # R3  2  4  5    

    T0 = Tree(tree_list=Tree.tree_list_XOR(3),
          name='T0',
          switches=[S0, S1, S2])
    T1 = Tree(tree_list=Tree.tree_list_XOR(3),
          name='T1',
          switches=[S0, S3, S4])
    T2 = Tree(tree_list=Tree.tree_list_XOR(3),
          name='T2',
          switches=[S1, S3, S5])
    T3 = Tree(tree_list=Tree.tree_list_XOR(3),
          name='T3',
          switches=[S2, S4, S5])

    dx = 5
    dy = 5
    ex = 1
    ey = 1

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, dx-1, dy-1],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[dx-1, dy-1, ex, ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[1*dx, 1*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1, ey/2/(dy-1)],
                relative_arrival_coordinates=[0, 1/2])
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
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, RE],
                 doors_list=[D0, D1, D2, D3],
                 fastest_solution="S0 S5 D0 D1 D2 D3",
                 level_color=get_color(),
                 name='Tetrahedron maximum matching',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.2, sa=0.5, li=0.6)
    c = Color.color_hls(hu=0.6, sa=0.9, li=0.7)
    lcolor.surrounding_color = c
    lcolor.contour_color = c
    return lcolor