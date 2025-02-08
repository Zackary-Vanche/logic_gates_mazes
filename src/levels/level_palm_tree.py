from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

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
    S16 = Switch(name='S16')

    T0 = Tree(tree_list=['AND',
                         ['INFOREQU', Tree.tree_list_SUM(12), [None]],
                         ['SUP', Tree.tree_list_SUM(3), Tree.tree_list_SUM(3)]],
                name='T0',
                switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, 6,
                          S0, S1, S10,
                          S4, S6, S7,])
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
    T13 = Tree(tree_list=Tree.tree_list_AND(5),
                name='T13',
                switches=[S12, S13, S14, S15, S16])

    dx = 0.9
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[-1*dx, ey, ex, 2*dy],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11])
    R1 = Room(name='R1',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S12])
    R2 = Room(name='R2',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[S13])
    R4 = Room(name='R4',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[])
    R5 = Room(name='R5',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S14])
    R6 = Room(name='R6',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[])
    R7 = Room(name='R7',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S15])
    R8 = Room(name='R8',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[])
    R9 = Room(name='R9',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S16])
    RE = Room(name='RE',
              position=[-1*dx, 0*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
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
                room_departure=R2,
                room_arrival=R3)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R4,
                room_arrival=R5)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R5,
                room_arrival=R6)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R7,
                room_arrival=R8)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R8,
                room_arrival=R9)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R1,
                room_arrival=R4)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R4,
                room_arrival=R7)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R2,
                room_arrival=R5)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R5,
                room_arrival=R8)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R3,
                room_arrival=R6)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R6,
                room_arrival=R9)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R1,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13],
                 fastest_solution="S0 S1 S4 S5 S8 S9 D0 S12 D1 D2 S13 D2 D9 S14 D10 D5 S15 D5 D6 S16 D6 D10 D9 D1 D13",
                 level_color=get_color(),
                 name='Palm tree',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.175, sa=0.35, li=0.2)
    lcolor.surrounding_color = Color.TOTAL_GREEN
    return lcolor