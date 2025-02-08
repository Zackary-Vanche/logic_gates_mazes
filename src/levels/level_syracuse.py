from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Level_color import Level_color
from Color import Color

def f(test_solution=False):

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8', value=1)
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')
    S15 = Switch(name='S15')

    SN1 = Switch(name='1', value=1)
    SN2 = Switch(name='2', value=2)
    SN3 = Switch(name='3', value=3)
    
    Slist_0 = [S0, S1, S2, S3,
               S4, S5, S6, S7]
    Slist_1 = [S8, S9, S10, S11,
               S12, S13, S14, S15]

    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_0)),
              name='V0',
              switches=Slist_0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_1)),
              name='V1',
              switches=Slist_1)

    tree_list_0 = ['EQU',
                   [None],
                   [None]]

    tree_list_1 = ['EQU',
                       [None],
                       ['DIV',
                            [None],
                            [None]]]

    tree_list_prod = ['PROD', [None], [None]]
    tree_list_3plus1 = ['SUM', tree_list_prod, [None]]
    tree_list_equ_3plus1 = ['EQU', [None], tree_list_3plus1]
    tree_list_equ_mod = ['EQU', [None], [None]] 
    tree_list_2 = ['AND', tree_list_equ_mod, tree_list_equ_3plus1]

    tree_list_3 = ['EQU', [None], [None], [None]]

    T0 = Tree(tree_list=tree_list_0,
              name='T0',
              switches = [V0,
                          V1])
    T1 = Tree(tree_list=tree_list_1,
              name='T1',
              switches = [V0,
                          V1,
                          SN2])
    T2 = Tree(tree_list=tree_list_2,
              name='T2',
              switches = [S8,
                          SN1,
                          V0,
                          SN3,
                          V1,
                          SN1],
              cut_expression=True,
              cut_expression_separator=']')
    T3 = Tree(tree_list=tree_list_3,
              name='T3',
              switches = [V0,
                          V1,
                          228])

    R0 = Room(name='R0',
              position = [0, 0, 4, 2],
              switches_list = Slist_0)
    R1 = Room(name='R1',
              position = [0, 4, 4, 2],
              switches_list = Slist_1)
    RE = Room(name='RE',
              position=[0, 8, 4, 1],
              is_exit=True)   # E pour exit ou end

    p = 0.17

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[p, 1/2],
              relative_arrival_coordinates=[p, 1/2])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R0,
              relative_departure_coordinates=[1-p, 1/2],
              relative_arrival_coordinates=[1-p, 1/2])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R1,
              room_arrival=R0,
              relative_departure_coordinates=[1-2*p, 1/2],
              relative_arrival_coordinates=[1-2*p, 1/2])
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R1,
              room_arrival=RE)    

    level = Maze(start_room_index=0, 
                 exit_room_index=-1, 
                 rooms_list=[R0, R1, RE], 
                 doors_list = [D0, D1, D2, D3], 
                 fastest_solution='S0 D0 S8 S9 D1 S0 S1 D0 S9 S10 D1 S1 S2 D0 S10 S11 D1 S2 S3 D0 S11 S12 D1 S3 S4 D0 S8 S10 S12 D2 S0 S2 S4 D0 S8 S9 S10 S11 D1 S0 S1 S2 S3 D0 S9 S10 S11 S12 D1 S1 S2 S3 S4 D0 S10 S11 S12 S13 D1 S2 S3 S4 S5 D0 S8 S10 S13 D2 S0 S2 S5 D0 S8 S9 S10 S12 D1 S0 S1 S2 S4 D0 S9 S10 S11 S13 D1 S1 S2 S3 S5 D0 S8 S10 S13 D2 S0 S2 S5 D0 S8 S9 S12 S13 D1 S0 S1 S4 S5 D0 S8 S11 S13 D2 S0 S3 S5 D0 S8 S10 S11 S12 D1 S0 S2 S3 S4 D0 S8 S12 D2 S0 S4 D0 S8 S11 D1 S0 S3 D0 S9 S12 D1 S1 S4 D0 S10 S13 D1 S2 S5 D0 S11 S14 D1 S3 S6 D0 S8 S10 S12 S14 D2 S0 S2 S4 S6 D0 S8 S9 S10 S11 S13 S14 D1 S0 S1 S2 S3 S5 S6 D0 S9 S10 S11 S12 S14 S15 D1 S1 S2 S3 S4 S6 S7 D0 S8 S10 S13 S15 D2 S0 S2 S5 S7 D0 S8 S9 S12 S14 D1 S0 S1 S4 S6 D0 S9 S10 S13 S15 D1 S1 S2 S5 S7 D0 S8 S10 S15 D2 S0 S2 S7 D0 S8 S9 S14 S15 D1 S0 S1 S6 S7 D0 S8 S11 S13 S15 D2 S0 S3 S5 S7 D0 S8 S10 S11 S12 S13 S14 D1 S0 S2 S3 S4 S5 S6 D0 S9 S11 S12 S13 S14 S15 D1 S1 S3 S4 S5 S6 S7 D0 S8 S10 S12 S15 D2 S0 S2 S4 S7 D0 S8 S9 S11 S14 D1 S0 S1 S3 S6 D0 S9 S10 S12 S15 D1 S1 S2 S4 S7 D0 D3',
                 level_color=get_color(),
                 name='Syracuse',
                 door_window_size = 400,
                 keep_proportions = True,
                 border=50)

    return level

def get_color():
    return Level_color(background_color=Color.color_hls(hu=0.6, li=0.15, sa=0.5),
                       room_color=Color.color_hls(hu=0.1, li=0.2, sa=0.5),
                       contour_color=Color.WHITE,
                       letters_color=Color.WHITE,
                       inside_room_color=Color.WHITE,
                       letter_contour_color=Color.BLACK)