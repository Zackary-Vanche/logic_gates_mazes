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
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    S9 = Switch(name='S9')

    Slist0 = [S0]
    Slist1 = [S1]
    Slist2 = [S2, S3]
    Slist3 = [S4, S5]
    Slist4 = [S6, S7]
    Slist5 = [S8, S9]

    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist0)),
          name='V0',
          switches=Slist0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(len(Slist1)),
          name='V1',
          switches=Slist1)
    V2 = Tree(tree_list=Tree.tree_list_BIN(len(Slist2)),
          name='V2',
          switches=Slist2)
    V3 = Tree(tree_list=Tree.tree_list_BIN(len(Slist3)),
          name='V3',
          switches=Slist3)
    V4 = Tree(tree_list=Tree.tree_list_BIN(len(Slist4)),
          name='V4',
          switches=Slist4)
    V5 = Tree(tree_list=Tree.tree_list_BIN(len(Slist5)),
          name='V5',
          switches=Slist5)

    Vlist = [V0, V1, V2, V3, V4, V5]
    
    tree_list_1 = ['EQU', [None], [None]]
    tree_list_2 = ['AND'] + [['EQU', [None], [None]]]*2
    tree_list_3 = ['EQU', [None], ['SUM', [None], [None]]]

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[1])
    T1 = Tree(tree_list=tree_list_1,
                name='T1',
                switches=[V0, V1])
    T2 = Tree(tree_list=tree_list_2,
                name='T2',
                switches=[V0, 0, V1, 1])
    T3 = Tree(tree_list=tree_list_3,
                name='T3',
                switches=[V0, V1, 1])
    T4 = Tree(tree_list=tree_list_1,
                name='T4',
                switches=[V2, V3])
    T5 = Tree(tree_list=tree_list_2,
                name='T5',
                switches=[V2, 0, V3, 2])
    T6 = Tree(tree_list=tree_list_3,
                name='T6',
                switches=[V2, V3, 1])
    T7 = Tree(tree_list=tree_list_1,
                name='T7',
                switches=[V4, V5])
    T8 = Tree(tree_list=tree_list_2,
                name='T8',
                switches=[V4, 0, V5, 3])
    T9 = Tree(tree_list=['EQU', ['SUM'] + [[None]]*3, [None]],
                name='T9',
                switches=[V1, V3, V5, 5])

    dx = 1.5
    dy = 1
    ex = 1.25
    ey = 1
    
    cy = 4*dy+ey

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, cy],
                switches_list=[])
    R1 = Room(name='R1',
                position=[5.5*dx, 0*dy, ex, ey],
                switches_list=Slist0)
    R2 = Room(name='R2',
                position=[2.5*dx, 1*dy, ex, ey],
                switches_list=Slist1)
    R3 = Room(name='R3',
                position=[5*dx, 2*dy, dx+ex, ey],
                switches_list=Slist2)
    R4 = Room(name='R4',
                position=[2*dx, 3*dy, dx+ex, ey],
                switches_list=Slist3)
    R5 = Room(name='R5',
                position=[5*dx, 4*dy, dx+ex, ey],
                switches_list=Slist4)
    R6 = Room(name='R6',
                position=[2*dx, 5*dy, dx+ex, ey],
                switches_list=Slist5)
    RE = Room(name='RE',
              position=[2*dx, -dy, dx+ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[0, ey/2/cy])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R0,
                relative_arrival_coordinates=[0, ey/2/cy])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R3)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R3,
                room_arrival=R4)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R4,
                room_arrival=R0,
                relative_arrival_coordinates=[0, (2*dy+ey/2)/cy])
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R4,
                room_arrival=R5)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R5,
                room_arrival=R6)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R6,
                room_arrival=R0,
                relative_arrival_coordinates=[0, (4*dy+ey/2)/cy])
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[0, ey/2/cy])
    
    hu = 0.1
    lcolor = Level_color(background_color=Color.color_hls(hu, li=0.8, sa=0.3),
                         room_color=Color.color_hls(hu, li=0.15, sa=0.8),
                         letters_color=Color.BLACK,
                         contour_color=Color.color_hls(hu=0.16, li=0.9, sa=1),
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.color_hls(hu=0.4, li=0.5, sa=0.2))

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9],
                 fastest_solution="D0 D1 S1 D2 D0 S0 D1 S1 D3 D4 S5 D5 D0 S0 D1 S1 D2 D0 S0 D1 S1 D3 S3 D4 S4 S5 D6 D7 S8 S9 D8 D0 S0 D1 S1 D2 D9",
                 level_color=lcolor,
                 name='Cattle',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level
    