from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def level_bridges(): 

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
    
    Slist1 = [S0, S1, S2, S3,
              S4, S5, S6, S7, S8]
    SlisT3 = [S9, S10, S11, S12, 
              S13, S14, S15, S16, S17]
    
    SlisT4 = [S0, S1, S2, S3,
              S9, S10, S11, S12]
    
    lgraph = [[0, 1],
              [0, 2],
              [0, 3],
              [0, 4],
              [0, 5],
              [1, 6],
              [2, 6],
              [3, 8],
              [4, 10],
              [5, 10],
              [6, 7],
              [7, 8],
              [8, 9],
              [9, 10],
              [10, 9]]
    
    tree_list_3 = ['EQU', Tree.tree_list_BIN(4), Tree.tree_list_BIN(4), [None]]

    T0 = Tree(tree_list=['AND'] + [['NAND',
                                    Tree.tree_list_NOT,
                                    ['EQU', [None], Tree.tree_list_BIN(4)],]]*7,
                empty=True,
                name='T0',
                switches=[S18, 1, S0, S1, S2, S3,
                          S19, 2, S0, S1, S2, S3,
                          S20, 3, S0, S1, S2, S3,
                          S21, 4, S0, S1, S2, S3,
                          S22, 5, S0, S1, S2, S3,
                          S23, 7, S0, S1, S2, S3,
                          S24, 9, S0, S1, S2, S3],
                cut_expression=True)

    Slist_tree_1 = []
    for c in lgraph:
        a, b = c
        Slist_tree_1.extend([
                             a,
                             b,
                             S0, S1, S2, S3,
                             S9, S10, S11, S12,
                             ])
    tree_list_EQUSET_BIN = ['EQUSET',
                            [None],
                            [None],
                            Tree.tree_list_BIN(4),
                            Tree.tree_list_BIN(4),]
    tree_list_1 = ['OR'] + [tree_list_EQUSET_BIN]*14
    
    
    # tree_list_1 = ['AND',
    #                ['OR'] + [tree_list_EQUSET_BIN]*14,
    #                ['EQU', Tree.tree_list_BIN(5), ['SUM', Tree.tree_list_BIN(4), [None]]]]
    # Slist_tree_1.extend([S4, S5, S6, S7, S8,
    #                      S13, S14, S15, S16, S17,
    #                      1])
    
    T1 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T1',
                switches=Slist_tree_1,
                cut_expression_depth_1=True)
    T2 = Tree(tree_list=['EQU',
                         Tree.tree_list_BIN(5),
                         ['SUM', Tree.tree_list_BIN(5), [None]]],
                empty=True,
                name='T2',
                switches=[S4, S5, S6, S7, S8,
                          S13, S14, S15, S16, S17,
                          1])
    # T2 = Tree(tree_list=['EQU',
    #                       Tree.tree_list_BIN(5),
    #                       Tree.tree_list_BIN(5),],
    #             empty=True,
    #             name='T2',
    #             switches=[S4, S5, S6, S7, S8,
    #                       S13, S14, S15, S16, S17])
    T3 = Tree(tree_list=['EQU'] + [Tree.tree_list_BIN(9)]*2,
                empty=True,
                name='T3',
                switches=Slist1+SlisT3)
    T4 = Tree(tree_list=tree_list_3,
                empty=True,
                name='T4',
                switches=SlisT4 + [1])
    T5 = Tree(tree_list=tree_list_3,
                empty=True,
                name='T5',
                switches=SlisT4 + [2])
    T6 = Tree(tree_list=tree_list_3,
                empty=True,
                name='T6',
                switches=SlisT4 + [3])
    T7 = Tree(tree_list=tree_list_3,
                empty=True,
                name='T7',
                switches=SlisT4 + [4])
    T8 = Tree(tree_list=tree_list_3,
                empty=True,
                name='T8',
                switches=SlisT4 + [5])
    T9 = Tree(tree_list=tree_list_3,
                empty=True,
                name='T9',
                switches=SlisT4 + [7])
    T10 = Tree(tree_list=tree_list_3,
                empty=True,
                name='T10',
                switches=SlisT4 + [9])
    T11 = Tree(tree_list=['AND',
                          Tree.tree_list_from_str('F'*4+'T'*7),
                          ['INFOREQU', Tree.tree_list_BIN(5), [None]]],
                empty=True,
                name='T11',
                switches=[S0, S1, S2, S3,
                          S18, S19, S20, S21, S22, S23, S24,
                          S4, S5, S6, S7, S8, 14])
    # T11 = Tree(tree_list=Tree.tree_list_from_str('T'*7),
    #             empty=True,
    #             name='T11',
    #             switches=[S18, S19, S20, S21, S22, S23, S24])
    
    ex = 1
    ey = 1
    ex0 = 0.75
    ey0 = 0.75

    R0 = Room(name='R0',
                position=[3+(ex-ex0)/2, 5+(ex-ex0)/2, ex0, ey0],
                switches_list=[])
    R1 = Room(name='R1',
                position=[0.5, 2.5, ex, 1.5*ey],
                switches_list=[S0, S1, S2, S3,])
    R2 = Room(name='R2',
                position=[2, 2.5, ex, 1.5*ey],
                switches_list=[S4, S5, S6, S7, S8])
    R3 = Room(name='R3',
                position=[3.5, 2.5, 1.5*ex, 1.5*ey],
                switches_list=SlisT3)
    R4 = Room(name='R4',
                position=[5, 4, ex, ey],
                switches_list=[S18])
    R5 = Room(name='R5',
                position=[5, 5.5, ex, ey],
                switches_list=[S19])
    R6 = Room(name='R6',
                position=[5, 7, ex, ey],
                switches_list=[S20])
    R7 = Room(name='R7',
                position=[3.5, 7, ex, ey],
                switches_list=[S21])
    R8 = Room(name='R8',
                position=[2, 7, ex, ey],
                switches_list=[S22])
    R9 = Room(name='R9',
                position=[0.5, 7, ex, ey],
                switches_list=[S23])
    R10 = Room(name='R10',
                position=[0.5, 5.5, ex, ey],
                switches_list=[S24])
    RE = Room(name='RE',
                  position=[0.5, 4.25, ex, ey],
                  is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[0, 0],
                relative_arrival_coordinates=[1, 1])
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
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 1/2])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R0,
                relative_departure_coordinates=[1/4, 1],
                relative_arrival_coordinates=[1/2, 0])
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R0,
                room_arrival=R4)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R0,
                room_arrival=R5)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=R6)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R0,
                room_arrival=R7)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R0,
                room_arrival=R8)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R0,
                room_arrival=R9)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R0,
                room_arrival=R10)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R0,
                room_arrival=RE)

    lcolor = Levels_colors_list.FROM_HUE(hu=0, sa=0.5, li=0.3)
    lcolor.surrounding_color = Color.TOTAL_YELLOW
    lcolor.contour_color = Color.TOTAL_YELLOW
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11],
                 fastest_solution="""D0 S0 D1 S4 D2 S9 S13 D3 D4 S18 D4 D0 S0 D1 S4 S5 D2 S9 S13 S14 D3 D0 S1 D1 S4 D2 S10 S13 D3 D5 S19 D5 D0 S1 D1 S4 S5 S6 D2 S10 S13 S14 S15 D3 D0 S2 D1 S4 D2 S11 S13 D3 D7 S21 D7 D0 S2 D1 S4 S5 D2 S11 S13 S14 D3 D0 S0 S1 D1 S4 D2 S9 S10 S13 D3 D6 S20 D6 D0 S0 S1 S3 D1 S4 S5 S6 S7 D2 S9 S10 S12 S13 S14 S15 S16 D3 D0 S0 S1 S2 S3 D1 S4 D2 S9 S10 S11 S12 S13 D3 D9 S23 D9 D0 S0 S1 S2 S3 D1 S4 S5 D2 S9 S10 S11 S12 S13 S14 D3 D0 S0 D1 S4 D2 S9 S13 D3 D10 S24 D10 D0 S0 S1 D1 S4 S5 S6 D2 S9 S10 S13 S14 S15 D3 D0 S0 S1 S2 S3 D1 S4 D2 S9 S10 S11 S12 S13 D3 D8 S22 D8 D0 S0 S2 D1 S4 S5 D2 S9 S11 S13 S14 D3 D11""",
                 level_color=lcolor,
                 name='Bridges',
                 keep_proportions=True,
                 door_window_size=750)
    
    return level