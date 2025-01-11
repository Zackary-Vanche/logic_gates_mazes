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
    ilist.append(rd_choice(ilist))
    rd_shuffle(ilist)

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    
    S6 = Switch(name='S6', value=ilist[0][0])
    S7 = Switch(name='S7', value=ilist[0][1])
    
    S8 = Switch(name='S8', value=ilist[1][0])
    S9 = Switch(name='S9', value=ilist[1][1])
    
    S10 = Switch(name='S10', value=ilist[2][0])
    S11 = Switch(name='S11', value=ilist[2][1])
    
    S12 = Switch(name='S12', value=ilist[3][0])
    S13 = Switch(name='S13', value=ilist[3][1])
    
    S14 = Switch(name='S14', value=ilist[4][0])
    S15 = Switch(name='S15', value=ilist[4][0])
    
    S16 = Switch(name='S16', value=ilist[4][0])
    S17 = Switch(name='S17', value=ilist[4][0])

    Slist0 = [S0, S1, S2]
    Slist1 = [S3, S4, S5]
    Slist2 = [S6, S7]
    Slist3 = [S8, S9]
    Slist4 = [S10, S11]
    Slist5 = [S12, S13]
    Slist6 = [S14, S15]
    Slist7 = [S16, S17]

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
    V7 = Tree(tree_list=Tree.tree_list_BIN(len(Slist6)),
          name='V7',
          switches=Slist7)

    Vlist = [V2, V3, V4, V5, V6, V7]
    
    value_list = []
    for V in Vlist:
        value_list.append(V.get_value())
        
    V8 = Tree(tree_list=['EQUSET'] + [[None]]*(len(Vlist)*2),
          name='V8',
          switches=Vlist + value_list)
    
    tree_list_3 = ['EQU', [None], [None]]
    tree_list_4 = ['IN'] + [[None]]*4
    tree_list_5 = ['IN'] + [[None]]*5

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[V8])
    T1 = Tree(tree_list=['EQU', [None], ['MOD', Tree.tree_list_SUM(2), [None]]],
                name='T1',
                switches=[V0, V1, 1, 8])
    T2 = Tree(tree_list=['EQU', [None], [None]],
                name='T2',
                switches=[V0, V1])
    T3 = Tree(tree_list=tree_list_3,
                name='T3',
                switches=[V0, 0])
    T4 = Tree(tree_list=tree_list_4,
                name='T4',
                switches=[V0, 0, 1, 7])
    T5 = Tree(tree_list=tree_list_5,
                name='T5',
                switches=[V0, 1, 2, 6, 7])
    T6 = Tree(tree_list=tree_list_5,
                name='T6',
                switches=[V0, 2, 3, 5, 6])
    T7 = Tree(tree_list=tree_list_4,
                name='T7',
                switches=[V0, 3, 4, 5])
    T8 = Tree(tree_list=tree_list_3,
                name='T8',
                switches=[V0, 4])
    T9 = Tree(tree_list=['AND',
                         ['EQU', [None], [None], [None]],
                         ['INFOREQU'] + [[None]]*len(Vlist),
                         [None],
                         ],
                name='T9',
                switches=[0, V0, V1] + Vlist + [V8],
                cut_expression_depth_1=False)

    p = 4/5

    dx = 1.25
    dy = 2.1
    ex = 0.8
    ey = ex*2
    
    ey0 = 0.5
    eys = 0.6
    
    ax = -0.15

    R0 = Room(name='R0',
                position=[0*dx, 1*dy, 6*dx+ex, ey0],
                switches_list=[])
    R1 = Room(name='R1',
                position=[0*dx, 0*dy-ax, 2*dx+ex, eys],
                switches_list=Slist0)
    R2 = Room(name='R2',
                position=[4*dx, 0*dy+ax, 2*dx+ex, eys],
                switches_list=Slist1)
    R3 = Room(name='R3',
                position=[0*dx*p, 2*dy, ex, ey],
                switches_list=Slist2)
    R4 = Room(name='R4',
                position=[1*dx*p, 2*dy+ax, ex, ey],
                switches_list=Slist3)
    R5 = Room(name='R5',
                position=[2*dx*p, 2*dy+2*ax, ex, ey],
                switches_list=Slist4)
    R6 = Room(name='R6',
                position=[3*dx*p, 2*dy+3*ax, ex, ey],
                switches_list=Slist5)
    R7 = Room(name='R7',
                position=[4*dx*p, 2*dy+4*ax, ex, ey],
                switches_list=Slist6)
    R8 = Room(name='R8',
                position=[5*dx*p, 2*dy+5*ax, ex, ey],
                switches_list=Slist7)
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
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R0,
                room_arrival=R8,
                relative_departure_coordinates=get_relative_departure_coordinates(5),
                relative_arrival_coordinates=rac)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=get_relative_departure_coordinates(6),
                relative_arrival_coordinates=rac)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Cocktail sort',
                 keep_proportions=True,
                 door_window_size=405,
                 random=True)
    
    return level

def get_color():
    hu = 0.5
    lcolor = Level_color(background_color=Color.color_hls(hu, li=0.6, sa=0.2),
                         room_color=Color.color_hls(hu, li=0.15, sa=0.6),
                         letters_color=Color.BLACK,
                         contour_color=Color.color_hls(hu=0.5, li=0.5, sa=1),
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.color_hls(hu=0.5, li=0.5, sa=1))
    return lcolor