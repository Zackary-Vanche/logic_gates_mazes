from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Level_color import Level_color
from Color import Color

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
    
    tree_list_BIN_3 = Tree.tree_list_BIN(3)

    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    Slist_3 = [S9, S10, S11]
    Slist_4 = [S12, S13, S14]
    Slist_5 = [S15, S16, S17]
    Slist_6 = [S18, S19, S20]
    V0 = Tree(tree_list=tree_list_BIN_3,
          name='V0',
          switches=Slist_0)
    V1 = Tree(tree_list=tree_list_BIN_3,
          name='V1',
          switches=Slist_1)
    V2 = Tree(tree_list=tree_list_BIN_3,
          name='V2',
          switches=Slist_2)
    V3 = Tree(tree_list=tree_list_BIN_3,
          name='V3',
          switches=Slist_3)
    V4 = Tree(tree_list=tree_list_BIN_3,
          name='V4',
          switches=Slist_4)
    V5 = Tree(tree_list=tree_list_BIN_3,
          name='V5',
          switches=Slist_5)
    V6 = Tree(tree_list=tree_list_BIN_3,
          name='V6',
          switches=Slist_6)
    V7 = Tree(tree_list=['DIFF'] + [[None]]*7,
          name='V7',
          switches=[V0, V1, V2, V3, V4, V5, V6])
    
    tree_list_1 = ['EQU',
                   ['SUM', [None], [None]],
                   ['PROD', [None], [None]],
                   ]
    
    T0 = Tree(tree_list=['DIFF', [None], [None]],
                name='T0',
                switches=[0, V0])
    T1 = Tree(tree_list=['INF', [None], [None]],
                name='T1',
                switches=[V0, V1])
    T2 = Tree(tree_list=tree_list_1,
                name='T2',
                switches=[V0, V1, 2, V4])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[1])
    T4 = Tree(tree_list=['INF', [None], [None]],
                name='T4',
                switches=[V2, V3])
    T5 = Tree(tree_list=['AND', tree_list_1, ['INF', [None], [None]]],
                name='T5',
                switches=[V2, V3, 2, V5,
                          V4, V5])
    T6 = Tree(tree_list=['AND', tree_list_1, [None]],
                name='T6',
                switches=[V4, V5, 2, V6, V7])

    dx = 1
    dy = 1
    ex = 1
    ey = 1

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, 3*ey],
                switches_list=[S0, S1, S2])
    R1 = Room(name='R1',
                position=[2*dx, 0*dy, ex, 3*ey],
                switches_list=[S3, S4, S5])
    R2 = Room(name='R2',
                position=[4*dx, 0*dy, ex, 3*ey],
                switches_list=[S6, S7, S8])
    R3 = Room(name='R3',
                position=[6*dx, 0*dy, ex, 3*ey],
                switches_list=[S9, S10, S11])
    R4 = Room(name='R4',
                position=[0*dx, 4*dy, 3*ex, ey],
                switches_list=[S12, S13, S14])
    R5 = Room(name='R5',
                position=[4*dx, 4*dy, 3*ex, ey],
                switches_list=[S15, S16, S17])
    R6 = Room(name='R6',
                position=[2*dx, 6*dy, 3*ex, ey],
                switches_list=[S18, S19, S20])
    RE = Room(name='RE',
              position=[6*dx, 5*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1, 2/3],
                relative_arrival_coordinates=[0, 1/3])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R4,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[1/2, 0])
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R4,
                room_arrival=R2,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[0, 1])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R3,
                relative_departure_coordinates=[1, 2/3],
                relative_arrival_coordinates=[0, 1/3])
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R3,
                room_arrival=R5,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[1/2, 0])
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R5,
                room_arrival=R6,
                relative_departure_coordinates=[0.5/3, 1],
                relative_arrival_coordinates=[1/2, 0])
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R6,
                room_arrival=RE,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 1/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution="S0 D0 S3 S4 D1 S13 D2 S6 S8 D3 S9 S10 S11 D4 S16 S17 D5 S20 D6",
                 level_color=get_color(),
                 name='Bloodline',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    hu = 0
    sa = 0.3
    li = 0.6
    lcolor = Level_color(background_color=Color.color_hls(hu, li*0.5 , sa),
                         room_color=Color.color_hls(hu, li*0.2, 0.8 * sa),
                         letters_color=Color.color_hls(hu=0.72, li=0.95, sa=0.9),
                         contour_color=Color.PINK,
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.TOTAL_RED)
    return lcolor