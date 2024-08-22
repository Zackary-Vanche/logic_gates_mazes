from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def level_desire_path(): 

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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18]

    V0 = Tree(tree_list=['INFOREQU', Tree.tree_list_SUM(len(Slist)), [None]],
              name='V0',
              switches=Slist + [5])
    
    tree_list_0 = Tree.tree_list_from_str('TF')

    T0 = Tree(tree_list=tree_list_0,
                        name='T0',
                        switches=[S0, S1, V0])
    T1 = Tree(tree_list=tree_list_0,
                        name='T1',
                        switches=[S1, S0, V0])
    T2 = Tree(tree_list=tree_list_0,
                        name='T2',
                        switches=[S0, S5, V0])
    T3 = Tree(tree_list=tree_list_0,
                        name='T3',
                        switches=[S5, S0, V0])
    T4 = Tree(tree_list=tree_list_0,
                        name='T4',
                        switches=[S1, S2, V0])
    T5 = Tree(tree_list=tree_list_0,
                        name='T5',
                        switches=[S2, S1, V0])
    T6 = Tree(tree_list=tree_list_0,
                        name='T6',
                        switches=[S1, S6, V0])
    T7 = Tree(tree_list=tree_list_0,
                        name='T7',
                        switches=[S6, S1, V0])
    T8 = Tree(tree_list=tree_list_0,
                        name='T8',
                        switches=[S2, S3, V0])
    T9 = Tree(tree_list=tree_list_0,
                        name='T9',
                        switches=[S3, S2, V0])
    T10 = Tree(tree_list=tree_list_0,
                        name='T10',
                        switches=[S2, S7, V0])
    T11 = Tree(tree_list=tree_list_0,
                        name='T11',
                        switches=[S7, S2, V0])
    T12 = Tree(tree_list=tree_list_0,
                        name='T12',
                        switches=[S3, S4, V0])
    T13 = Tree(tree_list=tree_list_0,
                        name='T13',
                        switches=[S4, S3, V0])
    T14 = Tree(tree_list=tree_list_0,
                        name='T14',
                        switches=[S3, S8, V0])
    T15 = Tree(tree_list=tree_list_0,
                        name='T15',
                        switches=[S8, S3, V0])
    T16 = Tree(tree_list=tree_list_0,
                        name='T16',
                        switches=[S4, S9, V0])
    T17 = Tree(tree_list=tree_list_0,
                        name='T17',
                        switches=[S9, S4, V0])
    T18 = Tree(tree_list=tree_list_0,
                        name='T18',
                        switches=[S5, S6, V0])
    T19 = Tree(tree_list=tree_list_0,
                        name='T19',
                        switches=[S6, S5, V0])
    T20 = Tree(tree_list=tree_list_0,
                        name='T20',
                        switches=[S5, S10, V0])
    T21 = Tree(tree_list=tree_list_0,
                        name='T21',
                        switches=[S10, S5, V0])
    T22 = Tree(tree_list=tree_list_0,
                        name='T22',
                        switches=[S6, S7, V0])
    T23 = Tree(tree_list=tree_list_0,
                        name='T23',
                        switches=[S7, S6, V0])
    T24 = Tree(tree_list=tree_list_0,
                        name='T24',
                        switches=[S6, S11, V0])
    T25 = Tree(tree_list=tree_list_0,
                        name='T25',
                        switches=[S11, S6, V0])
    T26 = Tree(tree_list=tree_list_0,
                        name='T26',
                        switches=[S7, S8, V0])
    T27 = Tree(tree_list=tree_list_0,
                        name='T27',
                        switches=[S8, S7, V0])
    T28 = Tree(tree_list=tree_list_0,
                        name='T28',
                        switches=[S7, S12, V0])
    T29 = Tree(tree_list=tree_list_0,
                        name='T29',
                        switches=[S12, S7, V0])
    T30 = Tree(tree_list=tree_list_0,
                        name='T30',
                        switches=[S8, S9, V0])
    T31 = Tree(tree_list=tree_list_0,
                        name='T31',
                        switches=[S9, S8, V0])
    T32 = Tree(tree_list=tree_list_0,
                        name='T32',
                        switches=[S8, S13, V0])
    T33 = Tree(tree_list=tree_list_0,
                        name='T33',
                        switches=[S13, S8, V0])
    T34 = Tree(tree_list=tree_list_0,
                        name='T34',
                        switches=[S9, S14, V0])
    T35 = Tree(tree_list=tree_list_0,
                        name='T35',
                        switches=[S14, S9, V0])
    T36 = Tree(tree_list=tree_list_0,
                        name='T36',
                        switches=[S10, S11, V0])
    T37 = Tree(tree_list=tree_list_0,
                        name='T37',
                        switches=[S11, S10, V0])
    T38 = Tree(tree_list=tree_list_0,
                        name='T38',
                        switches=[S10, S15, V0])
    T39 = Tree(tree_list=tree_list_0,
                        name='T39',
                        switches=[S15, S10, V0])
    T40 = Tree(tree_list=tree_list_0,
                        name='T40',
                        switches=[S11, S12, V0])
    T41 = Tree(tree_list=tree_list_0,
                        name='T41',
                        switches=[S12, S11, V0])
    T42 = Tree(tree_list=tree_list_0,
                        name='T42',
                        switches=[S11, S16, V0])
    T43 = Tree(tree_list=tree_list_0,
                        name='T43',
                        switches=[S16, S11, V0])
    T44 = Tree(tree_list=tree_list_0,
                        name='T44',
                        switches=[S12, S13, V0])
    T45 = Tree(tree_list=tree_list_0,
                        name='T45',
                        switches=[S13, S12, V0])
    T46 = Tree(tree_list=tree_list_0,
                        name='T46',
                        switches=[S12, S17, V0])
    T47 = Tree(tree_list=tree_list_0,
                        name='T47',
                        switches=[S17, S12, V0])
    T48 = Tree(tree_list=tree_list_0,
                        name='T48',
                        switches=[S13, S14, V0])
    T49 = Tree(tree_list=tree_list_0,
                        name='T49',
                        switches=[S14, S13, V0])
    T50 = Tree(tree_list=tree_list_0,
                        name='T50',
                        switches=[S13, S18, V0])
    T51 = Tree(tree_list=tree_list_0,
                        name='T51',
                        switches=[S18, S13, V0])
    T52 = Tree(tree_list=Tree.tree_list_AND(2),
                        name='T52',
                        switches=[S14, V0])
    T53 = Tree(tree_list=tree_list_0,
                        name='T53',
                        switches=[S15, S16, V0])
    T54 = Tree(tree_list=tree_list_0,
                        name='T54',
                        switches=[S16, S15, V0])
    T55 = Tree(tree_list=tree_list_0,
                        name='T55',
                        switches=[S16, S17, V0])
    T56 = Tree(tree_list=tree_list_0,
                        name='T56',
                        switches=[S17, S16, V0])
    T57 = Tree(tree_list=tree_list_0,
                        name='T57',
                        switches=[S17, S18, V0])
    T58 = Tree(tree_list=tree_list_0,
                        name='T58',
                        switches=[S18, S17, V0])
    T59 = Tree(tree_list=Tree.tree_list_AND(2),
                        name='T59',
                        switches=[S18, V0])
    T60 = Tree(tree_list=tree_list_0,
                        name='T60',
                        switches=[S1, S7, V0])
    T61 = Tree(tree_list=tree_list_0,
                        name='T61',
                        switches=[S7, S1, V0])
    T62 = Tree(tree_list=tree_list_0,
                        name='T62',
                        switches=[S12, S18, V0])
    T63 = Tree(tree_list=tree_list_0,
                        name='T63',
                        switches=[S18, S12, V0])

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S0])
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S1])
    R2 = Room(name='R2',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[S2])
    R3 = Room(name='R3',
                position=[3*dx, 0*dy, ex, ey],
                switches_list=[S3])
    R4 = Room(name='R4',
                position=[4*dx, 0*dy, ex, ey],
                switches_list=[S4])
    R5 = Room(name='R5',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S5])
    R6 = Room(name='R6',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S6])
    R7 = Room(name='R7',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S7])
    R8 = Room(name='R8',
                position=[3*dx, 1*dy, ex, ey],
                switches_list=[S8])
    R9 = Room(name='R9',
                position=[4*dx, 1*dy, ex, ey],
                switches_list=[S9])
    R10 = Room(name='R10',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S10])
    R11 = Room(name='R11',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S11])
    R12 = Room(name='R12',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S12])
    R13 = Room(name='R13',
                position=[3*dx, 2*dy, ex, ey],
                switches_list=[S13])
    R14 = Room(name='R14',
                position=[4*dx, 2*dy, ex, ey],
                switches_list=[S14])
    R15 = Room(name='R15',
                position=[0*dx, 3*dy, ex, ey],
                switches_list=[S15])
    R16 = Room(name='R16',
                position=[1*dx, 3*dy, ex, ey],
                switches_list=[S16])
    R17 = Room(name='R17',
                position=[2*dx, 3*dy, ex, ey],
                switches_list=[S17])
    R18 = Room(name='R18',
                position=[3*dx, 3*dy, ex, ey],
                switches_list=[S18])
    RE = Room(name='RE',
              position=[4*dx, 3*dy, ex, ey],
              is_exit=True)

    rp = 0.5
    ax = 0.25
    ay = 0.25
    rdc0 = [1/2, ay]
    rac0 = [1/2, ay]
    rdc1 = [1/2, 1-ay]
    rac1 = [1/2, 1-ay]
    rdc2 = [ax, 1/2]
    rac2 = [ax, 1/2]
    rdc3 = [1-ax, 1/2]
    rac3 = [1-ax, 1/2]
    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=rdc0,
                relative_arrival_coordinates=rac0,
                relative_position=rp)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R0,
                relative_departure_coordinates=rdc1,
                relative_arrival_coordinates=rac1,
                relative_position=rp)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=R5,
                relative_departure_coordinates=rdc2,
                relative_arrival_coordinates=rac2,
                relative_position=rp)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R5,
                room_arrival=R0,
                relative_departure_coordinates=rdc3,
                relative_arrival_coordinates=rac3,
                relative_position=rp)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=rdc0,
                relative_arrival_coordinates=rac0,
                relative_position=rp)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R2,
                room_arrival=R1,
                relative_departure_coordinates=rdc1,
                relative_arrival_coordinates=rac1,
                relative_position=rp)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R1,
                room_arrival=R6,
                relative_departure_coordinates=rdc2,
                relative_arrival_coordinates=rac2,
                relative_position=rp)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R6,
                room_arrival=R1,
                relative_departure_coordinates=rdc3,
                relative_arrival_coordinates=rac3,
                relative_position=rp)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R2,
                room_arrival=R3,
                relative_departure_coordinates=rdc0,
                relative_arrival_coordinates=rac0,
                relative_position=rp)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R3,
                room_arrival=R2,
                relative_departure_coordinates=rdc1,
                relative_arrival_coordinates=rac1,
                relative_position=rp)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R2,
                room_arrival=R7,
                relative_departure_coordinates=rdc2,
                relative_arrival_coordinates=rac2,
                relative_position=rp)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R7,
                room_arrival=R2,
                relative_departure_coordinates=rdc3,
                relative_arrival_coordinates=rac3,
                relative_position=rp)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R3,
                room_arrival=R4,
                relative_departure_coordinates=rdc0,
                relative_arrival_coordinates=rac0,
                relative_position=rp)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R4,
                room_arrival=R3,
                relative_departure_coordinates=rdc1,
                relative_arrival_coordinates=rac1,
                relative_position=rp)
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R3,
                room_arrival=R8,
                relative_departure_coordinates=rdc2,
                relative_arrival_coordinates=rac2,
                relative_position=rp)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R8,
                room_arrival=R3,
                relative_departure_coordinates=rdc3,
                relative_arrival_coordinates=rac3,
                relative_position=rp)

    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R4,
                room_arrival=R9,
                relative_departure_coordinates=rdc2,
                relative_arrival_coordinates=rac2,
                relative_position=rp)
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R9,
                room_arrival=R4,
                relative_departure_coordinates=rdc3,
                relative_arrival_coordinates=rac3,
                relative_position=rp)
    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=R5,
                room_arrival=R6,
                relative_departure_coordinates=rdc0,
                relative_arrival_coordinates=rac0,
                relative_position=rp)
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R6,
                room_arrival=R5,
                relative_departure_coordinates=rdc1,
                relative_arrival_coordinates=rac1,
                relative_position=rp)
    D20 = Door(two_way=False,
                tree=T20,
                name='D20',
                room_departure=R5,
                room_arrival=R10,
                relative_departure_coordinates=rdc2,
                relative_arrival_coordinates=rac2,
                relative_position=rp)
    D21 = Door(two_way=False,
                tree=T21,
                name='D21',
                room_departure=R10,
                room_arrival=R5,
                relative_departure_coordinates=rdc3,
                relative_arrival_coordinates=rac3,
                relative_position=rp)
    D22 = Door(two_way=False,
                tree=T22,
                name='D22',
                room_departure=R6,
                room_arrival=R7,
                relative_departure_coordinates=rdc0,
                relative_arrival_coordinates=rac0,
                relative_position=rp)
    D23 = Door(two_way=False,
                tree=T23,
                name='D23',
                room_departure=R7,
                room_arrival=R6,
                relative_departure_coordinates=rdc1,
                relative_arrival_coordinates=rac1,
                relative_position=rp)
    D24 = Door(two_way=False,
                tree=T24,
                name='D24',
                room_departure=R6,
                room_arrival=R11,
                relative_departure_coordinates=rdc2,
                relative_arrival_coordinates=rac2,
                relative_position=rp)
    D25 = Door(two_way=False,
                tree=T25,
                name='D25',
                room_departure=R11,
                room_arrival=R6,
                relative_departure_coordinates=rdc3,
                relative_arrival_coordinates=rac3,
                relative_position=rp)
    D26 = Door(two_way=False,
                tree=T26,
                name='D26',
                room_departure=R7,
                room_arrival=R8,
                relative_departure_coordinates=rdc0,
                relative_arrival_coordinates=rac0,
                relative_position=rp)
    D27 = Door(two_way=False,
                tree=T27,
                name='D27',
                room_departure=R8,
                room_arrival=R7,
                relative_departure_coordinates=rdc1,
                relative_arrival_coordinates=rac1,
                relative_position=rp)
    D28 = Door(two_way=False,
                tree=T28,
                name='D28',
                room_departure=R7,
                room_arrival=R12,
                relative_departure_coordinates=rdc2,
                relative_arrival_coordinates=rac2,
                relative_position=rp)
    D29 = Door(two_way=False,
                tree=T29,
                name='D29',
                room_departure=R12,
                room_arrival=R7,
                relative_departure_coordinates=rdc3,
                relative_arrival_coordinates=rac3,
                relative_position=rp)
    D30 = Door(two_way=False,
                tree=T30,
                name='D30',
                room_departure=R8,
                room_arrival=R9,
                relative_departure_coordinates=rdc0,
                relative_arrival_coordinates=rac0,
                relative_position=rp)
    D31 = Door(two_way=False,
                tree=T31,
                name='D31',
                room_departure=R9,
                room_arrival=R8,
                relative_departure_coordinates=rdc1,
                relative_arrival_coordinates=rac1,
                relative_position=rp)

    D32 = Door(two_way=False,
                tree=T32,
                name='D32',
                room_departure=R8,
                room_arrival=R13,
                relative_departure_coordinates=rdc2,
                relative_arrival_coordinates=rac2,
                relative_position=rp)
    D33 = Door(two_way=False,
                tree=T33,
                name='D33',
                room_departure=R13,
                room_arrival=R8,
                relative_departure_coordinates=rdc3,
                relative_arrival_coordinates=rac3,
                relative_position=rp)
    D34 = Door(two_way=False,
                tree=T34,
                name='D34',
                room_departure=R9,
                room_arrival=R14,
                relative_departure_coordinates=rdc2,
                relative_arrival_coordinates=rac2,
                relative_position=rp)
    D35 = Door(two_way=False,
                tree=T35,
                name='D35',
                room_departure=R14,
                room_arrival=R9,
                relative_departure_coordinates=rdc3,
                relative_arrival_coordinates=rac3,
                relative_position=rp)

    D36 = Door(two_way=False,
                tree=T36,
                name='D36',
                room_departure=R10,
                room_arrival=R11,
                relative_departure_coordinates=rdc0,
                relative_arrival_coordinates=rac0,
                relative_position=rp)
    D37 = Door(two_way=False,
                tree=T37,
                name='D37',
                room_departure=R11,
                room_arrival=R10,
                relative_departure_coordinates=rdc1,
                relative_arrival_coordinates=rac1,
                relative_position=rp)
    D38 = Door(two_way=False,
                tree=T38,
                name='D38',
                room_departure=R10,
                room_arrival=R15,
                relative_departure_coordinates=rdc2,
                relative_arrival_coordinates=rac2,
                relative_position=rp)
    D39 = Door(two_way=False,
                tree=T39,
                name='D39',
                room_departure=R15,
                room_arrival=R10,
                relative_departure_coordinates=rdc3,
                relative_arrival_coordinates=rac3,
                relative_position=rp)
    D40 = Door(two_way=False,
                tree=T40,
                name='D40',
                room_departure=R11,
                room_arrival=R12,
                relative_departure_coordinates=rdc0,
                relative_arrival_coordinates=rac0,
                relative_position=rp)
    D41 = Door(two_way=False,
                tree=T41,
                name='D41',
                room_departure=R12,
                room_arrival=R11,
                relative_departure_coordinates=rdc1,
                relative_arrival_coordinates=rac1,
                relative_position=rp)
    D42 = Door(two_way=False,
                tree=T42,
                name='D42',
                room_departure=R11,
                room_arrival=R16,
                relative_departure_coordinates=rdc2,
                relative_arrival_coordinates=rac2,
                relative_position=rp)
    D43 = Door(two_way=False,
                tree=T43,
                name='D43',
                room_departure=R16,
                room_arrival=R11,
                relative_departure_coordinates=rdc3,
                relative_arrival_coordinates=rac3,
                relative_position=rp)
    D44 = Door(two_way=False,
                tree=T44,
                name='D44',
                room_departure=R12,
                room_arrival=R13,
                relative_departure_coordinates=rdc0,
                relative_arrival_coordinates=rac0,
                relative_position=rp)
    D45 = Door(two_way=False,
                tree=T45,
                name='D45',
                room_departure=R13,
                room_arrival=R12,
                relative_departure_coordinates=rdc1,
                relative_arrival_coordinates=rac1,
                relative_position=rp)
    D46 = Door(two_way=False,
                tree=T46,
                name='D46',
                room_departure=R12,
                room_arrival=R17,
                relative_departure_coordinates=rdc2,
                relative_arrival_coordinates=rac2,
                relative_position=rp)
    D47 = Door(two_way=False,
                tree=T47,
                name='D47',
                room_departure=R17,
                room_arrival=R12,
                relative_departure_coordinates=rdc3,
                relative_arrival_coordinates=rac3,
                relative_position=rp)
    D48 = Door(two_way=False,
                tree=T48,
                name='D48',
                room_departure=R13,
                room_arrival=R14,
                relative_departure_coordinates=rdc0,
                relative_arrival_coordinates=rac0,
                relative_position=rp)
    D49 = Door(two_way=False,
                tree=T49,
                name='D49',
                room_departure=R14,
                room_arrival=R13,
                relative_departure_coordinates=rdc1,
                relative_arrival_coordinates=rac1,
                relative_position=rp)
    D50 = Door(two_way=False,
                tree=T50,
                name='D50',
                room_departure=R13,
                room_arrival=R18,
                relative_departure_coordinates=rdc2,
                relative_arrival_coordinates=rac2,
                relative_position=rp)
    D51 = Door(two_way=False,
                tree=T51,
                name='D51',
                room_departure=R18,
                room_arrival=R13,
                relative_departure_coordinates=rdc3,
                relative_arrival_coordinates=rac3,
                relative_position=rp)

    D52 = Door(two_way=False,
                tree=T52,
                name='D52',
                room_departure=R14,
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 1/2],
                relative_arrival_coordinates=[1/2, 1/2],
                relative_position=rp)
    D53 = Door(two_way=False,
                tree=T53,
                name='D53',
                room_departure=R15,
                room_arrival=R16,
                relative_departure_coordinates=rdc0,
                relative_arrival_coordinates=rac0,
                relative_position=rp)
    D54 = Door(two_way=False,
                tree=T54,
                name='D54',
                room_departure=R16,
                room_arrival=R15,
                relative_departure_coordinates=rdc1,
                relative_arrival_coordinates=rac1,
                relative_position=rp)
    D55 = Door(two_way=False,
                tree=T55,
                name='D55',
                room_departure=R16,
                room_arrival=R17,
                relative_departure_coordinates=rdc0,
                relative_arrival_coordinates=rac0,
                relative_position=rp)
    D56 = Door(two_way=False,
                tree=T56,
                name='D56',
                room_departure=R17,
                room_arrival=R16,
                relative_departure_coordinates=rdc1,
                relative_arrival_coordinates=rac1,
                relative_position=rp)
    D57 = Door(two_way=False,
                tree=T57,
                name='D57',
                room_departure=R17,
                room_arrival=R18,
                relative_departure_coordinates=rdc0,
                relative_arrival_coordinates=rac0,
                relative_position=rp)
    D58 = Door(two_way=False,
                tree=T58,
                name='D58',
                room_departure=R18,
                room_arrival=R17,
                relative_departure_coordinates=rdc1,
                relative_arrival_coordinates=rac1,
                relative_position=rp)
    D59 = Door(two_way=False,
                tree=T59,
                name='D59',
                room_departure=R18,
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 1/2],
                relative_arrival_coordinates=[1/2, 1/2],
                relative_position=rp)
    D60 = Door(two_way=False,
                tree=T60,
                name='D60',
                room_departure=R1,
                room_arrival=R7,
                relative_departure_coordinates=[1, 1],
                relative_arrival_coordinates=[0, 0],
                relative_position=0.3)
    D61 = Door(two_way=False,
                tree=T61,
                name='D61',
                room_departure=R7,
                room_arrival=R1,
                relative_departure_coordinates=[0, 0],
                relative_arrival_coordinates=[1, 1],
                relative_position=0.3)
    D62 = Door(two_way=False,
                tree=T62,
                name='D62',
                room_departure=R12,
                room_arrival=R18,
                relative_departure_coordinates=[1, 1],
                relative_arrival_coordinates=[0, 0],
                relative_position=0.3)
    D63 = Door(two_way=False,
                tree=T63,
                name='D63',
                room_departure=R18,
                room_arrival=R12,
                relative_departure_coordinates=[0, 0],
                relative_arrival_coordinates=[1, 1],
                relative_position=0.3)

    lcolor = Levels_colors_list.FROM_HUE(hu=0.2, sa=0.5, li=0.5)
    lcolor.room_color = Color.BLUE

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30, D31, D32, D33, D34, D35, D36, D37, D38, D39, D40, D41, D42, D43, D44, D45, D46, D47, D48, D49, D50, D51, D52, D53, D54, D55, D56, D57, D58, D59, D60, D61, D62, D63,],
                 fastest_solution="S0 D0 S1 D60 S7 D28 S12 D62 S18 D59",
                 level_color=lcolor,
                 name='Desire path',
                 keep_proportions=True,
                 door_window_size=300)

    # for door in level.doors_list:
    #     i = int(door.name.replace('D', ''))
    #     room_departure = door.room_departure
    #     room_arrival = door.room_arrival
    #     S0 = room_departure.switches_list[0]
    #     if room_arrival.is_exit:
    #         print(f'''    T{i} = Tree(tree_list=Tree.tree_list_AND(2),
    #                     name='T{i}',
    #                     switches=[{S0.name}, V0])''')
    #     else:
    #         S1 = room_arrival.switches_list[0]
    #         print(f'''    T{i} = Tree(tree_list=tree_list_0,
    #                     name='T{i}',
    #                     switches=[{S0.name}, {S1.name}, V0])''')
    
    return level