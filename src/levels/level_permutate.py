from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2', value=1)
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5', value=1)
    S6 = Switch(name='S6', value=1)
    S7 = Switch(name='S7', value=1)
    S8 = Switch(name='S8')
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    S12 = Switch(name='S12')
    S13 = Switch(name='S13')

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13]

    V0 = Tree(tree_list=Tree.tree_list_BIN(2),
          name='V0',
          switches=[S0, S1])
    V1 = Tree(tree_list=Tree.tree_list_BIN(2),
          name='V1',
          switches=[S2, S3])
    V2 = Tree(tree_list=Tree.tree_list_BIN(2),
          name='V2',
          switches=[S4, S5])
    V3 = Tree(tree_list=Tree.tree_list_BIN(2),
          name='V3',
          switches=[S6, S7])
    
    tree_list_DIFF = ['DIFF', [None], [None]]
    
    tree_list_4 = ['AND'] + [['EQU', [None], [None]]]*3

    T0 = Tree(tree_list=['AND',
                         Tree.tree_list_OR(2),
                         ['EQUSET'] + [[None]]*6],
                name='T0',
                switches=[S0, S1,
                          V1, V2, V3, 1, 2, 3])
    T1 = Tree(tree_list=tree_list_DIFF,
                name='T1',
                switches=[V0, 1])
    T2 = Tree(tree_list=tree_list_DIFF,
                name='T2',
                switches=[V0, 2])
    T3 = Tree(tree_list=tree_list_DIFF,
                name='T3',
                switches=[V0, 3])
    T4 = Tree(tree_list=tree_list_4,
                name='T4',
                switches=[V1, 1, V2, 2, V3, 3])
    T5 = Tree(tree_list=tree_list_4,
                name='T5',
                switches=[V1, 1, V2, 3, V3, 2])
    T6 = Tree(tree_list=tree_list_4,
                name='T6',
                switches=[V1, 2, V2, 1, V3, 3])
    T7 = Tree(tree_list=tree_list_4,
                name='T7',
                switches=[V1, 2, V2, 3, V3, 1])
    T8 = Tree(tree_list=tree_list_4,
                name='T8',
                switches=[V1, 3, V2, 1, V3, 2])
    T9 = Tree(tree_list=tree_list_4,
                name='T9',
                switches=[V1, 3, V2, 2, V3, 1])
    T10 = Tree(tree_list=Tree.tree_list_from_str('FFTFFTTTTTTTTT'),
                name='T10',
                switches=Slist)

    dx = 1.25
    dy = 1
    ex = 0.75
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S0, S1])
    R1 = Room(name='R1',
                position=[0*dx, -1*dy, ex, ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[-1*dx, -2*dy, ex, ey],
                switches_list=[S2, S3])
    R3 = Room(name='R3',
                position=[0*dx, -2*dy, ex, ey],
                switches_list=[S4, S5])
    R4 = Room(name='R4',
                position=[1*dx, -2*dy, ex, ey],
                switches_list=[S6, S7])
    R5 = Room(name='R5',
                position=[-1*dx, -1*dy, ex, ey],
                switches_list=[S8])
    R6 = Room(name='R6',
                position=[-1*dx, 0*dy, ex, ey],
                switches_list=[S9])
    R7 = Room(name='R7',
                position=[-1*dx, 1*dy, ex, ey],
                switches_list=[S10])
    R8 = Room(name='R8',
                position=[1*dx, -1*dy, ex, ey],
                switches_list=[S11])
    R9 = Room(name='R9',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S12])
    R10 = Room(name='R10',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S13])
    RE = Room(name='RE',
              position=[0*dx, 1*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
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
                room_departure=R0,
                room_arrival=R5)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R0,
                room_arrival=R6)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=R7)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R0,
                room_arrival=R8)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R0,
                room_arrival=R9)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R0,
                room_arrival=R10)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R0,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10],
                 fastest_solution="S0 D0 D2 S4 D2 D3 S6 D3 D0 S1 D5 S9 D5 D0 D1 S3 D1 D2 S5 D2 D0 S0 D8 S12 D8 D0 D1 S2 D1 D3 S6 D3 D0 S0 S1 D6 S10 D6 D0 D2 S5 D2 D3 S7 D3 D0 S1 D7 S11 D7 D0 D1 S2 D1 D2 S4 D2 D0 S0 D9 S13 D9 D0 D1 S3 D1 D3 S7 D3 D0 S1 D4 S8 D4 D10",
                 level_color=get_color(),
                 name='Permutate',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

get_color = lambda : Levels_colors_list.different_hues(hu_index=11, inverse_hues=True)