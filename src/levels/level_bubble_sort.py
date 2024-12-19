from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color
from random import shuffle as rd_shuffle
from random import choice as rd_choice

def f():
    
    ilist = [[0, 0],
             [0, 1],
             [1, 0],
             [1, 1]]
    ilist.append(rd_choice(ilist))
    rd_shuffle(ilist)

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    
    S4 = Switch(name='S4', value=ilist[0][0])
    S5 = Switch(name='S5', value=ilist[0][1])
    
    S6 = Switch(name='S6', value=ilist[1][0])
    S7 = Switch(name='S7', value=ilist[1][1])
    
    S8 = Switch(name='S8', value=ilist[2][0])
    S9 = Switch(name='S9', value=ilist[2][1])
    
    S10 = Switch(name='S10', value=ilist[3][0])
    S11 = Switch(name='S11', value=ilist[3][1])
    
    S12 = Switch(name='S12', value=ilist[4][0])
    S13 = Switch(name='S13', value=ilist[4][1])

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13]

    Slist0 = Slist[0:2]
    Slist1 = Slist[2:4]
    Slist2 = Slist[4:6]
    Slist3 = Slist[6:8]
    Slist4 = Slist[8:10]
    Slist5 = Slist[10:12]
    Slist6 = Slist[12:14]

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
    V6 = Tree(tree_list=Tree.tree_list_BIN(len(Slist5)),
          name='V6',
          switches=Slist6)

    Vlist = [V2, V3, V4, V5, V6]
    
    value_list = []
    for V in Vlist:
        value_list.append(V.get_value())
        
    V7 = Tree(tree_list=['EQUSET'] + [[None]]*(len(Vlist)*2),
          name='V7',
          switches=Vlist + value_list)
    
    tree_list_3 = ['EQU', [None], [None]]
    tree_list_4 = ['IN', [None], [None], [None]]

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[V7])
    T1 = Tree(tree_list=['EQU', [None], ['MOD', Tree.tree_list_SUM(2), [None]]],
                name='T1',
                switches=[V0, V1, 1, 4])
    T2 = Tree(tree_list=['EQU', [None], [None]],
                name='T2',
                switches=[V0, V1])
    T3 = Tree(tree_list=tree_list_3,
                name='T3',
                switches=[V0, 0])
    T4 = Tree(tree_list=tree_list_4,
                name='T4',
                switches=[V0, 0, 1])
    T5 = Tree(tree_list=tree_list_4,
                name='T5',
                switches=[V0, 1, 2])
    T6 = Tree(tree_list=tree_list_4,
                name='T6',
                switches=[V0, 2, 3])
    T7 = Tree(tree_list=tree_list_3,
                name='T7',
                switches=[V0, 3])
    T8 = Tree(tree_list=['AND',
                         ['INFOREQU'] + [[None]]*len(Vlist),
                         [None],
                         Tree.tree_list_NOR(4)],
                name='T8',
                switches=Vlist + [V7, S0, S1, S2, S3])

    dx = 1.25
    dy = 1.75
    ex = 0.8
    ey = ex*2
    
    ey0 = 0.5
    eys = 0.6
    
    ax = 0.15

    R0 = Room(name='R0',
                position=[0*dx, 1*dy, 6*dx+ex, ey0],
                switches_list=[])
    R1 = Room(name='R1',
                position=[0*dx, 0*dy-ax, dx+ex, eys],
                switches_list=Slist0)
    R2 = Room(name='R2',
                position=[5*dx, 0*dy+ax, dx+ex, eys],
                switches_list=Slist1)
    R3 = Room(name='R3',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=Slist2)
    R4 = Room(name='R4',
                position=[1*dx, 2*dy+ax, ex, ey],
                switches_list=Slist3)
    R5 = Room(name='R5',
                position=[2*dx, 2*dy+2*ax, ex, ey],
                switches_list=Slist4)
    R6 = Room(name='R6',
                position=[3*dx, 2*dy+3*ax, ex, ey],
                switches_list=Slist5)
    R7 = Room(name='R7',
                position=[4*dx, 2*dy+4*ax, ex, ey],
                switches_list=Slist6)
    RE = Room(name='RE',
              position=[5*dx, 1.8*dy, dx+ex, ey],
              is_exit=True)
    
    def get_relative_departure_coordinates(i):
        return [(i+2)/12, 1/2]
    
    rac = [1/2, eys/2/ey]
    
    n = 10
    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1/n, 0],
                relative_arrival_coordinates=[1/2, 1])
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
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[1-1/n, 0])
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R0,
                room_arrival=R3,
                relative_departure_coordinates=get_relative_departure_coordinates(0),
                relative_arrival_coordinates=rac)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R0,
                room_arrival=R4,
                relative_departure_coordinates=get_relative_departure_coordinates(1),
                relative_arrival_coordinates=rac)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R0,
                room_arrival=R5,
                relative_departure_coordinates=get_relative_departure_coordinates(2),
                relative_arrival_coordinates=rac)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=R6,
                relative_departure_coordinates=get_relative_departure_coordinates(3),
                relative_arrival_coordinates=rac)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R0,
                room_arrival=R7,
                relative_departure_coordinates=get_relative_departure_coordinates(4),
                relative_arrival_coordinates=rac)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=get_relative_departure_coordinates(5),
                relative_arrival_coordinates=rac)
    
    hu = 0.7
    lcolor = Level_color(background_color=Color.color_hls(hu, li=0.6, sa=0.3),
                         room_color=Color.color_hls(hu, li=0.15, sa=0.6),
                         letters_color=Color.BLACK,
                         contour_color=Color.color_hls(hu=0.5, li=0.5, sa=1),
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.color_hls(hu=0.5, li=0.5, sa=1))

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8],
                 fastest_solution=None,
                 level_color=lcolor,
                 name='Bubble sort',
                 keep_proportions=True,
                 door_window_size=400,
                 random=True)
    
    return level