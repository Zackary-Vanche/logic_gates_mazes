from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from os.path import exists as os_path_exists

def level_cube(): 

    v = 1

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')

    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')

    S6 = Switch(name='S6', value=v)
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')

    S9 = Switch(name='S9')
    S10 = Switch(name='S10', value=v)
    S11 = Switch(name='S11')

    S12 = Switch(name='S12', value=v)
    S13 = Switch(name='S13', value=v)
    S14 = Switch(name='S14')

    S15 = Switch(name='S15')
    S16 = Switch(name='S16')
    S17 = Switch(name='S17', value=v)

    S18 = Switch(name='S18', value=v)
    S19 = Switch(name='S19')
    S20 = Switch(name='S20', value=v)

    S21 = Switch(name='S21')
    S22 = Switch(name='S22', value=v)
    S23 = Switch(name='S23', value=v)

    S24 = Switch(name='S24', value=v)
    S25 = Switch(name='S25', value=v)
    S26 = Switch(name='S26', value=v)
    
    tree_list_EQU_BIN = ['EQU', Tree.tree_list_BIN(3), [None]]
    def tree_list_IN_BIN(n):
        return ['IN', Tree.tree_list_BIN(3)] + [[None]]*n
    tree_list_IN_BIN_2 = tree_list_IN_BIN(2)
    tree_list_IN_BIN_3 = tree_list_IN_BIN(3)
    tree_list_IN_BIN_4 = tree_list_IN_BIN(4)
    tree_list_DIFF_BIN = ['DIFF'] + [Tree.tree_list_BIN(3)]*8
    
    tree_list_1 = ['AND',
                   tree_list_EQU_BIN,
                   ['EQU', Tree.tree_list_BIN(3), Tree.tree_list_BIN(3)]]
    tree_list_2 = ['AND',
                   tree_list_IN_BIN_2,
                   ['EQU', Tree.tree_list_BIN(3), Tree.tree_list_BIN(3)]]
    
    cut_expression = 0

    T0 = Tree(tree_list=tree_list_IN_BIN_4,
                empty=True,
                name='T0',
                switches=[S0, S1, S2, 1, 3, 4, 7])
    T1 = Tree(tree_list=tree_list_IN_BIN_3,
                empty=True,
                name='T1',
                switches=[S0, S1, S2, 2, 5, 6])
    T2 = Tree(tree_list=tree_list_DIFF_BIN,
                empty=True,
                name='T2',
                switches=[S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26],
                cut_expression=cut_expression)
    T3 = Tree(tree_list=tree_list_IN_BIN_3,
                empty=True,
                name='T3',
                switches=[S0, S1, S2, 1, 3, 4])
    T4 = Tree(tree_list=tree_list_DIFF_BIN,
                empty=True,
                name='T4',
                switches=[S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26],
                cut_expression=cut_expression)
    T5 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T5',
                switches=[S0, S1, S2, 1, 3,
                          S3, S4, S5,
                          S6, S7, S8,])
    T6 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T6',
                switches=[S0, S1, S2, 1, 4,
                          S6, S7, S8,
                          S24, S25, S26])
    T7 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T7',
                switches=[S0, S1, S2, 1, 5,
                          S24, S25, S26,
                          S21, S22, S23])
    T8 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T8',
                switches=[S0, S1, S2, 1, 6,
                          S21, S22, S23,
                          S3, S4, S5])
    T9 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T9',
                switches=[S0, S1, S2, 2, 3,
                          S12, S13, S14,
                          S9, S10, S11])
    T10 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T10',
                switches=[S0, S1, S2, 2, 6,
                          S9, S10, S11,
                          S15, S16, S17])
    T11 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T11',
                switches=[S0, S1, S2, 2, 5,
                          S15, S16, S17,
                          S18, S19, S20]) # 5
    T12 = Tree(tree_list=tree_list_2,
                empty=True,
                name='T12',
                switches=[S0, S1, S2, 2, 4,
                          S18, S19, S20,
                          S12, S13, S14]) # 4
    T13 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T13',
                switches=[S0, S1, S2, 6,
                          S3, S4, S5,
                          S9, S10, S11])
    T14 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T14',
                switches=[S0, S1, S2, 3,
                          S9, S10, S11,
                          S3, S4, S5])
    T15 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T15',
                switches=[S0, S1, S2, 3,
                          S6, S7, S8,
                          S12, S13, S14])
    T16 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T16',
                switches=[S0, S1, S2, 4,
                          S12, S13, S14,
                          S6, S7, S8])
    T17 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T17',
                switches=[S0, S1, S2, 6,
                          S15, S16, S17,
                          S21, S22, S23])
    T18 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T18',
                switches=[S0, S1, S2, 5,
                          S21, S22, S23,
                          S15, S16, S17])
    T19 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T19',
                switches=[S0, S1, S2, 5,
                          S18, S19, S20,
                          S24, S25, S26])
    T20 = Tree(tree_list=tree_list_1,
                empty=True,
                name='T20',
                switches=[S0, S1, S2, 4,
                          S24, S25, S26,
                          S18, S19, S20])
    filename = 'levels/CUBE_random_exits.txt'
    if os_path_exists(filename):
        with open(filename, 'r') as fr:
            lines = fr.readlines()
            exit_str = rd_choice(lines)
        T21 = Tree(tree_list=Tree.tree_list_from_str(exit_str),
                    empty=True,
                    name='T21',
                    switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26])
    else:
        T21 = Tree(tree_list=Tree.tree_list_from_str('111'),
                    empty=True,
                    name='T21',
                    switches=[S0, S1, S2])
    ex = 1
    ey = 0.5
    ax = 1
    ay = 1.1

    R0 = Room(name='R0',
                position=[0*ax, 10*ay, 9.5*ex, 1*ey],
                switches_list=[S0, S1, S2])
    R1 = Room(name='R1',
                position=[5*ax, 0*ay, 4.5*ex, 1*ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[0*ax, 2*ay, 3*ex, 1*ey],
                switches_list=[S3, S4, S5])
    R3 = Room(name='R3',
                position=[6*ax, 2*ay, 3*ex, 1*ey],
                switches_list=[S6, S7, S8])
    R4 = Room(name='R4',
                position=[1*ax, 4*ay, 3*ex, 1*ey],
                switches_list=[S9, S10, S11])
    R5 = Room(name='R5',
                position=[5*ax, 4*ay, 3*ex, 1*ey],
                switches_list=[S12, S13, S14])
    R6 = Room(name='R6',
                position=[1*ax, 6*ay, 3*ex, 1*ey],
                switches_list=[S15, S16, S17])
    R7 = Room(name='R7',
                position=[5*ax, 6*ay, 3*ex, 1*ey],
                switches_list=[S18, S19, S20])
    R8 = Room(name='R8',
                position=[0*ax, 8*ay, 3*ex, 1*ey],
                switches_list=[S21, S22, S23])
    R9 = Room(name='R9',
                position=[6*ax, 8*ay, 3*ex, 1*ey],
                switches_list=[S24, S25, S26])
    RE = Room(name='RE',
              position=[0*ax, 0*ay, 3.5*ex, 1*ey],
              is_exit=True)

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[9.25/9.5, 1/2],
                relative_arrival_coordinates=[4.25/4.5, 1/2])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R6,
                relative_departure_coordinates=[3.5/9.5, 0],
                relative_arrival_coordinates=[2.5/3, 1],
                relative_position=1/4)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R6,
                room_arrival=R0,
                relative_departure_coordinates=[2.5/3, 1],
                relative_arrival_coordinates=[3.5/9.5, 0],
                relative_position=1/4)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R3,
                relative_departure_coordinates=[2.5/4.5, 1/2],
                relative_arrival_coordinates=[1/3, 1/2])
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R3,
                room_arrival=R1,
                relative_departure_coordinates=[2/3, 1/2],
                relative_arrival_coordinates=[3.5/4.5, 1/2])
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R2,
                room_arrival=R3,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 1/2],
                relative_position=0.75/3)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R3,
                room_arrival=R9,
                relative_departure_coordinates=[2.5/3, 1/2],
                relative_arrival_coordinates=[2.5/3, 1/2],
                relative_position=1/5)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R9,
                room_arrival=R8,
                relative_departure_coordinates=[0, 1/2],
                relative_arrival_coordinates=[1, 1/2],
                relative_position=0.75/3)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R8,
                room_arrival=R2,
                relative_departure_coordinates=[0.5/3, 1/2],
                relative_arrival_coordinates=[0.5/3, 1/2],
                relative_position=1/5)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R5,
                room_arrival=R4)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R4,
                room_arrival=R6)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R6,
                room_arrival=R7)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R7,
                room_arrival=R5)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R2,
                room_arrival=R4,
                relative_departure_coordinates=[2/3, 1/2],
                relative_arrival_coordinates=[2/3, 1/2])
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R4,
                room_arrival=R2,
                relative_departure_coordinates=[1/3, 1/2],
                relative_arrival_coordinates=[1/3, 1/2])
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R3,
                room_arrival=R5,
                relative_departure_coordinates=[1/3, 1/2],
                relative_arrival_coordinates=[1/3, 1/2])
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R5,
                room_arrival=R3,
                relative_departure_coordinates=[2/3, 1/2],
                relative_arrival_coordinates=[2/3, 1/2])
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R6,
                room_arrival=R8,
                relative_departure_coordinates=[1/3, 1/2],
                relative_arrival_coordinates=[1/3, 1/2])
    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=R8,
                room_arrival=R6,
                relative_departure_coordinates=[2/3, 1/2],
                relative_arrival_coordinates=[2/3, 1/2])
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R7,
                room_arrival=R9,
                relative_departure_coordinates=[2/3, 1/2],
                relative_arrival_coordinates=[2/3, 1/2])
    D20 = Door(two_way=False,
                tree=T20,
                name='D20',
                room_departure=R9,
                room_arrival=R7,
                relative_departure_coordinates=[1/3, 1/2],
                relative_arrival_coordinates=[1/3, 1/2])
    D21 = Door(two_way=False,
                tree=T21,
                name='D21',
                room_departure=R1,
                room_arrival=RE,
                relative_departure_coordinates=[0, 1/2],
                relative_arrival_coordinates=[1, 1/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.5),
                 name='Cube',
                 keep_proportions=True,
                 door_window_size=1050,
                 random=True)
    
    return level