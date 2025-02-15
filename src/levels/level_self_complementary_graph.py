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
    Slist_0 = [S0, S1]
    Slist_1 = [S2, S3]
    Slist_2 = [S4, S5]
    Slist_3 = [S6, S7]
    Slist_4 = [S8, S9]
    Slist_5 = [S10, S11]
    Slist_6 = [S12, S13]
    Slist_7 = [S14, S15]
    Slist_8 = [S16, S17]
    Slist_9 = [S18, S19]
    
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
    
    Vlist = [V4, V5,
             V6, V7,
             V8, V9,]
    
    for i in range(len(Vlist)):
        Va = Vlist[i]
        Vlist.append(Tree(tree_list=["SUM"] + [["PROD", [None], Tree.tree_list_EQU(2)]]*4,
                          name=f'V{i+10}',
                          switches=[V0, Va, 0,
                                    V1, Va, 1,
                                    V2, Va, 2,
                                    V3, Va, 3,]))
    
    V_edges_list = []
    for i in range(len(Vlist)//2):
        Va = Vlist[2*i]
        Vb = Vlist[2*i+1]
        V_edges_list.append(Tree(tree_list=["SUM",
                                            Tree.tree_list_MAX(2),
                                            ["PROD",
                                             [None],
                                             Tree.tree_list_MIN(2)]],
                                  name=f'V{16+i}',
                                  switches=[Va, Vb, 4, Va, Vb]))

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[1])
    T1 = Tree(tree_list=Tree.tree_list_DIFF(2),
                name='T1',
                switches=[V0, V1])
    T2 = Tree(tree_list=Tree.tree_list_DIFF(3),
                name='T2',
                switches=[V0, V1, V2])
    T3 = Tree(tree_list=Tree.tree_list_DIFF(4),
                name='T3',
                switches=[V0, V1, V2, V3])
    T4 = Tree(tree_list=Tree.tree_list_INF(2),
                name='T4',
                switches=[V4, V5])
    T5 = Tree(tree_list=Tree.tree_list_INF(2),
                name='T5',
                switches=[V6, V7])
    T6 = Tree(tree_list=["AND",
                         Tree.tree_list_INF(2),
                         Tree.tree_list_DIFF(len(V_edges_list)),
                         Tree.tree_list_INF(4),],
                name='T6',
                switches=[V8, V9]+V_edges_list+V_edges_list[:4],
                cut_expression_depth_1=True)

    dx = 1
    dy = 1
    ex = 0.6
    ey = 0.6
    epsilony = 0.3

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[1*dx, 0*dy-epsilony, ex, ey],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[2*dx, 0*dy-epsilony, ex, ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[3*dx, 0*dy, ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[3*dx, 1*dy, ex, ey],
                switches_list=Slist_4+Slist_5)
    R5 = Room(name='R5',
                position=[2*dx, 1*dy+epsilony, ex, ey],
                switches_list=Slist_6+Slist_7)
    R6 = Room(name='R6',
                position=[1*dx, 1*dy+epsilony, ex, ey],
                switches_list=Slist_8+Slist_9)
    RE = Room(name='RE',
              position=[0*dx, 1*dy, ex, ey],
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
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution="S0 D0 S3 D1 S4 S5 D2 D3 S11 D4 S14 S15 D5 S16 S19 D6",
                 level_color=get_color(),
                 name='Self-complementary graph',
                 keep_proportions=True,
                 door_window_size=420)
    
    return level

def get_color():
    hu = 0.15
    lcolor = Levels_colors_list.FROM_HUE(hu, sa=0.4, li=0.2)
    lcolor.background_color = Color.color_hls(hu, sa=0.4, li=0.15)
    lcolor.contour_color = Color.color_hls(hu, sa=1, li=0.4)
    return lcolor