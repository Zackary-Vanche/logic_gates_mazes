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
    
    tree_list_0 = Tree.tree_list_from_str('TFT')

    T0 = Tree(tree_list=['EQU', [None], ['SUM'] + [[None]]*12],
              name='T0',
              switches=[7,
                        S0, S1, S2,
                        S3, S4, S5,
                        S6, S7, S8,
                        S9, S10, S11])

    T1 = Tree(tree_list=tree_list_0,
              name='T1',
              switches=[S12, S13, S0])
    T2 = Tree(tree_list=tree_list_0,
              name='T2',
              switches=[S13, S12, S0])

    T3 = Tree(tree_list=tree_list_0,
              name='T3',
              switches=[S13, S14, S1])
    T4 = Tree(tree_list=tree_list_0,
              name='T4',
              switches=[S14, S13, S1])

    T5 = Tree(tree_list=tree_list_0,
              name='T5',
              switches=[S14, S15, S2])
    T6 = Tree(tree_list=tree_list_0,
              name='T6',
              switches=[S15, S14, S2])

    T7 = Tree(tree_list=tree_list_0,
              name='T7',
              switches=[S16, S17, S5])
    T8 = Tree(tree_list=tree_list_0,
              name='T8',
              switches=[S17, S16, S5])

    T9 = Tree(tree_list=tree_list_0,
              name='T9',
              switches=[S17, S18, S3])
    T10 = Tree(tree_list=tree_list_0,
               name='T10',
               switches=[S18, S17, S3])

    T11 = Tree(tree_list=tree_list_0,
               name='T11',
               switches=[S18, S19, S4])
    T12 = Tree(tree_list=tree_list_0,
               name='T12',
               switches=[S19, S18, S4])

    T13 = Tree(tree_list=tree_list_0,
               name='T13',
               switches=[S20, S21, S4])
    T14 = Tree(tree_list=tree_list_0,
               name='T14',
               switches=[S21, S20, S4])

    T15 = Tree(tree_list=tree_list_0,
               name='T15',
               switches=[S21, S22, S3])
    T16 = Tree(tree_list=tree_list_0,
               name='T16',
               switches=[S22, S21, S3])

    T17 = Tree(tree_list=tree_list_0,
               name='T17',
               switches=[S22, S23, S5])
    T18 = Tree(tree_list=tree_list_0,
               name='T18',
               switches=[S23, S22, S5])

    T19 = Tree(tree_list=tree_list_0,
               name='T19',
               switches=[S24, S25, S2])
    T20 = Tree(tree_list=tree_list_0,
               name='T20',
               switches=[S25, S24, S2])

    T21 = Tree(tree_list=tree_list_0,
               name='T21',
               switches=[S25, S26, S1])
    T22 = Tree(tree_list=tree_list_0,
               name='T22',
               switches=[S26, S25, S1])

    T23 = Tree(tree_list=tree_list_0,
               name='T23',
               switches=[S26, S27, S0])
    T24 = Tree(tree_list=tree_list_0,
               name='T24',
               switches=[S27, S26, S0])

    T25 = Tree(tree_list=tree_list_0,
               name='T25',
               switches=[S12, S16, S11])
    T26 = Tree(tree_list=tree_list_0,
               name='T26',
               switches=[S16, S12, S11])

    T27 = Tree(tree_list=tree_list_0,
               name='T27',
               switches=[S16, S20, S10])
    T28 = Tree(tree_list=tree_list_0,
               name='T28',
               switches=[S20, S16, S10])

    T29 = Tree(tree_list=tree_list_0,
               name='T29',
               switches=[S20, S24, S9])
    T30 = Tree(tree_list=tree_list_0,
               name='T30',
               switches=[S24, S20, S9])

    T31 = Tree(tree_list=tree_list_0,
               name='T31',
               switches=[S13, S17, S6])
    T32 = Tree(tree_list=tree_list_0,
               name='T32',
               switches=[S17, S13, S6])

    T33 = Tree(tree_list=tree_list_0,
               name='T33',
               switches=[S17, S21, S8])
    T34 = Tree(tree_list=tree_list_0,
               name='T34',
               switches=[S21, S17, S8])

    T35 = Tree(tree_list=tree_list_0,
               name='T35',
               switches=[S21, S25, S7])
    T36 = Tree(tree_list=tree_list_0,
               name='T36',
               switches=[S25, S21, S7])

    T37 = Tree(tree_list=tree_list_0,
               name='T37',
               switches=[S14, S18, S7])
    T38 = Tree(tree_list=tree_list_0,
               name='T38',
               switches=[S18, S14, S7])

    T39 = Tree(tree_list=tree_list_0,
               name='T39',
               switches=[S18, S22, S8])
    T40 = Tree(tree_list=tree_list_0,
               name='T40',
               switches=[S22, S18, S8])

    T41 = Tree(tree_list=tree_list_0,
               name='T41',
               switches=[S22, S26, S6])
    T42 = Tree(tree_list=tree_list_0,
               name='T42',
               switches=[S26, S22, S6])

    T43 = Tree(tree_list=tree_list_0,
               name='T43',
               switches=[S15, S19, S9])
    T44 = Tree(tree_list=tree_list_0,
               name='T44',
               switches=[S19, S15, S9])

    T45 = Tree(tree_list=tree_list_0,
               name='T45',
               switches=[S19, S23, S10])
    T46 = Tree(tree_list=tree_list_0,
               name='T46',
               switches=[S23, S19, S10])

    T47 = Tree(tree_list=tree_list_0,
               name='T47',
               switches=[S23, S27, S11])
    T48 = Tree(tree_list=tree_list_0,
               name='T48',
               switches=[S27, S23, S11])

    T49 = Tree(tree_list=['NOT', Tree.tree_list_from_str('TTT')],
               name='T49',
               switches=[S3, S6, S9])
    T50 = Tree(tree_list=[None],
               name='T50',
               switches=[S28])
    T51 = Tree(tree_list=['AND',
                          Tree.tree_list_AND(8),
                          Tree.tree_list_AND(9)],
                      name='T51',
                      switches=[S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28],
                      cut_expression=True)
    
    dx = 1.2
    dy = 1
    ex = 0.5
    ey = 0.38
    
    R0 = Room(name='R0',
              position=[0*dx, -0.3, 3+ex, ey/2],
              switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11])

    R1 = Room(name='R1',
              position=[3*dx, 0*dy, ex, ey],
              switches_list=[S12])
    R2 = Room(name='R2',
              position=[3*dx, 1*dy, ex, ey],
              switches_list=[S13])
    R3 = Room(name='R3',
              position=[3*dx, 2*dy, ex, ey],
              switches_list=[S14])
    R4 = Room(name='R4',
              position=[3*dx, 3*dy, ex, ey],
              switches_list=[S15])
    R5 = Room(name='R5',
              position=[2*dx, 0*dy, ex, ey],
              switches_list=[S16])
    R6 = Room(name='R6',
              position=[2*dx, 1*dy, ex, ey],
              switches_list=[S17])
    R7 = Room(name='R7',
              position=[2*dx, 2*dy, ex, ey],
              switches_list=[S18])
    R8 = Room(name='R8',
              position=[2*dx, 3*dy, ex, ey],
              switches_list=[S19])
    R9 = Room(name='R9',
              position=[1*dx, 0*dy, ex, ey],
              switches_list=[S20])
    R10 = Room(name='R10',
              position=[1*dx, 1*dy, ex, ey],
              switches_list=[S21])
    R11 = Room(name='R11',
               position=[1*dx, 2*dy, ex, ey],
               switches_list=[S22])
    R12 = Room(name='R12',
               position=[1*dx, 3*dy, ex, ey],
               switches_list=[S23])
    R13 = Room(name='R13',
               position=[0*dx, 0*dy, ex, ey],
               switches_list=[S24])
    R14 = Room(name='R14',
               position=[0*dx, 1*dy, ex, ey],
               switches_list=[S25])
    R15 = Room(name='R15',
               position=[0*dx, 2*dy, ex, ey],
               switches_list=[S26])
    R16 = Room(name='R16',
               position=[0*dx, 3*dy, ex, ey],
               switches_list=[S27])
    R17 = Room(name='R17',
               position=[-1*dx+2*ex/3, 2*dy+ey, ex, 1-ey],
               switches_list=[S28])
    RE = Room(name='RE',
              position=[3.75*dx, 1*dy, ex, ey],
              is_exit=True)
    
    rp = 0.375

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
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R7,
                room_arrival=R6,
                relative_position=rp)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R7,
                room_arrival=R8,
                relative_position=rp)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R8,
                room_arrival=R7,
                relative_position=rp)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R9,
                room_arrival=R10,
                relative_position=rp)
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R10,
                room_arrival=R9,
                relative_position=rp)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R10,
                room_arrival=R11,
                relative_position=rp)
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R11,
                room_arrival=R10,
                relative_position=rp)
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R11,
                room_arrival=R12,
                relative_position=rp)
    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=R12,
                room_arrival=R11,
                relative_position=rp)
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R13,
                room_arrival=R14,
                relative_position=rp)
    D20 = Door(two_way=False,
                tree=T20,
                name='D20',
                room_departure=R14,
                room_arrival=R13,
                relative_position=rp)
    D21 = Door(two_way=False,
                tree=T21,
                name='D21',
                room_departure=R14,
                room_arrival=R15,
                relative_position=rp)
    D22 = Door(two_way=False,
                tree=T22,
                name='D22',
                room_departure=R15,
                room_arrival=R14,
                relative_position=rp)
    D23 = Door(two_way=False,
                tree=T23,
                name='D23',
                room_departure=R15,
                room_arrival=R16,
                relative_position=rp)
    D24 = Door(two_way=False,
                tree=T24,
                name='D24',
                room_departure=R16,
                room_arrival=R15,
                relative_position=rp)
    D25 = Door(two_way=False,
                tree=T25,
                name='D25',
                room_departure=R1,
                room_arrival=R5,
                relative_position=rp)
    D26 = Door(two_way=False,
                tree=T26,
                name='D26',
                room_departure=R5,
                room_arrival=R1,
                relative_position=rp)
    D27 = Door(two_way=False,
                tree=T27,
                name='D27',
                room_departure=R5,
                room_arrival=R9,
                relative_position=rp)
    D28 = Door(two_way=False,
                tree=T28,
                name='D28',
                room_departure=R9,
                room_arrival=R5,
                relative_position=rp)
    D29 = Door(two_way=False,
                tree=T29,
                name='D29',
                room_departure=R9,
                room_arrival=R13,
                relative_position=rp)
    D30 = Door(two_way=False,
                tree=T30,
                name='D30',
                room_departure=R13,
                room_arrival=R9,
                relative_position=rp)
    D31 = Door(two_way=False,
                tree=T31,
                name='D31',
                room_departure=R2,
                room_arrival=R6,
                relative_position=rp)
    D32 = Door(two_way=False,
                tree=T32,
                name='D32',
                room_departure=R6,
                room_arrival=R2,
                relative_position=rp)
    D33 = Door(two_way=False,
                tree=T33,
                name='D33',
                room_departure=R6,
                room_arrival=R10,
                relative_position=rp)
    D34 = Door(two_way=False,
                tree=T34,
                name='D34',
                room_departure=R10,
                room_arrival=R6,
                relative_position=rp)
    D35 = Door(two_way=False,
                tree=T35,
                name='D35',
                room_departure=R10,
                room_arrival=R14,
                relative_position=rp)
    D36 = Door(two_way=False,
                tree=T36,
                name='D36',
                room_departure=R14,
                room_arrival=R10,
                relative_position=rp)
    D37 = Door(two_way=False,
                tree=T37,
                name='D37',
                room_departure=R3,
                room_arrival=R7,
                relative_position=rp)
    D38 = Door(two_way=False,
                tree=T38,
                name='D38',
                room_departure=R7,
                room_arrival=R3,
                relative_position=rp)
    D39 = Door(two_way=False,
                tree=T39,
                name='D39',
                room_departure=R7,
                room_arrival=R11,
                relative_position=rp)
    D40 = Door(two_way=False,
                tree=T40,
                name='D40',
                room_departure=R11,
                room_arrival=R7,
                relative_position=rp)
    D41 = Door(two_way=False,
                tree=T41,
                name='D41',
                room_departure=R11,
                room_arrival=R15,
                relative_position=rp)
    D42 = Door(two_way=False,
                tree=T42,
                name='D42',
                room_departure=R15,
                room_arrival=R11,
                relative_position=rp)
    D43 = Door(two_way=False,
                tree=T43,
                name='D43',
                room_departure=R4,
                room_arrival=R8,
                relative_position=rp)
    D44 = Door(two_way=False,
                tree=T44,
                name='D44',
                room_departure=R8,
                room_arrival=R4,
                relative_position=rp)
    D45 = Door(two_way=False,
                tree=T45,
                name='D45',
                room_departure=R8,
                room_arrival=R12,
                relative_position=rp)
    D46 = Door(two_way=False,
                tree=T46,
                name='D46',
                room_departure=R12,
                room_arrival=R8,
                relative_position=rp)
    D47 = Door(two_way=False,
                tree=T47,
                name='D47',
                room_departure=R12,
                room_arrival=R16,
                relative_position=rp)
    D48 = Door(two_way=False,
                tree=T48,
                name='D48',
                room_departure=R16,
                room_arrival=R12,
                relative_position=rp)
    D49 = Door(two_way=False,
                tree=T49,
                name='D49',
                room_departure=R15,
                room_arrival=R17)
    D50 = Door(two_way=False,
                tree=T50,
                name='D50',
                room_departure=R17,
                room_arrival=R16)
    D51 = Door(two_way=False,
                tree=T51,
                name='D51',
                room_departure=R2,
                room_arrival=RE)
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30, D31, D32, D33, D34, D35, D36, D37, D38, D39, D40, D41, D42, D43, D44, D45, D46, D47, D48, D49, D50, D51],
                 fastest_solution='S1 S2 S4 S5 S8 S9 S11 D0 S12 D25 S16 D7 S17 D33 S21 D14 S20 D29 S24 D19 S25 D21 S26 D49 S28 D50 S27 D48 S23 D18 S22 D40 S18 D11 S19 D44 S15 D6 S14 D4 S13 D51',
                 level_color=Levels_colors_list.FROM_HUE(hu=0.6, sa=0.4, li=0.3),
                 name='Central symmetry',
                 keep_proportions=True,
                 y_separation=27,
                 door_window_size=250)
    
    return level