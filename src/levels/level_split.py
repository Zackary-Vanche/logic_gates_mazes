from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
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
    S23 = Switch(name='S23')
    S24 = Switch(name='S24')
    S25 = Switch(name='S25')
    S26 = Switch(name='S26')
    S27 = Switch(name='S27')
    S28 = Switch(name='S28')
    S29 = Switch(name='S29')
    S30 = Switch(name='S30')
    S31 = Switch(name='S31')
    S32 = Switch(name='S32')
    S33 = Switch(name='S33')
    S34 = Switch(name='S34')
    S35 = Switch(name='S35')
    S36 = Switch(name='S36')
    S37 = Switch(name='S37')
    S38 = Switch(name='S38')
    S39 = Switch(name='S39')
    S40 = Switch(name='S40')
    S41 = Switch(name='S41')
    S42 = Switch(name='S42')
    S43 = Switch(name='S43')
    S44 = Switch(name='S44')
    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    Slist_3 = [S9, S10, S11]
    Slist_4 = [S12, S13, S14]
    Slist_5 = [S15, S16, S17]
    Slist_6 = [S18, S19, S20]
    Slist_7 = [S21, S22, S23]
    Slist_8 = [S24, S25, S26]
    Slist_9 = [S27, S28, S29]
    Slist_10 = [S30, S31, S32]
    Slist_11 = [S33, S34, S35]
    Slist_12 = [S36, S37, S38]
    Slist_13 = [S39, S40, S41]
    Slist_14 = [S42, S43, S44]
    
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
    V9 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_9)),
          name='V9',
          switches=Slist_9)
    V10 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_10)),
          name='V10',
          switches=Slist_10)
    V11 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_11)),
          name='V11',
          switches=Slist_11)
    V12 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_12)),
          name='V12',
          switches=Slist_12)
    V13 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_13)),
          name='V13',
          switches=Slist_13)
    V14 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_14)),
          name='V14',
          switches=Slist_14)
    
    Vlist = [V5, V6,
             V7, V8,
             V9, V10,
             V11, V12,
             V13, V14]
    
    for i in range(len(Vlist)):
        Va = Vlist[i]
        Vlist.append(Tree(tree_list=["SUM"] + [["PROD", [None], Tree.tree_list_EQU(2)]]*5,
                          name=f'V{i+15}',
                          switches=[V0, Va, 0,
                                    V1, Va, 1,
                                    V2, Va, 2,
                                    V3, Va, 3,
                                    V4, Va, 4],
                          cut_expression_depth_1=True))
    
    V_edges_list = []
    for i in range(len(Vlist)//2):
        Va = Vlist[2*i]
        Vb = Vlist[2*i+1]
        V_edges_list.append(Tree(tree_list=["SUM",
                                            Tree.tree_list_MAX(2),
                                            ["PROD",
                                             [None],
                                             Tree.tree_list_MIN(2)]],
                                  name=f'V{26+i}',
                                  switches=[Va, Vb, 4, Va, Vb]))
        
    V36 = Tree(tree_list=["DIFF", ["SUM"]+[Tree.tree_list_EQU(2)]*10, [None], [None]],
          name='V36',
          switches=[V5, 0, V6, 0,
                    V7, 0, V8, 0,
                    V9, 0, V10, 0,
                    V11, 0, V12, 0,
                    V13, 0, V14, 0,
                    1, 3,])
    
    V37 = Tree(tree_list=["DIFF", ["SUM"]+[Tree.tree_list_EQU(2)]*10, [None], [None]],
          name='V37',
          switches=[V5, 1, V6, 1,
                    V7, 1, V8, 1,
                    V9, 1, V10, 1,
                    V11, 1, V12, 1,
                    V13, 1, V14, 1,
                    1, 3,])
    
    V38 = Tree(tree_list=Tree.tree_list_AND(2),
          name='V38',
          switches=[V36, V37])

    T0 = Tree(tree_list=Tree.tree_list_INF(2),
                name='T0',
                switches=[V0, 5])
    T1 = Tree(tree_list=["AND", Tree.tree_list_DIFF(2), Tree.tree_list_INF(2)],
                name='T1',
                switches=[V0, V1, V1, 5])
    T2 = Tree(tree_list=["AND", Tree.tree_list_DIFF(3), Tree.tree_list_INF(2)],
                name='T2',
                switches=[V0, V1, V2, V2, 5])
    T3 = Tree(tree_list=["AND", Tree.tree_list_DIFF(4), Tree.tree_list_INF(2)],
                name='T3',
                switches=[V0, V1, V2, V3, V3, 5])
    T4 = Tree(tree_list=["AND", Tree.tree_list_DIFF(5), Tree.tree_list_INF(2)],
                name='T4',
                switches=[V0, V1, V2, V3, V4, V4, 5])
    
    T5 = Tree(tree_list=["AND",
                         Tree.tree_list_INF(3),
                         Tree.tree_list_DIFF(2)],
                name='T5',
                switches=[V5, V6, 5]+V_edges_list[:1]+V_edges_list[5:6],
                cut_expression_depth_1=True)
    T6 = Tree(tree_list=["AND",
                         Tree.tree_list_INF(3),
                         Tree.tree_list_DIFF(4),
                         Tree.tree_list_INF(2)],
                name='T6',
                switches=[V7, V8, 5]+V_edges_list[:2]+V_edges_list[5:7]+V_edges_list[:2],
                cut_expression_depth_1=True)
    T7 = Tree(tree_list=["AND",
                         Tree.tree_list_INF(3),
                         Tree.tree_list_DIFF(6),
                         Tree.tree_list_INF(3)],
                name='T7',
                switches=[V9, V10, 5]+V_edges_list[:3]+V_edges_list[5:8]+V_edges_list[:3],
                cut_expression_depth_1=True)
    T8 = Tree(tree_list=["AND",
                         Tree.tree_list_INF(3),
                         Tree.tree_list_DIFF(8),
                         Tree.tree_list_INF(4)],
                name='T8',
                switches=[V11, V12, 5]+V_edges_list[:4]+V_edges_list[5:9]+V_edges_list[:4],
                cut_expression_depth_1=True)
    T9 = Tree(tree_list=["AND",
                         Tree.tree_list_INF(3),
                         Tree.tree_list_DIFF(len(V_edges_list)),
                         Tree.tree_list_INF(5),
                         [None]],
                name='T9',
                switches=[V13, V14, 5]+V_edges_list+V_edges_list[:5]+[V38],
                cut_expression_depth_1=True)

    dx = 1
    dy = 1.5
    ex = 0.6
    ey = 1
    ay = 0.2
    by = 0.3

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[1*dx, 0*dy-ay, ex, ey],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[2*dx, 0*dy-by, ex, ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[3*dx, 0*dy-ay, ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[4*dx, 0*dy, ex, ey],
                switches_list=Slist_4)
    
    R5 = Room(name='R5',
                position=[4*dx, 1*dy, ex, ey],
                switches_list=Slist_5+Slist_6)
    R6 = Room(name='R6',
                position=[3*dx, 1*dy+ay, ex, ey],
                switches_list=Slist_7+Slist_8)
    R7 = Room(name='R7',
                position=[2*dx, 1*dy+by, ex, ey],
                switches_list=Slist_9+Slist_10)
    R8 = Room(name='R8',
                position=[1*dx, 1*dy+ay, ex, ey],
                switches_list=Slist_11+Slist_12)
    R9 = Room(name='R9',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=Slist_13+Slist_14)
    RE = Room(name='RE',
              position=[2*dx, 0.5*dy, ex, ey],
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
                room_arrival=R5)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R5,
                room_arrival=R6)
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
                room_arrival=R9)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R9,
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 0.1])
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9,],
                 fastest_solution="S0 D0 S4 D1 S8 D2 S9 S10 D3 D4 S18 D5 S25 D6 S27 S30 S31 D7 S34 S38 D8 S39 S40 S44 D9",
                 level_color=get_color(),
                 name='Split',
                 keep_proportions=True,
                 door_window_size=395)
    
    return level

def get_color():
    hu = 0.15+1/3
    lcolor = Levels_colors_list.FROM_HUE(hu, sa=0.4, li=0.2)
    lcolor.background_color = Color.color_hls(hu, sa=0.4, li=0.15)
    lcolor.contour_color = Color.color_hls(hu, sa=1, li=0.4)
    return lcolor