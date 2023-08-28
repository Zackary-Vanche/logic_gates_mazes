from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_tour(): 

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
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11]
    
    tree_list = Tree.tree_list_from_str('TF')

    T0 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T0',
                      switches=[S0, S5])
    T1 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T1',
                      switches=[S0, S7])
    T2 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T2',
                      switches=[S1, S6])
    T3 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T3',
                      switches=[S1, S8])
    T4 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T4',
                      switches=[S2, S3])
    T5 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T5',
                      switches=[S2, S7])
    T6 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T6',
                      switches=[S3, S2])
    T7 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T7',
                      switches=[S3, S8])
    T8 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T8',
                      switches=[S3, S10])
    T9 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T9',
                      switches=[S4, S9])
    T10 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T10',
                      switches=[S4, S11])
    T11 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T11',
                      switches=[S5, S0])
    T12 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T12',
                      switches=[S5, S6])
    T13 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T13',
                      switches=[S5, S10])
    T14 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T14',
                      switches=[S6, S1])
    T15 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T15',
                      switches=[S6, S5])
    T16 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T16',
                      switches=[S6, S11])
    T17 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T17',
                      switches=[S7, S0])
    T18 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T18',
                      switches=[S7, S2])
    T19 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T19',
                      switches=[S8, S1])
    T20 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T20',
                      switches=[S8, S3])
    T21 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T21',
                      switches=[S8, S9])
    T22 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T22',
                      switches=[S9, S4])
    T23 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T23',
                      switches=[S9, S8])
    T24 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T24',
                      switches=[S10, S3])
    T25 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T25',
                      switches=[S10, S5])
    T26 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T26',
                      switches=[S11, S4])
    T27 = Tree(tree_list=tree_list,
                      empty=True,
                      name='T27',
                      switches=[S11, S6])
    T28 = Tree(tree_list=Tree.tree_list_AND(len(Slist)),
                name='T28',
                switches=Slist)

    dx = 3
    dy = 1
    ex = 0.4
    ey = 0.8

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S0])
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S1])
    R2 = Room(name='R2',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[S2])
    R3 = Room(name='R3',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S3])
    R4 = Room(name='R4',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S4])
    R5 = Room(name='R5',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S5])
    R6 = Room(name='R6',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S6])
    R7 = Room(name='R7',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S7])
    R8 = Room(name='R8',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S8])
    R9 = Room(name='R9',
                position=[0*dx, 3*dy, ex, ey],
                switches_list=[S9])
    R10 = Room(name='R10',
                position=[1*dx, 3*dy, ex, ey],
                switches_list=[S10])
    R11 = Room(name='R11',
                position=[2*dx, 3*dy, ex, ey],
                switches_list=[S11])
    RE = Room(name='RE',
              position=[dx/2, -0.3, ex, 0.4],
              is_exit=True)
    
    rp = 0.18
    
    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R5,
                relative_position=rp)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R7,
                relative_position=rp)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R6,
                relative_position=rp)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R8,
                relative_position=rp)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R3,
                relative_position=rp)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R2,
                room_arrival=R7,
                relative_position=rp)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R3,
                room_arrival=R2,
                relative_position=rp)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R3,
                room_arrival=R8,
                relative_position=rp)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R3,
                room_arrival=R10,
                relative_position=rp)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R4,
                room_arrival=R9,
                relative_position=rp)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R4,
                room_arrival=R11,
                relative_position=rp)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R5,
                room_arrival=R0,
                relative_position=rp)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R5,
                room_arrival=R6,
                relative_position=rp)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R5,
                room_arrival=R10,
                relative_position=rp)
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R6,
                room_arrival=R1,
                relative_position=rp)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R6,
                room_arrival=R5,
                relative_position=rp)
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R6,
                room_arrival=R11,
                relative_position=rp)
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R7,
                room_arrival=R0,
                relative_position=rp)
    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=R7,
                room_arrival=R2,
                relative_position=rp)
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R8,
                room_arrival=R1,
                relative_position=rp)
    D20 = Door(two_way=False,
                tree=T20,
                name='D20',
                room_departure=R8,
                room_arrival=R3,
                relative_position=rp)
    D21 = Door(two_way=False,
                tree=T21,
                name='D21',
                room_departure=R8,
                room_arrival=R9,
                relative_position=rp)
    D22 = Door(two_way=False,
                tree=T22,
                name='D22',
                room_departure=R9,
                room_arrival=R4,
                relative_position=rp)
    D23 = Door(two_way=False,
                tree=T23,
                name='D23',
                room_departure=R9,
                room_arrival=R8,
                relative_position=rp)
    D24 = Door(two_way=False,
                tree=T24,
                name='D24',
                room_departure=R10,
                room_arrival=R3,
                relative_position=rp)
    D25 = Door(two_way=False,
                tree=T25,
                name='D25',
                room_departure=R10,
                room_arrival=R5,
                relative_position=rp)
    D26 = Door(two_way=False,
                tree=T26,
                name='D26',
                room_departure=R11,
                room_arrival=R4,
                relative_position=rp)
    D27 = Door(two_way=False,
                tree=T27,
                name='D27',
                room_departure=R11,
                room_arrival=R6,
                relative_position=rp)
    D28 = Door(two_way=False,
                tree=T28,
                name='D28',
                room_departure=R1,
                room_arrival=RE,
                relative_position=.5)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9,
                             D10, D11, D12, D13, D14, D15, D16, D17, D18, D19,
                             D20, D21, D22, D23, D24, D25, D26, D27, D28],
                 fastest_solution="S0 D1 S7 D18 S2 D4 S3 D8 S10 D25 S5 D12 S6 D16 S11 D26 S4 D9 S9 D23 S8 D19 S1 D28",
                 level_color=Levels_colors_list.FROM_HUE(hu=0.9, sa=0.2, li=0.5),
                 name='Tour',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

    