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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15]
    
    tree_list_XOR2 = Tree.tree_list_XOR(2)

    V0 = Tree(tree_list=tree_list_XOR2,
          name='V0',
          switches=[S0, S1])
    V1 = Tree(tree_list=tree_list_XOR2,
          name='V1',
          switches=[S0, S2])
    V2 = Tree(tree_list=tree_list_XOR2,
          name='V2',
          switches=[S1, S3])
    V3 = Tree(tree_list=tree_list_XOR2,
          name='V3',
          switches=[S1, S4])
    V4 = Tree(tree_list=tree_list_XOR2,
          name='V4',
          switches=[S2, S4])
    V5 = Tree(tree_list=tree_list_XOR2,
          name='V5',
          switches=[S3, S5])
    V6 = Tree(tree_list=tree_list_XOR2,
          name='V6',
          switches=[S4, S5])

    T0 = Tree(tree_list=['AND',
                         ['EQU', Tree.tree_list_SUM(2), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(4), [None]],
                         ['EQU', Tree.tree_list_SUM(2), [None]],
                         ['EQU', Tree.tree_list_SUM(2), [None]],
                         ['EQU', Tree.tree_list_SUM(4), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(2), [None]],
                         ['EQU', Tree.tree_list_SUM(6), [None]],
                         ['SUP', Tree.tree_list_SUM(8), [None]],
                         ],
                name='T0',
                switches=[S6, S7, 1,
                          S6, S8, V0, 2,
                          S7, S9, V1, 2,
                          S8, S10, V2, 2,
                          V0, V1, V3, V4, 2,
                          S9, S11, 2,
                          S10, S12, 1,
                          V2, V3, V5, V6, 2,
                          S11, S13, V4, 2,
                          S12, S14, V5, 2,
                          S13, S15, V6, 2,
                          S14, S15, 2,
                          S0, S1, S2, S3, S4, S5, 2,
                          S7, S9, S12, S14, V0, V2, V4, V6, 4,
                          ],
                cut_expression_depth_1=True)
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[S6])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[S7])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[S8])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[V0])
    T5 = Tree(tree_list=[None],
                name='T5',
                switches=[V1])
    T6 = Tree(tree_list=[None],
                name='T6',
                switches=[S9])
    T7 = Tree(tree_list=[None],
                name='T7',
                switches=[S10])
    T8 = Tree(tree_list=[None],
                name='T8',
                switches=[V2])
    T9 = Tree(tree_list=[None],
                name='T9',
                switches=[V3])
    T10 = Tree(tree_list=[None],
                name='T10',
                switches=[V4])
    T11 = Tree(tree_list=[None],
                name='T11',
                switches=[S11])
    T12 = Tree(tree_list=[None],
                name='T12',
                switches=[S12])
    T13 = Tree(tree_list=[None],
                name='T13',
                switches=[V5])
    T14 = Tree(tree_list=[None],
                name='T14',
                switches=[V6])
    T15 = Tree(tree_list=[None],
                name='T15',
                switches=[S13])
    T16 = Tree(tree_list=[None],
                name='T16',
                switches=[S14])
    T17 = Tree(tree_list=[None],
                name='T17',
                switches=[S15])
    T18 = Tree(tree_list=[None],
                name='T18',
                switches=[1])

    dx = 1
    dy = 1
    ex = 0.6
    ey = 0.6
    
    d0 = 2*dx/3
    d1 = dx/3

    R0 = Room(name='R0',
              position=[0*dx, -1*dy-0.25+ey, 4*dx+ex, 0.25],
              switches_list=Slist)
    R1 = Room(name='R1',
              position=[0*dx, 0*dy, ex, ey],
              switches_list=[])
    R2 = Room(name='R2',
              position=[1*dx+d0/3, 0*dy, ex, ey],
              switches_list=[])
    R3 = Room(name='R3',
              position=[0*dx, 1*dy, ex, ey],
              switches_list=[])
    R4 = Room(name='R4',
              position=[2*dx+2*d0/3, 0*dy, ex, ey],
              switches_list=[])
    R5 = Room(name='R5',
              position=[1*dx+d1/3, 1*dy, ex, ey],
              switches_list=[])
    R6 = Room(name='R6',
              position=[0*dx, 2*dy, ex, ey],
              switches_list=[])
    R7 = Room(name='R7',
              position=[3*dx+d0, 0*dy, ex, ey],
              switches_list=[])
    R8 = Room(name='R8',
              position=[2*dx+2*d1/3, 1*dy, ex, ey],
              switches_list=[])
    R9 = Room(name='R9',
              position=[1*dx, 2*dy, ex, ey],
              switches_list=[])
    R10 = Room(name='R10',
               position=[3*dx+d1, 1*dy, ex, ey],
               switches_list=[])
    R11 = Room(name='R11',
               position=[2*dx, 2*dy, ex, ey],
               switches_list=[])
    R12 = Room(name='R12',
               position=[3*dx, 2*dy, ex, ey],
               switches_list=[])
    RE = Room(name='RE',
              position=[4*dx, 2*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
              tree=T0,
              name='D0',
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1/4, 1/2])
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
                room_departure=R2,
                room_arrival=R4)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R5)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R5)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R3,
                room_arrival=R6)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R4,
                room_arrival=R7)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R4,
                room_arrival=R8)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R5,
                room_arrival=R8)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R5,
                room_arrival=R9)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R6,
                room_arrival=R9)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R7,
                room_arrival=R10)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R8,
                room_arrival=R10)
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R8,
                room_arrival=R11)
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R9,
                room_arrival=R11)
    D16 = Door(two_way=True,
                tree=T16,
                name='D16',
                room_departure=R10,
                room_arrival=R12)
    D17 = Door(two_way=True,
                tree=T17,
                name='D17',
                room_departure=R11,
                room_arrival=R12)
    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=R7,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18],
                 fastest_solution="S1 S4 S7 S8 S9 S11 S12 S14 S15 D0 D2 D6 D11 D10 D4 D3 D8 D14 D17 D16 D12 D18",
                 level_color=Levels_colors_list.FROM_HUE(hu=0.7, sa=0.3, li=0.5),
                 name='Expedition',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level