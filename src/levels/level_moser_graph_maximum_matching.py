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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10]
    
    #       A
    #  0  1   2  3
    # B 4 C   D 5 E
    #  6 7     8 9
    #   F   10  G
    
    T0 = Tree(tree_list=Tree.tree_list_XOR(4),
                name='T0',
                switches=[S0, S1, S2, S3])
    T1 = Tree(tree_list=["INF", Tree.tree_list_SUM(3), [None]],
                name='T1',
                switches=[S0, S4, S6, 1])
    T2 = Tree(tree_list=Tree.tree_list_XOR(3),
                name='T2',
                switches=[S1, S4, S7])
    T3 = Tree(tree_list=Tree.tree_list_XOR(3),
                name='T3',
                switches=[S2, S5, S8])
    T4 = Tree(tree_list=Tree.tree_list_XOR(3),
                name='T4',
                switches=[S3, S5, S9])
    T5 = Tree(tree_list=Tree.tree_list_XOR(3),
                name='T5',
                switches=[S6, S7, S10])
    T6 = Tree(tree_list=Tree.tree_list_XOR(3),
                name='T6',
                switches=[S8, S9, S10])

    dx = 1.5
    dy = 1
    ex = 0.4
    ey = 0.4
    a = 0.6

    R0 = Room(name='R0',
                position=[2*dx, 2*dy, dx+ex, dy+ey],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[2*dx-a, 2*dy-a, ex, ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[2*dx-a, 2.5*dy, ex, ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[2*dx-a+ex, 3*dy+a, ex, ey],
                switches_list=[])
    R4 = Room(name='R4',
                position=[3*dx+a-ex, 3*dy+a, ex, ey],
                switches_list=[])
    R5 = Room(name='R5',
                position=[3*dx+a, 2.5*dy, ex, ey],
                switches_list=[])
    R6 = Room(name='R6',
                position=[3*dx+a, 2*dy-a, ex, ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[2.5*dx, 2*dy-a, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[ex/2/(dx+ex), ey/2/(dy+ey)])
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
                room_arrival=R6)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R6,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution="S1 S5 S10 D0 D1 D2 D3 D4 D5 D6",
                 level_color=get_color(),
                 name='Moser graph maximum matching',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.5, sa=0.5, li=0.6)
    c = Color.color_hls(hu=0.7, sa=0.9, li=0.7)
    lcolor.surrounding_color = c
    lcolor.contour_color = c
    return lcolor