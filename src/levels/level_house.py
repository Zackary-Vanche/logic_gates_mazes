from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_house(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    
    Slist = [S0, S1, S2, S3, S4, S5, S6]
    tree_list_AND = Tree.tree_list_AND(len(Slist))

    T0 = Tree(tree_list=[None],
                      empty=True,
                      name='T0',
                      switches=[1])
    T1 = Tree(tree_list=[None],
                      empty=True,
                      name='T1',
                      switches=[1])
    T2 = Tree(tree_list=tree_list_AND,
                      empty=True,
                      name='T2',
                      switches=Slist)
    T3 = Tree(tree_list=[None],
                      empty=True,
                      name='T3',
                      switches=[1])
    T4 = Tree(tree_list=tree_list_AND,
                      empty=True,
                      name='T4',
                      switches=Slist)
    T5 = Tree(tree_list=[None],
                      empty=True,
                      name='T5',
                      switches=[1])
    T6 = Tree(tree_list=tree_list_AND,
                      empty=True,
                      name='T6',
                      switches=Slist)
    T7 = Tree(tree_list=[None],
                      empty=True,
                      name='T7',
                      switches=[1])
    T8 = Tree(tree_list=tree_list_AND,
                      empty=True,
                      name='T8',
                      switches=Slist)
    T9 = Tree(tree_list=[None],
                      empty=True,
                      name='T9',
                      switches=[1])
    T10 = Tree(tree_list=tree_list_AND,
                      empty=True,
                      name='T10',
                      switches=Slist)
    T11 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T11',
                      switches=[S0])
    T12 = Tree(tree_list=[None],
                      empty=True,
                      name='T12',
                      switches=[S0])
    T13 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T13',
                      switches=[S1])
    T14 = Tree(tree_list=[None],
                      empty=True,
                      name='T14',
                      switches=[S1])
    T15 = Tree(tree_list=[None],
                      empty=True,
                      name='T15',
                      switches=[S0])
    T16 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T16',
                      switches=[S0])
    T17 = Tree(tree_list=[None],
                      empty=True,
                      name='T17',
                      switches=[S1])
    T18 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T18',
                      switches=[S1])
    T19 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T19',
                      switches=[S2])
    T20 = Tree(tree_list=[None],
                      empty=True,
                      name='T20',
                      switches=[S2])
    T21 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T21',
                      switches=[S3])
    T22 = Tree(tree_list=[None],
                      empty=True,
                      name='T22',
                      switches=[S3])
    T23 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T23',
                      switches=[S4])
    T24 = Tree(tree_list=[None],
                      empty=True,
                      name='T24',
                      switches=[S4])
    T25 = Tree(tree_list=[None],
                      empty=True,
                      name='T25',
                      switches=[S2])
    T26 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T26',
                      switches=[S2])
    T27 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T27',
                      switches=[S5])
    T28 = Tree(tree_list=[None],
                      empty=True,
                      name='T28',
                      switches=[S5])
    T29 = Tree(tree_list=[None],
                      empty=True,
                      name='T29',
                      switches=[S3])
    T30 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T30',
                      switches=[S3])
    T31 = Tree(tree_list=[None],
                      empty=True,
                      name='T31',
                      switches=[S4])
    T32 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T32',
                      switches=[S4])
    T33 = Tree(tree_list=[None],
                      empty=True,
                      name='T33',
                      switches=[S5])
    T34 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T34',
                      switches=[S5])
    T35 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T35',
                      switches=[S6])
    T36 = Tree(tree_list=[None],
                      empty=True,
                      name='T36',
                      switches=[S6])
    T37 = Tree(tree_list=[None],
                      empty=True,
                      name='T37',
                      switches=[S6])
    T38 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T38',
                      switches=[S6])
    T39 = Tree(tree_list=tree_list_AND,
                empty=True,
                name='T39',
                switches=Slist)
    
    ex = 1
    ey = 1
    
    dx = 1
    dy = 1
    
    epsilon = 0.15

    R0 = Room(name='R0',
                position=[-1.5*dx, 3*dy, ex, ey],
                switches_list=[])
    R1 = Room(name='R1',
                position=[7.5*dx, 3*dy, ex, ey],
                switches_list=[])

    R2 = Room(name='R2',
                position=[3*dx, 0*dy+3*ey/4, ex, ey/2],
                switches_list=[])

    R3 = Room(name='R3',
                position=[1.5*dx, 2*dy+ey/4, ex, ey/2],
                switches_list=[S0])
    R4 = Room(name='R4',
                position=[4.5*dx, 2*dy+ey/4, ex, ey/2],
                switches_list=[S1])

    R5 = Room(name='R5',
                position=[1*dx-epsilon, 4*dy-epsilon, ex, ey],
                switches_list=[])
    R6 = Room(name='R6',
                position=[3*dx+ex/4, 4*dy, ex/2, ey],
                switches_list=[S2])
    R7 = Room(name='R7',
                position=[5*dx+epsilon, 4*dy-epsilon, ex, ey],
                switches_list=[])

    R8 = Room(name='R8',
                position=[1*dx, 6*dy+ey/4, ex, ey/2],
                switches_list=[S3])
    R9 = Room(name='R9',
                position=[3*dx, 6*dy, ex, ey],
                switches_list=[S4])
    R10 = Room(name='R10',
                position=[5*dx, 6*dy+ey/4, ex, ey/2],
                switches_list=[S5])

    R11 = Room(name='R11',
                position=[1*dx-epsilon, 8*dy+epsilon, ex, ey],
                switches_list=[])
    R12 = Room(name='R12',
                position=[3*dx+ex/4, 8*dy, ex/2, ey],
                switches_list=[S6])
    R13 = Room(name='R13',
                position=[5*dx+epsilon, 8*dy+epsilon, ex, ey],
                switches_list=[])

    RE = Room(name='RE',
              position=[7.5*dx, 1*dy, ex, ey],
              is_exit=True)
    
    rp = 0.6

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R2,
                relative_departure_coordinates=[0, 0],
                relative_arrival_coordinates=[0, 0])
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R1,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[1, 0])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R0,
                room_arrival=R5,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[0, 0])
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R5,
                room_arrival=R0,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[1, 1])
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R1,
                room_arrival=R7,
                relative_departure_coordinates=[0, 0],
                relative_arrival_coordinates=[1, 0])
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R7,
                room_arrival=R1,
                relative_departure_coordinates=[1, 1],
                relative_arrival_coordinates=[0, 1])
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R0,
                room_arrival=R11,
                relative_departure_coordinates=[1, 1],
                relative_arrival_coordinates=[0, 0])
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R11,
                room_arrival=R0,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[0, 1])
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R1,
                room_arrival=R13,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[1, 0])
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R13,
                room_arrival=R1,
                relative_departure_coordinates=[1, 1],
                relative_arrival_coordinates=[1, 1])

    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R2,
                room_arrival=R3,
                relative_departure_coordinates=[0, 0],
                relative_arrival_coordinates=[0, 0])
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R3,
                room_arrival=R2,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[0, 1])
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R2,
                room_arrival=R4,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[1, 0])
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R4,
                room_arrival=R2,
                relative_departure_coordinates=[0, 0],
                relative_arrival_coordinates=[1, 1])
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R3,
                room_arrival=R5,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[0, 0])
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R5,
                room_arrival=R3,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[1, 1])
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R4,
                room_arrival=R7,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[0, 0])
    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=R7,
                room_arrival=R4,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[1, 1])
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R5,
                room_arrival=R6,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[0, 0])
    D20 = Door(two_way=False,
                tree=T20,
                name='D20',
                room_departure=R6,
                room_arrival=R5,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[1, 1])
    D21 = Door(two_way=False,
                tree=T21,
                name='D21',
                room_departure=R5,
                room_arrival=R8,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[0, 0])
    D22 = Door(two_way=False,
                tree=T22,
                name='D22',
                room_departure=R8,
                room_arrival=R5,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[1, 1])
    D23 = Door(two_way=False,
                tree=T23,
                name='D23',
                room_departure=R5,
                room_arrival=R9,
                relative_departure_coordinates=[1, 1],
                relative_arrival_coordinates=[1, 0],
                relative_position=rp)
    D24 = Door(two_way=False,
                tree=T24,
                name='D24',
                room_departure=R9,
                room_arrival=R5,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[1, 1])
    D25 = Door(two_way=False,
                tree=T25,
                name='D25',
                room_departure=R6,
                room_arrival=R7,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[0, 0])
    D26 = Door(two_way=False,
                tree=T26,
                name='D26',
                room_departure=R7,
                room_arrival=R6,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[1, 1])
    D27 = Door(two_way=False,
                tree=T27,
                name='D27',
                room_departure=R7,
                room_arrival=R10,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[0, 0])
    D28 = Door(two_way=False,
                tree=T28,
                name='D28',
                room_departure=R10,
                room_arrival=R7,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[1, 1])
    D29 = Door(two_way=False,
                tree=T29,
                name='D29',
                room_departure=R8,
                room_arrival=R11,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[0, 0])
    D30 = Door(two_way=False,
                tree=T30,
                name='D30',
                room_departure=R11,
                room_arrival=R8,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[1, 1])
    D31 = Door(two_way=False,
                tree=T31,
                name='D31',
                room_departure=R9,
                room_arrival=R13,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[0, 0])
    D32 = Door(two_way=False,
                tree=T32,
                name='D32',
                room_departure=R13,
                room_arrival=R9,
                relative_departure_coordinates=[0, 0],
                relative_arrival_coordinates=[0, 1],
                relative_position=rp)
    D33 = Door(two_way=False,
                tree=T33,
                name='D33',
                room_departure=R10,
                room_arrival=R13,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[0, 0])
    D34 = Door(two_way=False,
                tree=T34,
                name='D34',
                room_departure=R13,
                room_arrival=R10,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[1, 1])
    D35 = Door(two_way=False,
                tree=T35,
                name='D35',
                room_departure=R11,
                room_arrival=R12,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[0, 0])
    D36 = Door(two_way=False,
                tree=T36,
                name='D36',
                room_departure=R12,
                room_arrival=R11,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[1, 1])
    D37 = Door(two_way=False,
                tree=T37,
                name='D37',
                room_departure=R12,
                room_arrival=R13,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[0, 0])
    D38 = Door(two_way=False,
                tree=T38,
                name='D38',
                room_departure=R13,
                room_arrival=R12,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[1, 1])
    D39 = Door(two_way=False,
                tree=T39,
                name='D39',
                room_departure=R1,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9,
                             D10, D11, D12, D13, D14, D15, D16, D17, D18, D19,
                             D20, D21, D22, D23, D24, D25, D26, D27, D28, D29,
                             D30, D31, D32, D33, D34, D35, D36, D37, D38, D39],
                 fastest_solution="D1 D11 S0 D12 D13 S1 D17 D26 S2 D20 D21 S3 D22 D23 S4 D31 D34 S5 D33 D38 S6 D37 D10 D39",
                 level_color=Levels_colors_list.FROM_HUE(hu=0.1, sa=0.4, li=0.3),
                 name='House',
                 keep_proportions=True,
                 door_window_size=400,
                 y_separation=40)
    
    return level