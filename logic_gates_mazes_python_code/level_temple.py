# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:54:32 2022

@author: utilisateur
"""


from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_temple():
    
    S0 = Switch(name='S0', value=1)
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    S9 = Switch(name='S9')
    S10 = Switch(name='S10', value=1)
    S11 = Switch(name='S11')
    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')
    S15 = Switch(name='S15')
    S16 = Switch(name='S16')
    S17 = Switch(name='S17')
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')
    S20 = Switch(name='S20', value=1)
    S21 = Switch(name='S21')
    S22 = Switch(name='S22')
    S23 = Switch(name='S23')
    S24 = Switch(name='S24')
    S25 = Switch(name='S25')
    S26 = Switch(name='S26')
    S27 = Switch(name='S27')
    S28 = Switch(name='S28')
    S29 = Switch(name='S29')

    T0 = Tree(tree_list=['OR', Tree.tree_list_nor_3, Tree.tree_list_XOR3],
              empty=True,
              name='T0',
              switches = [S27, S28, S29, S27, S28, S29])
    T1 = Tree(tree_list=['OR', Tree.tree_list_nor_3, Tree.tree_list_XOR3],
              empty=True,
              name='T1',
              switches = [S27, S28, S29, S27, S28, S29])
    T2 = Tree(tree_list=['OR', Tree.tree_list_nor_3, Tree.tree_list_XOR3],
              empty=True,
              name='T2',
              switches = [S27, S28, S29, S27, S28, S29])
    T3 = Tree(tree_list=Tree.tree_list_XOR3,
              empty=True,
              name='T3',
              switches = [S0, S1, S2])
    T4 = Tree(tree_list=Tree.tree_list_XOR3,
                empty=True,
                name='T4',
                switches = [S3, S4, S5])
    T5 = Tree(tree_list=Tree.tree_list_XOR3,
                empty=True,
                name='T5',
                switches = [S6, S7, S8])
    T6 = Tree(tree_list=['AND_4', 
                         Tree.tree_list_XOR3, 
                         Tree.tree_list_nand,
                         Tree.tree_list_nand,
                         Tree.tree_list_nand], # 1 9 2 9 2 10
                empty=True,
                name='T6',
                switches = [S9, S10, S11,
                            S1, S9,
                            S2, S9,
                            S2, S10])
    T7 = Tree(tree_list=['AND_4', 
                         Tree.tree_list_XOR3, 
                         Tree.tree_list_nand,
                         Tree.tree_list_nand,
                         Tree.tree_list_nand], # 4 12 5 12 5 13
                empty=True,
                name='T7',
                switches = [S12, S13, S14,
                            S4, S12,
                            S5, S12,
                            S5, S13])
    T8 = Tree(tree_list=['AND_4', 
                         Tree.tree_list_XOR3, 
                         Tree.tree_list_nand,
                         Tree.tree_list_nand,
                         Tree.tree_list_nand], # 7 15 8 15 8 16
                empty=True,
                name='T8',
                switches = [S15, S16, S17,
                            S7, S15,
                            S8, S15,
                            S8, S16])
    T9 = Tree(tree_list=['AND_4', 
                         Tree.tree_list_XOR3, 
                         Tree.tree_list_nand,
                         Tree.tree_list_nand,
                         Tree.tree_list_nand], # 10 18 11 18 11 19
                empty=True,
                name='T9',
                switches = [S18, S19, S20,
                            S10, S18,
                            S11, S18,
                            S11, S19])
    T10 = Tree(tree_list=['AND_4', 
                         Tree.tree_list_XOR3, 
                         Tree.tree_list_nand,
                         Tree.tree_list_nand,
                         Tree.tree_list_nand], # 13 21 14 21 14 22
                empty=True,
                name='T10',
                switches = [S21, S22, S23,
                            S13, S21,
                            S14, S21,
                            S14, S22])
    T11 = Tree(tree_list=['AND_4', 
                         Tree.tree_list_XOR3, 
                         Tree.tree_list_nand,
                         Tree.tree_list_nand,
                         Tree.tree_list_nand], # 16 24 17 24 17 25
                empty=True,
                name='T11',
                switches = [S24, S25, S26,
                            S16, S24,
                            S17, S24,
                            S17, S25])
    T12 = Tree(tree_list=Tree.tree_list_nor_3,
                empty=True,
                name='T12',
                switches = [S0, S1, S2])
    T13 = Tree(tree_list=Tree.tree_list_nor_3,
                empty=True,
                name='T13',
                switches = [S3, S4, S5])
    T14 = Tree(tree_list=Tree.tree_list_nor_3,
                empty=True,
                name='T14',
                switches = [S6, S7, S8])
    T15 = Tree(tree_list=Tree.tree_list_nor_6,
                empty=True,
                name='T15',
                switches = [S0, S1, S2, S9, S10, S11])
    T16 = Tree(tree_list=Tree.tree_list_nor_6,
                empty=True,
                name='T16',
                switches = [S3, S4, S5, S12, S13, S14])
    T17 = Tree(tree_list=Tree.tree_list_nor_6,
                empty=True,
                name='T17',
                switches = [S6, S7, S8, S15, S16, S17])
    T18 = Tree(tree_list=Tree.tree_list_nor_6,
                empty=True,
                name='T18',
                switches = [S9, S10, S11, S18, S19, S20])
    T19 = Tree(tree_list=Tree.tree_list_nor_6,
                empty=True,
                name='T19',
                switches = [S12, S13, S14, S21, S22, S23])
    T20 = Tree(tree_list=Tree.tree_list_nor_6,
                empty=True,
                name='T20',
                switches = [S15, S16, S17, S24, S25, S26])
    T21 = Tree(tree_list=Tree.tree_list_XOR10,
                empty=True,
                name='T21',
                switches = [S0, S3, S6,
                            S9, S12, S15,
                            S18, S21, S24,
                            S27])
    T22 = Tree(tree_list=Tree.tree_list_XOR10,
                empty=True,
                name='T22',
                switches = [S1, S4, S7,
                            S10, S13, S16,
                            S19, S22, S25,
                            S28])
    T23 = Tree(tree_list=Tree.tree_list_XOR10,
                empty=True,
                name='T23',
                switches = [S2, S5, S8,
                            S11, S14, S17,
                            S20, S23, S26,
                            S29])
    T24 = Tree(tree_list=Tree.tree_list_and_3,
                empty=True,
                name='T24',
                switches = [S6, S16, S26])
    
    R0 = Room(name='R0',
              position = [13.75, -3.75, 1.5, 1.5],
              switches_list = [])
    R1 = Room(name='R1',
              position = [0, 0, 4.5, 1.5],
              switches_list = [S0, S1, S2])
    R2 = Room(name='R2',
              position = [5, 0, 4.5, 1.5],
              switches_list = [S3, S4, S5])
    R3 = Room(name='R3',
              position = [10, 0, 4.5, 1.5],
              switches_list = [S6, S7, S8])
    R4 = Room(name='R4',
              position = [0, 4, 4.5, 1.5],
              switches_list = [S9, S10, S11])
    R5 = Room(name='R5',
              position = [5, 4, 4.5, 1.5],
              switches_list = [S12, S13, S14])
    R6 = Room(name='R6',
              position = [10, 4, 4.5, 1.5],
              switches_list = [S15, S16, S17])
    R7 = Room(name='R7',
              position = [0, 8, 4.5, 1.5],
              switches_list = [S18, S19, S20])
    R8 = Room(name='R8',
              position = [5, 8, 4.5, 1.5],
              switches_list = [S21, S22, S23])
    R9 = Room(name='R9',
              position = [10, 8, 4.5, 1.5],
              switches_list = [S24, S25, S26])
    R10 = Room(name='R10',
               position = [0, 13, 6, 1.5],
               switches_list = [S27, S28, S29])
    R11 = Room(name='R11',
               position = [9, 13, 1.5, 1.5],
               switches_list = [])
    R12 = Room(name='R12',
               position = [13.75, 13, 1.5, 1.5],
               switches_list = [])
    RE = Room(name='RE',
              position = [5, -3.5, 3, 1.5],
              is_exit = True)  # E pour exit ou end
    
    D0 = Door(two_way=False,
                tree=T0,
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=False,
                tree=T1,
                room_departure=R0,
                room_arrival=R2)
    D2 = Door(two_way=False,
                tree=T2,
                room_departure=R0,
                room_arrival=R3)
    D3 = Door(two_way=False,
                tree=T3,
                room_departure=R1,
                room_arrival=R4,
                relative_departure_coordinates=[1/5, 1/2],
                relative_arrival_coordinates=[1/5, 1/2])
    D4 = Door(two_way=False,
                tree=T4,
                room_departure=R2,
                room_arrival=R5,
                relative_departure_coordinates=[1/5, 1/2],
                relative_arrival_coordinates=[1/5, 1/2])
    D5 = Door(two_way=False,
                tree=T5,
                room_departure=R3,
                room_arrival=R6,
                relative_departure_coordinates=[1/5, 1/2],
                relative_arrival_coordinates=[1/5, 1/2])
    D6 = Door(two_way=False,
                tree=T6,
                room_departure=R4,
                room_arrival=R7,
                relative_departure_coordinates=[1/5, 1/2],
                relative_arrival_coordinates=[1/5, 1/2])
    D7 = Door(two_way=False,
                tree=T7,
                room_departure=R5,
                room_arrival=R8,
                relative_departure_coordinates=[1/5, 1/2],
                relative_arrival_coordinates=[1/5, 1/2])
    D8 = Door(two_way=False,
                tree=T8,
                room_departure=R6,
                room_arrival=R9,
                relative_departure_coordinates=[1/5, 1/2],
                relative_arrival_coordinates=[1/5, 1/2])
    D9 = Door(two_way=False,
                tree=T9,
                room_departure=R7,
                room_arrival=R10,
                relative_departure_coordinates=[1/5, 1/2],
                relative_arrival_coordinates=[1/5, 1/2])
    D10 = Door(two_way=False,
                tree=T10,
                room_departure=R8,
                room_arrival=R10,
                relative_departure_coordinates=[1/5, 1/2],
                relative_arrival_coordinates=[1/2, 1/2])
    D11 = Door(two_way=False,
                tree=T11,
                room_departure=R9,
                room_arrival=R10,
                relative_departure_coordinates=[1/5, 1/2],
                relative_arrival_coordinates=[4/5, 1/2])
    D12 = Door(two_way=False,
                tree=T12,
                room_departure=R1,
                room_arrival=R4,
                relative_departure_coordinates=[4/5, 1/2],
                relative_arrival_coordinates=[4/5, 1/2])
    D13 = Door(two_way=False,
                tree=T13,
                room_departure=R2,
                room_arrival=R5,
                relative_departure_coordinates=[4/5, 1/2],
                relative_arrival_coordinates=[4/5, 1/2])
    D14 = Door(two_way=False,
                tree=T14,
                room_departure=R3,
                room_arrival=R6,
                relative_departure_coordinates=[4/5, 1/2],
                relative_arrival_coordinates=[4/5, 1/2])
    D15 = Door(two_way=False,
                tree=T15,
                room_departure=R4,
                room_arrival=R7,
                relative_departure_coordinates=[4/5, 1/2],
                relative_arrival_coordinates=[4/5, 1/2])
    D16 = Door(two_way=False,
                tree=T16,
                room_departure=R5,
                room_arrival=R8,
                relative_departure_coordinates=[4/5, 1/2],
                relative_arrival_coordinates=[4/5, 1/2])
    D17 = Door(two_way=False,
                tree=T17,
                room_departure=R6,
                room_arrival=R9,
                relative_departure_coordinates=[4/5, 1/2],
                relative_arrival_coordinates=[4/5, 1/2])
    D18 = Door(two_way=False,
                tree=T18,
                room_departure=R7,
                room_arrival=R10,
                relative_departure_coordinates=[4/5, 1/2],
                relative_arrival_coordinates=[1/5, 1/2])
    D19 = Door(two_way=False,
                tree=T19,
                room_departure=R8,
                room_arrival=R10,
                relative_departure_coordinates=[4/5, 1/2],
                relative_arrival_coordinates=[1/2, 1/2])
    D20 = Door(two_way=False,
                tree=T20,
                room_departure=R9,
                room_arrival=R10,
                relative_departure_coordinates=[1, 1],
                relative_arrival_coordinates=[4/5, 1/2])
    D21 = Door(two_way=False,
                tree=T21,
                room_departure=R10,
                room_arrival=R11,
                relative_departure_coordinates=[5.5/6, 1/2])
    D22 = Door(two_way=False,
                tree=T22,
                room_departure=R11,
                room_arrival=R12)
    D23 = Door(two_way=False,
                tree=T23,
                room_departure=R12,
                room_arrival=R0,
                relative_departure_coordinates=[1,0],
                relative_arrival_coordinates=[1,1])
    D24 = Door(two_way=False,
                tree=T24,
                room_departure=R0,
                room_arrival=RE,
                relative_position=0.6)
    
    l_help_txt = [ 
"""This level is the retranscription of a really known puzzle game.
Once you find which game it is, the level is over.
"""]
        
    level = Maze(start_room_index=0, 
                 exit_room_index=-1, 
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, RE], 
                 doors_list = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24], 
                 fastest_solution="""D0 S0 D12 D6 D9 S27 D21 D22 D23
D2 D14 D17 S24 D11 S27 D21 D22 D23
D0 D12 S10 D15 D9 S28 D21 D22 D23
D2 D14 S15 D8 S24 S25 D11 S28 D21 D22 D23
D0 D12 D15 S20 D18 S29 D21 D22 D23
D2 S6 D5 S15 S16 D8 S25 S26 D11 S29 D21 D22 D23 D24""".replace('\n', ' '),
                 level_color=Levels_colors_list.BEIGE_AND_BROWN,
                 name='Temple',
                 help_txt = l_help_txt,
                 border = 30,
                 door_window_size = 575)

    return level

if __name__ == "__main__":
    
    level = level_temple
    
    level().try_solution('''
D0 S0 D12 D6 D9 S27 D21 D22 D23
D2 D14 D17 S24 D11 S27 D21 D22 D23
D0 D12 S10 D15 D9 S28 D21 D22 D23
D1 D13 D16 S22 D10 S28 D21 D22 D23
D2 D14 D17 S24 D20 S27 D21 D22 D23
D1 D13 S12 D7 D10 S27 D21 D22 D23
D0 D12 D15 S20 D18 S29 D21 D22 D23
D2 D14 D17 S26 D11 S29 D21 D22 D23
D1 D13 S12 D16 D10 S27 D21 D22 D23
D0 D12 D15 S18 D9 S27 D21 D22 D23
D1 D13 D16 S22 D19 S28 D21 D22 D23
D2 D14 S16 D8 D11 S28 D21 D22 D23
D0 D12 D15 S18 D18 S27 D21 D22 D23
D2 S6 D5 D8 D11 S27 D21 D22 D23
D24
''', verbose=2)

    solutions = level().find_all_solutions(verbose=3,
                                                  stop_at_first_solution=False)
    
    level().try_solution(solutions[-1],
                                verbose=3,
                                allow_all_doors=True,
                                allow_all_switches=True)
    
    solutions_reverse = level().find_all_solutions(verbose=3,
                                                          stop_at_first_solution=False,
                                                          reverse_actions_order=True)
    
    level().try_solution(solutions_reverse[-1],
                                verbose=3,
                                allow_all_doors=True,
                                allow_all_switches=True)
    
    print(solutions[-1])
    print(solutions_reverse[-1])