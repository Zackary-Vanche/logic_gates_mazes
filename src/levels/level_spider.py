from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_spider(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')

    T0 = Tree(tree_list=Tree.tree_list_not,
                     name='T0',
                     switches=[S0])
    T1 = Tree(tree_list=[None],
                     name='T1',
                     switches=[S0])
    T2 = Tree(tree_list=Tree.tree_list_not,
                     name='T2',
                     switches=[S1])
    T3 = Tree(tree_list=[None],
                     name='T3',
                     switches=[S1])
    T4 = Tree(tree_list=[None],
                     name='T4',
                     switches=[S0])
    T5 = Tree(tree_list=Tree.tree_list_not,
                     name='T5',
                     switches=[S0])
    T6 = Tree(tree_list=[None],
                     name='T6',
                     switches=[S1])
    T7 = Tree(tree_list=Tree.tree_list_not,
                     name='T7',
                     switches=[S1])
    T8 = Tree(tree_list=Tree.tree_list_not,
                     name='T8',
                     switches=[S2])
    T9 = Tree(tree_list=[None],
                     name='T9',
                     switches=[S5])
    T10 = Tree(tree_list=Tree.tree_list_not,
                     name='T10',
                     switches=[S3])
    T11 = Tree(tree_list=[None],
                     name='T11',
                     switches=[S3])
    T12 = Tree(tree_list=Tree.tree_list_not,
                     name='T12',
                     switches=[S5])
    T13 = Tree(tree_list=[None],
                     name='T13',
                     switches=[S2])
    T14 = Tree(tree_list=Tree.tree_list_not,
                     name='T14',
                     switches=[S4])
    T15 = Tree(tree_list=[None],
                     name='T15',
                     switches=[S4])
    T16 = Tree(tree_list=[None],
                     name='T16',
                     switches=[S3])
    T17 = Tree(tree_list=Tree.tree_list_not,
                     name='T17',
                     switches=[S3])
    T18 = Tree(tree_list=[None],
                     name='T18',
                     switches=[S4])
    T19 = Tree(tree_list=Tree.tree_list_not,
                     name='T19',
                     switches=[S4])

    T20 = Tree(tree_list=Tree.tree_list_AND(6),
                name='T20',
                switches=[S0, S1, S2, S3, S4, S5])
    
    ex = 0.3
    ey = 0.3

    R0 = Room(name='R0',
                position=[0, 5, 3, ey],
                switches_list=[])
    R1 = Room(name='R1',
                position=[0, 3, 1, 1],
                switches_list=[S0])
    R2 = Room(name='R2',
                position=[2, 3, 1, 1],
                switches_list=[S1])
    R3 = Room(name='R3',
                position=[-1-ex, 1, ex, 3],
                switches_list=[])
    R4 = Room(name='R4',
                position=[4, 1, ex, 3],
                switches_list=[])
    R5 = Room(name='R5',
                position=[1, 2, 1, 1],
                switches_list=[S2, S5])
    R6 = Room(name='R6',
                position=[0, 1, 1, 1],
                switches_list=[S3])
    R7 = Room(name='R7',
                position=[2, 1, 1, 1],
                switches_list=[S4])
    R8 = Room(name='R8',
                position=[0, -ey, 3, ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[4, 5, 1, ey],
              is_exit=True)
    
    rp = 0.4

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R0,
                relative_arrival_coordinates=[0, 1])

    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=R2)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R0,
                relative_arrival_coordinates=[1, 1])

    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R1,
                room_arrival=R3,
                relative_arrival_coordinates=[0, 1])
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R1)

    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R2,
                room_arrival=R4,
                relative_arrival_coordinates=[1, 1])
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R4,
                room_arrival=R2)

    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R3,
                room_arrival=R5,
                relative_position=rp)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R5,
                room_arrival=R3,
                relative_position=rp)

    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R3,
                room_arrival=R6)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R6,
                room_arrival=R3,
                relative_arrival_coordinates=[0, 0])

    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R4,
                room_arrival=R5,
                relative_position=rp)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R5,
                room_arrival=R4,
                relative_position=rp)

    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R4,
                room_arrival=R7)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R7,
                room_arrival=R4,
                relative_arrival_coordinates=[1, 0])

    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R6,
                room_arrival=R8,
                relative_arrival_coordinates=[0, 0])
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R8,
                room_arrival=R6)

    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=R7,
                room_arrival=R8,
                relative_arrival_coordinates=[1, 0])
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R8,
                room_arrival=R7)

    D20 = Door(two_way=False,
                tree=T20,
                name='D20',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 1/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20],
                 fastest_solution='D0 S0 D4 D8 S2 S5 D9 D10 S3 D16 D19 S4 D15 D7 S1 D3 D20',
                 level_color=Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.3),
                 name='Spider',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level
# [S0, S1, S2, S3, S4]