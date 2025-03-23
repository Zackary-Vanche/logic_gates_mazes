from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    Slist_0 = [S0, S1]
    Slist_1 = [S2, S3]
    Slist_2 = [S4, S5]
    Slist_3 = [S6, S7]
    tl = ["SUM",
          ["PROD", Tree.tree_list_from_str('TF'), [None]],
          ["PROD", Tree.tree_list_from_str('FF'), [None]],
          ["PROD", Tree.tree_list_from_str('FT'), [None]]]
    V0 = Tree(tree_list=tl,
          name='V0',
          switches=[S0, S1, -1,
                    S0, S1, 0,
                    S0, S1, 1])
    V1 = Tree(tree_list=tl,
          name='V1',
          switches=[S2, S3, -1,
                    S2, S3, 0,
                    S2, S3, 1])
    V2 = Tree(tree_list=tl,
          name='V2',
          switches=[S4, S5, -1,
                    S4, S5, 0,
                    S4, S5, 1])
    V3 = Tree(tree_list=tl,
          name='V3',
          switches=[S6, S7, -1,
                    S6, S7, 0,
                    S6, S7, 1])
    V4 = Tree(tree_list=["SUM"]+[["PROD", [None], ["POW", [None], [None]]]]*4,
          name='V4',
          switches=[V0, 3, 0,
                    V1, 3, 1,
                    V2, 3, 2,
                    V3, 3, 3,],
          cut_expression_depth_1=True)

    T0 = Tree(tree_list=Tree.tree_list_NAND(2),
                name='T0',
                switches=[S0, S1])
    T1 = Tree(tree_list=Tree.tree_list_NAND(2),
                name='T1',
                switches=[S2, S3])
    T2 = Tree(tree_list=Tree.tree_list_NAND(2),
                name='T2',
                switches=[S4, S5])
    T3 = Tree(tree_list=Tree.tree_list_NAND(2),
                name='T3',
                switches=[S6, S7])
    
    n = 0
    for k in range(4):
        n += rd_choice([-1, 0, +1]) * 3**k
    
    T4 = Tree(tree_list=Tree.tree_list_EQU(2),
                name='T4',
                switches=[V4, n])

    dx = 1
    dy = 1.5
    ex = 0.5
    ey = 1
    ay = 0.25
    eye = 0.65

    R0 = Room(name='R0',
                position=[0*dx, ay, ex, ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[3*dx, ay, ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[2*dx, 1*dy, ex, eye],
                switches_list=[])
    RE = Room(name='RE',
              position=[1*dx, 1*dy, ex, eye],
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
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Balanced ternary',
                 keep_proportions=True,
                 door_window_size=450,
                 random=True)
    
    sol_list = level.find_all_solutions()[0]
    sol = ' '.join(sol_list[0])
    level.fastest_solution = sol
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.45, sa=0.15, li=0.7)
    lcolor.surrounding_color = Color.IVORY
    lcolor.contour_color = Color.IVORY
    return lcolor