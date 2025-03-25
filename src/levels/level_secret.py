from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

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
    
    V1 = Tree(tree_list=Tree.tree_list_OR(2),
                name='V1',
                switches=[S0, S2])
    V2 = Tree(tree_list=Tree.tree_list_OR(2),
                name='V2',
                switches=[S0, S3])
    V3 = Tree(tree_list=Tree.tree_list_OR(2),
                name='V3',
                switches=[S0, S5])
    V4 = Tree(tree_list=Tree.tree_list_OR(2),
                name='V4',
                switches=[S1, S3])
    V5 = Tree(tree_list=Tree.tree_list_OR(2),
                name='V5',
                switches=[S1, S4])
    V6 = Tree(tree_list=Tree.tree_list_OR(2),
                name='V6',
                switches=[S1, S6])
    V7 = Tree(tree_list=Tree.tree_list_OR(2),
                name='V7',
                switches=[S2, S5])
    V8 = Tree(tree_list=Tree.tree_list_OR(2),
                name='V8',
                switches=[S3, S5])
    V9 = Tree(tree_list=Tree.tree_list_OR(2),
                name='V9',
                switches=[S3, S6])
    V10 = Tree(tree_list=Tree.tree_list_OR(2),
                name='V10',
                switches=[S4, S6])
    V11 = Tree(tree_list=Tree.tree_list_OR(2),
                name='V11',
                switches=[S5, S6])
    V12 = Tree(tree_list=Tree.tree_list_OR(2),
                name='V12',
                switches=[S5, S7])
    V13 = Tree(tree_list=Tree.tree_list_OR(2),
                name='V13',
                switches=[S6, S7])
    

    T0 = Tree(tree_list=["EQU", Tree.tree_list_SUM(8), [None]],
                name='T0',
                switches=[S0, S1, S2, S3, S4, S5, S6, S7, 2])
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[V1])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[V2])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[V3])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[V4])
    T5 = Tree(tree_list=[None],
                name='T5',
                switches=[V5])
    T6 = Tree(tree_list=[None],
                name='T6',
                switches=[V6])
    T7 = Tree(tree_list=[None],
                name='T7',
                switches=[V7])
    T8 = Tree(tree_list=[None],
                name='T8',
                switches=[V8])
    T9 = Tree(tree_list=[None],
                name='T9',
                switches=[V9])
    T10 = Tree(tree_list=[None],
                name='T10',
                switches=[V10])
    T11 = Tree(tree_list=[None],
                name='T11',
                switches=[V11])
    T12 = Tree(tree_list=[None],
                name='T12',
                switches=[V12])
    T13 = Tree(tree_list=[None],
                name='T13',
                switches=[V13])
    T14 = Tree(tree_list=["AND",
                          Tree.tree_list_AND(8),
                          ["DIFF", Tree.tree_list_SUM(4), [None]],
                          ["INF", Tree.tree_list_SUM(5), Tree.tree_list_SUM(5)]
                          ],
                name='T14',
                switches=[S8, S9, S10, S11, S12, S13, S14, S15,
                          V2, V4, V8, V9, 2,
                          V1, V2, V3, V7, V8,
                          V4, V5, V6, V9, V10])

    dx = 2
    dy = 2
    ex = 1
    ey = 1

    R0 = Room(name='R0',
                position=[2*dx, 2*dy, 5*ex, 3*ey],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7])
    R1 = Room(name='R1',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S8])
    R2 = Room(name='R2',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S9])
    R3 = Room(name='R3',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[S10])
    R4 = Room(name='R4',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S11])
    R5 = Room(name='R5',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S12])
    R6 = Room(name='R6',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S13])
    R7 = Room(name='R7',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S14])
    R8 = Room(name='R8',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S15])
    RE = Room(name='RE',
              position=[3*dx, 1*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R4,
                relative_departure_coordinates=[0, 0],
                relative_arrival_coordinates=[1, 1])
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R3)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R4)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R6)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R4)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R2,
                room_arrival=R5)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R2,
                room_arrival=R7)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R3,
                room_arrival=R6)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R4,
                room_arrival=R6)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R4,
                room_arrival=R7)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R5,
                room_arrival=R7)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R6,
                room_arrival=R7)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R6,
                room_arrival=R8)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R7,
                room_arrival=R8)
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R1,
                room_arrival=RE)
    
    doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14]

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, RE],
                 doors_list=doors_list,
                 fastest_solution="S2 S6 D0 S11 D9 S14 D6 S9 D6 D10 S12 D10 D13 S15 D13 D11 S13 D7 S10 D1 S8 D14",
                 level_color=get_color(),
                 name='Secret',
                 keep_proportions=True,
                 door_window_size=320)
    
    # for door in doors_list:
    #     ra = door.room_departure
    #     rb = door.room_arrival
    #     if ra.name == 'R0':
    #         continue
    #     if rb.name == 'RE':
    #         continue
    #     sa = "S" + str(int(ra.switches_list[0].name.replace('S', ''))-8)
    #     sb = "S" + str(int(rb.switches_list[0].name.replace('S', ''))-8)
    #     V = door.name.replace('D', 'V')
    #     print(f"""{V} = Tree(tree_list=Tree.tree_list_OR(2),
    #         name='{V}',
    #         switches=[{sa}, {sb}])""")
    # for door in doors_list:
    #     T = door.name.replace('D', 'T')
    #     V = door.name.replace('D', 'V')
    #     print(f"""{T} = Tree(tree_list=[None],
    #         name='{T}',
    #         switches=[{V}])""")
    
    return level

get_color = lambda : Levels_colors_list.opposite_hues(4)