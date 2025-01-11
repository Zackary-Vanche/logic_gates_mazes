from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def f(fast_solution_finding=False):
    
    v = 0

    S0 = Switch(name='S0', value=v)
    S1 = Switch(name='S1')
    S2 = Switch(name='S2', value=v)
    S3 = Switch(name='S3', value=v)
    S4 = Switch(name='S4')
    S5 = Switch(name='S5', value=v)
    S6 = Switch(name='S6')
    S7 = Switch(name='S7', value=v)
    S8 = Switch(name='S8')
    S9 = Switch(name='S9', value=v)
    S10 = Switch(name='S10', value=v)
    S11 = Switch(name='S11', value=v)
    S12 = Switch(name='S12')
    S13 = Switch(name='S13', value=v)
    S14 = Switch(name='S14')
    S15 = Switch(name='S15', value=v)
    S16 = Switch(name='S16', value=v)
    S17 = Switch(name='S17', value=v)
    S18 = Switch(name='S18', value=v)

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
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18]
    
    tree_list_1 = [None]
    
    def tree_list_EQU_SUM(n):
        return ['EQU', [None], Tree.tree_list_SUM(n)]

    T0 = Tree(tree_list=['AND',
                         [None],
                         tree_list_EQU_SUM(3),
                         tree_list_EQU_SUM(4),
                         tree_list_EQU_SUM(3),
                         tree_list_EQU_SUM(2),
                         tree_list_EQU_SUM(3),
                         tree_list_EQU_SUM(4),
                         tree_list_EQU_SUM(4),
                         tree_list_EQU_SUM(3),
                         tree_list_EQU_SUM(2),
                         tree_list_EQU_SUM(3),
                         tree_list_EQU_SUM(3),
                         tree_list_EQU_SUM(2),
                         tree_list_EQU_SUM(4),],
                name='T0',
                switches=[S0,
                          2, S0, S1, S10,
                          2, S1, S2, S12, S18,
                          2, S2, S3, S14,
                          2, S3, S16,
                          2, S4, S10, S11,
                          2, S4, S5, S12, S13,
                          2, S5, S6, S14, S15,
                          2, S6, S16, S17,
                          2, S7, S11,
                          2, S7, S8, S13,
                          2, S8, S9, S15,
                          2, S9, S17,
                          3, S5, S8, S13, S15,],
                cut_expression=True)
    T1 = Tree(tree_list=tree_list_1,
                name='T1',
                switches=[S1])
    T2 = Tree(tree_list=tree_list_1,
                name='T2',
                switches=[S2])
    T3 = Tree(tree_list=tree_list_1,
                name='T3',
                switches=[S3])
    T4 = Tree(tree_list=tree_list_1,
                name='T4',
                switches=[S4])
    T5 = Tree(tree_list=tree_list_1,
                name='T5',
                switches=[S5])
    T6 = Tree(tree_list=tree_list_1,
                name='T6',
                switches=[S6])
    T7 = Tree(tree_list=tree_list_1,
                name='T7',
                switches=[S7])
    T8 = Tree(tree_list=tree_list_1,
                name='T8',
                switches=[S8])
    T9 = Tree(tree_list=tree_list_1,
                name='T9',
                switches=[S9])
    T10 = Tree(tree_list=tree_list_1,
                name='T10',
                switches=[S10])
    T11 = Tree(tree_list=tree_list_1,
                name='T11',
                switches=[S11])
    T12 = Tree(tree_list=tree_list_1,
                name='T12',
                switches=[S12])
    T13 = Tree(tree_list=tree_list_1,
                name='T13',
                switches=[S13])
    T14 = Tree(tree_list=tree_list_1,
                name='T14',
                switches=[S14])
    T15 = Tree(tree_list=tree_list_1,
                name='T15',
                switches=[S15])
    T16 = Tree(tree_list=tree_list_1,
                name='T16',
                switches=[S16])
    T17 = Tree(tree_list=tree_list_1,
                name='T17',
                switches=[S17])
    T18 = Tree(tree_list=tree_list_1,
                name='T18',
                switches=[S18])
    T19 = Tree(tree_list=Tree.tree_list_AND(12),
                name='T19',
                switches=[S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30],
                cut_expression=True)
    
    
    dx = 0.9
    dy = 1
    ex = 0.5
    ey = 0.5
    
    ey0 = 2*dy+ey

    R0 = Room(name='R0',
                position=[-1*dx, 0*dy, ex, ey0],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S19])
    R2 = Room(name='R2',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S20])
    R3 = Room(name='R3',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[S21])
    R4 = Room(name='R4',
                position=[3*dx, 0*dy, ex, ey],
                switches_list=[S22])
    R5 = Room(name='R5',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S23])
    R6 = Room(name='R6',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S24])
    R7 = Room(name='R7',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S25])
    R8 = Room(name='R8',
                position=[3*dx, 1*dy, ex, ey],
                switches_list=[S26])
    R9 = Room(name='R9',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S27])
    R10 = Room(name='R10',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S28])
    R11 = Room(name='R11',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S29])
    R12 = Room(name='R12',
                position=[3*dx, 2*dy, ex, ey],
                switches_list=[S30])
    R13 = Room(name='R13',
                position=[1*dx, -1*dy, ex, ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[2*dx, -1*dy, ex, ey],
              is_exit=True)
    
    if fast_solution_finding:
        for room in [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12]:
            room.possible_switches_values = [[1]]

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1/2, ey/2/ey0])
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R5,
                room_arrival=R6)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R6,
                room_arrival=R7)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R7,
                room_arrival=R8)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R9,
                room_arrival=R10)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R10,
                room_arrival=R11)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R11,
                room_arrival=R12)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R1,
                room_arrival=R5)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R5,
                room_arrival=R9)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R2,
                room_arrival=R6)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R6,
                room_arrival=R10)
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R3,
                room_arrival=R7)
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R7,
                room_arrival=R11)
    D16 = Door(two_way=True,
                tree=T16,
                name='D16',
                room_departure=R4,
                room_arrival=R8)
    D17 = Door(two_way=True,
                tree=T17,
                name='D17',
                room_departure=R8,
                room_arrival=R12)
    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=R2,
                room_arrival=R13)
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R13,
                room_arrival=RE)
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19],
                 fastest_solution="S0 S2 S3 S5 S7 S9 S10 S11 S13 S15 S16 S17 S18 D0 S19 D10 S23 D11 S27 D7 S28 D13 S24 D5 S25 D15 S29 D9 S30 D17 S26 D16 S22 D3 S21 D2 S20 D18 D19",
                 level_color=get_color(),
                 name='Water lily',
                 keep_proportions=True,
                 door_window_size=330)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.6, sa=0.5, li=0.6)
    lcolor.room_color = Color.GREEN
    lcolor.inside_room_color = Color.IVORY
    lcolor.surrounding_color = Color.PINK
    return lcolor