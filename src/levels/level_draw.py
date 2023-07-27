from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_draw(): 

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
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13]
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
    T12 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T12',
                      switches=[S2])
    T13 = Tree(tree_list=[None],
                      empty=True,
                      name='T13',
                      switches=[S0])
    T14 = Tree(tree_list=[None],
                      empty=True,
                      name='T14',
                      switches=[S2])
    T15 = Tree(tree_list=[None],
                      empty=True,
                      name='T15',
                      switches=[S1])
    T16 = Tree(tree_list=[None],
                      empty=True,
                      name='T16',
                      switches=[S4])
    T17 = Tree(tree_list=[None],
                      empty=True,
                      name='T17',
                      switches=[S3])
    T18 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T18',
                      switches=[S1])
    T19 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T19',
                      switches=[S4])
    T20 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T20',
                      switches=[S6])
    T21 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T21',
                      switches=[S8])
    T22 = Tree(tree_list=[None],
                      empty=True,
                      name='T22',
                      switches=[S5])
    T23 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T23',
                      switches=[S3])
    T24 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T24',
                      switches=[S5])
    T25 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T25',
                      switches=[S11])
    T26 = Tree(tree_list=[None],
                      empty=True,
                      name='T26',
                      switches=[S6])
    T27 = Tree(tree_list=[None],
                      empty=True,
                      name='T27',
                      switches=[S8])
    T28 = Tree(tree_list=[None],
                      empty=True,
                      name='T28',
                      switches=[S9])
    T29 = Tree(tree_list=[None],
                      empty=True,
                      name='T29',
                      switches=[S10])
    T30 = Tree(tree_list=[None],
                      empty=True,
                      name='T30',
                      switches=[S11])
    T31 = Tree(tree_list=[None],
                      empty=True,
                      name='T31',
                      switches=[S7])
    T32 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T32',
                      switches=[S9])
    T33 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T33',
                      switches=[S12])
    T34 = Tree(tree_list=[None],
                      empty=True,
                      name='T34',
                      switches=[S12])
    T35 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T35',
                      switches=[S10])
    T36 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T36',
                      switches=[S7])
    T37 = Tree(tree_list=Tree.tree_list_NOT,
                      empty=True,
                      name='T37',
                      switches=[S13])
    T38 = Tree(tree_list=[None],
                      empty=True,
                      name='T38',
                      switches=[S13])
    T39 = Tree(tree_list=tree_list_AND,
                empty=True,
                name='T39',
                switches=Slist)
    
    dx = 1
    dy = 1
    ex = 1
    ey = 1

    R0 = Room(name='R0',
                position=[0*dx+ex/2, 0*dy, ex/2, 11*ey],
                switches_list=[])
    R1 = Room(name='R1',
                position=[12*dx, 0*dy, ex/2, 11*ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[6*dx, 0*dy, ex, ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S0])
    R4 = Room(name='R4',
                position=[10*dx, 1*dy, ex, ey],
                switches_list=[S2])
    R5 = Room(name='R5',
                position=[4*dx, 2*dy, ex, ey],
                switches_list=[S1])
    R6 = Room(name='R6',
                position=[6*dx, 2*dy, ex, ey],
                switches_list=[S4])
    R7 = Room(name='R7',
                position=[8*dx, 2*dy, ex, ey],
                switches_list=[S3])
    R8 = Room(name='R8',
                position=[4*dx, 4*dy, ex, ey],
                switches_list=[])
    R9 = Room(name='R9',
                position=[6*dx, 4*dy, ex, ey],
                switches_list=[S5])
    R10 = Room(name='R10',
                position=[8*dx, 4*dy, ex, ey],
                switches_list=[])
    R11 = Room(name='R11',
                position=[7*dx, 5*dy, ex, ey],
                switches_list=[S6])
    R12 = Room(name='R12',
                position=[2*dx, 6*dy, ex, ey],
                switches_list=[S8])
    R13 = Room(name='R13',
                position=[4*dx, 6*dy, ex, ey],
                switches_list=[S9])
    R14 = Room(name='R14',
                position=[8*dx, 6*dy, ex, ey],
                switches_list=[S10])
    R15 = Room(name='R15',
                position=[10*dx, 6*dy, ex, ey],
                switches_list=[S11])
    R16 = Room(name='R16',
                position=[5*dx, 7*dy, ex, ey],
                switches_list=[S7])
    R17 = Room(name='R17',
                position=[4*dx, 8*dy, ex, ey],
                switches_list=[])
    R18 = Room(name='R18',
                position=[6*dx, 8*dy, ex, ey],
                switches_list=[S12])
    R19 = Room(name='R19',
                position=[8*dx, 8*dy, ex, ey],
                switches_list=[])
    R20 = Room(name='R20',
                position=[6*dx, 10*dy, ex, ey],
                switches_list=[S13])
    RE = Room(name='RE',
              position=[3*dx, 10*dy, ex, ey],
              is_exit=True)
    
    rp = 0.65
    
    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1/2, 3.5/11],
                relative_arrival_coordinates=[1/2, 3.5/11])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R2,
                relative_departure_coordinates=[1/2, 0.5/11])
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R1,
                relative_arrival_coordinates=[1/2, 0.5/11])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R0,
                room_arrival=R8,
                relative_departure_coordinates=[1/2, 4.5/11],
                relative_position=rp)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R8,
                room_arrival=R0,
                relative_arrival_coordinates=[1/2, 4.5/11],
                relative_position=rp)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R1,
                room_arrival=R10,
                relative_departure_coordinates=[1/2, 4.5/11],
                relative_position=rp)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R10,
                room_arrival=R1,
                relative_arrival_coordinates=[1/2, 4.5/11],
                relative_position=rp)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R0,
                room_arrival=R17,
                relative_departure_coordinates=[1/2, 8.5/11],
                relative_position=rp)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R17,
                room_arrival=R0,
                relative_arrival_coordinates=[1/2, 8.5/11],
                relative_position=rp)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R1,
                room_arrival=R19,
                relative_departure_coordinates=[1/2, 8.5/11],
                relative_position=rp)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R19,
                room_arrival=R1,
                relative_arrival_coordinates=[1/2, 8.5/11],
                relative_position=rp)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R2,
                room_arrival=R3)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R2,
                room_arrival=R4)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R3,
                room_arrival=R8)
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R4,
                room_arrival=R10)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R5,
                room_arrival=R2)
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R6,
                room_arrival=R10)
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R7,
                room_arrival=R2)
    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=R8,
                room_arrival=R5)
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R8,
                room_arrival=R6)
    D20 = Door(two_way=False,
                tree=T20,
                name='D20',
                room_departure=R8,
                room_arrival=R11,
                relative_departure_coordinates=[1, 1],
                relative_arrival_coordinates=[0, 1])
    D21 = Door(two_way=False,
                tree=T21,
                name='D21',
                room_departure=R8,
                room_arrival=R12)
    D22 = Door(two_way=False,
                tree=T22,
                name='D22',
                room_departure=R9,
                room_arrival=R8)
    D23 = Door(two_way=False,
                tree=T23,
                name='D23',
                room_departure=R10,
                room_arrival=R7)
    D24 = Door(two_way=False,
                tree=T24,
                name='D24',
                room_departure=R10,
                room_arrival=R9)
    D25 = Door(two_way=False,
                tree=T25,
                name='D25',
                room_departure=R10,
                room_arrival=R15)
    D26 = Door(two_way=False,
                tree=T26,
                name='D26',
                room_departure=R11,
                room_arrival=R19,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[0, 0])
    D27 = Door(two_way=False,
                tree=T27,
                name='D27',
                room_departure=R12,
                room_arrival=R17)
    D28 = Door(two_way=False,
                tree=T28,
                name='D28',
                room_departure=R13,
                room_arrival=R8)
    D29 = Door(two_way=False,
                tree=T29,
                name='D29',
                room_departure=R14,
                room_arrival=R10)
    D30 = Door(two_way=False,
                tree=T30,
                name='D30',
                room_departure=R15,
                room_arrival=R19)
    D31 = Door(two_way=False,
                tree=T31,
                name='D31',
                room_departure=R16,
                room_arrival=R8,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[1, 1])
    D32 = Door(two_way=False,
                tree=T32,
                name='D32',
                room_departure=R17,
                room_arrival=R13)
    D33 = Door(two_way=False,
                tree=T33,
                name='D33',
                room_departure=R17,
                room_arrival=R18)
    D34 = Door(two_way=False,
                tree=T34,
                name='D34',
                room_departure=R18,
                room_arrival=R19)
    D35 = Door(two_way=False,
                tree=T35,
                name='D35',
                room_departure=R19,
                room_arrival=R14)
    D36 = Door(two_way=False,
                tree=T36,
                name='D36',
                room_departure=R19,
                room_arrival=R16,
                relative_departure_coordinates=[0, 0],
                relative_arrival_coordinates=[1, 0])
    D37 = Door(two_way=False,
                tree=T37,
                name='D37',
                room_departure=R19,
                room_arrival=R20)
    D38 = Door(two_way=False,
                tree=T38,
                name='D38',
                room_departure=R20,
                room_arrival=R17)
    D39 = Door(two_way=False,
                tree=T39,
                name='D39',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 10.5/11])


    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9,
                             D10, D11, D12, D13, D14, D15, D16, D17, D18, D19,
                             D20, D21, D22, D23, D24, D25, D26, D27, D28, D29,
                             D30, D31, D32, D33, D34, D35, D36, D37, D38, D39],
                 fastest_solution="D3 D18 S1 D15 D11 S0 D13 D19 S4 D16 D23 S3 D17 D12 S2 D14 D24 S5 D22 D20 S6 D26 D35 S10 D29 D25 S11 D30 D36 S7 D31 D21 S8 D27 D33 S12 D34 D37 S13 D38 D32 S9 D28 D4 D39",
                 level_color=Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.5),
                 name='Draw',
                 keep_proportions=True,
                 door_window_size=500)
    
    return level

