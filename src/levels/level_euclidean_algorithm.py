from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color
from random import choice as rd_choice

def level_euclidean_algorithm(): 

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
    
    S18 = Switch(name='S18', value=rd_choice([0, 1]))
    S19 = Switch(name='S19', value=rd_choice([0, 1]))
    S20 = Switch(name='S20', value=rd_choice([0, 1]))
    S21 = Switch(name='S21', value=rd_choice([0, 1]))
    S22 = Switch(name='S22', value=rd_choice([0, 1]))
    S23 = Switch(name='S23', value=1)
    
    S24 = Switch(name='S24', value=rd_choice([0, 1]))
    S25 = Switch(name='S25', value=rd_choice([0, 1]))
    S26 = Switch(name='S26', value=rd_choice([0, 1]))
    S27 = Switch(name='S27', value=rd_choice([0, 1]))
    S28 = Switch(name='S28', value=rd_choice([0, 1]))
    S29 = Switch(name='S29', value=1)

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7,
             S8, S9, S10, S11, S12, S13, S14, S15,
             S16, S17, S18, S19, S20, S21, S22, S23,
             S24, S25, S26, S27, S28, S29]
    
    n = 6
    Slist0 = Slist[0:n]
    Slist1 = Slist[n:2*n]
    Slist2 = Slist[2*n:3*n]
    Slist3 = Slist[3*n:4*n]
    Slist4 = Slist[4*n:5*n]

    V0 = Tree(tree_list=Tree.tree_list_BIN(n),
          name='V0',
          switches=Slist0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(n),
          name='V1',
          switches=Slist1)
    V2 = Tree(tree_list=Tree.tree_list_BIN(n),
          name='V2',
          switches=Slist2)
    V3 = Tree(tree_list=Tree.tree_list_BIN(n),
          name='V3',
          switches=Slist3)
    V4 = Tree(tree_list=Tree.tree_list_BIN(n),
          name='V4',
          switches=Slist4)
    V5 = Tree(tree_list=['MIN', [None], [None]],
          name='V5',
          switches=[V1, V2])
    V6 = Tree(tree_list=['MAX', [None], [None]],
          name='V6',
          switches=[V1, V2])
    V7 = Tree(tree_list=['EQU',
                          ['SUM', [None], ['MINUS', [None]]],
                          [None]],
          name='V7',
          switches=[V6, V5, V4])
    
    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[1])
    T1 = Tree(tree_list=['EQU', [None], [None]],
                name='T1',
                switches=[V1, V3])
    T2 = Tree(tree_list=['EQU', [None], [None]],
                name='T2',
                switches=[V2, V4])
    T3 = Tree(tree_list=['EQU', [None], [None]],
                name='T3',
                switches=[V3, V5])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[V7])
    T5 = Tree(tree_list=['AND',
                         [None],
                         ['EQU', [None], [None]],
                         ['EQU', [None], [None]]],
                name='T5',
                switches=[V7,
                          V5, 0,
                          V0, V6])

    ex = 2
    ey = 3
    ax = 2
    ay = 1
    dx = ex+ax
    dy = ey+ay
    
    hu = 0.55
    background_color=Color.color_hls(hu, li=0.6, sa=0.4)
    room_color=Color.color_hls(hu, li=0.1, sa=0.3)
    letters_color=Color.BLACK
    contour_color=Color.YELLOW
    inside_room_color=Color.WHITE
    surrounding_color=Color.YELLOW
    lcolor = Level_color(background_color=background_color,
                         room_color=room_color,
                         letters_color=letters_color,
                         contour_color=contour_color,
                         inside_room_color=inside_room_color,
                         surrounding_color=surrounding_color)
    
    Ra = Room(name='',
                position=[ex, ey, ax, ay],
                switches_list=[],
                inside_color=room_color)
    e = 0.2
    Rb = Room(name='',
                position=[ex+e, ey+e, ax-2*e, ay-2*e],
                switches_list=[],
                inside_color=background_color)
    R0 = Room(name='R0',
                position=[-3, 0*dy, ex, ey],
                switches_list=Slist0,
                inside_color=room_color)
    R1 = Room(name='R1',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=Slist1,
                inside_color=room_color)
    R2 = Room(name='R2',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=Slist2,
                inside_color=room_color)
    R3 = Room(name='R3',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=Slist3,
                inside_color=room_color)
    R4 = Room(name='R4',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=Slist4,
                inside_color=room_color)
    RE = Room(name='RE',
              position=[-3, 1*dy, 2, ey],
              is_exit=True,
              inside_color=room_color)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                inside_color=room_color)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                inside_color=room_color)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3,
                inside_color=room_color)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4,
                inside_color=room_color)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R1,
                inside_color=room_color)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R4,
                room_arrival=RE,
                relative_departure_coordinates=[0, 1/2],
                relative_arrival_coordinates=[1, 1/2],
                inside_color=room_color)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, Ra, Rb, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5],
                 fastest_solution=None,
                 level_color=lcolor,
                 name='Euclidean algorithm',
                 keep_proportions=True,
                 door_window_size=350,
                 uniform_surrounding_colors=True,
                 uniform_inside_room_color=False,
                 random=True)
    
    return level