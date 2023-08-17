from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def level_postman(fast_solution_finding=False): 

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
    
    SlisT13 = [S0, S1, S2, S3,
              S9, S10, S11, S12]
    
    lgraph = [[0, 4],
              [0, 6],
              [0, 8],
              [1, 4],
              [1, 10],
              [1, 14],
              [2, 6],
              [2, 10],
              [2, 12],
              [3, 8],
              [3, 12],
              [3, 14],
              [4, 5],
              [6, 7],
              [8, 9],
              [10, 11],
              [12, 13],
              [14, 15]]
    
    assert len(lgraph) == 18
    
    tree_list_3 = ['EQU', Tree.tree_list_BIN(4), Tree.tree_list_BIN(4), [None]]

    T0 = Tree(tree_list=['AND'] + [['NAND',
                                    Tree.tree_list_NOT,
                                    ['EQU', [None], Tree.tree_list_BIN(4)],]]*6,
                name='T0',
                switches=[S18, 5, S0, S1, S2, S3,
                          S19, 7, S0, S1, S2, S3,
                          S20, 9, S0, S1, S2, S3,
                          S21, 11, S0, S1, S2, S3,
                          S22, 13, S0, S1, S2, S3,
                          S23, 15, S0, S1, S2, S3],
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
    tree_list_1 = ['OR'] + [tree_list_EQUSET_BIN]*len(lgraph)
    
    
    # tree_list_1 = ['AND',
    #                ['OR'] + [tree_list_EQUSET_BIN]*14,
    #                ['EQU', Tree.tree_list_BIN(5), ['SUM', Tree.tree_list_BIN(4), [None]]]]
    # Slist_tree_1.extend([S4, S5, S6, S7, S8,
    #                      S13, S14, S15, S16, S17,
    #                      1])
    
    T1 = Tree(tree_list=tree_list_1,
                name='T1',
                switches=Slist_tree_1,
                cut_expression_depth_1=True)
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[int(not fast_solution_finding)])
    # T2 = Tree(tree_list=['EQU',
    #                       Tree.tree_list_BIN(5),
    #                       Tree.tree_list_BIN(5),],
    #             
    #             name='T2',
    #             switches=[S4, S5, S6, S7, S8,
    #                       S13, S14, S15, S16, S17])
    T3 = Tree(tree_list=['EQU',
                         Tree.tree_list_BIN(5),
                         ['SUM', Tree.tree_list_BIN(5), [None]]],
                name='T3',
                switches=[S4, S5, S6, S7, S8,
                          S13, S14, S15, S16, S17,
                          1])
    T4 = Tree(tree_list=Tree.tree_list_XNOR(2),
                name='T4',
                switches=[S0, S9])
    T5 = Tree(tree_list=Tree.tree_list_XNOR(2),
                name='T5',
                switches=[S1, S10])
    T6 = Tree(tree_list=Tree.tree_list_XNOR(2),
                name='T6',
                switches=[S2, S11])
    T7 = Tree(tree_list=Tree.tree_list_XNOR(2),
                name='T7',
                switches=[S3, S12])
    T8 = Tree(tree_list=Tree.tree_list_XNOR(2),
                name='T8',
                switches=[S4, S13])
    T9 = Tree(tree_list=Tree.tree_list_XNOR(2),
                name='T9',
                switches=[S5, S14])
    T10 = Tree(tree_list=Tree.tree_list_XNOR(2),
                name='T10',
                switches=[S6, S15])
    T11 = Tree(tree_list=Tree.tree_list_XNOR(2),
                name='T11',
                switches=[S7, S16])
    T12 = Tree(tree_list=Tree.tree_list_XNOR(2),
                name='T12',
                switches=[S8, S17])
    T13 = Tree(tree_list=tree_list_3,
                name='T13',
                switches=SlisT13 + [5])
    T14 = Tree(tree_list=tree_list_3,
                name='T14',
                switches=SlisT13 + [7])
    T15 = Tree(tree_list=tree_list_3,
                name='T15',
                switches=SlisT13 + [9])
    T16 = Tree(tree_list=tree_list_3,
                name='T16',
                switches=SlisT13 + [11])
    T17 = Tree(tree_list=tree_list_3,
                name='T17',
                switches=SlisT13 + [13])
    T18 = Tree(tree_list=tree_list_3,
                name='T18',
                switches=SlisT13 + [15])
    T19 = Tree(tree_list=['AND',
                          Tree.tree_list_from_str('F'*4+'T'*7),
                          ['INFOREQU', Tree.tree_list_BIN(5), [None]]],
                name='T19',
                switches=[S0, S1, S2, S3,
                          S18, S19, S20, S21, S22, S23, S24,
                          S4, S5, S6, S7, S8, 30])
    # T11 = Tree(tree_list=Tree.tree_list_from_str('T'*7),
    #             
    #             name='T11',
    #             switches=[S18, S19, S20, S21, S22, S23, S24])
    
    ex = 1
    ey = 1
    delta_x = 2.75
    delta_y = 2.25
    ex3 = 0.75
    ey3 = 0.5
    dx3 = 1.5
    dy3 = 1+1/8

    R0 = Room(name='R0',
                position=[2.75, 5.5, ex, ey/2],
                switches_list=[])
    R1 = Room(name='R1',
                position=[0.75, 3.25, ex/2, 2*ey],
                switches_list=[S0, S1, S2, S3])
    R2 = Room(name='R2',
                position=[1.75, 2.25, ex/2, 5*ey/2],
                switches_list=[S4, S5, S6, S7, S8])
    R3 = Room(name='R3',
                position=[delta_x, delta_y, ex3, ey3],
                switches_list=[S9])
    R4 = Room(name='R4',
                position=[delta_x+dx3, delta_y, ex3, ey3],
                switches_list=[S10])
    R5 = Room(name='R5',
                position=[delta_x+2*dx3, delta_y, ex3, ey3],
                switches_list=[S11])
    R6 = Room(name='R6',
                position=[delta_x+2*dx3, delta_y+dy3, ex3, ey3],
                switches_list=[S12])
    R7 = Room(name='R7',
                position=[delta_x+dx3, delta_y+dy3, ex3, ey3],
                switches_list=[S13])
    R8 = Room(name='R8',
                position=[delta_x, delta_y+dy3, ex3, ey3],
                switches_list=[S14])
    R9 = Room(name='R9',
                position=[delta_x, delta_y+2*dy3, ex3, ey3],
                switches_list=[S15])
    R10 = Room(name='R10',
                position=[delta_x+dx3, delta_y+2*dy3, ex3, ey3],
                switches_list=[S16])
    R11 = Room(name='R11',
                position=[delta_x+2*dx3, delta_y+2*dy3, ex3, ey3],
                switches_list=[S17])
    R12 = Room(name='R12',
                position=[5, 5.5, ex, ey/2],
                switches_list=[S18])
    R13 = Room(name='R13',
                position=[5, 6.25, ex, ey/2],
                switches_list=[S19])
    R14 = Room(name='R14',
                position=[3.5, 6.5, ex, ey/2],
                switches_list=[S20])
    R15 = Room(name='R15',
                position=[2, 6.5, ex, ey/2],
                switches_list=[S21])
    R16 = Room(name='R16',
                position=[0.5, 6.25, ex, ey/2],
                switches_list=[S22])
    R17 = Room(name='R17',
                position=[0.5, 5.5, ex, ey/2],
                switches_list=[S23])
    RE = Room(name='RE',
                  position=[2.75, 7.25, ex, ey/2],
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
                room_departure=R0,
                room_arrival=R2,
                relative_departure_coordinates=[0, 0],
                relative_arrival_coordinates=[1, 1])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R3,
                relative_departure_coordinates=[1, 1/3],
                relative_arrival_coordinates=[0, 1])
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R3,
                room_arrival=R4)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R4,
                room_arrival=R5)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R5,
                room_arrival=R6)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R6,
                room_arrival=R7)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R7,
                room_arrival=R8)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R8,
                room_arrival=R9)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R9,
                room_arrival=R10)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R10,
                room_arrival=R11)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R11,
                room_arrival=R0,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[1, 0])
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R0,
                room_arrival=R12)
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R0,
                room_arrival=R13)
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R0,
                room_arrival=R14)
    D16 = Door(two_way=True,
                tree=T16,
                name='D16',
                room_departure=R0,
                room_arrival=R15)
    D17 = Door(two_way=True,
                tree=T17,
                name='D17',
                room_departure=R0,
                room_arrival=R16)
    D18 = Door(two_way=True,
                tree=T18,
                name='D18',
                room_departure=R0,
                room_arrival=R17)
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R0,
                room_arrival=RE)

    lcolor = Levels_colors_list.FROM_HUE(hu=0.6, sa=0.4, li=0.4)
    lcolor.surrounding_color = Color.BRIGHT_KHAKI
    lcolor.contour_color = Color.BRIGHT_KHAKI
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19],
                 fastest_solution=None,
                 level_color=lcolor,
                 name='Postman',
                 keep_proportions=True,
                 door_window_size=750)
    
    return level