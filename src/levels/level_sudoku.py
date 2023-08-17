from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_sudoku(fast_solution_finding=False):
    
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
    S29 = Switch(name='S29')
    S30 = Switch(name='S30')
    S31 = Switch(name='S31')
    
    SN0 = Switch(name='0', value=0)
    SN1 = Switch(name='1', value=1)
    SN2 = Switch(name='2', value=2)
    SN3 = Switch(name='3', value=3)
    
    SNlist = [SN0, SN1, SN2, SN3]
    
    tree_list_0 = ['EQUSET'] + [Tree.tree_list_BIN(2)]*4 + [[None]]*4

    T0 = Tree(tree_list=tree_list_0,
              name='T0',
              switches = [S0, S1, S2, S3, S4, S5, S6, S7] + SNlist)
    T1 = Tree(tree_list=tree_list_0,
              name='T1',
              switches = [S8, S9, S10, S11, S12, S13, S14, S15] + SNlist)
    T2 = Tree(tree_list=tree_list_0,
              name='T2',
              switches = [S16, S17, S18, S19, S20, S21, S22, S23] + SNlist)
    T3 = Tree(tree_list=['AND'] + [tree_list_0]*9 + [['XOR'] + [[None]]*4] + [Tree.tree_list_OR(2),
                                                                              Tree.tree_list_NAND(2),
                                                                              Tree.tree_list_XOR(2)],
                name='T3',
                switches = [S24, S25, S26, S27, S28, S29, S30, S31,
                            SN0, SN1, SN2, SN3,
                            S0, S1, S8, S9, S16, S17, S24, S25,
                            SN0, SN1, SN2, SN3,
                            S2, S3, S10, S11, S18, S19, S26, S27,
                            SN0, SN1, SN2, SN3,
                            S4, S5, S12, S13, S20, S21, S28, S29,
                            SN0, SN1, SN2, SN3,
                            S6, S7, S14, S15, S22, S23, S30, S31,
                            SN0, SN1, SN2, SN3,
                            S0, S1, S2, S3, S8, S9, S10, S11,
                            SN0, SN1, SN2, SN3,
                            S4, S5, S6, S7, S12, S13, S14, S15,
                            SN0, SN1, SN2, SN3,
                            S16, S17, S18, S19, S24, S25, S26, S27,
                            SN0, SN1, SN2, SN3,
                            S20, S21, S22, S23, S28, S29, S30, S31,
                            SN0, SN1, SN2, SN3,
                            S0, S4, S16, S20,
                            S30, S14, S8, S18, S3, S7
                            ],
                cut_expression=True,
                cut_expression_separator=')')
    
    if fast_solution_finding:
        possible_switches_values = [[0, 0, 1, 0, 0, 1, 1, 1],
                                    [0, 0, 1, 0, 1, 1, 0, 1],
                                    [0, 0, 0, 1, 1, 0, 1, 1],
                                    [0, 0, 0, 1, 1, 1, 1, 0],
                                    [0, 0, 1, 1, 1, 0, 0, 1],
                                    [0, 0, 1, 1, 0, 1, 1, 0],
                                    [1, 0, 0, 0, 0, 1, 1, 1],
                                    [1, 0, 0, 0, 1, 1, 0, 1],
                                    [1, 0, 0, 1, 0, 0, 1, 1],
                                    [1, 0, 0, 1, 1, 1, 0, 0],
                                    [1, 0, 1, 1, 0, 0, 0, 1],
                                    [0, 0, 1, 1, 0, 1, 0, 0],
                                    [0, 1, 0, 0, 1, 0, 1, 1],
                                    [0, 1, 0, 0, 1, 1, 1, 0],
                                    [0, 1, 1, 0, 0, 0, 1, 1],
                                    [0, 1, 1, 0, 1, 1, 0, 0],
                                    [0, 1, 1, 1, 0, 0, 1, 0],
                                    [0, 1, 1, 1, 1, 0, 0, 0],
                                    [1, 1, 0, 0, 1, 0, 0, 1],
                                    [1, 1, 0, 0, 0, 1, 1, 0],
                                    [1, 1, 1, 0, 0, 0, 0, 1],
                                    [1, 1, 1, 0, 0, 1, 0, 0],
                                    [1, 1, 0, 1, 0, 0, 1, 0],
                                    [1, 1, 0, 1, 1, 0, 0, 0]]
    else:
        possible_switches_values = None

    R0 = Room(name='R0',
              position = [0, 3, 2, 4],
              switches_list = [S0, S1, S2, S3, S4, S5, S6, S7],
              possible_switches_values=possible_switches_values)
    R1 = Room(name='R1',
              position = [0, 0, 4, 2],
              switches_list = [S8, S9, S10, S11, S12, S13, S14, S15],
              possible_switches_values=possible_switches_values)
    R2 = Room(name='R2',
              position = [5, 0, 2, 4],
              switches_list = [S16, S17, S18, S19, S20, S21, S22, S23],
              possible_switches_values=possible_switches_values)
    R3 = Room(name='R3',
              position = [3, 5, 4, 2],
              switches_list = [S24, S25, S26, S27, S28, S29, S30, S31],
              possible_switches_values=possible_switches_values)
    RE = Room(name='RE',
              position=[3, 3, 1, 1],
              is_exit=True)   # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1/2, 0],
              relative_arrival_coordinates=[1/4, 1])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=[1, 1/2],
              relative_arrival_coordinates=[0, 1/4])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=[1/2, 1],
              relative_arrival_coordinates=[3/4, 0])
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=RE,
              relative_departure_coordinates=[1/8, 0],
              relative_arrival_coordinates=[1/2, 1])
    
    level = Maze(start_room_index=0, 
                 exit_room_index=-1, 
                 rooms_list=[R0, R1, R2, R3, RE], 
                 doors_list=[D0, D1, D2, D3], 
                 fastest_solution='S0 S1 S2 S7 D0 S9 S12 S14 S15 D1 S18 S19 S21 S22 D2 S24 S27 S28 S29 D3',
                 level_color=Levels_colors_list.FROM_HUE(0, sa=1, li=0.9),
                 name='Sudoku',
                 door_window_size = 600,
                 keep_proportions = True)

    return level