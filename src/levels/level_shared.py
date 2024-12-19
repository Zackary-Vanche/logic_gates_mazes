from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')

    Slist = [S0, S1, S2, S3, S4]

    T0 = Tree(tree_list=['EQU', Tree.tree_list_SUM(3), [None]],
                name='T0',
                switches=[S0, S1, S2, 2])
    T1 = Tree(tree_list=['EQU', Tree.tree_list_SUM(5), [None]],
                name='T1',
                switches=Slist + [4])
    T2 = Tree(tree_list=['EQU', Tree.tree_list_SUM(3), [None]],
                name='T2',
                switches=[S2, S3, S4, 2])

    dx = 1
    dy = 1
    ex = 1
    ey = 0.5
    
    ex2 = 0.5
    ey2 = 1.5

    R0 = Room(name='R0',
                position=[0*dx, 1*dy, 4*dx+ex, ey],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[2*dx+(ex-ex2)/2, -ey2, ex2, ey2],
                switches_list=[])
    RE = Room(name='RE',
              position=[4*dx, 0*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[ex/2/(4*dx+ex), 1/2])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=RE)
    
    hu = 0.825
    lcolor = Level_color(background_color=Color.color_hls(hu, li=0.8, sa=0.4),
                         room_color=Color.color_hls(hu, li=0.5, sa=0.4),
                         letters_color=Color.BLACK,
                         contour_color=Color.color_hls(hu=0.9, li=0.5, sa=1),
                         inside_room_color=Color.BLACK,
                         surrounding_color=Color.BLACK)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, RE],
                 doors_list=[D0, D1, D2],
                 fastest_solution="S0 S1 S3 S4 D0 D1 D2",
                 level_color=lcolor,
                 name='Shared',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level
