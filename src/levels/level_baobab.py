from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_baobab(fast_solution_finding=False): 

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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12]

    T0 = Tree(tree_list=['AND', ['EQU', Tree.tree_list_SUM(13), [None]],] + [['EQU', Tree.tree_list_SUM(3), [None]]]*6,
                name='T0',
                switches=Slist + [7,
                                  S0, S1, S2, 1,
                                  S0, S3, S4, 1,
                                  S2, S5, S7, 1,
                                  S4, S8, S9, 1,
                                  S7, S10, S12, 1,
                                  S9, S1, S12, 1,
                                  ],
                cut_expression_depth_1=True)
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[S0])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[S1])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[S2])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[S3])
    T5 = Tree(tree_list=[None],
                name='T5',
                switches=[S4])
    T6 = Tree(tree_list=[None],
                name='T6',
                switches=[S5])
    T7 = Tree(tree_list=[None],
                name='T7',
                switches=[S6])
    T8 = Tree(tree_list=[None],
                name='T8',
                switches=[S7])
    T9 = Tree(tree_list=[None],
                name='T9',
                switches=[S8])
    T10 = Tree(tree_list=[None],
                name='T10',
                switches=[S9])
    T11 = Tree(tree_list=[None],
                name='T11',
                switches=[S10])
    T12 = Tree(tree_list=[None],
                name='T12',
                switches=[S11])
    T13 = Tree(tree_list=[None],
                name='T13',
                switches=[S12])
    T14 = Tree(tree_list=Tree.tree_list_AND(8),
                name='T14',
                switches=[S13, S14, S15, S16, S17, S18, S19, S20])

    dx = 1.5
    dy = 1
    ex = 0.8
    ey = 0.4
    a = 0.4

    R0 = Room(name='R0',
                position=[0*dx, 4*dy-a, 2*dx+ex, 2.75*ey],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[1*dx, 3*dy, ex, ey],
                switches_list=[S13])
    R2 = Room(name='R2',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S14])
    R3 = Room(name='R3',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S15])
    R4 = Room(name='R4',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S16])
    R5 = Room(name='R5',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S17])
    R6 = Room(name='R6',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S18])
    R7 = Room(name='R7',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S19])
    R8 = Room(name='R8',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S20])
    RE = Room(name='RE',
              position=[-1*dx, -1*dy+a, 4*dx+ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R4,
                relative_departure_coordinates=[(2*dx+ex/2)/(2*dx+ex), 1/2])
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R3)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R4)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R3)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R2,
                room_arrival=R5)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R3,
                room_arrival=R4)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R3,
                room_arrival=R6)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R4,
                room_arrival=R7)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R5,
                room_arrival=R6)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R5,
                room_arrival=R8)
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
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R5,
                room_arrival=RE,
                relative_arrival_coordinates=[(dx+ex/2)/(4*dx+ex), 1/2])
    
    if fast_solution_finding:
        for room in [R1, R2, R3, R4, R5, R6, R7, R8]:
            room.possible_switches_values = [[1]]

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14],
                 fastest_solution="S1 S3 S5 S6 S8 S10 S11 D0 S16 D6 S15 D2 S13 D2 D4 S14 D4 D7 S18 D11 S19 D11 D12 S20 D12 D9 S17 D14",
                 level_color=Levels_colors_list.FROM_HUE(hu=0.16, sa=0.2, li=0.35),
                 name='Baobab',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level