from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice

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
    
    S12 = Switch(name='S12', value=rd_choice([0, 1]))
    S13 = Switch(name='S13', value=rd_choice([0, 1]))
    S14 = Switch(name='S14', value=rd_choice([0, 1]))
    S15 = Switch(name='S15', value=rd_choice([0, 1]))
    S16 = Switch(name='S16', value=rd_choice([0, 1]))
    S17 = Switch(name='S17', value=rd_choice([0, 1]))
    S18 = Switch(name='S18', value=rd_choice([0, 1]))
    S19 = Switch(name='S19', value=rd_choice([0, 1]))
    S20 = Switch(name='S20', value=rd_choice([0, 1]))
    S21 = Switch(name='S21', value=rd_choice([0, 1]))
    S22 = Switch(name='S22', value=rd_choice([0, 1]))
    S23 = Switch(name='S23', value=rd_choice([0, 1]))
    S24 = Switch(name='S24', value=rd_choice([0, 1]))
    S25 = Switch(name='S25', value=rd_choice([0, 1]))
    S26 = Switch(name='S26', value=rd_choice([0, 1]))
    S27 = Switch(name='S27', value=rd_choice([0, 1]))

    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    Slist_3 = [S9, S10, S11]
    Slist_4 = [S12, S13]
    Slist_5 = [S14, S15]
    Slist_6 = [S16, S17]
    Slist_7 = [S18, S19]
    Slist_8 = [S20, S21]
    Slist_9 = [S22, S23]
    Slist_10 = [S24, S25]
    Slist_11 = [S26, S27]
    
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

    Vlist = [V4, V5, V6, V7, V8, V9, V10, V11]
    
    tree_list_aux = ["EQU", [None]] + [["SUM"] + [Tree.tree_list_EQU(2)]*8]        
    tree_list_V12 = ["AND"] + [tree_list_aux]*4
    
    Slist_V12 = []
    for i in range(4):
        Slist_V12.append([V0, V1, V2, V3][i])
        for V in Vlist:
            Slist_V12.append(V)
            Slist_V12.append(i)
    
    V12 = Tree(tree_list=tree_list_V12,
               name='V12',
               switches=Slist_V12,
               cut_expression_depth_1=True)

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[V12])
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[1])
    T2 = Tree(tree_list=Tree.tree_list_INFOREQU(2),
                name='T2',
                switches=[V4, V5])
    T3 = Tree(tree_list=Tree.tree_list_INFOREQU(2),
                name='T3',
                switches=[V5, V6])
    T4 = Tree(tree_list=Tree.tree_list_INFOREQU(2),
                name='T4',
                switches=[V6, V7])
    T5 = Tree(tree_list=Tree.tree_list_INFOREQU(2),
                name='T5',
                switches=[V7, V8])
    T6 = Tree(tree_list=Tree.tree_list_INFOREQU(2),
                name='T6',
                switches=[V8, V9])
    T7 = Tree(tree_list=Tree.tree_list_INFOREQU(2),
                name='T7',
                switches=[V9, V10])
    T8 = Tree(tree_list=["AND", Tree.tree_list_INFOREQU(2), [None]],
                name='T8',
                switches=[V10, V11, V12])

    R0 = Room(name='R0',
                position=[2, 3.25, 3, 4],
                switches_list=Slist_0+Slist_1+Slist_2+Slist_3)
    R1 = Room(name='R1',
                position=[3, 0, 1, 2],
                switches_list=Slist_4)
    R2 = Room(name='R2',
                position=[0, 1, 1, 2],
                switches_list=Slist_5)
    R3 = Room(name='R3',
                position=[-1.5, 4, 1, 2],
                switches_list=Slist_6)
    R4 = Room(name='R4',
                position=[0, 7, 1, 2],
                switches_list=Slist_7)
    R5 = Room(name='R5',
                position=[3, 8, 1, 2],
                switches_list=Slist_8)
    R6 = Room(name='R6',
                position=[6, 7, 1, 2],
                switches_list=Slist_9)
    R7 = Room(name='R7',
                position=[7.5, 4, 1, 2],
                switches_list=Slist_10)
    R8 = Room(name='R8',
                position=[6, 1, 1, 2],
                switches_list=Slist_11)
    RE = Room(name='RE',
              position=[5.5, -1, 2, 0.75],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1/2, 0],
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
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[1/2, 1])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Pigeonhole sort',
                 keep_proportions=True,
                 door_window_size=550,
                 random=True)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.1, sa=0.3, li=0.6)
    lcolor.room_color = Color.color_hls(hu=0.6, sa=0.4, li=0.4)
    return lcolor