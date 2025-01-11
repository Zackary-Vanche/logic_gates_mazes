from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color
from random import shuffle as rd_shuffle

def f():
    
    ilist = [[0, 1, 0],
             [1, 0, 0],
             [1, 1, 0],
             [0, 0, 1],
             [0, 1, 1],
             [1, 0, 1]]
    rd_shuffle(ilist)
    
    S0 = Switch(name='S0', value=ilist[0][0])
    S1 = Switch(name='S1', value=ilist[0][1])
    S2 = Switch(name='S2', value=ilist[0][2])
    
    S3 = Switch(name='S3', value=ilist[1][0])
    S4 = Switch(name='S4', value=ilist[1][1])
    S5 = Switch(name='S5', value=ilist[1][2])
    
    S6 = Switch(name='S6', value=ilist[2][0])
    S7 = Switch(name='S7', value=ilist[2][1])
    S8 = Switch(name='S8', value=ilist[2][2])
    
    S9 = Switch(name='S9', value=ilist[3][0])
    S10 = Switch(name='S10', value=ilist[3][1])
    S11 = Switch(name='S11', value=ilist[3][2])
    
    S12 = Switch(name='S12', value=ilist[4][0])
    S13 = Switch(name='S13', value=ilist[4][1])
    S14 = Switch(name='S14', value=ilist[4][2])
    
    S15 = Switch(name='S15', value=1)
    S16 = Switch(name='S16', value=1)
    S17 = Switch(name='S17', value=1)
    S18 = Switch(name='S18', value=1)
    S19 = Switch(name='S19', value=1)
    S20 = Switch(name='S20', value=1)
    S21 = Switch(name='S21', value=1)
    S22 = Switch(name='S22', value=1)
    S23 = Switch(name='S23', value=1)
    S24 = Switch(name='S24', value=1)
    S25 = Switch(name='S25', value=1)
    S26 = Switch(name='S26', value=1)
    S27 = Switch(name='S27', value=1)
    S28 = Switch(name='S28', value=1)
    S29 = Switch(name='S29', value=1)

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14,
             S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29]
    
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
    
    Vlist = [V0, V1, V2, V3, V4]
    
    value_list = []
    for V in Vlist:
        value_list.append(V.get_value())
    
    tree_list_0 = [None]
    tree_list_EQU = ['EQU', [None], [None]]
    tree_list_INF = ['INF', [None], [None]]

    T0 = Tree(tree_list=tree_list_0,
                name='T0',
                switches=[1])
    T1 = Tree(tree_list=tree_list_EQU,
                name='T1',
                switches=[V0, V1])
    T2 = Tree(tree_list=tree_list_EQU,
                name='T2',
                switches=[V1, V2])
    T3 = Tree(tree_list=tree_list_EQU,
                name='T3',
                switches=[V2, V3])
    T4 = Tree(tree_list=tree_list_EQU,
                name='T4',
                switches=[V3, V4])
    T5 = Tree(tree_list=tree_list_EQU,
                name='T5',
                switches=[V4, 0])
    T6 = Tree(tree_list=tree_list_0,
                name='T6',
                switches=[1])
    
    
    T7 = Tree(tree_list=tree_list_EQU,
                name='T7',
                switches=[V0, V5])
    T8 = Tree(tree_list=['AND', tree_list_EQU, tree_list_INF],
                name='T8',
                switches=[V0, V6, V6, V5])
    T9 = Tree(tree_list=['AND', tree_list_EQU, tree_list_INF],
                name='T9',
                switches=[V0, V7, V7, V6])
    T10 = Tree(tree_list=['AND', tree_list_EQU, tree_list_INF],
                name='T10',
                switches=[V0, V8, V8, V7])
    T11 = Tree(tree_list=['AND', tree_list_EQU, tree_list_INF],
                name='T11',
                switches=[V0, V9, V9, V8])
    
    
    T12 = Tree(tree_list=tree_list_EQU,
                name='T12',
                switches=[V5, V6])
    T13 = Tree(tree_list=tree_list_EQU,
                name='T13',
                switches=[V6, V7])
    T14 = Tree(tree_list=tree_list_EQU,
                name='T14',
                switches=[V7, V8])
    T15 = Tree(tree_list=tree_list_EQU,
                name='T15',
                switches=[V8, V9])
    T16 = Tree(tree_list=['AND',
                          ['EQUSET'] + [[None]]*10,
                          ['SUP'] + [[None]]*5,],
                name='T16',
                switches=[V5, V6, V7, V8, V9] + value_list + [V5, V6, V7, V8, V9])

    dx = 2
    ex = 1
    ey = 3
    
    ey0 = 0.5
    ay = 1
    
    deltay2 = 0.5
    deltay3 = 0.7

    R0 = Room(name='R0',
                position=[0*dx, ey+ay, 4*dx+ex, ey0],
                switches_list=[])
    R1 = Room(name='R1',
                position=[0*dx, 0, ex, ey],
                switches_list=Slist0)
    R2 = Room(name='R2',
                position=[1*dx, deltay2, ex, ey],
                switches_list=Slist1)
    R3 = Room(name='R3',
                position=[2*dx, deltay3, ex, ey],
                switches_list=Slist2)
    R4 = Room(name='R4',
                position=[3*dx, deltay2, ex, ey],
                switches_list=Slist3)
    R5 = Room(name='R5',
                position=[4*dx, 0, ex, ey],
                switches_list=Slist4)
    R6 = Room(name='R6',
                position=[4*dx, ey+ey0+2*ay, ex, ey],
                switches_list=Slist5)
    R7 = Room(name='R7',
                position=[3*dx, ey+ey0+2*ay, ex, ey],
                switches_list=Slist6)
    R8 = Room(name='R8',
                position=[2*dx, ey+ey0+2*ay, ex, ey],
                switches_list=Slist7)
    R9 = Room(name='R9',
                position=[1*dx, ey+ey0+2*ay, ex, ey],
                switches_list=Slist8)
    R10 = Room(name='R10',
                position=[0*dx, ey+ey0+2*ay, ex, ey],
                switches_list=Slist9)
    RE = Room(name='RE',
              position=[5*dx, ey, ex, 2*ay+ey0],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[ex/2/(4*dx+ex), 0],
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
                room_arrival=R0,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[(4*dx+ex/2)/(4*dx+ex), 0])
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=R6,
                relative_departure_coordinates=[(3*dx+ex)/(4*dx+ex), 1],
                relative_arrival_coordinates=[0, 0])
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R6,
                room_arrival=R0,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[(4*dx+ex/2)/(4*dx+ex), 1])
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R7,
                room_arrival=R0,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[(3*dx+ex/2)/(4*dx+ex), 1])
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R8,
                room_arrival=R0,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[(2*dx+ex/2)/(4*dx+ex), 1])
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R9,
                room_arrival=R0,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[(1*dx+ex/2)/(4*dx+ex), 1])
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R10,
                room_arrival=R0,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[ex/2/(4*dx+ex), 1])
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R6,
                room_arrival=R7)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R7,
                room_arrival=R8)
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R8,
                room_arrival=R9)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R9,
                room_arrival=R10)
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 1/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Insertion sort',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level


def get_color():
    hu = 0.9
    lcolor = Level_color(background_color=Color.color_hls(hu, li=0.7, sa=0.3),
                         room_color=Color.color_hls(hu, li=0.4, sa=0.4),
                         letters_color=Color.BLACK,
                         contour_color=Color.color_hls(hu=0.9, li=0.1, sa=1),
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.color_hls(hu=0.9, li=0.1, sa=1))
    return lcolor