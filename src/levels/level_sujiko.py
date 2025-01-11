from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

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
    
    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    Slist_3 = [S9, S10, S11]
    Slist_4 = [S12, S13, S14]
    Slist_5 = [S15, S16, S17]
    Slist_6 = [S18, S19, S20]
    Slist_7 = [S21, S22, S23]
    Slist_8 = [S24, S25, S26, S27]
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_0)),
              name='V0',
              switches=Slist_0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_1)),
              name='V1',
              switches=Slist_1)
    V2 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_2)),
              name='V2',
              switches=Slist_2)
    V3 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_3)),
              name='V3',
              switches=Slist_3)
    V4 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_4)),
              name='V4',
              switches=Slist_4)
    V5 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_5)),
              name='V5',
              switches=Slist_5)
    V6 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_6)),
              name='V6',
              switches=Slist_6)
    V7 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_7)),
              name='V7',
              switches=Slist_7)
    V8 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_8)),
              name='V8',
              switches=Slist_8)
    
    tree_list_EQU = ['EQU', ['SUM'] + [[None]]*4, [None]]

    
    T0 = Tree(tree_list=[None],
              name='T0',
              switches = [1])
    T1 = Tree(tree_list=[None],
              name='T1',
              switches = [1])
    T2 = Tree(tree_list=[None],
              name='T2',
              switches = [1])
    T3 = Tree(tree_list=[None],
              name='T3',
              switches = [1])
    T4 = Tree(tree_list=tree_list_EQU,
              name='T4',
              switches = [V0, V1, V3, V4, 14])
    T5 = Tree(tree_list=tree_list_EQU,
              name='T5',
              switches = [V1, V2, V4, V5, 13])
    T6 = Tree(tree_list=Tree.tree_list_OR(2),
                name='T6',
                switches = [S12, S16])
    T7 = Tree(tree_list=tree_list_EQU,
                name='T7',
                switches = [V3, V4, V6, V7, 12])
    T8 = Tree(tree_list=['AND',
                            ['EQU', ['SUM'] + [[None]]*3 + [[None]], [None]],
                            ['DIFF'] + [[None]]*8 + [[None]]],
                name='T8',
                switches = [V4, V5, V7, V8, 11,
                            V0, V1, V2, V3, V4, V5, V6, V7, V8])
    
    lx = 1
    ly = 4
    dx = lx+1.25
    dy = ly+1.5
    ey = 1.2
    
    R0 = Room(name='R0',
              position = [3*dx, 0, lx, ly],
              switches_list = Slist_0)
    R1 = Room(name='R1',
              position = [2*dx, -ey, lx, ly],
              switches_list = Slist_1)
    R2 = Room(name='R2',
              position = [dx, 0, lx, ly],
              switches_list = Slist_2)
    R3 = Room(name='R3',
              position = [0, -ey, lx, ly],
              switches_list = Slist_3)
    R4 = Room(name='R4',
              position = [0, dy, lx, ly],
              switches_list = Slist_4)
    R5 = Room(name='R5',
              position = [dx, dy-ey, lx, ly],
              switches_list = Slist_5)
    R6 = Room(name='R6',
              position = [2*dx, dy, lx, ly],
              switches_list = Slist_6)
    R7 = Room(name='R7',
              position = [3*dx, dy-ey, lx, ly],
              switches_list = Slist_7)
    R8 = Room(name='R8',
              position = [4*dx, dy-ey, lx, ly+1],
              switches_list = Slist_8)
    RE = Room(name='RE',
              position=[4*dx-0.1, -ey, lx+0.2, ly-1],
              is_exit=True)   # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[0, 0],
              relative_arrival_coordinates=[1, 0])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[1, 1])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=[0, 0],
              relative_arrival_coordinates=[1, 0])
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=R4)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R4,
              room_arrival=R5,
              relative_departure_coordinates=[1, 0],
              relative_arrival_coordinates=[0, 0])
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R5,
              room_arrival=R6,
              relative_departure_coordinates=[1, 1],
              relative_arrival_coordinates=[0, 1])
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R6,
              room_arrival=R7,
              relative_departure_coordinates=[1, 0],
              relative_arrival_coordinates=[0, 0])
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R7,
              room_arrival=R8,
              relative_departure_coordinates=[1, 1],
              relative_arrival_coordinates=[0, 1])
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R8,
              room_arrival=RE,
              relative_departure_coordinates=[1/2, 0],
              relative_arrival_coordinates=[1/2, 1])
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8],
                 fastest_solution='S2 D0 S3 S4 D1 S6 S7 S8 D2 S10 S11 D3 S12 D4 S16 D5 S18 S20 D6 D7 S27 D8',
                 level_color=get_color(),
                 name='Sujiko',
                 door_window_size=400,
                 keep_proportions=True)

    return level

def get_color():
    return Levels_colors_list.FROM_HUE(0.9, sa=1, li=0.3)