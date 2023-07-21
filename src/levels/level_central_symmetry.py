from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_central_symmetry(): 

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
    
    tree_list_0 = Tree.tree_list_from_str('TF')
    tree_list_1 = [None]

    T0 = Tree(tree_list=[None],
              empty=True,
              name='T0',
              switches=[1])
    T1 = Tree(tree_list=tree_list_0,
              empty=True,
              name='T1',
              switches=[S1, S2])
    T2 = Tree(tree_list=tree_list_0,
              empty=True,
              name='T2',
              switches=[S2, S1])
    T3 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T3',
                      switches=[S2, S3])
    T4 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T4',
                      switches=[S3, S2])
    T5 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T5',
                      switches=[S3, S4])
    T6 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T6',
                      switches=[S4, S3])
    T7 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T7',
                      switches=[S5, S6])
    T8 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T8',
                      switches=[S6, S5])
    T9 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T9',
                      switches=[S6, S7])
    T20 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T20',
                      switches=[S7, S6])
    T21 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T21',
                      switches=[S7, S8])
    T22 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T22',
                      switches=[S8, S7])
    T23 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T23',
                      switches=[S9, S20])
    T24 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T24',
                      switches=[S20, S9])
    T25 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T25',
                      switches=[S20, S21])
    T26 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T26',
                      switches=[S21, S20])
    T27 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T27',
                      switches=[S21, S22])
    T28 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T28',
                      switches=[S22, S21])
    T29 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T29',
                      switches=[S23, S24])
    T30 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T30',
                      switches=[S24, S23])
    T31 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T31',
                      switches=[S24, S25])
    T32 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T32',
                      switches=[S25, S24])
    T33 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T33',
                      switches=[S25, S26])
    T34 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T34',
                      switches=[S26, S25])
    T35 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T35',
                      switches=[S1, S5])
    T36 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T36',
                      switches=[S5, S1])
    T37 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T37',
                      switches=[S5, S9])
    T38 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T38',
                      switches=[S9, S5])
    T39 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T39',
                      switches=[S9, S23])
    T40 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T40',
                      switches=[S23, S9])
    T41 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T41',
                      switches=[S2, S6])
    T42 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T42',
                      switches=[S6, S2])
    T43 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T43',
                      switches=[S6, S20])
    T44 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T44',
                      switches=[S20, S6])
    T45 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T45',
                      switches=[S20, S24])
    T46 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T46',
                      switches=[S24, S20])
    T47 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T47',
                      switches=[S3, S7])
    T48 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T48',
                      switches=[S7, S3])
    T49 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T49',
                      switches=[S7, S21])
    T50 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T50',
                      switches=[S21, S7])
    T51 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T51',
                      switches=[S21, S25])
    T52 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T52',
                      switches=[S25, S21])
    T53 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T53',
                      switches=[S4, S8])
    T54 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T54',
                      switches=[S8, S4])
    T55 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T55',
                      switches=[S8, S22])
    T56 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T56',
                      switches=[S22, S8])
    T57 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T57',
                      switches=[S22, S26])
    T58 = Tree(tree_list=tree_list_0,
                      empty=True,
                      name='T58',
                      switches=[S26, S22])
    T59 = Tree(tree_list=[None],
                      empty=True,
                      name='T59',
                      switches=[1])
    T60 = Tree(tree_list=[None],
                      empty=True,
                      name='T60',
                      switches=[1])
    T61 = Tree(tree_list=['AND',
                          Tree.tree_list_AND(14),
                          Tree.tree_list_AND(15)],
                      empty=True,
                      name='T61',
                      switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28],
                      cut_expression=True)
    
    ex = 0.39
    ey = 0.39
    
    R0 = Room(name='R0',
              position=[0, -1+ey, 3+ex, ey/2],
              switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11])

    R1 = Room(name='R1',
              position=[3, 0, ex, ey],
              switches_list=[S12])
    R2 = Room(name='R2',
              position=[3, 1, ex, ey],
              switches_list=[S13])
    R3 = Room(name='R3',
              position=[3, 2, ex, ey],
              switches_list=[S14])
    R4 = Room(name='R4',
              position=[3, 3, ex, ey],
              switches_list=[S15])
    R5 = Room(name='R5',
              position=[2, 0, ex, ey],
              switches_list=[S16])
    R6 = Room(name='R6',
              position=[2, 1, ex, ey],
              switches_list=[S17])
    R7 = Room(name='R7',
              position=[2, 2, ex, ey],
              switches_list=[S18])
    R8 = Room(name='R8',
              position=[2, 3, ex, ey],
              switches_list=[S19])
    R9 = Room(name='R9',
              position=[1, 0, ex, ey],
              switches_list=[S20])
    R20 = Room(name='R20',
              position=[1, 1, ex, ey],
              switches_list=[S21])
    R21 = Room(name='R21',
               position=[1, 2, ex, ey],
               switches_list=[S22])
    R22 = Room(name='R22',
               position=[1, 3, ex, ey],
               switches_list=[S23])
    R23 = Room(name='R23',
               position=[0, 0, ex, ey],
               switches_list=[S24])
    R24 = Room(name='R24',
               position=[0, 1, ex, ey],
               switches_list=[S25])
    R25 = Room(name='R25',
               position=[0, 2, ex, ey],
               switches_list=[S26])
    R26 = Room(name='R26',
               position=[0, 3, ex, ey],
               switches_list=[S27])
    R27 = Room(name='R27',
               position=[-1+2*ex/3, 2+ey, ex, 1-ey],
               switches_list=[S28])
    RE = Room(name='RE',
              position=[4-3*ex/4, 1, ex, ey],
              is_exit=True)
    
    rp = 0.375

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[(3+ex/2)/(3+ex), 1],
                relative_arrival_coordinates=[1/2, 0])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                relative_position=rp)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R1,
                relative_position=rp)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R3,
                relative_position=rp)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R3,
                room_arrival=R2,
                relative_position=rp)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R4,
                relative_position=rp)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R4,
                room_arrival=R3,
                relative_position=rp)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R5,
                room_arrival=R6,
                relative_position=rp)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R6,
                room_arrival=R5,
                relative_position=rp)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R6,
                room_arrival=R7,
                relative_position=rp)
    D20 = Door(two_way=False,
                tree=T20,
                name='D20',
                room_departure=R7,
                room_arrival=R6,
                relative_position=rp)
    D21 = Door(two_way=False,
                tree=T21,
                name='D21',
                room_departure=R7,
                room_arrival=R8,
                relative_position=rp)
    D22 = Door(two_way=False,
                tree=T22,
                name='D22',
                room_departure=R8,
                room_arrival=R7,
                relative_position=rp)
    D23 = Door(two_way=False,
                tree=T23,
                name='D23',
                room_departure=R9,
                room_arrival=R20,
                relative_position=rp)
    D24 = Door(two_way=False,
                tree=T24,
                name='D24',
                room_departure=R20,
                room_arrival=R9,
                relative_position=rp)
    D25 = Door(two_way=False,
                tree=T25,
                name='D25',
                room_departure=R20,
                room_arrival=R21,
                relative_position=rp)
    D26 = Door(two_way=False,
                tree=T26,
                name='D26',
                room_departure=R21,
                room_arrival=R20,
                relative_position=rp)
    D27 = Door(two_way=False,
                tree=T27,
                name='D27',
                room_departure=R21,
                room_arrival=R22,
                relative_position=rp)
    D28 = Door(two_way=False,
                tree=T28,
                name='D28',
                room_departure=R22,
                room_arrival=R21,
                relative_position=rp)
    D29 = Door(two_way=False,
                tree=T29,
                name='D29',
                room_departure=R23,
                room_arrival=R24,
                relative_position=rp)
    D30 = Door(two_way=False,
                tree=T30,
                name='D30',
                room_departure=R24,
                room_arrival=R23,
                relative_position=rp)
    D31 = Door(two_way=False,
                tree=T31,
                name='D31',
                room_departure=R24,
                room_arrival=R25,
                relative_position=rp)
    D32 = Door(two_way=False,
                tree=T32,
                name='D32',
                room_departure=R25,
                room_arrival=R24,
                relative_position=rp)
    D33 = Door(two_way=False,
                tree=T33,
                name='D33',
                room_departure=R25,
                room_arrival=R26,
                relative_position=rp)
    D34 = Door(two_way=False,
                tree=T34,
                name='D34',
                room_departure=R26,
                room_arrival=R25,
                relative_position=rp)
    D35 = Door(two_way=False,
                tree=T35,
                name='D35',
                room_departure=R1,
                room_arrival=R5,
                relative_position=rp)
    D36 = Door(two_way=False,
                tree=T36,
                name='D36',
                room_departure=R5,
                room_arrival=R1,
                relative_position=rp)
    D37 = Door(two_way=False,
                tree=T37,
                name='D37',
                room_departure=R5,
                room_arrival=R9,
                relative_position=rp)
    D38 = Door(two_way=False,
                tree=T38,
                name='D38',
                room_departure=R9,
                room_arrival=R5,
                relative_position=rp)
    D39 = Door(two_way=False,
                tree=T39,
                name='D39',
                room_departure=R9,
                room_arrival=R23,
                relative_position=rp)
    D40 = Door(two_way=False,
                tree=T40,
                name='D40',
                room_departure=R23,
                room_arrival=R9,
                relative_position=rp)
    D41 = Door(two_way=False,
                tree=T41,
                name='D41',
                room_departure=R2,
                room_arrival=R6,
                relative_position=rp)
    D42 = Door(two_way=False,
                tree=T42,
                name='D42',
                room_departure=R6,
                room_arrival=R2,
                relative_position=rp)
    D43 = Door(two_way=False,
                tree=T43,
                name='D43',
                room_departure=R6,
                room_arrival=R20,
                relative_position=rp)
    D44 = Door(two_way=False,
                tree=T44,
                name='D44',
                room_departure=R20,
                room_arrival=R6,
                relative_position=rp)
    D45 = Door(two_way=False,
                tree=T45,
                name='D45',
                room_departure=R20,
                room_arrival=R24,
                relative_position=rp)
    D46 = Door(two_way=False,
                tree=T46,
                name='D46',
                room_departure=R24,
                room_arrival=R20,
                relative_position=rp)
    D47 = Door(two_way=False,
                tree=T47,
                name='D47',
                room_departure=R3,
                room_arrival=R7,
                relative_position=rp)
    D48 = Door(two_way=False,
                tree=T48,
                name='D48',
                room_departure=R7,
                room_arrival=R3,
                relative_position=rp)
    D49 = Door(two_way=False,
                tree=T49,
                name='D49',
                room_departure=R7,
                room_arrival=R21,
                relative_position=rp)
    D50 = Door(two_way=False,
                tree=T50,
                name='D50',
                room_departure=R21,
                room_arrival=R7,
                relative_position=rp)
    D51 = Door(two_way=False,
                tree=T51,
                name='D51',
                room_departure=R21,
                room_arrival=R25,
                relative_position=rp)
    D52 = Door(two_way=False,
                tree=T52,
                name='D52',
                room_departure=R25,
                room_arrival=R21,
                relative_position=rp)
    D53 = Door(two_way=False,
                tree=T53,
                name='D53',
                room_departure=R4,
                room_arrival=R8,
                relative_position=rp)
    D54 = Door(two_way=False,
                tree=T54,
                name='D54',
                room_departure=R8,
                room_arrival=R4,
                relative_position=rp)
    D55 = Door(two_way=False,
                tree=T55,
                name='D55',
                room_departure=R8,
                room_arrival=R22,
                relative_position=rp)
    D56 = Door(two_way=False,
                tree=T56,
                name='D56',
                room_departure=R22,
                room_arrival=R8,
                relative_position=rp)
    D57 = Door(two_way=False,
                tree=T57,
                name='D57',
                room_departure=R22,
                room_arrival=R26,
                relative_position=rp)
    D58 = Door(two_way=False,
                tree=T58,
                name='D58',
                room_departure=R26,
                room_arrival=R22,
                relative_position=rp)
    D59 = Door(two_way=False,
                tree=T59,
                name='D59',
                room_departure=R25,
                room_arrival=R27)
    D60 = Door(two_way=False,
                tree=T60,
                name='D60',
                room_departure=R27,
                room_arrival=R26)
    D61 = Door(two_way=False,
                tree=T61,
                name='D61',
                room_departure=R2,
                room_arrival=RE)
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R20, R21, R22, R23, R24, R25, R26, R27, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30, D31, D32, D33, D34, D35, D36, D37, D38, D39, D40, D41, D42, D43, D44, D45, D46, D47, D48, D49, D50, D51, D52, D53, D54, D55, D56, D57, D58, D59, D60, D61],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.5),
                 name='Central Symmetry',
                 keep_proportions=True,
                 y_separation=27,
                 door_window_size=600)
    
    return level