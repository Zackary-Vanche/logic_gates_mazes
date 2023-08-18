from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def level_sheffer_stroke():

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
    
    tree_list = Tree.tree_list_NAND(2)

    # NOT
    T0 = Tree(tree_list=tree_list,
                name='T0',
                switches=[S0, S0])

    # AND
    V0 = Tree(tree_list=tree_list,
              name='V0',
              switches=[S1, S2])
    T1 = Tree(tree_list=tree_list,
                name='T1',
                switches=[V0, V0])

    # NAND
    T2 = Tree(tree_list=tree_list,
                name='T2',
                switches=[S3, S4])

    # OR
    V1 = Tree(tree_list=tree_list,
              name='V1',
              switches=[S5, S5])
    V2 = Tree(tree_list=tree_list,
              name='V2',
              switches=[S6, S6])
    T3 = Tree(tree_list=tree_list,
              name='T3',
              switches=[V1, V2])

    # NOR
    V3 = Tree(tree_list=tree_list,
              name='V3',
              switches=[S7, S7])
    V4 = Tree(tree_list=tree_list,
              name='V4',
              switches=[S8, S8])
    V5 = Tree(tree_list=tree_list,
              name='V5',
              switches=[V3, V4])
    T4 = Tree(tree_list=tree_list,
              name='T4',
              switches=[V5, V5])

    # XOR
    V6 = Tree(tree_list=tree_list,
              name='V6',
              switches=[S9, S10])
    V7 = Tree(tree_list=tree_list,
              name='V7',
              switches=[S9, V6])
    V8 = Tree(tree_list=tree_list,
              name='V8',
              switches=[V6, S10])
    T5 = Tree(tree_list=tree_list,
              name='T5',
              switches=[V7, V8])

    # XNOR
    V9 = Tree(tree_list=tree_list,
              name='V9',
              switches=[S11, S12])
    V10 = Tree(tree_list=tree_list,
              name='V10',
              switches=[S11, V9])
    V11 = Tree(tree_list=tree_list,
              name='V11',
              switches=[V9, S12])
    V12 = Tree(tree_list=tree_list,
              name='V12',
              switches=[V10, V11])
    T6 = Tree(tree_list=tree_list,
                name='T6',
                switches=[V12, V12])
    dx = 1
    dy = 1
    ex = 1
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S0])
    R1 = Room(name='R1',
                position=[-0.5*dx, 1*dy, ex, ey],
                switches_list=[S1, S2])
    R2 = Room(name='R2',
                position=[-0.5*dx, 2*dy, ex, ey],
                switches_list=[S3, S4])
    R3 = Room(name='R3',
                position=[0*dx, 3*dy, ex, ey],
                switches_list=[S5, S6])
    R4 = Room(name='R4',
                position=[2*dx, 3*dy, ex, ey],
                switches_list=[S7, S8])
    R5 = Room(name='R5',
                position=[2.5*dx, 2*dy, ex, ey],
                switches_list=[S9, S10])
    R6 = Room(name='R6',
                position=[2.5*dx, 1*dy, ex, ey],
                switches_list=[S11, S12])
    RE = Room(name='RE',
              position=[2*dx, 0*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
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
                room_arrival=RE)
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0, sa=0.4, li=0.5)
    lcolor.background_color = Color.IVORY
    lcolor.letters_color = Color.BLACK
    lcolor.surrounding_color = Color.BLACK
    lcolor.contour_color = Color.BLACK

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution="D0 S1 S2 D1 D2 S5 D3 D4 S9 D5 D6",
                 level_color=lcolor,
                 name='Sheffer stroke',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level