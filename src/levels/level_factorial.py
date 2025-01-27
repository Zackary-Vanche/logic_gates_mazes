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
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')
    S15 = Switch(name='S15')
    S16 = Switch(name='S16')
    S17 = Switch(name='S17')
    
    Slist_0 = [S0]
    Slist_1 = [S1, S2]
    Slist_2 = [S3, S4, S5]
    Slist_3 = [S6, S7, S8, S9, S10]
    Slist_4 = [S11, S12, S13, S14, S15, S16, S17]
    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_0)),
          name='V0',
          switches=Slist_0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_1)),
          name='V1',
          switches=Slist_1)
    V2 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_2)),
          name='V2',
          switches=Slist_2)
    V3 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_3)),
          name='V3',
          switches=Slist_3)
    V4 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_4)),
          name='V4',
          switches=Slist_4)
    
    tl = ['EQU', [None], Tree.tree_list_PROD(2)]

    T0 = Tree(tree_list=Tree.tree_list_EQU(2),
                name='T0',
                switches=[V0, 1])
    T1 = Tree(tree_list=tl,
                name='T1',
                switches=[V1, 2, V0])
    T2 = Tree(tree_list=tl,
                name='T2',
                switches=[V2, 3, V1])
    T3 = Tree(tree_list=tl,
                name='T3',
                switches=[V3, 4, V2])
    T4 = Tree(tree_list=tl,
                name='T4',
                switches=[V4, 5, V3])

    dx = 4.5
    dy = 3
    ex = 3
    ey = 2

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[1*dx, 0*dy-ey, ex, ey],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[1*dx, 1*dy+ey, ex, ey],
                switches_list=Slist_4)
    RE = Room(name='RE',
              position=[0*dx, 1*dy, ex, ey],
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
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4],
                 fastest_solution="S0 D0 S2 D1 S4 S5 D2 S9 S10 D3 S14 S15 S16 S17 D4",
                 level_color=get_color(),
                 name='Factorial',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    hu = 0.4
    lcolor = Level_color(background_color=Color.color_hls(hu, li=0.7, sa=0.25),
                         room_color=Color.color_hls(hu, li=0.2, sa=0.5),
                         letters_color=Color.BLACK,
                         contour_color=Color.ELECTRIC_BLUE,
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.ELECTRIC_BLUE)
    return lcolor