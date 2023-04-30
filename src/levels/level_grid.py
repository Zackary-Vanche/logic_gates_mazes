from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from os.path import exists as os_path_exists
from Color import Color

def level_grid(): 

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
    
    tree_list_1 = ['EQU', Tree.tree_list_BIN(2), [None]]
    tree_list_2 = ['AND',
                   tree_list_1,
                   ['EQU', Tree.tree_list_not, [None]]]

    T0 = Tree(tree_list=['EQU'] + [Tree.tree_list_BIN(9)]*2,
                empty=True,
                name='T0',
                switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8,
                          S13, S14, S15, S16, S17, S18, S19, S20, S21])
    T1 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T1',
                switches=[S9, S10, 1])
    T2 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T2',
                switches=[S9, S10, 2])
    T3 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T3',
                switches=[S9, S10, 3])
    T4 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T4',
                switches=[S9, S10, 1, S0, S13])
    T5 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T5',
                switches=[S9, S10, 2, S3, S16])
    T6 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T6',
                switches=[S9, S10, 3, S6, S19])
    T7 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T7',
                switches=[S9, S10, 1, S1, S14])
    T8 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T8',
                switches=[S9, S10, 2, S4, S17])
    T9 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T9',
                switches=[S9, S10, 3, S7, S20])
    T10 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T10',
                switches=[S9, S10, 1, S2, S15])
    T11 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T11',
                switches=[S9, S10, 2, S5, S18])
    T12 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T12',
                switches=[S9, S10, 3, S8, S21])
    T13 = Tree(tree_list=[None],
                empty=True,
                name='T13',
                switches=[1])
    T14 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T14',
                switches=[S11, S12, 1])
    T15 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T15',
                switches=[S11, S12, 2])
    T16 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T16',
                switches=[S11, S12, 3])
    T17 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T17',
                switches=[S11, S12, 1, S6, S19])
    T18 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T18',
                switches=[S11, S12, 2, S7, S20])
    T19 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T19',
                switches=[S11, S12, 3, S8, S21])
    T20 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T20',
                switches=[S11, S12, 1, S3, S16])
    T21 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T21',
                switches=[S11, S12, 2, S4, S17])
    T22 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T22',
                switches=[S11, S12, 3, S5, S18])
    T23 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T23',
                switches=[S11, S12, 1, S0, S13])
    T24 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T24',
                switches=[S11, S12, 2, S1, S14])
    T25 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T25',
                switches=[S11, S12, 3, S2, S15])
    T26 = Tree(tree_list=['EQU', ['SUM'] + [Tree.tree_list_XOR(2)]*9, [None]],
                empty=True,
                name='T26',
                switches=[S0, S13,
                          S1, S14,
                          S2, S15,
                          S3, S16,
                          S4, S17,
                          S5, S18,
                          S6, S19,
                          S7, S20,
                          S8, S21,
                          5])
    filename = 'levels/Grid_random_exits.txt'
    if os_path_exists(filename):
        with open(filename, 'r') as fr:
            lines = fr.readlines()
            l = rd_choice(lines)
        T27 = Tree(tree_list=Tree.tree_list_from_str(l[:13]),
                   empty=True,
                   name='T27',
                   switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12])
    else:
        T27 = Tree(tree_list=Tree.tree_list_AND(4),
                    empty=True,
                    name='T27',
                    switches=[S9, S10, S11, S12])

    ex = 0.9
    ey = 0.9
    epsilon = 0.4
    
    # [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24]

    R0 = Room(name='R0',
              position=[-1, 2, 2+ex, 2+ey],
              switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8])
    R1 = Room(name='R1',
                position=[2+ex, 2, 2+ex, ey],
                switches_list=[S9, S10, S11, S12])
    R2 = Room(name='R2',
                position=[2, 4, ex, ey],
                switches_list=[S13])
    R3 = Room(name='R3',
                position=[2, 6, ex, ey],
                switches_list=[S14])
    R4 = Room(name='R4',
                position=[2, 8, ex, ey],
                switches_list=[S15])
    R5 = Room(name='R5',
                position=[4, 4, ex, ey],
                switches_list=[S16])
    R6 = Room(name='R6',
                position=[4, 6, ex, ey],
                switches_list=[S17])
    R7 = Room(name='R7',
                position=[4, 8, ex, ey],
                switches_list=[S18])
    R8 = Room(name='R8',
                position=[6, 4, ex, ey],
                switches_list=[S19])
    R9 = Room(name='R9',
                position=[6, 6, ex, ey],
                switches_list=[S20])
    R10 = Room(name='R10',
                position=[6, 8, ex, ey],
                switches_list=[S21])
    R11 = Room(name='R11',
                position=[4, 10, 2+ex, epsilon],
                switches_list=[])
    R12 = Room(name='R12',
                position=[8, 6, epsilon, 2+ey],
                switches_list=[])
    R13 = Room(name='R13',
                position=[0, 6, ex, ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[6+ex, 2, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1, ex/2/(2+ex)],
                relative_arrival_coordinates=[0, 1/2])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=[0.5/3, 1/2])
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R5,
                relative_departure_coordinates=[1.5/3, 1/2])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R8,
                relative_departure_coordinates=[2.5/3, 1/2])
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R3)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R5,
                room_arrival=R6)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R8,
                room_arrival=R9)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R3,
                room_arrival=R4)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R6,
                room_arrival=R7)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R9,
                room_arrival=R10)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R4,
                room_arrival=R11,
                relative_arrival_coordinates=[0.5/3, 1])
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R7,
                room_arrival=R11,
                relative_arrival_coordinates=[1.5/3, 1])
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R10,
                room_arrival=R11,
                relative_arrival_coordinates=[2.5/3, 1])
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R11,
                room_arrival=R12,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[0, 1])
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R12,
                room_arrival=R8,
                relative_departure_coordinates=[0, 0],
                relative_arrival_coordinates=[1, 1])
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R12,
                room_arrival=R9,
                relative_departure_coordinates=[1, 1.5/3])
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R12,
                room_arrival=R10,
                relative_departure_coordinates=[1, 2.5/3])
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R8,
                room_arrival=R5)
    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=R9,
                room_arrival=R6)
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R10,
                room_arrival=R7)
    D20 = Door(two_way=False,
                tree=T20,
                name='D20',
                room_departure=R5,
                room_arrival=R2)
    D21 = Door(two_way=False,
                tree=T21,
                name='D21',
                room_departure=R6,
                room_arrival=R3)
    D22 = Door(two_way=False,
                tree=T22,
                name='D22',
                room_departure=R7,
                room_arrival=R4)
    D23 = Door(two_way=False,
                tree=T23,
                name='D23',
                room_departure=R2,
                room_arrival=R13)
    D24 = Door(two_way=False,
                tree=T24,
                name='D24',
                room_departure=R3,
                room_arrival=R13)
    D25 = Door(two_way=False,
                tree=T25,
                name='D25',
                room_departure=R4,
                room_arrival=R13)
    D26 = Door(two_way=False,
                tree=T26,
                name='D26',
                room_departure=R13,
                room_arrival=R0,
                relative_departure_coordinates=[0, 0],
                relative_arrival_coordinates=[0, 1])
    D27 = Door(two_way=False,
                tree=T27,
                name='D27',
                room_departure=R1,
                room_arrival=RE,
                relative_departure_coordinates=[2.5/3, 1/2])
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0.65, sa=0.5, li=0.6)
    lcolor.background_color = Color.BLACK_BLUE
    lcolor.surrounding_color = Color.IVORY

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27],
                 fastest_solution=None,
                 level_color=lcolor,
                 name='Grid',
                 keep_proportions=True,
                 door_window_size=800)
    
    return level

