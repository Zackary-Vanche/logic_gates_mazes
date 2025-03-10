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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12]

    tree_list = Tree.tree_list_NOR(2)
    
    T0 = Tree(tree_list=[None],
              name='T0',
              switches=[1])

    # NOT
    T1 = Tree(tree_list=['AND', tree_list, [None]],
                name='T1',
                switches=[S0, S0, S13])

    # AND
    V0 = Tree(tree_list=tree_list,
              name='V0',
              switches=[S1, S1])
    V1 = Tree(tree_list=tree_list,
              name='V1',
              switches=[S2, S2])
    T2 = Tree(tree_list=['AND', tree_list, [None]],
                name='T2',
                switches=[V0, V1, S13])

    # NAND
    V2 = Tree(tree_list=tree_list,
              name='V2',
              switches=[S3, S3])
    V3 = Tree(tree_list=tree_list,
              name='V3',
              switches=[S4, S4])
    V4 = Tree(tree_list=tree_list,
              name='V4',
              switches=[V2, V3])
    T3 = Tree(tree_list=['AND', tree_list, [None]],
                name='T3',
                switches=[V4, V4, S13])

    # OR
    V5 = Tree(tree_list=tree_list,
              name='V5',
              switches=[S5, S6])
    T4 = Tree(tree_list=['AND', tree_list, [None]],
                name='T4',
                switches=[V5, V5, S13])

    # NOR
    T5 = Tree(tree_list=['AND', tree_list, [None]],
                name='T5',
                switches=[S7, S8, S13])

    # XOR
    V6 = Tree(tree_list=tree_list,
              name='V6',
              switches=[S9, S9])
    V7 = Tree(tree_list=tree_list,
              name='V7',
              switches=[S9, S10])
    V8 = Tree(tree_list=tree_list,
              name='V8',
              switches=[S10, S10])
    V9 = Tree(tree_list=tree_list,
              name='V9',
              switches=[V6, V8])
    T6 = Tree(tree_list=['AND', tree_list, [None]],
                name='T6',
                switches=[V7, V9, S13])

    # XNOR
    V10 = Tree(tree_list=tree_list,
              name='V10',
              switches=[S11, S12])
    V11 = Tree(tree_list=tree_list,
              name='V11',
              switches=[S11, V10])
    V12 = Tree(tree_list=tree_list,
              name='V12',
              switches=[V10, S12])
    T7 = Tree(tree_list=['AND', tree_list, [None]],
                name='T7',
                switches=[V11, V12, S13])

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
              position=[3*dx, 0*dy, 2*ex, 7*ey],
              switches_list=Slist)
    R1 = Room(name='R1',
                position=[2*dx, 3*dy, ex, ey],
                switches_list=[S13])
    R2 = Room(name='R2',
                position=[1.55*dx, 2*dy, ex, ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[1.55*dx, 1*dy, ex, ey],
                switches_list=[])
    R4 = Room(name='R4',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[])
    R5 = Room(name='R5',
                position=[0.5*dx, 0*dy, ex, ey],
                switches_list=[])
    R6 = Room(name='R6',
                position=[0.95*dx, 1*dy, ex, ey],
                switches_list=[])
    R7 = Room(name='R7',
                position=[0.95*dx, 2*dy, ex, ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[0.5*dx, 3*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
              tree=T0,
              name='D0',
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[0, 6.5/7],
              relative_arrival_coordinates=[1, 1/2])
    D1 = Door(two_way=False,
              tree=T1,
              name='D1',
              room_departure=R1,
              room_arrival=R2)
    D2 = Door(two_way=False,
              tree=T2,
              name='D2',
              room_departure=R2,
              room_arrival=R3)
    D3 = Door(two_way=False,
              tree=T3,
              name='D3',
              room_departure=R3,
              room_arrival=R4)
    D4 = Door(two_way=False,
              tree=T4,
              name='D4',
              room_departure=R4,
              room_arrival=R5)
    D5 = Door(two_way=False,
              tree=T5,
              name='D5',
              room_departure=R5,
              room_arrival=R6)
    D6 = Door(two_way=False,
              tree=T6,
              name='D6',
              room_departure=R6,
              room_arrival=R7)
    D7 = Door(two_way=False,
              tree=T7,
              name='D7',
              room_departure=R7,
              room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7],
                 fastest_solution="S1 S2 S5 S9 D0 S13 D1 D2 D3 D4 D5 D6 D7",
                 level_color=get_color(),
                 name="Peirce's arrow",
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0, sa=0.4, li=0.5)
    lcolor.background_color = Color.BLACK
    lcolor.contour_color = Color.WHITE
    lcolor.inside_room_surrounding_color = Color.BLACK
    return lcolor