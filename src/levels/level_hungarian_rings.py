from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle
from Color import Color

def level_hungarian_rings():
    
    v_list = [[0, 0, 0],
              [0, 0, 1],
              [0, 1, 0],
              [0, 1, 1],
              [1, 0, 0],
              [1, 0, 1],
              [1, 1, 0],
              [1, 1, 1]]
    rd_shuffle(v_list)

    S0 = Switch(name='S0')

    S1 = Switch(name='S1', value=v_list[0][0])
    S2 = Switch(name='S2', value=v_list[0][1])
    S3 = Switch(name='S3', value=v_list[0][2])

    S4 = Switch(name='S4', value=v_list[1][0])
    S5 = Switch(name='S5', value=v_list[1][1])
    S6 = Switch(name='S6', value=v_list[1][2])

    S7 = Switch(name='S7', value=v_list[2][0])
    S8 = Switch(name='S8', value=v_list[2][1])
    S9 = Switch(name='S9', value=v_list[2][2])

    S10 = Switch(name='S10', value=v_list[3][0])
    S11 = Switch(name='S11', value=v_list[3][1])
    S12 = Switch(name='S12', value=v_list[3][2])

    S13 = Switch(name='S13', value=v_list[4][0])
    S14 = Switch(name='S14', value=v_list[4][1])
    S15 = Switch(name='S15', value=v_list[4][2])

    S16 = Switch(name='S16', value=v_list[5][0])
    S17 = Switch(name='S17', value=v_list[5][1])
    S18 = Switch(name='S18', value=v_list[5][2])

    S19 = Switch(name='S19', value=v_list[6][0])
    S20 = Switch(name='S20', value=v_list[6][1])
    S21 = Switch(name='S21', value=v_list[6][2])

    S22 = Switch(name='S22', value=v_list[7][0])
    S23 = Switch(name='S23', value=v_list[7][1])
    S24 = Switch(name='S24', value=v_list[7][2])
    
    tree_list_EQU_BIN = ['EQU'] + [Tree.tree_list_BIN(3)]*2
    tree_list_1 = ['AND', [None], tree_list_EQU_BIN]
    tree_list_6 = ['AND', Tree.tree_list_not, tree_list_EQU_BIN]

    T0 = Tree(tree_list=[None],
                empty=True,
                name='T0',
                switches=[S0])
    T1 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T1',
                switches=[S0, S1, S2, S3, S4, S5, S6])
    T2 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T2',
                switches=[S0, S4, S5, S6, S7, S8, S9])
    T3 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T3',
                switches=[S0, S7, S8, S9, S19, S20, S21])
    T4 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T4',
                switches=[S0, S19, S20, S21, S22, S23, S24])
    T5 = Tree(tree_list=Tree.tree_list_not,
                empty=True,
                name='T5',
                switches=[S0])
    T6 = Tree(tree_list=tree_list_6,
                empty=True,
                name='T6',
                switches=[S0, S13, S14, S15, S10, S11, S12])
    T7 = Tree(tree_list=tree_list_6,
                empty=True,
                name='T7',
                switches=[S0, S10, S11, S12, S7, S8, S9])
    T8 = Tree(tree_list=tree_list_6,
                empty=True,
                name='T8',
                switches=[S0, S7, S8, S9, S16, S17, S18])
    T9 = Tree(tree_list=tree_list_6,
                empty=True,
                name='T9',
                switches=[S0, S16, S17, S18, S22, S23, S24])
    T10 = Tree(tree_list=['DIFF'] + [Tree.tree_list_BIN(3)]*8,
                empty=True,
                name='T10',
                switches=[S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24],
                cut_expression=True)
    T11 = Tree(tree_list=['AND', [None]] + [['EQU', [None], Tree.tree_list_BIN(3)]]*8,
                empty=True,
                name='T11',
                switches=[S0,
                          0, S1, S2, S3,
                          1, S4, S5, S6,
                          2, S7, S8, S9,
                          3, S10, S11, S12,
                          4, S13, S14, S15,
                          5, S16, S17, S18,
                          6, S19, S20, S21,
                          7, S22, S23, S24,],
                cut_expression=True)

    R0 = Room(name='R0',
                position=[4, 3.25, 1, 0.5],
                switches_list=[S0])
    R1 = Room(name='R1',
                position=[2, 3, 0.5, 2],
                switches_list=[S1, S2, S3])
    R2 = Room(name='R2',
                position=[2, 8, 0.5, 2],
                switches_list=[S4, S5, S6])
    R3 = Room(name='R3',
                position=[3, 8, 3, 0.5],
                switches_list=[S7, S8, S9])
    R4 = Room(name='R4',
                position=[6.5, 8, 0.5, 2],
                switches_list=[S10, S11, S12])
    R5 = Room(name='R5',
                position=[6.5, 3, 0.5, 2],
                switches_list=[S13, S14, S15])
    R6 = Room(name='R6',
                position=[2.5, 5, 0.5, 3],
                switches_list=[S16, S17, S18])
    R7 = Room(name='R7',
                position=[6, 5, 0.5, 3],
                switches_list=[S19, S20, S21])
    R8 = Room(name='R8',
                position=[3, 4.5, 3, 0.5],
                switches_list=[S22, S23, S24])
    RE = Room(name='RE',
              position=[4, 2, 1, 0.5],
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
                room_arrival=R3,
                relative_departure_coordinates=[1/2, 5.5/6])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R7)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R7,
                room_arrival=R8)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R0,
                room_arrival=R5)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R5,
                room_arrival=R4)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R4,
                room_arrival=R3,
                relative_departure_coordinates=[1/2, 5.5/6])
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R3,
                room_arrival=R6)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R6,
                room_arrival=R8)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R8,
                room_arrival=R0)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R0,
                room_arrival=RE)
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0.9, sa=1, li=0.35)
    lcolor.background_color = Color.DARK_RED

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11],
                 fastest_solution=None,
                 level_color=lcolor,
                 name='Hungarian_rings',
                 keep_proportions=True,
                 door_window_size=500,
                 random=True)
    
    return level

