from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def level_fir(fast_solution_finding=False):
    
    v = 0

    S0 = Switch(name='S0', value=v)
    S1 = Switch(name='S1', value=v)
    S2 = Switch(name='S2', value=v)
    S3 = Switch(name='S3', value=v)
    S4 = Switch(name='S4', value=v)
    S5 = Switch(name='S5', value=v)
    S6 = Switch(name='S6', value=v)
    S7 = Switch(name='S7', value=v)
    S8 = Switch(name='S8', value=v)
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8]
    
    V0 = Tree(tree_list=['AND',
                         ['EQU', Tree.tree_list_SUM(9), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(4), [None]]],
              name='V0',
              switches=Slist+[5,
                              S0, S1, S2, 2,
                              S2, S3, S4, S7, 3])

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[V0])
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[V0])
    T2 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T2',
                switches=[S0, S10])
    T3 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T3',
                switches=[S1, S9])
    T4 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T4',
                switches=[S2, S9])
    T5 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T5',
                switches=[S3, S10])
    T6 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T6',
                switches=[S4, S12])
    T7 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T7',
                switches=[S5, S13])
    T8 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T8',
                switches=[S6, S14])
    T9 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T9',
                switches=[S7, S12])
    T10 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T10',
                switches=[S8, S14])
    T11 = Tree(tree_list=Tree.tree_list_AND(6),
                name='T11',
                switches=[S9, S10, S11, S12, S13, S14])

    dx = 1.5
    dy = 1
    ex = 0.75
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 3*dy, 2*dx+ex, ey/2],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S9])
    R2 = Room(name='R2',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S10])
    R3 = Room(name='R3',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S11])
    R4 = Room(name='R4',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S12])
    R5 = Room(name='R5',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S13])
    R6 = Room(name='R6',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S14])
    RE = Room(name='RE',
              position=[2*dx, 2*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R2)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R3)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R1,
                room_arrival=R4)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R2,
                room_arrival=R4)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R3,
                room_arrival=R4)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R3,
                room_arrival=R5)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R3,
                room_arrival=R6)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R4,
                room_arrival=R6)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R5,
                room_arrival=R6)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R2,
                room_arrival=RE)

    lcolor = Levels_colors_list.FROM_HUE(hu=0.4, sa=0.5, li=0.175)
    lcolor.background_color = Color.color_hls(hu=0.16, sa=0.5, li=0.075)
    
    if fast_solution_finding:
        for room in [R1, R2, R3, R4, R5, R6]:
            room.possible_switches_values = [[1]]

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11],
                 fastest_solution="S0 S2 S4 S7 S8 D1 S10 D2 S9 D4 S12 D6 S11 D6 D9 S14 D10 S13 D10 D9 D4 D2 D11",
                 level_color=lcolor,
                 name='Fir',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level