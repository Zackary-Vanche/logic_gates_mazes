from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color
from random import shuffle as rd_shuffle

def level_cycle_sort(): 
    
    ilist = [[0, 0, 0],
             [1, 0, 0],
             [0, 1, 0],
             [1, 1, 0],
             [0, 0, 1],
             [1, 0, 1],
             [0, 1, 1],
             [1, 1, 1]]
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
    
    S15 = Switch(name='S15', value=ilist[5][0])
    S16 = Switch(name='S16', value=ilist[5][1])
    S17 = Switch(name='S17', value=ilist[5][2])
    
    Slist_1 = [S0, S1, S2]
    Slist_2 = [S3, S4, S5]
    Slist_3 = [S6, S7, S8]
    Slist_4 = [S9, S10, S11]
    Slist_5 = [S12, S13, S14]
    Slist_6 = [S15, S16, S17]
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_1)),
          name='V0',
          switches=Slist_1)
    V1 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_2)),
          name='V1',
          switches=Slist_2)
    V2 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_3)),
          name='V2',
          switches=Slist_3)
    V3 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_4)),
          name='V3',
          switches=Slist_4)
    V4 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_5)),
          name='V4',
          switches=Slist_5)
    V5 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_6)),
          name='V5',
          switches=Slist_6)
    
    Vlist = [V0, V1, V2, V3, V4, V5]
    value_list = []
    for V in Vlist:
        value_list.append(V.get_value())
    value_list.sort()
    
    tree_list_V6 = ["EQU",
                    ["SUM"] + [Tree.tree_list_SUP(2)]*6,
                    [None]]
    
    def get_V(i):
        V = Tree(tree_list=tree_list_V6,
              name=f'V{i+6}',
              switches=[Vlist[i], value_list[0],
                        Vlist[i], value_list[1],
                        Vlist[i], value_list[2],
                        Vlist[i], value_list[3],
                        Vlist[i], value_list[4],
                        Vlist[i], value_list[5],
                        i])
        return V
    
    V6 = get_V(0)
    V7 = get_V(1)
    V8 = get_V(2)
    V9 = get_V(3)
    V10 = get_V(4)
    V11 = get_V(5)
        
    V12 = Tree(tree_list=["EQUSET"] + [[None]]*(2*len(Vlist)),
          name='V12',
          switches=Vlist + value_list,
          cut_expression=True)
    
    tree_list_6 = ["AND", [None], Tree.tree_list_EQU(2)]
    
    # R0
    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[V12])
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[V12])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[V12])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[V12])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[V12])
    T5 = Tree(tree_list=[None],
                name='T5',
                switches=[V12])
    
    # R1
    T6 = Tree(tree_list=tree_list_6,
                name='T6',
                switches=[V6, V0, V1])
    T7 = Tree(tree_list=tree_list_6,
                name='T7',
                switches=[V6, V0, V2])
    T8 = Tree(tree_list=tree_list_6,
                name='T8',
                switches=[V6, V0, V3])
    T9 = Tree(tree_list=tree_list_6,
                name='T9',
                switches=[V6, V0, V4])
    T10 = Tree(tree_list=tree_list_6,
                name='T10',
                switches=[V6, V0, V5])
    
    # R2
    T11 = Tree(tree_list=tree_list_6,
                name='T11',
                switches=[V7, V1, V0])
    T12 = Tree(tree_list=tree_list_6,
                name='T12',
                switches=[V7, V1, V2])
    T13 = Tree(tree_list=tree_list_6,
                name='T13',
                switches=[V7, V1, V3])
    T14 = Tree(tree_list=tree_list_6,
                name='T14',
                switches=[V7, V1, V4])
    T15 = Tree(tree_list=tree_list_6,
                name='T15',
                switches=[V7, V1, V5])
    
    # R3
    T16 = Tree(tree_list=tree_list_6,
                name='T16',
                switches=[V8, V2, V0])
    T17 = Tree(tree_list=tree_list_6,
                name='T17',
                switches=[V8, V2, V1])
    T18 = Tree(tree_list=tree_list_6,
                name='T18',
                switches=[V8, V2, V3])
    T19 = Tree(tree_list=tree_list_6,
                name='T19',
                switches=[V8, V2, V4])
    T20 = Tree(tree_list=tree_list_6,
                name='T20',
                switches=[V8, V2, V5])
    
    # R4
    T21 = Tree(tree_list=tree_list_6,
                name='T21',
                switches=[V9, V3, V0])
    T22 = Tree(tree_list=tree_list_6,
                name='T22',
                switches=[V9, V3, V1])
    T23 = Tree(tree_list=tree_list_6,
                name='T23',
                switches=[V9, V3, V2])
    T24 = Tree(tree_list=tree_list_6,
                name='T24',
                switches=[V9, V3, V4])
    T25 = Tree(tree_list=tree_list_6,
                name='T25',
                switches=[V9, V3, V5])
    
    # R5
    T26 = Tree(tree_list=tree_list_6,
                name='T26',
                switches=[V10, V4, V0])
    T27 = Tree(tree_list=tree_list_6,
                name='T27',
                switches=[V10, V4, V1])
    T28 = Tree(tree_list=tree_list_6,
                name='T28',
                switches=[V10, V4, V2])
    T29 = Tree(tree_list=tree_list_6,
                name='T29',
                switches=[V10, V4, V3])
    T30 = Tree(tree_list=tree_list_6,
                name='T30',
                switches=[V10, V4, V5])
    
    # R6
    T31 = Tree(tree_list=tree_list_6,
                name='T31',
                switches=[V11, V5, V0])
    T32 = Tree(tree_list=tree_list_6,
                name='T32',
                switches=[V11, V5, V1])
    T33 = Tree(tree_list=tree_list_6,
                name='T33',
                switches=[V11, V5, V2])
    T34 = Tree(tree_list=tree_list_6,
                name='T34',
                switches=[V11, V5, V3])
    T35 = Tree(tree_list=tree_list_6,
                name='T35',
                switches=[V11, V5, V4])
    
    # T36 = Tree(tree_list=["AND",
    #                       Tree.tree_list_EQU(2),
    #                       Tree.tree_list_INF(6),],
    #             name='T36',
    #             switches=[V0, 0] + Vlist)
    
    T36 = Tree(tree_list=Tree.tree_list_INF(6),
                name='T36',
                switches=Vlist)
    
    dy = 2.1
    dx = 1.9
    ey = 0.7
    ex = 3.5
    ay = 1.4
    ey0 = 0.5
    
    cx0 = 7*dx+ex
    
    R0 = Room(name='R0',
                position=[0*dx, -ay-ey0, cx0, ey0],
                switches_list=[])
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[1*dx, 4*dy, ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[6*dx, 4*dy, ex, ey],
                switches_list=Slist_4)
    R5 = Room(name='R5',
                position=[7*dx, 2*dy, ex, ey],
                switches_list=Slist_5)
    R6 = Room(name='R6',
                position=[6*dx, 0*dy, ex, ey],
                switches_list=Slist_6)
    RE = Room(name='RE',
              position=[cx0/2-ex/2, 4*dy+ey, ex, ey],
              is_exit=True)
    
    rp = 0.3
    rp6 = 0.35
    
    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[(dx+ex/2)/cx0, 1/2])
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R2,
                relative_departure_coordinates=[ex/4/cx0, 1/2],
                relative_position=0.6)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=R3,
                relative_position=0.125)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R0,
                room_arrival=R4,
                relative_position=0.125)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R0,
                room_arrival=R5,
                relative_departure_coordinates=[(cx0-ex/4)/cx0, 1/2],
                relative_position=0.6)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R0,
                room_arrival=R6,
                relative_departure_coordinates=[(6*dx+ex/2)/cx0, 1/2])
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R1,
                room_arrival=R2,
                relative_position=rp6)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R1,
                room_arrival=R3,
                relative_position=rp)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R1,
                room_arrival=R4,
                relative_position=rp)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R1,
                room_arrival=R5,
                relative_position=rp)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R1,
                room_arrival=R6,
                relative_position=rp)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R2,
                room_arrival=R1,
                relative_position=rp)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R2,
                room_arrival=R3,
                relative_position=rp)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R2,
                room_arrival=R4,
                relative_position=rp)
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R2,
                room_arrival=R5,
                relative_position=rp)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R2,
                room_arrival=R6,
                relative_position=rp)
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R3,
                room_arrival=R1,
                relative_position=rp)
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R3,
                room_arrival=R2,
                relative_position=rp6)
    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=R3,
                room_arrival=R4,
                relative_position=rp)
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R3,
                room_arrival=R5,
                relative_position=rp)
    D20 = Door(two_way=False,
                tree=T20,
                name='D20',
                room_departure=R3,
                room_arrival=R6,
                relative_position=rp)
    D21 = Door(two_way=False,
                tree=T21,
                name='D21',
                room_departure=R4,
                room_arrival=R1,
                relative_position=rp)
    D22 = Door(two_way=False,
                tree=T22,
                name='D22',
                room_departure=R4,
                room_arrival=R2,
                relative_position=rp)
    D23 = Door(two_way=False,
                tree=T23,
                name='D23',
                room_departure=R4,
                room_arrival=R3,
                relative_position=rp)
    D24 = Door(two_way=False,
                tree=T24,
                name='D24',
                room_departure=R4,
                room_arrival=R5,
                relative_position=rp6)
    D25 = Door(two_way=False,
                tree=T25,
                name='D25',
                room_departure=R4,
                room_arrival=R6,
                relative_position=rp)
    D26 = Door(two_way=False,
                tree=T26,
                name='D26',
                room_departure=R5,
                room_arrival=R1,
                relative_position=rp)
    D27 = Door(two_way=False,
                tree=T27,
                name='D27',
                room_departure=R5,
                room_arrival=R2,
                relative_position=rp)
    D28 = Door(two_way=False,
                tree=T28,
                name='D28',
                room_departure=R5,
                room_arrival=R3,
                relative_position=rp)
    D29 = Door(two_way=False,
                tree=T29,
                name='D29',
                room_departure=R5,
                room_arrival=R4,
                relative_position=rp)
    D30 = Door(two_way=False,
                tree=T30,
                name='D30',
                room_departure=R5,
                room_arrival=R6,
                relative_position=rp)
    D31 = Door(two_way=False,
                tree=T31,
                name='D31',
                room_departure=R6,
                room_arrival=R1,
                relative_position=rp)
    D32 = Door(two_way=False,
                tree=T32,
                name='D32',
                room_departure=R6,
                room_arrival=R2,
                relative_position=rp)
    D33 = Door(two_way=False,
                tree=T33,
                name='D33',
                room_departure=R6,
                room_arrival=R3,
                relative_position=rp)
    D34 = Door(two_way=False,
                tree=T34,
                name='D34',
                room_departure=R6,
                room_arrival=R4,
                relative_position=rp)
    D35 = Door(two_way=False,
                tree=T35,
                name='D35',
                room_departure=R6,
                room_arrival=R5,
                relative_position=rp6)
    D36 = Door(two_way=False,
                tree=T36,
                name='D36',
                room_departure=R0,
                room_arrival=RE,
                relative_position=0.575)
    
    hu = 0.6
    lcolor = Level_color(background_color=Color.color_hls(hu, li=0.7, sa=0.3),
                         room_color=Color.color_hls(hu, li=0.4, sa=0.4),
                         letters_color=Color.BLACK,
                         contour_color=Color.color_hls(hu=0.12, li=0.4, sa=0.4),
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.color_hls(hu=0.12, li=0.4, sa=0.4))
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5,
                             D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30, D31, D32, D33, D34, D35, D36],
                 fastest_solution=None,
                 level_color=lcolor,
                 name='Cycle sort',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level
