from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_mansion(): 

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
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9]
    
    tree_list_0 = Tree.tree_list_XOR(2)

    T0 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T0',
                  switches=[S0, S1])
    T1 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T1',
                  switches=[S1, S0])
    T2 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T2',
                  switches=[S0, S2])
    T3 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T3',
                  switches=[S2, S0])
    T4 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T4',
                  switches=[S0, S3])
    T5 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T5',
                  switches=[S3, S0])
    T6 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T6',
                  switches=[S1, S7])
    T7 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T7',
                  switches=[S7, S1])
    T8 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T8',
                  switches=[S2, S5])
    T9 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T9',
                  switches=[S5, S2])
    T10 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T10',
                  switches=[S3, S9])
    T11 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T11',
                  switches=[S9, S3])
    T12 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T12',
                  switches=[S4, S5])
    T13 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T13',
                  switches=[S5, S4])
    T14 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T14',
                  switches=[S4, S7])
    T15 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T15',
                  switches=[S7, S4])
    T16 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T16',
                  switches=[S5, S6])
    T17 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T17',
                  switches=[S6, S5])
    T18 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T18',
                  switches=[S6, S9])
    T19 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T19',
                  switches=[S9, S6])
    T20 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T20',
                  switches=[S7, S8])
    T21 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T21',
                  switches=[S8, S7])
    T22 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T22',
                  switches=[S8, S9])
    T23 = Tree(tree_list=tree_list_0,
                  empty=True,
                  name='T23',
                  switches=[S9, S8])
    T24 = Tree(tree_list=Tree.tree_list_from_str('1001011111'),
                empty=True,
                name='T24',
                switches=Slist)
    
    ex = 1
    ey = 1

    R0 = Room(name='R0',
                position=[3, 0, ex, ey],
                switches_list=[S0])
    R1 = Room(name='R1',
                position=[0, 2, ex, ey],
                switches_list=[S1])
    R2 = Room(name='R2',
                position=[3, 2, ex, ey],
                switches_list=[S2])
    R3 = Room(name='R3',
                position=[6, 2, ex, ey],
                switches_list=[S3])
    R4 = Room(name='R4',
                position=[1, 4, ex, ey],
                switches_list=[S4])
    R5 = Room(name='R5',
                position=[3, 4, ex, ey],
                switches_list=[S5])
    R6 = Room(name='R6',
                position=[5, 4, ex, ey],
                switches_list=[S6])
    R7 = Room(name='R7',
                position=[0, 6, ex, ey],
                switches_list=[S7])
    R8 = Room(name='R8',
                position=[3, 6, ex, ey],
                switches_list=[S8])
    R9 = Room(name='R9',
                position=[6, 6, ex, ey],
                switches_list=[S9])
    RE = Room(name='RE',
              position=[3, -2, ex, ey],
              is_exit=True)
    
    e = 0.1

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[e, e],
                relative_arrival_coordinates=[e, e])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R0,
                relative_departure_coordinates=[1-e, e],
                relative_arrival_coordinates=[e, 1-e])
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=R2,
                relative_departure_coordinates=[e, 1-e],
                relative_arrival_coordinates=[e, e])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R0,
                relative_departure_coordinates=[1-e, 1-e],
                relative_arrival_coordinates=[1-e, e])
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R0,
                room_arrival=R3,
                relative_departure_coordinates=[1-e, e],
                relative_arrival_coordinates=[1-e, e])
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R0,
                relative_departure_coordinates=[1-e, 1-e],
                relative_arrival_coordinates=[e, e])
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R1,
                room_arrival=R7,
                relative_departure_coordinates=[e, 1-e],
                relative_arrival_coordinates=[e, e],
                relative_position=0.4)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R7,
                room_arrival=R1,
                relative_departure_coordinates=[2*e, 1-e],
                relative_arrival_coordinates=[2*e, e],
                relative_position=0.4)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R2,
                room_arrival=R5,
                relative_departure_coordinates=[e, 1-e],
                relative_arrival_coordinates=[e, e])
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R5,
                room_arrival=R2,
                relative_departure_coordinates=[1-e, 1-e],
                relative_arrival_coordinates=[1-e, e])
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R3,
                room_arrival=R9,
                relative_departure_coordinates=[1-2*e, 1-e],
                relative_arrival_coordinates=[1-2*e, e],
                relative_position=0.4)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R9,
                room_arrival=R3,
                relative_departure_coordinates=[1-e, 1-e],
                relative_arrival_coordinates=[1-e, e],
                relative_position=0.4)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R4,
                room_arrival=R5,
                relative_departure_coordinates=[1-e, e],
                relative_arrival_coordinates=[e, e],)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R5,
                room_arrival=R4,
                relative_departure_coordinates=[1-e, 1-e],
                relative_arrival_coordinates=[e, 1-e],)
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R4,
                room_arrival=R7,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[1, 0])
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R7,
                room_arrival=R4,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[0, 1])
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R5,
                room_arrival=R6,
                relative_departure_coordinates=[1-e, e],
                relative_arrival_coordinates=[e, e],)
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R6,
                room_arrival=R5,
                relative_departure_coordinates=[1-e, 1-e],
                relative_arrival_coordinates=[e, 1-e],)
    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=R6,
                room_arrival=R9,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[0, 0])
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R9,
                room_arrival=R6,
                relative_departure_coordinates=[1, 1],
                relative_arrival_coordinates=[1/2, 0])
    D20 = Door(two_way=False,
                tree=T20,
                name='D20',
                room_departure=R7,
                room_arrival=R8,
                relative_departure_coordinates=[1-e, e],
                relative_arrival_coordinates=[e, e],)
    D21 = Door(two_way=False,
                tree=T21,
                name='D21',
                room_departure=R8,
                room_arrival=R7,
                relative_departure_coordinates=[1-e, 1-e],
                relative_arrival_coordinates=[e, 1-e],)
    D22 = Door(two_way=False,
                tree=T22,
                name='D22',
                room_departure=R8,
                room_arrival=R9,
                relative_departure_coordinates=[1-e, e],
                relative_arrival_coordinates=[e, e],)
    D23 = Door(two_way=False,
                tree=T23,
                name='D23',
                room_departure=R9,
                room_arrival=R8,
                relative_departure_coordinates=[1-e, 1-e],
                relative_arrival_coordinates=[e, 1-e],)
    D24 = Door(two_way=False,
                tree=T24,
                name='D24',
                room_departure=R0,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24],
                 fastest_solution="S0 D4 S3 D10 S9 D19 S6 D17 S5 D9 D3 D0 S1 D6 S7 D20 D22 S9 D11 S3 D5 S0 D0 S1 D6 D20 S8 D22 S9 D11 S3 D5 S0 D24",
                 level_color=Levels_colors_list.FROM_HUE(hu=0.1, sa=0.4, li=0.4),
                 name='Mansion',
                 keep_proportions=False,
                 door_window_size=500)
    
    return level
