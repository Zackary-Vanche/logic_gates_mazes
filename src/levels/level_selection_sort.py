from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color
from random import shuffle as rd_shuffle

def f():
    
    ilist = [[0, 0, 0],
             [0, 1, 0],
             [1, 0, 0],
             [1, 1, 0],
             [0, 0, 1],
             [0, 1, 1],
             [1, 0, 1],
             [1, 1, 1]]
    rd_shuffle(ilist)

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    
    S9 = Switch(name='S9', value=ilist[0][0])
    S10 = Switch(name='S10', value=ilist[0][1])
    S11 = Switch(name='S11', value=ilist[0][2])
    
    S12 = Switch(name='S12', value=ilist[1][0])
    S13 = Switch(name='S13', value=ilist[1][1])
    S14 = Switch(name='S14', value=ilist[1][2])
    
    S15 = Switch(name='S15', value=ilist[2][0])
    S16 = Switch(name='S16', value=ilist[2][1])
    S17 = Switch(name='S17', value=ilist[2][2])
    
    S18 = Switch(name='S18', value=ilist[3][0])
    S19 = Switch(name='S19', value=ilist[3][1])
    S20 = Switch(name='S20', value=ilist[3][2])
    
    S21 = Switch(name='S21', value=ilist[4][0])
    S22 = Switch(name='S22', value=ilist[4][1])
    S23 = Switch(name='S23', value=ilist[4][2])
    
    S24 = Switch(name='S24', value=ilist[5][0])
    S25 = Switch(name='S25', value=ilist[5][1])
    S26 = Switch(name='S26', value=ilist[5][2])
    
    S27 = Switch(name='S27', value=ilist[6][0])
    S28 = Switch(name='S28', value=ilist[6][1])
    S29 = Switch(name='S29', value=ilist[6][2])

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29]

    Slist0 = Slist[0:3]
    Slist1 = Slist[3:6]
    Slist2 = Slist[6:9]
    Slist3 = Slist[9:12]
    Slist4 = Slist[12:15]
    Slist5 = Slist[15:18]
    Slist6 = Slist[18:21]
    Slist7 = Slist[21:24]
    Slist8 = Slist[24:27]
    Slist9 = Slist[27:30]

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
    V9 = Tree(tree_list=Tree.tree_list_BIN(len(Slist9)),
          name='V9',
          switches=Slist9)

    Vlist = [V3, V4, V5, V6, V7, V8, V9]
    
    value_list = []
    for V in Vlist:
        value_list.append(V.get_value())
        
    V10 = Tree(tree_list=['EQUSET'] + [[None]]*(len(Vlist)*2),
          name='V10',
          switches=Vlist + value_list)
    
    tree_list_4 = ['IN'] + [[None]]*3

    T0 = Tree(tree_list=['AND',
                         [None],
                         ]+[['NOT',
                             ['AND',
                              ['EQU', [None], [None]],
                              ['SUP', [None], [None]]]]]*6,
                name='T0',
                switches=[V10,
                          1, V0, V3, V4,
                          2, V0, V4, V5,
                          3, V0, V5, V6,
                          4, V0, V6, V7,
                          5, V0, V7, V8,
                          6, V0, V8, V9],
                cut_expression_depth_1=True)
    T1 = Tree(tree_list=['EQU', [None], Tree.tree_list_SUM(2)],
                name='T1',
                switches=[V0, V2, 1])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[1])
    T3 = Tree(tree_list=['EQU', [None], [None]],
                name='T3',
                switches=[V0, V2])
    T4 = Tree(tree_list=tree_list_4,
                name='T4',
                switches=[1, V0, V1])
    T5 = Tree(tree_list=tree_list_4,
                name='T5',
                switches=[2, V0, V1])
    T6 = Tree(tree_list=tree_list_4,
                name='T6',
                switches=[3, V0, V1])
    T7 = Tree(tree_list=tree_list_4,
                name='T7',
                switches=[4, V0, V1])
    T8 = Tree(tree_list=tree_list_4,
                name='T8',
                switches=[5, V0, V1])
    T9 = Tree(tree_list=tree_list_4,
                name='T9',
                switches=[6, V0, V1])
    T10 = Tree(tree_list=tree_list_4,
                name='T10',
                switches=[7, V0, V1])
    T11 = Tree(tree_list=['AND',
                          [None],
                          ['INFOREQU'] + [[None]]*len(Vlist),
                          ['EQU'] + [[None]]*4],
                name='T11',
                switches=[V10] + Vlist + [7, V0, V1, V2],
                cut_expression_depth_1=True)

    dx = 2
    dy = 1
    ex = 0.9
    ey = 0.9
    
    ay = dy
    bx = ex*3/2
    
    ex0 = 0.6

    R0 = Room(name='R0',
                position=[2*dx+(ex0-ex)/2, 0*dy, ex0, 6*dy+ey],
                switches_list=[])
    R1 = Room(name='R1',
                position=[1*dx, 4*dy, ex, 2*dy+ey],
                switches_list=Slist0)
    R2 = Room(name='R2',
                position=[0*dx, 2*dy, ex, 2*dy+ey],
                switches_list=Slist1)
    R3 = Room(name='R3',
                position=[1*dx, 0*dy, ex, 2*dy+ey],
                switches_list=Slist2,
                room_of_possible_switches=R1)
    R4 = Room(name='R4',
                position=[3*dx, 0*ay, 3*ex, ey],
                switches_list=Slist3)
    R5 = Room(name='R5',
                position=[3*dx+bx, 1*ay, 3*ex, ey],
                switches_list=Slist4)
    R6 = Room(name='R6',
                position=[3*dx, 2*ay, 3*ex, ey],
                switches_list=Slist5)
    R7 = Room(name='R7',
                position=[3*dx+bx, 3*ay, 3*ex, ey],
                switches_list=Slist6)
    R8 = Room(name='R8',
                position=[3*dx, 4*ay, 3*ex, ey],
                switches_list=Slist7)
    R9 = Room(name='R9',
                position=[3*dx+bx, 5*ay, 3*ex, ey],
                switches_list=Slist8)
    R10 = Room(name='R10',
                position=[3*dx, 6*ay, 3*ex, ey],
                switches_list=Slist9)
    RE = Room(name='RE',
              position=[ex+0.1, 3*dy, dx-0.1, ey],
              is_exit=True)

    n = 9
    
    def get_relative_departure_coordinates(i):
        k = 1
        return [1/2, (i+k)/(7+k)]
    
    rac=[1/8, 1/2]

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[ex/2/ex0, 1-1/n])
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
                room_arrival=R0,
                relative_arrival_coordinates=[ex/2/ex0, 1/n])
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R0,
                room_arrival=R4,
                relative_departure_coordinates=get_relative_departure_coordinates(0),
                relative_arrival_coordinates=rac)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R0,
                room_arrival=R5,
                relative_departure_coordinates=get_relative_departure_coordinates(1),
                relative_arrival_coordinates=rac)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=R6,
                relative_departure_coordinates=get_relative_departure_coordinates(2),
                relative_arrival_coordinates=rac)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R0,
                room_arrival=R7,
                relative_departure_coordinates=get_relative_departure_coordinates(3),
                relative_arrival_coordinates=rac)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R0,
                room_arrival=R8,
                relative_departure_coordinates=get_relative_departure_coordinates(4),
                relative_arrival_coordinates=rac)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R0,
                room_arrival=R9,
                relative_departure_coordinates=get_relative_departure_coordinates(5),
                relative_arrival_coordinates=rac)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R0,
                room_arrival=R10,
                relative_departure_coordinates=get_relative_departure_coordinates(6),
                relative_arrival_coordinates=rac)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[0, 1/2],
                relative_arrival_coordinates=[1, 1/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Selection sort',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def get_color():
    hu = 0.1
    lcolor = Level_color(background_color=Color.color_hls(hu, li=0.6, sa=0.2),
                         room_color=Color.color_hls(hu, li=0.15, sa=0.6),
                         letters_color=Color.BLACK,
                         contour_color=Color.color_hls(hu=0.9, li=0.4, sa=1),
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.color_hls(hu=0.9, li=0.3, sa=1))
    return lcolor