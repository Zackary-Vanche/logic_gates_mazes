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

    Slist_0 = [S0, S1, S2, S3]
    Slist_1 = [S4, S5, S6, S7]
    Slist_2 = [S8, S9, S10, S11]
    Slist_3 = [S12, S13, S14, S15]
    Slist_4 = [S16, S17, S18, S19]
    Slist_5 = [S20, S21, S22, S23]
    Slist_6 = [S24, S25, S26, S27]
    Slist_7 = [S28, S29, S30, S31]
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
    
    Vlist = [V0, V1, V2, V3, V4, V5, V6, V7]
    Vdict = {'D':V0, # 7
             'E':V1, # 5
             'M':V2, # 1
             'N':V3, # 6
             'O':V4, # 0
             'R':V5, # 8
             'S':V6, # 9
             'Y':V7} # 2
    
    def get_V_tree(i):
        tree_list_aux = ["PROD", [None], ["POW", [None], [None]]]
        return ["SUM"] + [tree_list_aux]*i
    
    V8 = Tree(tree_list=get_V_tree(4),
              name='V8',
              switches=[Vdict['S'], 10, 3, 
                        Vdict['E'], 10, 2,
                        Vdict['N'], 10, 1,
                        Vdict['D'], 10, 0])
    V9 = Tree(tree_list=get_V_tree(4),
              name='V9',
              switches=[Vdict['M'], 10, 3, 
                        Vdict['O'], 10, 2,
                        Vdict['R'], 10, 1,
                        Vdict['E'], 10, 0])
    V10 = Tree(tree_list=get_V_tree(5),
               name='V10',
               switches=[Vdict['M'], 10, 4, 
                         Vdict['O'], 10, 3,
                         Vdict['N'], 10, 2,
                         Vdict['E'], 10, 1,
                         Vdict['Y'], 10, 0])
    V11 = Tree(tree_list=["EQU", Tree.tree_list_SUM(2), [None]],
          name='V11',
          switches=[V8, V9, V10]) 

    def get_tree(i):
        if i == 7:
            return Tree(tree_list=["AND",
                                   Tree.tree_list_INF(2),
                                   Tree.tree_list_DIFF(i+1),
                                   [None]],
                        name=f'T{i}',
                        switches=[Vlist[i], 10]+Vlist[:i+1]+[V11])
        elif i >= 1:
            return Tree(tree_list=["AND",
                                   Tree.tree_list_INF(2),
                                   Tree.tree_list_DIFF(i+1)],
                        name=f'T{i}',
                        switches=[Vlist[i], 10]+Vlist[:i+1])
        else:
            return Tree(tree_list=Tree.tree_list_INF(2),
                        name=f'T{i}',
                        switches=[Vlist[i], 10])
    T0 = get_tree(0)
    T1 = get_tree(1)
    T2 = get_tree(2)
    T3 = get_tree(3)
    T4 = get_tree(4)
    T5 = get_tree(5)
    T6 = get_tree(6)
    T7 = get_tree(7)

    dx = 0.85
    dy = 1
    ex = 0.5
    ey = 0.5
    
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
                position=[0*dx, 1*dy, ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=Slist_4)
    R5 = Room(name='R5',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=Slist_5)
    R6 = Room(name='R6',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=Slist_6)
    R7 = Room(name='R7',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=Slist_7)
    RE = Room(name='RE',
              position=[2*dx, 2*dy, ex, ey],
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
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7],
                 fastest_solution="S0 S1 S2 D0 S4 S6 D1 S8 D2 S13 S14 D3 D4 S23 D5 S24 S27 D6 S29 D7",
                 level_color=get_color(),
                 name='SEND + MORE = MONEY',
                 keep_proportions=True,
                 door_window_size=500)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.4, sa=0.4, li=0.4)
    lcolor.surrounding_color = Color.color_hls(hu=0.16, sa=0.9, li=0.6)
    lcolor.contour_color = Color.color_hls(hu=0.16, sa=0.9, li=0.6)
    return lcolor 