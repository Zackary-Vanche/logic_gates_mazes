from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from os.path import exists as os_path_exists

def level_line_and_columns(): 

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
    
    T0 = Tree(tree_list=[None],
                        name='T0',
                        switches=[1])
    T1 = Tree(tree_list=[None],
                        name='T1',
                        switches=[1])
    T2 = Tree(tree_list=[None],
                        name='T2',
                        switches=[1])
    T3 = Tree(tree_list=[None],
                        name='T3',
                        switches=[S0])
    T4 = Tree(tree_list=Tree.tree_list_AND(2),
                        name='T4',
                        switches=[S1, S0])
    T5 = Tree(tree_list=Tree.tree_list_AND(2),
                        name='T5',
                        switches=[S5, S0])
    T6 = Tree(tree_list=Tree.tree_list_AND(2),
                        name='T6',
                        switches=[S9, S0])
    T7 = Tree(tree_list=Tree.tree_list_AND(2),
                        name='T7',
                        switches=[S13, S0])
    T8 = Tree(tree_list=[None],
                        name='T8',
                        switches=[S0])
    T9 = Tree(tree_list=Tree.tree_list_AND(2),
                        name='T9',
                        switches=[S2, S0])
    T10 = Tree(tree_list=Tree.tree_list_AND(2),
                        name='T10',
                        switches=[S6, S0])
    T11 = Tree(tree_list=Tree.tree_list_AND(2),
                        name='T11',
                        switches=[S10, S0])
    T12 = Tree(tree_list=Tree.tree_list_AND(2),
                        name='T12',
                        switches=[S14, S0])
    T13 = Tree(tree_list=[None],
                        name='T13',
                        switches=[S0])
    T14 = Tree(tree_list=Tree.tree_list_AND(2),
                        name='T14',
                        switches=[S3, S0])
    T15 = Tree(tree_list=Tree.tree_list_AND(2),
                        name='T15',
                        switches=[S7, S0])
    T16 = Tree(tree_list=Tree.tree_list_AND(2),
                        name='T16',
                        switches=[S11, S0])
    T17 = Tree(tree_list=Tree.tree_list_AND(2),
                        name='T17',
                        switches=[S15, S0])
    T18 = Tree(tree_list=[None],
                        name='T18',
                        switches=[S0])
    T19 = Tree(tree_list=Tree.tree_list_AND(2),
                        name='T19',
                        switches=[S4, S0])
    T20 = Tree(tree_list=Tree.tree_list_AND(2),
                        name='T20',
                        switches=[S8, S0])
    T21 = Tree(tree_list=Tree.tree_list_AND(2),
                        name='T21',
                        switches=[S12, S0])
    T22 = Tree(tree_list=Tree.tree_list_AND(2),
                        name='T22',
                        switches=[S16, S0])
    T23 = Tree(tree_list=Tree.tree_list_NOT,
                        name='T23',
                        switches=[S0])
    T24 = Tree(tree_list=Tree.tree_list_from_str('TF'),
                        name='T24',
                        switches=[S1, S0])
    T25 = Tree(tree_list=Tree.tree_list_from_str('TF'),
                        name='T25',
                        switches=[S2, S0])
    T26 = Tree(tree_list=Tree.tree_list_from_str('TF'),
                        name='T26',
                        switches=[S3, S0])
    T27 = Tree(tree_list=Tree.tree_list_from_str('TF'),
                        name='T27',
                        switches=[S4, S0])
    T28 = Tree(tree_list=Tree.tree_list_NOT,
                        name='T28',
                        switches=[S0])
    T29 = Tree(tree_list=Tree.tree_list_from_str('TF'),
                        name='T29',
                        switches=[S5, S0])
    T30 = Tree(tree_list=Tree.tree_list_from_str('TF'),
                        name='T30',
                        switches=[S6, S0])
    T31 = Tree(tree_list=Tree.tree_list_from_str('TF'),
                        name='T31',
                        switches=[S7, S0])
    T32 = Tree(tree_list=Tree.tree_list_from_str('TF'),
                        name='T32',
                        switches=[S8, S0])
    T33 = Tree(tree_list=Tree.tree_list_NOT,
                        name='T33',
                        switches=[S0])
    T34 = Tree(tree_list=Tree.tree_list_from_str('TF'),
                        name='T34',
                        switches=[S9, S0])
    T35 = Tree(tree_list=Tree.tree_list_from_str('TF'),
                        name='T35',
                        switches=[S10, S0])
    T36 = Tree(tree_list=Tree.tree_list_from_str('TF'),
                        name='T36',
                        switches=[S11, S0])
    T37 = Tree(tree_list=Tree.tree_list_from_str('TF'),
                        name='T37',
                        switches=[S12, S0])
    T38 = Tree(tree_list=Tree.tree_list_NOT,
                        name='T38',
                        switches=[S0])
    T39 = Tree(tree_list=Tree.tree_list_from_str('TF'),
                        name='T39',
                        switches=[S13, S0])
    T40 = Tree(tree_list=Tree.tree_list_from_str('TF'),
                        name='T40',
                        switches=[S14, S0])
    T41 = Tree(tree_list=Tree.tree_list_from_str('TF'),
                        name='T41',
                        switches=[S15, S0])
    T42 = Tree(tree_list=Tree.tree_list_from_str('TF'),
                        name='T42',
                        switches=[S16, S0])
    filename = 'levels/Line_and_columns_random_exits.txt'
    if os_path_exists(filename):
        with open(filename, 'r') as fr:
            lines = fr.readlines()
            l = rd_choice(lines)
        T43 = Tree(tree_list=['AND',
                              Tree.tree_list_from_str(l[0:4]),
                              Tree.tree_list_from_str(l[4:8]),
                              Tree.tree_list_from_str(l[8:12]),
                              Tree.tree_list_from_str(l[12:16]),],
                    name='T43',
                    switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16],
                    cut_expression_depth_1=True)
    else:
        T43 = Tree(tree_list=[None],
                    name='T43',
                    switches=[S0])

    dx = 1.25
    dy = 1
    ex = 0.75
    ey = 0.25
    
    ex0 = 0.25
    ax0 = 0.5
    ey0 = 0.25
    ay0 = 0.5

    R0 = Room(name='R0',
                position=[0*dx, -ay0-ey0, 3*dx+ex, ey0],
                switches_list=[S0])
    R1 = Room(name='R1',
                position=[-ax0-ex0, 0*dy, ex0, 3*dy+ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[0*dx, 3*dy+ey+ay0, 3*dx+ex, ey0],
                switches_list=[])
    R3 = Room(name='R3',
                position=[3*dx+ex+ax0, 0*dy, ex0, 3*dy+ey],
                switches_list=[])
    R4 = Room(name='R4',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S1])
    R5 = Room(name='R5',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S2])
    R6 = Room(name='R6',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[S3])
    R7 = Room(name='R7',
                position=[3*dx, 0*dy, ex, ey],
                switches_list=[S4])
    R8 = Room(name='R8',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S5])
    R9 = Room(name='R9',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S6])
    R10 = Room(name='R10',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S7])
    R11 = Room(name='R11',
                position=[3*dx, 1*dy, ex, ey],
                switches_list=[S8])
    R12 = Room(name='R12',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S9])
    R13 = Room(name='R13',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S10])
    R14 = Room(name='R14',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S11])
    R15 = Room(name='R15',
                position=[3*dx, 2*dy, ex, ey],
                switches_list=[S12])
    R16 = Room(name='R16',
                position=[0*dx, 3*dy, ex, ey],
                switches_list=[S13])
    R17 = Room(name='R17',
                position=[1*dx, 3*dy, ex, ey],
                switches_list=[S14])
    R18 = Room(name='R18',
                position=[2*dx, 3*dy, ex, ey],
                switches_list=[S15])
    R19 = Room(name='R19',
                position=[3*dx, 3*dy, ex, ey],
                switches_list=[S16])
    RE = Room(name='RE',
              position=[4*dx, -ay0-ey0, 0.75, ey0],
              is_exit=True)
    
    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[1, 0])
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=[1, 1],
                relative_arrival_coordinates=[0, 0])
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[0, 1])

    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R0,
                room_arrival=R4,
                relative_departure_coordinates=[1/5, 1],
                relative_arrival_coordinates=[1/2, 0])
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R8)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R8,
                room_arrival=R12)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R12,
                room_arrival=R16)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R16,
                room_arrival=R2,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[1/5, 0])
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R0,
                room_arrival=R5,
                relative_departure_coordinates=[2/5, 1],
                relative_arrival_coordinates=[1/2, 0])
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R5,
                room_arrival=R9)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R9,
                room_arrival=R13)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R13,
                room_arrival=R17)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R17,
                room_arrival=R2,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[2/5, 0])
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R0,
                room_arrival=R6,
                relative_departure_coordinates=[3/5, 1],
                relative_arrival_coordinates=[1/2, 0])
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R6,
                room_arrival=R10)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R10,
                room_arrival=R14)
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R14,
                room_arrival=R18)
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R18,
                room_arrival=R2,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[3/5, 0])
    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=R0,
                room_arrival=R7,
                relative_departure_coordinates=[4/5, 1],
                relative_arrival_coordinates=[1/2, 0])
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R7,
                room_arrival=R11)
    D20 = Door(two_way=False,
                tree=T20,
                name='D20',
                room_departure=R11,
                room_arrival=R15)
    D21 = Door(two_way=False,
                tree=T21,
                name='D21',
                room_departure=R15,
                room_arrival=R19)
    D22 = Door(two_way=False,
                tree=T22,
                name='D22',
                room_departure=R19,
                room_arrival=R2,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[4/5, 0])
    
    D23 = Door(two_way=False,
                tree=T23,
                name='D23',
                room_departure=R1,
                room_arrival=R4,
                relative_departure_coordinates=[1, 1/5],
                relative_arrival_coordinates=[0, 1/2])
    D24 = Door(two_way=False,
                tree=T24,
                name='D24',
                room_departure=R4,
                room_arrival=R5)
    D25 = Door(two_way=False,
                tree=T25,
                name='D25',
                room_departure=R5,
                room_arrival=R6)
    D26 = Door(two_way=False,
                tree=T26,
                name='D26',
                room_departure=R6,
                room_arrival=R7)
    D27 = Door(two_way=False,
                tree=T27,
                name='D27',
                room_departure=R7,
                room_arrival=R3,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 1/5])
    D28 = Door(two_way=False,
                tree=T28,
                name='D28',
                room_departure=R1,
                room_arrival=R8,
                relative_departure_coordinates=[1, 2/5],
                relative_arrival_coordinates=[0, 1/2])
    D29 = Door(two_way=False,
                tree=T29,
                name='D29',
                room_departure=R8,
                room_arrival=R9)
    D30 = Door(two_way=False,
                tree=T30,
                name='D30',
                room_departure=R9,
                room_arrival=R10)
    D31 = Door(two_way=False,
                tree=T31,
                name='D31',
                room_departure=R10,
                room_arrival=R11)
    D32 = Door(two_way=False,
                tree=T32,
                name='D32',
                room_departure=R11,
                room_arrival=R3,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 2/5])
    D33 = Door(two_way=False,
                tree=T33,
                name='D33',
                room_departure=R1,
                room_arrival=R12,
                relative_departure_coordinates=[1, 3/5],
                relative_arrival_coordinates=[0, 1/2])
    D34 = Door(two_way=False,
                tree=T34,
                name='D34',
                room_departure=R12,
                room_arrival=R13)
    D35 = Door(two_way=False,
                tree=T35,
                name='D35',
                room_departure=R13,
                room_arrival=R14)
    D36 = Door(two_way=False,
                tree=T36,
                name='D36',
                room_departure=R14,
                room_arrival=R15)
    D37 = Door(two_way=False,
                tree=T37,
                name='D37',
                room_departure=R15,
                room_arrival=R3,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 3/5])
    D38 = Door(two_way=False,
                tree=T38,
                name='D38',
                room_departure=R1,
                room_arrival=R16,
                relative_departure_coordinates=[1, 4/5],
                relative_arrival_coordinates=[0, 1/2])
    D39 = Door(two_way=False,
                tree=T39,
                name='D39',
                room_departure=R16,
                room_arrival=R17)
    D40 = Door(two_way=False,
                tree=T40,
                name='D40',
                room_departure=R17,
                room_arrival=R18)
    D41 = Door(two_way=False,
                tree=T41,
                name='D41',
                room_departure=R18,
                room_arrival=R19)
    D42 = Door(two_way=False,
                tree=T42,
                name='D42',
                room_departure=R19,
                room_arrival=R3,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 4/5])
    D43 = Door(two_way=False,
                tree=T43,
                name='D43',
                room_departure=R3,
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[1/2, 1])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30, D31, D32, D33, D34, D35, D36, D37, D38, D39, D40, D41, D42, D43],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0.85, sa=0.5, li=0.3),
                 name='Line and columns',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level
