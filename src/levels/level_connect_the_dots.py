from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_connect_the_dots():
    
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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13]
    
    tree_list_1 = Tree.tree_list_from_str('TF')
    
    T0 = Tree(tree_list=Tree.tree_list_from_str('FF'),
                      empty=True,
                      name='T0',
                      switches=[S0, S3])
    T1 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T1',
                      switches=[S1])
    T2 = Tree(tree_list=[None],
                      empty=True,
                      name='T2',
                      switches=[1])
    T3 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T3',
                      switches=[S0, S1])
    T4 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T4',
                      switches=[S0, S4])
    T5 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T5',
                      switches=[S1, S0])
    T6 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T6',
                      switches=[S1, S2])
    T7 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T7',
                      switches=[S1, S5])
    T8 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T8',
                      switches=[S2, S1])
    T9 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T9',
                      switches=[S2, S6])
    T10 = Tree(tree_list=[None],
                      empty=True,
                      name='T10',
                      switches=[1])
    T11 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T11',
                      switches=[S3, S4])
    T12 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T12',
                      switches=[S3, S7])
    T13 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T13',
                      switches=[S4, S0])
    T14 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T14',
                      switches=[S4, S3])
    T15 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T15',
                      switches=[S4, S5])
    T16 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T16',
                      switches=[S4, S5, S8])
    T17 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T17',
                      switches=[S5, S1])
    T18 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T18',
                      switches=[S5, S4])
    T19 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T19',
                      switches=[S5, S6])
    T20 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T20',
                      switches=[S5, S9])
    T21 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T21',
                      switches=[S6, S2])
    T22 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T22',
                      switches=[S6, S5])
    T23 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T23',
                      switches=[S6, S10])
    T24 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T24',
                      switches=[S7, S3])
    T25 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T25',
                      switches=[S7, S8])
    T26 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T26',
                      switches=[S7, S11])
    T27 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T27',
                      switches=[S8, S4])
    T28 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T28',
                      switches=[S8, S7])
    T29 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T29',
                      switches=[S8, S9])
    T30 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T30',
                      switches=[S8, S12])
    T31 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T31',
                      switches=[S9, S5])
    T32 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T32',
                      switches=[S9, S8])
    T33 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T33',
                      switches=[S9, S10])
    T34 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T34',
                      switches=[S9, S13])
    T35 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T35',
                      switches=[S10, S6])
    T36 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T36',
                      switches=[S10, S9])
    T37 = Tree(tree_list=[None],
                      empty=True,
                      name='T37',
                      switches=[S10])
    T38 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T38',
                      switches=[S11, S7])
    T39 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T39',
                      switches=[S11, S12])
    T40 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T40',
                      switches=[S12, S8])
    T41 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T41',
                      switches=[S12, S11])
    T42 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T42',
                      switches=[S12, S13])
    T43 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T43',
                      switches=[S13, S9])
    T44 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T44',
                      switches=[S13, S12])
    T45 = Tree(tree_list=[None],
                      empty=True,
                      name='T45',
                      switches=[S13])
    T46 = Tree(tree_list=Tree.tree_list_AND(len(Slist)),
                      empty=True,
                      name='T46',
                      switches=Slist)
    
    ex = 0.4
    ey = 0.4
    dx = 1
    dy = 1
    
    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[])
    R1 = Room(name='R1',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S0])
    R2 = Room(name='R2',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S1])
    R3 = Room(name='R3',
                position=[0*dx, 3*dy, ex, ey],
                switches_list=[S2])
    R4 = Room(name='R4',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S3])
    R5 = Room(name='R5',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S4])
    R6 = Room(name='R6',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S5])
    R7 = Room(name='R7',
                position=[1*dx, 3*dy, ex, ey],
                switches_list=[S6])
    R8 = Room(name='R8',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[S7])
    R9 = Room(name='R9',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S8])
    R10 = Room(name='R10',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S9])
    R11 = Room(name='R11',
                position=[2*dx, 3*dy, ex, ey],
                switches_list=[S10])
    R12 = Room(name='R12',
                position=[3*dx, 0*dy, ex, ey],
                switches_list=[S11])
    R13 = Room(name='R13',
                position=[3*dx, 1*dy, ex, ey],
                switches_list=[S12])
    R14 = Room(name='R14',
                position=[3*dx, 2*dy, ex, ey],
                switches_list=[S13])
    R15 = Room(name='R15',
              position=[3*dx, 3*dy, ex, ey])
    RE = Room(name='RE',
              position=[4*dx, 3*dy, ex, ey],
              is_exit=True)
    
    epsilon = 0.05
    a = [epsilon, epsilon]
    b = [1-epsilon, epsilon]
    c = [epsilon, 1-epsilon]
    d = [1-epsilon, 1-epsilon]
    
    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=c,
                relative_arrival_coordinates=a)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R4,
                relative_departure_coordinates=d,
                relative_arrival_coordinates=c)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R0,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=d)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=c,
                relative_arrival_coordinates=a)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R1,
                room_arrival=R5,
                relative_departure_coordinates=d,
                relative_arrival_coordinates=c)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R2,
                room_arrival=R1,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=d)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R2,
                room_arrival=R3,
                relative_departure_coordinates=c,
                relative_arrival_coordinates=a)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R2,
                room_arrival=R6,
                relative_departure_coordinates=d,
                relative_arrival_coordinates=c)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R3,
                room_arrival=R2,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=d)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R3,
                room_arrival=R7,
                relative_departure_coordinates=d,
                relative_arrival_coordinates=c)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R4,
                room_arrival=R0,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=a)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R4,
                room_arrival=R5,
                relative_departure_coordinates=c,
                relative_arrival_coordinates=a)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R4,
                room_arrival=R8,
                relative_departure_coordinates=d,
                relative_arrival_coordinates=c)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R5,
                room_arrival=R1,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=a)
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R5,
                room_arrival=R4,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=d)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R5,
                room_arrival=R6,
                relative_departure_coordinates=c,
                relative_arrival_coordinates=a)
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R5,
                room_arrival=R9,
                relative_departure_coordinates=d,
                relative_arrival_coordinates=c)
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R6,
                room_arrival=R2,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=a)
    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=R6,
                room_arrival=R5,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=d)
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R6,
                room_arrival=R7,
                relative_departure_coordinates=c,
                relative_arrival_coordinates=a)
    D20 = Door(two_way=False,
                tree=T20,
                name='D20',
                room_departure=R6,
                room_arrival=R10,
                relative_departure_coordinates=d,
                relative_arrival_coordinates=c)
    D21 = Door(two_way=False,
                tree=T21,
                name='D21',
                room_departure=R7,
                room_arrival=R3,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=a)
    D22 = Door(two_way=False,
                tree=T22,
                name='D22',
                room_departure=R7,
                room_arrival=R6,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=d)
    D23 = Door(two_way=False,
                tree=T23,
                name='D23',
                room_departure=R7,
                room_arrival=R11,
                relative_departure_coordinates=d,
                relative_arrival_coordinates=c)
    D24 = Door(two_way=False,
                tree=T24,
                name='D24',
                room_departure=R8,
                room_arrival=R4,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=a)
    D25 = Door(two_way=False,
                tree=T25,
                name='D25',
                room_departure=R8,
                room_arrival=R9,
                relative_departure_coordinates=c,
                relative_arrival_coordinates=a)
    D26 = Door(two_way=False,
                tree=T26,
                name='D26',
                room_departure=R8,
                room_arrival=R12,
                relative_departure_coordinates=d,
                relative_arrival_coordinates=c)
    D27 = Door(two_way=False,
                tree=T27,
                name='D27',
                room_departure=R9,
                room_arrival=R5,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=a)
    D28 = Door(two_way=False,
                tree=T28,
                name='D28',
                room_departure=R9,
                room_arrival=R8,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=d)
    D29 = Door(two_way=False,
                tree=T29,
                name='D29',
                room_departure=R9,
                room_arrival=R10,
                relative_departure_coordinates=c,
                relative_arrival_coordinates=a)
    D30 = Door(two_way=False,
                tree=T30,
                name='D30',
                room_departure=R9,
                room_arrival=R13,
                relative_departure_coordinates=d,
                relative_arrival_coordinates=c)
    D31 = Door(two_way=False,
                tree=T31,
                name='D31',
                room_departure=R10,
                room_arrival=R6,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=a)
    D32 = Door(two_way=False,
                tree=T32,
                name='D32',
                room_departure=R10,
                room_arrival=R9,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=d)
    D33 = Door(two_way=False,
                tree=T33,
                name='D33',
                room_departure=R10,
                room_arrival=R11,
                relative_departure_coordinates=c,
                relative_arrival_coordinates=a)
    D34 = Door(two_way=False,
                tree=T34,
                name='D34',
                room_departure=R10,
                room_arrival=R14,
                relative_departure_coordinates=d,
                relative_arrival_coordinates=c)
    D35 = Door(two_way=False,
                tree=T35,
                name='D35',
                room_departure=R11,
                room_arrival=R7,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=a)
    D36 = Door(two_way=False,
                tree=T36,
                name='D36',
                room_departure=R11,
                room_arrival=R10,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=d)
    D37 = Door(two_way=False,
                tree=T37,
                name='D37',
                room_departure=R11,
                room_arrival=R15)
    D38 = Door(two_way=False,
                tree=T38,
                name='D38',
                room_departure=R12,
                room_arrival=R8,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=a)
    D39 = Door(two_way=False,
                tree=T39,
                name='D39',
                room_departure=R12,
                room_arrival=R13,
                relative_departure_coordinates=c,
                relative_arrival_coordinates=a)
    D40 = Door(two_way=False,
                tree=T40,
                name='D40',
                room_departure=R13,
                room_arrival=R9,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=a)
    D41 = Door(two_way=False,
                tree=T41,
                name='D41',
                room_departure=R13,
                room_arrival=R12,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=d)
    D42 = Door(two_way=False,
                tree=T42,
                name='D42',
                room_departure=R13,
                room_arrival=R14,
                relative_departure_coordinates=c,
                relative_arrival_coordinates=a)
    D43 = Door(two_way=False,
                tree=T43,
                name='D43',
                room_departure=R14,
                room_arrival=R10,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=a)
    D44 = Door(two_way=False,
                tree=T44,
                name='D44',
                room_departure=R14,
                room_arrival=R13,
                relative_departure_coordinates=b,
                relative_arrival_coordinates=d)
    D45 = Door(two_way=False,
                tree=T45,
                name='D45',
                room_departure=R14,
                room_arrival=R15)
    D46= Door(two_way=False,
                tree=T46,
                name='D46',
                room_departure=R15,
                room_arrival=RE)
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30, D31, D32, D33, D34, D35, D36, D37, D38, D39, D40, D41, D42, D43, D44, D45, D46],
                 fastest_solution="D0 S0 D2 D1 S3 D11 S4 D15 S5 D17 S1 D6 S2 D9 S6 D23 S10 D36 S9 D32 S8 D28 S7 D26 S11 D39 S12 D42 S13 D45 D46",
                 level_color=Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.5),
                 name='Connect the dots',
                 keep_proportions=True,
                 door_window_size=250)
    
    return level