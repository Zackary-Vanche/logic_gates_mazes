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
             [1, 0, 0],
             [0, 1, 0],
             [1, 1, 0],
             [0, 0, 1],
             [1, 0, 1],
             [0, 1, 1],
             [1, 1, 1]]
    rd_shuffle(ilist)
    
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    
    S3 = Switch(name='S3', value=ilist[0][0])
    S4 = Switch(name='S4', value=ilist[0][1])
    S5 = Switch(name='S5', value=ilist[0][2])
    
    S6 = Switch(name='S6', value=ilist[1][0])
    S7 = Switch(name='S7', value=ilist[1][1])
    S8 = Switch(name='S8', value=ilist[1][2])
    
    S9 = Switch(name='S9', value=ilist[2][0])
    S10 = Switch(name='S10', value=ilist[2][1])
    S11 = Switch(name='S11', value=ilist[2][2])
    
    S12 = Switch(name='S12', value=ilist[3][0])
    S13 = Switch(name='S13', value=ilist[3][1])
    S14 = Switch(name='S14', value=ilist[3][2])
    
    S15 = Switch(name='S15', value=ilist[4][0])
    S16 = Switch(name='S16', value=ilist[4][1])
    S17 = Switch(name='S17', value=ilist[4][2])
    
    S18 = Switch(name='S18', value=ilist[5][0])
    S19 = Switch(name='S19', value=ilist[5][1])
    S20 = Switch(name='S20', value=ilist[5][2])
    
    S21 = Switch(name='S21', value=ilist[6][0])
    S22 = Switch(name='S22', value=ilist[6][1])
    S23 = Switch(name='S23', value=ilist[6][2])
    
    S24 = Switch(name='S24', value=ilist[7][0])
    S25 = Switch(name='S25', value=ilist[7][1])
    S26 = Switch(name='S26', value=ilist[7][2])

    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    Slist_3 = [S9, S10, S11]
    Slist_4 = [S12, S13, S14]
    Slist_5 = [S15, S16, S17]
    Slist_6 = [S18, S19, S20]
    Slist_7 = [S21, S22, S23]
    Slist_8 = [S24, S25, S26]
    
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
    V5 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_5)),
          name='V5',
          switches=Slist_5)
    V6 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_6)),
          name='V6',
          switches=Slist_6)
    V7 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_7)),
          name='V7',
          switches=Slist_7)
    V8 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_8)),
          name='V8',
          switches=Slist_8)
    Vlist = [V1, V2, V3, V4, V5, V6, V7, V8]
    value_list = []
    for V in Vlist:
        value_list.append(V.get_value())
    V9 = Tree(tree_list=["EQUSET"] + [[None]]*16,
          name='V9',
          switches=Vlist + value_list)
    
    def get_tree_list(i):
        return ["AND", Tree.tree_list_EQU(2), Tree.tree_list_SUP(2), Tree.tree_list_INF(i+1)]
    
    def get_Vlist(i):
        return [V0] + [i] + Vlist[i:i+2] + Vlist[:i+1]
    
    tree_list_0 = ["OR",
                   ["AND", Tree.tree_list_EQU(2), Tree.tree_list_SUP(2)],]
    Slist_T0 = [V0, 0, V1, V2,]
    for i in range(1, 7):
        tree_list_0.append(get_tree_list(i))
        Slist_T0.extend(get_Vlist(i))
        
    tree_list_3 = ["IN"] + [[None]]*3

    T0 = Tree(tree_list=tree_list_0,
                name='T0',
                switches=Slist_T0,
                cut_expression_depth_1=True)
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[V9])
    T2 = Tree(tree_list=Tree.tree_list_EQU(2),
                name='T2',
                switches=[V0, 0])
    T3 = Tree(tree_list=tree_list_3,
                name='T3',
                switches=[V0, 0, 1])
    T4 = Tree(tree_list=tree_list_3,
                name='T4',
                switches=[V0, 1, 2])
    T5 = Tree(tree_list=tree_list_3,
                name='T5',
                switches=[V0, 2, 3])
    T6 = Tree(tree_list=tree_list_3,
                name='T6',
                switches=[V0, 3, 4])
    T7 = Tree(tree_list=tree_list_3,
                name='T7',
                switches=[V0, 4, 5])
    T8 = Tree(tree_list=tree_list_3,
                name='T8',
                switches=[V0, 5, 6])
    T9 = Tree(tree_list=Tree.tree_list_EQU(2),
                name='T9',
                switches=[V0, 6])
    T10 = Tree(tree_list=Tree.tree_list_INF(len(Vlist)),
                name='T10',
                switches=Vlist)

    dx = 1.8
    ex = 0.8
    ey = 0.8
    ey0 = 0.4
    a = 1
    eye = 2*a+ey0
    dy0 = -3*ey-a
    dy1 = 0
    dy2 = ey0+a
    epsilonx = 1.5

    R0 = Room(name='R0',
                position=[-2*ex, dy1+(ey0-eye)/2, ex, eye],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[0*dx+epsilonx, dy1, 3*dx+ex-epsilonx, ey0],
                switches_list=[])
    R2 = Room(name='R2',
                position=[0*dx, dy0, ex, 3*ey],
                switches_list=Slist_1)
    R3 = Room(name='R3',
                position=[0*dx, dy2, ex, 3*ey],
                switches_list=Slist_2)
    R4 = Room(name='R4',
                position=[1*dx, dy0, ex, 3*ey],
                switches_list=Slist_3)
    R5 = Room(name='R5',
                position=[1*dx, dy2, ex, 3*ey],
                switches_list=Slist_4)
    R6 = Room(name='R6',
                position=[2*dx, dy0, ex, 3*ey],
                switches_list=Slist_5)
    R7 = Room(name='R7',
                position=[2*dx, dy2, ex, 3*ey],
                switches_list=Slist_6)
    R8 = Room(name='R8',
                position=[3*dx, dy0, ex, 3*ey],
                switches_list=Slist_7)
    R9 = Room(name='R9',
                position=[3*dx, dy2, ex, 3*ey],
                switches_list=Slist_8)
    RE = Room(name='RE',
              position=[3*dx+ex+1, dy1+(ey0-eye)/2, ex, eye],
              is_exit=True)
    
    def get_rc(i):
        if i%2 == 0:
            i = i//2
            return [(i*dx+ex/2)/(3*dx+ex), 0]
        else:
            i = i//2
            return [(i*dx+ex/2)/(3*dx+ex), 1]
    
    rac0 = [1/2, 1]
    rac1 = [1/2, 0]

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 1/2],
                relative_position=0.725)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R0,
                relative_departure_coordinates=[0, 1/2],
                relative_arrival_coordinates=[1, 1/2],
                relative_position=0.725)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=get_rc(0),
                relative_arrival_coordinates=rac0)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R3,
                relative_departure_coordinates=get_rc(1),
                relative_arrival_coordinates=rac1)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R1,
                room_arrival=R4,
                relative_departure_coordinates=get_rc(2),
                relative_arrival_coordinates=rac0)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R1,
                room_arrival=R5,
                relative_departure_coordinates=get_rc(3),
                relative_arrival_coordinates=rac1)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R1,
                room_arrival=R6,
                relative_departure_coordinates=get_rc(4),
                relative_arrival_coordinates=rac0)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R1,
                room_arrival=R7,
                relative_departure_coordinates=get_rc(5),
                relative_arrival_coordinates=rac1)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R1,
                room_arrival=R8,
                relative_departure_coordinates=get_rc(6),
                relative_arrival_coordinates=rac0)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R1,
                room_arrival=R9,
                relative_departure_coordinates=get_rc(7),
                relative_arrival_coordinates=rac1)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R1,
                room_arrival=RE,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 1/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Gnome sort',
                 keep_proportions=True,
                 door_window_size=425,
                 random=True)
    
    return level

def get_color():
    hu = 0
    lcolor = Level_color(background_color=Color.color_hls(hu, li=0.7, sa=0.3),
                         room_color=Color.color_hls(hu, li=0.4, sa=0.4),
                         letters_color=Color.BLACK,
                         contour_color=Color.color_hls(hu=0, li=0.1, sa=1),
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.color_hls(hu=0, li=0.1, sa=1))
    return lcolor