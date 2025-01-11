from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from numpy import sqrt

def f():

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

    SN1 = Switch(value=1)
    SN2 = Switch(value=2)
    
    tree_list_SUM = ['SUM'] + [[None]]*4
    
    tree_list_EQU_SUM = ['EQU', tree_list_SUM, [None]]
    
    tree_list_DIFF = ['DIFF'] + [Tree.tree_list_BIN(4)]*4
    
    tree_list_1 = ['AND',
                   Tree.tree_list_NAND(3),
                   Tree.tree_list_NAND(3),
                   tree_list_EQU_SUM]

    T0 = Tree(tree_list=tree_list_1,
              name='T0',
              switches = [S0, S1, S2,
                          S1, S2, S3,
                          S0, S1, S2, S3, SN2])
    T1 = Tree(tree_list=tree_list_1,
              name='T1',
              switches = [S4, S5, S6,
                          S5, S6, S7,
                          S4, S5, S6, S7, SN2])
    T2 = Tree(tree_list=tree_list_1,
              name='T2',
              switches = [S8, S9, S10,
                          S9, S10, S11,
                          S8, S9, S10, S11, SN2])
    T3 = Tree(tree_list=tree_list_1,
              name='T3',
              switches = [S12, S13, S14,
                          S13, S14, S15,
                          S12, S13, S14, S15, SN2])
    T4 = Tree(tree_list=['AND'] + [Tree.tree_list_NAND(3)]*8 + [tree_list_EQU_SUM]*4 + [tree_list_DIFF]*2,
              name='T4',
              switches = [S0, S4, S8,
                          S4, S8, S12,
                          S1, S5, S9,
                          S5, S9, S13,
                          S2, S6, S10,
                          S6, S10, S14,
                          S3, S7, S11,
                          S7, S11, S15,
                          S0, S4, S8, S12, SN2,
                          S1, S5, S9, S13, SN2,
                          S2, S6, S10, S14, SN2,
                          S3, S7, S11, S15, SN2,
                          S0, S1, S2, S3,
                          S4, S5, S6, S7,
                          S8, S9, S10, S11,
                          S12, S13, S14, S15,
                          S0, S4, S8, S12,
                          S1, S5, S9, S13,
                          S2, S6, S10, S14,
                          S3, S7, S11, S15,
                          ],
              cut_expression=True)
    T5 = Tree(tree_list=['AND',
                         Tree.tree_list_XOR(4),
                         Tree.tree_list_XOR(4),
                         Tree.tree_list_XOR(2),
                         Tree.tree_list_OR(2)
                         ],
              name='T5',
              switches = [S1, S7, S8, S14,
                          S2, S4, S11, S13,
                          S3, S6,
                          S6, S12,
                          ])
    
    ex = 1
    ey = ex

    R0 = Room(name='R0',
              position = [0, 7, 4*ex, 1*ey],
              switches_list = [S0, S1, S2, S3,])
    R1 = Room(name='R1',
              position = [0, 2, 1*ex, 4*ey],
              switches_list = [S4, S5, S6, S7,])
    R2 = Room(name='R2',
              position = [2, 5, 4*ex, 1*ey],
              switches_list = [S8, S9, S10, S11,])
    R3 = Room(name='R3',
              position = [2, 0, 1*ex, 4*ey],
              switches_list = [S12, S13, S14, S15,])
    R4 = Room(name='R4',
              position = [4, 3, 3*ex, 1*ey],
              switches_list = [])
    R5 = Room(name='R5',
              position = [4, 0, 1*ex, 2*ey],
              switches_list = [])
    RE = Room(name='RE',
              position=[6-1+sqrt(2)/2, sqrt(2)/2, 1, 1],
              is_exit=True)   # E pour exit ou end

    rp = 1/2

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp,
              relative_departure_coordinates=[0, 0],
              relative_arrival_coordinates=[1, 1])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2,
              relative_position=rp,
              relative_departure_coordinates=[1, 1],
              relative_arrival_coordinates=[0, 0])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3,
              relative_position=rp,
              relative_departure_coordinates=[0, 0],
              relative_arrival_coordinates=[1, 1])
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=R4,
              relative_position=rp,
              relative_departure_coordinates=[1, 1],
              relative_arrival_coordinates=[0, 0])
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R4,
              room_arrival=R5,
              relative_position=rp,
              relative_departure_coordinates=[0, 0],
              relative_arrival_coordinates=[1, 1])
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R5,
              room_arrival=RE,
              relative_position=rp,
              relative_departure_coordinates=[1, 1],
              relative_arrival_coordinates=[1-sqrt(2)/2, 1-sqrt(2)/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5],
                 fastest_solution='S0 S1 D0 S5 S6 D1 S10 S11 D2 S12 S15 D3 D4 D5',
                 level_color=get_color(),
                 name='Takuzu',
                 door_window_size=600,
                 keep_proportions=True,
                 y_separation=40,
                 border=40)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.45, sa=0.4, li=0.25)