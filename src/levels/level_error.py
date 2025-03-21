from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from os.path import exists as os_path_exists

current_folder = '/'.join(__file__.split('\\')[:-1])

def f(): 
    
    v = 1

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')

    S3 = Switch(name='S3', value=v)
    S4 = Switch(name='S4', value=v)
    S5 = Switch(name='S5')

    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')

    S9 = Switch(name='S9', value=v)
    S10 = Switch(name='S10')
    S11 = Switch(name='S11', value=v)

    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')

    S15 = Switch(name='S15')
    S16 = Switch(name='S16', value=v)
    S17 = Switch(name='S17', value=v)

    S18 = Switch(name='S18')
    S19 = Switch(name='S19')
    S20 = Switch(name='S20')

    S21 = Switch(name='S21', value=v)
    S22 = Switch(name='S22', value=v)
    S23 = Switch(name='S23', value=v)

    S24 = Switch(name='S24')
    S25 = Switch(name='S25')
    S26 = Switch(name='S26')

    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    Slist_3 = [S9, S10, S11]
    Slist_4 = [S12, S13, S14]
    Slist_5 = [S15, S16, S17]
    Slist_6 = [S18, S19, S20]
    Slist_7 = [S21, S22, S23]
    Slist_8 = [S24, S25, S26]
    
    tree_list_4thD = ['E'] + [[None]]*24

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
    V9 = Tree(tree_list=tree_list_4thD,
              name='V9',
              switches=[S0, S1, S2,
                        S3, S4, S5,
                        S6, S7, S8,
                        S9, S10, S11,
                        S12, S13, S14,
                        S15, S16, S17,
                        S18, S19, S20,
                        S21, S22, S23,])
    
    def tree_list_IN_BIN(n):
        return ['IN', [None]] + [[None]]*n
    
    tree_list_EQU_BIN = ['EQU', [None], [None]]
    
    tree_list_0 = ['AND',
                   tree_list_IN_BIN(3),
                   [None]]
    tree_list_1 = ['AND', tree_list_IN_BIN(3), tree_list_EQU_BIN]
    tree_list_8 = ['AND', tree_list_IN_BIN(1), tree_list_EQU_BIN]

    T0 = Tree(tree_list=tree_list_0,
                name='T0',
                switches=[V8, 1, 2, 3, V9],
                cut_expression=False)
    T1 = Tree(tree_list=tree_list_1,
                name='T1',
                switches=[V8, 1, 2, 3,
                          V0, V1])
    T2 = Tree(tree_list=tree_list_0,
                name='T2',
                switches=[V8, 1, 4, 5, V9],
                cut_expression=False,
                cut_expression_separator='~')
    T3 = Tree(tree_list=tree_list_1,
                name='T3',
                switches=[V8, 1, 4, 5,
                          V2, V3])
    T4 = Tree(tree_list=tree_list_0,
                name='T4',
                switches=[V8, 2, 4, 6, V9],
                cut_expression=False)
    T5 = Tree(tree_list=tree_list_1,
                name='T5',
                switches=[V8, 2, 4, 6,
                          V4, V5])
    T6 = Tree(tree_list=tree_list_0,
                name='T6',
                switches=[V8, 3, 5, 6, V9],
                cut_expression=False)
    T7 = Tree(tree_list=tree_list_1,
                name='T7',
                switches=[V8, 3, 5, 6,
                          V6, V7])
    T8 = Tree(tree_list=tree_list_8,
                name='T8',
                switches=[V8, 1,
                          V1, V3])
    T9 = Tree(tree_list=tree_list_8,
                name='T9',
                switches=[V8, 2,
                          V1, V5])
    T10 = Tree(tree_list=tree_list_8,
                name='T10',
                switches=[V8, 3,
                          V1, V7])
    T11 = Tree(tree_list=tree_list_8,
                name='T11',
                switches=[V8, 4,
                          V3, V5])
    T12 = Tree(tree_list=tree_list_8,
                name='T12',
                switches=[V8, 5,
                          V3, V7])
    T13 = Tree(tree_list=tree_list_8,
                name='T13',
                switches=[V8, 6,
                          V5, V7])
    T14 = Tree(tree_list=[None],
                name='T14',
                switches=[1])
    filename = current_folder+'/Error_random_exits.txt'
    if os_path_exists(filename):
        with open(filename, 'r') as fr:
            lines = fr.readlines()
            l = rd_choice(lines)
        T15 = Tree(tree_list=Tree.tree_list_from_str(l),
                    name='T15',
                    switches=[S0, S1, S2,
                              S3, S4, S5,
                              S6, S7, S8,
                              S9, S10, S11,
                              S12, S13, S14,
                              S15, S16, S17,
                              S18, S19, S20,
                              S21, S22, S23,
                              S24, S25, S26])
    else:
        T15 = Tree(tree_list=Tree.tree_list_from_str('TTT'),
                    name='T15',
                    switches=[S24, S25, S26])
    
    ax = 1.75
    ay = 3

    R0 = Room(name='R0',
                position=[1/8*ax, 6*ay, 1.3, 3],
                switches_list=[S24])
    R1 = Room(name='R1',
                position=[9*ax, 4.5*ay, 1.3, 10],
                switches_list=[S25, S26])
    R2 = Room(name='R2',
                position=[2*ax, 8*ay, 6, 1],
                switches_list=[S0, S1, S2])
    R3 = Room(name='R3',
                position=[4*ax, 6.25*ay, 6, 1],
                switches_list=[S3, S4, S5])
    R4 = Room(name='R4',
                position=[0.35*ax, 2*ay, 1, 5],
                switches_list=[S6, S7, S8])
    R5 = Room(name='R5',
                position=[2*ax, 4*ay, 1.3, 5],
                switches_list=[S9, S10, S11])
    R6 = Room(name='R6',
                position=[-1*ax, 0.5*ay, 8, 1],
                switches_list=[S12, S13, S14])
    R7 = Room(name='R7',
                position=[0*ax, 1.5*ay, 7, 1],
                switches_list=[S15, S16, S17])
    R8 = Room(name='R8',
                position=[8*ax, 4.25*ay, 1.3, 5],
                switches_list=[S18, S19, S20])
    R9 = Room(name='R9',
                position=[6*ax, 2*ay, 1.3, 5],
                switches_list=[S21, S22, S23])
    RE = Room(name='RE',
              position=[8*ax, 2*ay, 2, 3],
              is_exit=True)

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R2,
                relative_arrival_coordinates=[0.5/3, 1/2])
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R2,
                room_arrival=R3,
                relative_position=0.4)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=R4,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[1/2, 1])
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R4,
                room_arrival=R5)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R0,
                room_arrival=R6,
                relative_departure_coordinates=[0, 0],
                relative_arrival_coordinates=[0, 1])
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R6,
                room_arrival=R7)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=R8,
                relative_arrival_coordinates=[1/2, 2/3],
                relative_position=0.8)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R8,
                room_arrival=R9)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R3,
                room_arrival=R5,
                relative_departure_coordinates=[0.5/3, 1/2])
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R3,
                room_arrival=R7,
                relative_position=0.35)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R3,
                room_arrival=R9,
                relative_arrival_coordinates=[1/2, 2.5/3])
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R5,
                room_arrival=R7,
                relative_departure_coordinates=[1/2, 0.5/3])
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R5,
                room_arrival=R9,
                relative_position=0.6)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R7,
                room_arrival=R9,
                relative_departure_coordinates=[2.5/3, 1/2])
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 1],
                relative_position=0.7)
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R1,
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[1/2, 1/2],
                relative_position=0.35)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15],#, D15, D16, D17, D18, D19],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Error',
                 keep_proportions=True,
                 door_window_size=450,
                 y_separation=40,
                 random=True)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.21, sa=0.3, li=0.2)