from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_circonvolution(): 

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
    S32 = Switch(name='S32')
    S33 = Switch(name='S33')
    S34 = Switch(name='S34')
    S35 = Switch(name='S35')
    S36 = Switch(name='S36')
    S37 = Switch(name='S37')
    S38 = Switch(name='S38')
    S39 = Switch(name='S39')

    Slist_0 = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23]
    
    tree_list_1 = Tree.tree_list_XOR(2)

    T0 = Tree(tree_list=[None],
                      name='T0',
                      switches=[1])
    T1 = Tree(tree_list=tree_list_1,
                      name='T1',
                      switches=[S24, S25])
    T2 = Tree(tree_list=tree_list_1,
                      name='T2',
                      switches=[S24, S28])
    T3 = Tree(tree_list=tree_list_1,
                      name='T3',
                      switches=[S25, S26])
    T4 = Tree(tree_list=tree_list_1,
                      name='T4',
                      switches=[S25, S29])
    T5 = Tree(tree_list=tree_list_1,
                      name='T5',
                      switches=[S26, S27])
    T6 = Tree(tree_list=tree_list_1,
                      name='T6',
                      switches=[S26, S30])
    T7 = Tree(tree_list=tree_list_1,
                      name='T7',
                      switches=[S27, S31])
    T8 = Tree(tree_list=tree_list_1,
                      name='T8',
                      switches=[S28, S29])
    T9 = Tree(tree_list=tree_list_1,
                      name='T9',
                      switches=[S28, S32])
    T10 = Tree(tree_list=tree_list_1,
                      name='T10',
                      switches=[S29, S30])
    T11 = Tree(tree_list=tree_list_1,
                      name='T11',
                      switches=[S29, S33])
    T12 = Tree(tree_list=tree_list_1,
                      name='T12',
                      switches=[S30, S31])
    T13 = Tree(tree_list=tree_list_1,
                      name='T13',
                      switches=[S30, S34])
    T14 = Tree(tree_list=tree_list_1,
                      name='T14',
                      switches=[S31, S35])
    T15 = Tree(tree_list=tree_list_1,
                      name='T15',
                      switches=[S32, S33])
    T16 = Tree(tree_list=tree_list_1,
                      name='T16',
                      switches=[S32, S36])
    T17 = Tree(tree_list=tree_list_1,
                      name='T17',
                      switches=[S33, S34])
    T18 = Tree(tree_list=tree_list_1,
                      name='T18',
                      switches=[S33, S37])
    T19 = Tree(tree_list=tree_list_1,
                      name='T19',
                      switches=[S34, S35])
    T20 = Tree(tree_list=tree_list_1,
                      name='T20',
                      switches=[S34, S38])
    T21 = Tree(tree_list=tree_list_1,
                      name='T21',
                      switches=[S35, S39])
    T22 = Tree(tree_list=tree_list_1,
                      name='T22',
                      switches=[S36, S37])
    T23 = Tree(tree_list=tree_list_1,
                      name='T23',
                      switches=[S37, S38])
    T24 = Tree(tree_list=tree_list_1,
                      name='T24',
                      switches=[S38, S39])
    T25 = Tree(tree_list=[None],
                name='T25',
                switches=[1])
    
    ex = 0.4
    ey = 0.4
    dx = 1
    dy = 1

    R0 = Room(name='R0',
                position=[-1*dx, 0*dy, ex, 2*dy+ey+(dy-ey)/2],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S24])
    R2 = Room(name='R2',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S25])
    R3 = Room(name='R3',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S26])
    R4 = Room(name='R4',
                position=[0*dx, 3*dy, ex, ey],
                switches_list=[S27])
    R5 = Room(name='R5',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S28])
    R6 = Room(name='R6',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S29])
    R7 = Room(name='R7',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S30])
    R8 = Room(name='R8',
                position=[1*dx, 3*dy, ex, ey],
                switches_list=[S31])
    R9 = Room(name='R9',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[S32])
    R10 = Room(name='R10',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S33])
    R11 = Room(name='R11',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S34])
    R12 = Room(name='R12',
                position=[2*dx, 3*dy, ex, ey],
                switches_list=[S35])
    R13 = Room(name='R13',
                position=[3*dx, 0*dy, ex, ey],
                switches_list=[S36])
    R14 = Room(name='R14',
                position=[3*dx, 1*dy, ex, ey],
                switches_list=[S37])
    R15 = Room(name='R15',
                position=[3*dx, 2*dy, ex, ey],
                switches_list=[S38])
    R16 = Room(name='R16',
                position=[3*dx, 3*dy, ex, ey],
                switches_list=[S39])
    RE = Room(name='RE',
              position=[-1*dx, 3*dy, ex, ey],
              is_exit=True)
    
    rp = 1/2

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_position=1/2)
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                relative_position=rp)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R5,
                relative_position=rp)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R3,
                relative_position=rp)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R6,
                relative_position=rp)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R4,
                relative_position=rp)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R3,
                room_arrival=R7,
                relative_position=rp)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R4,
                room_arrival=R8,
                relative_position=rp)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R5,
                room_arrival=R6,
                relative_position=rp)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R5,
                room_arrival=R9,
                relative_position=rp)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R6,
                room_arrival=R7,
                relative_position=rp)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R6,
                room_arrival=R10,
                relative_position=rp)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R7,
                room_arrival=R8,
                relative_position=rp)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R7,
                room_arrival=R11,
                relative_position=rp)
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R8,
                room_arrival=R12,
                relative_position=rp)
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R9,
                room_arrival=R10,
                relative_position=rp)
    D16 = Door(two_way=True,
                tree=T16,
                name='D16',
                room_departure=R9,
                room_arrival=R13,
                relative_position=rp)
    D17 = Door(two_way=True,
                tree=T17,
                name='D17',
                room_departure=R10,
                room_arrival=R11,
                relative_position=rp)
    D18 = Door(two_way=True,
                tree=T18,
                name='D18',
                room_departure=R10,
                room_arrival=R14,
                relative_position=rp)
    D19 = Door(two_way=True,
                tree=T19,
                name='D19',
                room_departure=R11,
                room_arrival=R12,
                relative_position=rp)
    D20 = Door(two_way=True,
                tree=T20,
                name='D20',
                room_departure=R11,
                room_arrival=R15,
                relative_position=rp)
    D21 = Door(two_way=True,
                tree=T21,
                name='D21',
                room_departure=R12,
                room_arrival=R16,
                relative_position=rp)
    D22 = Door(two_way=True,
                tree=T22,
                name='D22',
                room_departure=R13,
                room_arrival=R14,
                relative_position=rp)
    D23 = Door(two_way=True,
                tree=T23,
                name='D23',
                room_departure=R14,
                room_arrival=R15,
                relative_position=rp)
    D24 = Door(two_way=True,
                tree=T24,
                name='D24',
                room_departure=R15,
                room_arrival=R16,
                relative_position=rp)
    D25 = Door(two_way=True,
                tree=T25,
                name='D25',
                room_departure=R4,
                room_arrival=RE,
                relative_position=rp)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9,
                             D10, D11, D12, D13, D14, D15, D16, D17, D18, D19,
                             D20, D21, D22, D23, D24, D25],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.5),
                 name='TODO',
                 keep_proportions=True,
                 door_window_size=500)
    
    return level