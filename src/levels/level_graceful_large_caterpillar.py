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

    Slist_0 = [S0, S1, S2, S3]
    Slist_1 = [S4, S5, S6, S7]
    Slist_2 = [S8, S9, S10, S11]
    Slist_3 = [S12, S13, S14, S15]
    Slist_4 = [S16, S17, S18, S19]
    Slist_5 = [S20, S21, S22, S23]
    Slist_6 = [S24, S25, S26, S27]
    Slist_7 = [S28, S29, S30, S31]
    Slist_8 = [S32, S33, S34, S35]
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
    V7 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_6)),
          name='V7',
          switches=Slist_7)
    V8 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_6)),
          name='V8',
          switches=Slist_8)
    
    tree_list_V = ["SUM", Tree.tree_list_PROD(2), [None]]
    
    V9 = Tree(tree_list=tree_list_V,
          name='V9',
          switches=[2, V0, 1])
    V10 = Tree(tree_list=tree_list_V,
          name='V10',
          switches=[2, V1, 1])
    V11 = Tree(tree_list=tree_list_V,
          name='V11',
          switches=[2, V2, 1])
    V12 = Tree(tree_list=tree_list_V,
          name='V12',
          switches=[2, V3, 1])
    V13 = Tree(tree_list=tree_list_V,
          name='V13',
          switches=[2, V4, 1])
    V14 = Tree(tree_list=tree_list_V,
          name='V14',
          switches=[2, V5, 1])
    V15 = Tree(tree_list=tree_list_V,
          name='V15',
          switches=[2, V6, 1])
    V16 = Tree(tree_list=tree_list_V,
          name='V16',
          switches=[2, V7, 1])
    V17 = Tree(tree_list=tree_list_V,
          name='V17',
          switches=[2, V8, 1])
    
    tree_list_minus = ["SUM", Tree.tree_list_MAX(2), ["MINUS", Tree.tree_list_MIN(2)]]
    
    # 9     10     11
    #   12  13  14
    #15     16     17
    
    V18 = Tree(tree_list=tree_list_minus,
          name='V18',
          switches=[V9, V12]*2)
    V19 = Tree(tree_list=tree_list_minus,
          name='V19',
          switches=[V10, V13]*2)
    V20 = Tree(tree_list=tree_list_minus,
          name='V20',
          switches=[V11, V14]*2)
    V21 = Tree(tree_list=tree_list_minus,
          name='V21',
          switches=[V12, V13]*2)
    V22 = Tree(tree_list=tree_list_minus,
          name='V22',
          switches=[V12, V15]*2)
    V23 = Tree(tree_list=tree_list_minus,
          name='V23',
          switches=[V13, V14]*2)
    V24 = Tree(tree_list=tree_list_minus,
          name='V24',
          switches=[V13, V16]*2)
    V25 = Tree(tree_list=tree_list_minus,
          name='V25',
          switches=[V14, V17]*2)
    
    Vlist_origin = [V0, V1, V2, V3, V4, V5, V6, V7, V8]

    Vlist = [V9, V10, V11, V12, V13, V14, V15, V16, V17,
             V18, V19, V20, V21, V22, V23, V24, V25]

    def get_tree(i):
        if i == 0:
            return Tree(tree_list=Tree.tree_list_INF(2),
                        name=f'T{i}',
                        switches=[Vlist_origin[i], 10])
        if i == 2:
            return Tree(tree_list=["AND", Tree.tree_list_DIFF(i+1), Tree.tree_list_INF(2), Tree.tree_list_INF(2)],
                        name=f'T{i}',
                        switches=Vlist_origin[:i+1] + [Vlist_origin[i], 10, V0, V2])
        if i < 8:
            return Tree(tree_list=["AND", Tree.tree_list_DIFF(i+1), Tree.tree_list_INF(2)],
                        name=f'T{i}',
                        switches=Vlist_origin[:i+1] + [Vlist_origin[i], 10])
        else:
            return Tree(tree_list=Tree.tree_list_EQUSET(2*len(Vlist)),
                        name=f'T{i}',
                        switches=Vlist+[i for i in range(1, len(Vlist)+1)])
        
    T0 = get_tree(0)
    T1 = get_tree(1)
    T2 = get_tree(2)
    T3 = get_tree(3)
    T4 = get_tree(4)
    T5 = get_tree(5)
    T6 = get_tree(6)
    T7 = get_tree(7)
    T8 = get_tree(8)

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5
    
    a = 0.25

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=Slist_4)
    R5 = Room(name='R5',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=Slist_5)
    R6 = Room(name='R6',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=Slist_6)
    R7 = Room(name='R7',
                position=[-ex-a, 1*dy, ex, ey],
                switches_list=Slist_7)
    R8 = Room(name='R8',
                position=[1*dx-ex-a, 1*dy, ex, ey],
                switches_list=Slist_8)
    RE = Room(name='RE',
              position=[2*dx-ex-a, 1*dy, ex, ey],
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
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8],
                 fastest_solution="S0 D0 S4 S5 D1 S9 S10 D2 S15 D3 D4 S20 S22 D5 S25 D6 S30 D7 S32 S33 S34 D8",
                 level_color=get_color(),
                 name='Graceful large caterpillar',
                 keep_proportions=True,
                 door_window_size=345)
    
    return level

def get_color():
    color=Color.color_hls(hu=0.9, li=0.7, sa=0.8)
    lcolor=Levels_colors_list.FROM_HUE(hu=0.9, sa=0.2, li=0.3)
    lcolor.surrounding_color=color
    lcolor.contour_color=color
    return lcolor