from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color
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
    S20 = Switch(name='S20')
    S21 = Switch(name='S21')
    S22 = Switch(name='S22')

    Slist0 = [S0]
    Slist1 = [S1]
    Slist2 = [S2]
    Slist3 = [S3, S4]
    Slist4 = [S5, S6]
    Slist5 = [S7, S8, S9]
    Slist6 = [S10, S11, S12, S13]
    Slist7 = [S14, S15, S16, S17]
    Slist8 = [S18, S19, S20, S21, S22]

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
    V6 = Tree(tree_list=Tree.tree_list_BIN(len(Slist6)),
          name='V6',
          switches=Slist6)
    V7 = Tree(tree_list=Tree.tree_list_BIN(len(Slist7)),
          name='V7',
          switches=Slist7)
    V8 = Tree(tree_list=Tree.tree_list_BIN(len(Slist8)),
          name='V8',
          switches=Slist8)
    
    tree_list_0 = ['EQU', Tree.tree_list_SUM(2), [None]]
    T0 = Tree(tree_list=['EQU', [None], [None]],
                name='T0',
                switches=[V0, 0])
    T1 = Tree(tree_list=['EQU', [None], [None]],
                name='T1',
                switches=[V1, 1])
    T2 = Tree(tree_list=tree_list_0,
                name='T2',
                switches=[V0, V1, V2])
    T3 = Tree(tree_list=tree_list_0,
                name='T3',
                switches=[V1, V2, V3])
    T4 = Tree(tree_list=tree_list_0,
                name='T4',
                switches=[V2, V3, V4])
    T5 = Tree(tree_list=tree_list_0,
                name='T5',
                switches=[V3, V4, V5])
    T6 = Tree(tree_list=tree_list_0,
                name='T6',
                switches=[V4, V5, V6])
    T7 = Tree(tree_list=tree_list_0,
                name='T7',
                switches=[V5, V6, V7])
    T8 = Tree(tree_list=tree_list_0,
                name='T8',
                switches=[V6, V7, V8])

    dx = 1
    dy = 1
    ex = dx
    ey = dy

    R0 = Room(name='R0',
                position=[3*dx, 0*dy, ex, ey],
                switches_list=Slist0)
    R1 = Room(name='R1',
                position=[5*dx, 0*dy, ex, ey],
                switches_list=Slist1)
    R2 = Room(name='R2',
                position=[7*dx, 0*dy, ex, ey],
                switches_list=Slist2)
    R3 = Room(name='R3',
                position=[6*dx, 2*dy, 2*ex, ey],
                switches_list=Slist3)
    R4 = Room(name='R4',
                position=[3*dx, 2*dy, 2*ex, ey],
                switches_list=Slist4)
    R5 = Room(name='R5',
                position=[2*dx, 4*dy, 3*ex, ey],
                switches_list=Slist5)
    R6 = Room(name='R6',
                position=[6*dx, 4*dy, 4*ex, ey],
                switches_list=Slist6)
    R7 = Room(name='R7',
                position=[6*dx, 6*dy, 4*ex, ey],
                switches_list=Slist7)
    R8 = Room(name='R8',
                position=[-1*dx, 6*dy, 5*ex, ey],
                switches_list=Slist8)
    RE = Room(name='RE',
              position=[-1*dx, 8*dy, 4*ex, ey],
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
                room_arrival=R3,
                relative_arrival_coordinates=[1.5/2, 1/2])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R5,
                relative_arrival_coordinates=[2/3, 1/2])
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R5,
                room_arrival=R6,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 1/2])
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R6,
                room_arrival=R7)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R7,
                room_arrival=R8)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R8,
                room_arrival=RE,
                relative_arrival_coordinates=[2.5/4, 1/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8],
                 fastest_solution="D0 S1 D1 S2 D2 S4 D3 S5 S6 D4 S7 S9 D5 S13 D6 S14 S16 S17 D7 S18 S20 S22 D8",
                 level_color=get_color(),
                 name='Fibonacci sequence',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    hu = 0.8
    lcolor = Level_color(background_color=Color.color_hls(hu, li=0.7, sa=0.25),
                         room_color=Color.color_hls(hu, li=0.2, sa=0.5),
                         letters_color=Color.BLACK,
                         contour_color=Color.ELECTRIC_BLUE,
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.ELECTRIC_BLUE)
    return lcolor