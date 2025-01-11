from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Level_color import Level_color
from Color import Color

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
    Slist_10 = [S20, S21]
    Slist_11 = [S22, S23]
    Slist_12 = [S24, S25]
    Slist_13 = [S26, S27]
    Slist_14 = [S28, S29]
    Slist_15 = [S30, S31]
    Slist_16 = [S32, S33]
    Slist_17 = [S34, S35]
    Slist_18 = [S36, S37]
    Slist_19 = [S38, S39, S40]
    
    Slist_20 = Slist_0+Slist_1+Slist_2+Slist_3
    Slist_21 = Slist_4+Slist_5+Slist_6+Slist_7
    Slist_22 = Slist_8+Slist_9+Slist_10+Slist_11
    Slist_23 = Slist_12+Slist_13+Slist_14+Slist_15
    Slist_24 = Slist_16+Slist_17+Slist_18+Slist_19
    
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
    V15 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_15)),
          name='V15',
          switches=Slist_15)
    V16 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_16)),
          name='V16',
          switches=Slist_16)
    V17 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_17)),
          name='V17',
          switches=Slist_17)
    V18 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_18)),
          name='V18',
          switches=Slist_18)
    V19 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_19)),
          name='V19',
          switches=Slist_19)
    V20 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_20)),
          name='V20',
          switches=Slist_20)
    V21 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_21)),
          name='V21',
          switches=Slist_21)
    V22 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_22)),
          name='V22',
          switches=Slist_22)
    V23 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_23)),
          name='V23',
          switches=Slist_23)
    V24 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_24)),
          name='V24',
          switches=Slist_24)
    
    tree_list_0 = ["AND",
                   Tree.tree_list_INFOREQU(4),
                   ["EQU", Tree.tree_list_SUM(4), [None]]]
    tree_list_1 = tree_list_0 + [Tree.tree_list_INF(2)]
    
    b = False

    T0 = Tree(tree_list=tree_list_0,
                name='T0',
                switches=[V0, V1, V2, V3]*2+[4],
                cut_expression_depth_1=b)
    T1 = Tree(tree_list=tree_list_1,
                name='T1',
                switches=[V4, V5, V6, V7]*2+[4, V20, V21],
                cut_expression_depth_1=b)
    T2 = Tree(tree_list=tree_list_1,
                name='T2',
                switches=[V8, V9, V10, V11]*2+[4, V21, V22],
                cut_expression_depth_1=b)
    T3 = Tree(tree_list=tree_list_1,
                name='T3',
                switches=[V12, V13, V14, V15]*2+[4, V22, V23],
                cut_expression_depth_1=b)
    T4 = Tree(tree_list=tree_list_1,
                name='T4',
                switches=[V16, V17, V18, V19]*2+[4, V23, V24],
                cut_expression_depth_1=b)

    dx = 4
    dy = 2
    ex = 4
    ey = 2

    R0 = Room(name='R0',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=Slist_20)
    R1 = Room(name='R1',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=Slist_21)
    R2 = Room(name='R2',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=Slist_22)
    R3 = Room(name='R3',
                position=[1*dx, 3*dy, ex, ey],
                switches_list=Slist_23)
    R4 = Room(name='R4',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=Slist_24)
    RE = Room(name='RE',
              position=[2*dx, 0*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[1, 0])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[0, 0])
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[0, 1])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4,
                relative_departure_coordinates=[1, 1],
                relative_arrival_coordinates=[1, 1])
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=RE,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[1, 1/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4],
                 fastest_solution="S0 S2 S4 S6 D0 S10 S12 S15 D1 S21 S23 D2 S28 S30 S31 D3 S40 D4",
                 level_color=get_color(),
                 name='Integer partition',
                 keep_proportions=True,
                 door_window_size=350)
    
    return level
    
def get_color():
    hu = 0.25
    sa = 0.6
    lcolor = Level_color(background_color=Color.color_hls(hu, 0.4, sa),
                         room_color=Color.color_hls(hu, 0.15, 0.8 * sa),
                         letters_color=Color.BLACK,
                         contour_color=Color.color_hls(hu=0.1, li=0.7, sa=1),
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.color_hls(hu=0.1, li=0.8, sa=1))
    return lcolor    