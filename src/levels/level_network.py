from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from Color import Color

def f(): 

    A0 = Switch(name='S0', value = rd_choice([0, 1]))
    A1 = Switch(name='S1', value = rd_choice([0, 1]))
    B0 = Switch(name='S2', value = rd_choice([0, 1]))
    B1 = Switch(name='S3', value = rd_choice([0, 1]))
    C0 = Switch(name='S4')
    C1 = Switch(name='S5')
    C2 = Switch(name='S6')
    C3 = Switch(name='S7')
    
    a = A0.value + A1.value*2
    b = B0.value + B1.value*2
    c = a*b
    str_c = bin(c)[2:]
    while len(str_c) < 5:
        str_c = '0' + str_c
    bin_c = []
    for k in str_c:
        bin_c.append(int(k))
    bin_c.reverse()
    
    # Names of the V elements are inverted on purpose

    V0 = Tree(tree_list=Tree.tree_list_AND(2),
              name='V1',
              switches=[A0, B1])
    V1 = Tree(tree_list=Tree.tree_list_AND(2), # C0
              name='V0',
              switches=[A0, B0])
    V2 = Tree(tree_list=Tree.tree_list_AND(2),
              name='V2',
              switches=[A1, B0])
    V3 = Tree(tree_list=Tree.tree_list_AND(2),
              name='V3',
              switches=[A1, B1])
    V4 = Tree(tree_list=Tree.tree_list_XOR(2), # C1
              name='V4',
              switches=[V0, V2])
    V5 = Tree(tree_list=Tree.tree_list_AND(2),
              name='V5',
              switches=[V0, V2])
    V6 = Tree(tree_list=Tree.tree_list_XOR(2), # C2
              name='V6',
              switches=[V3, V5])
    V7 = Tree(tree_list=Tree.tree_list_AND(2), # C3
              name='V7',
              switches=[V3, V5])
    T0 = Tree(tree_list=['AND'] + [['EQU', [None], [None]]]*4,
              name='T0',
              switches=[C0, V1,
                        C1, V4,
                        C2, V6,
                        C3, V7])

    dx = 1
    dy = 1
    ex = 1
    ey = 1

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[A0, A1, B0, B1])
    R1 = Room(name='R1',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[C0, C1, C2, C3])
    RE = Room(name='RE',
              position=[2*dx, -1*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R1,
                room_arrival=RE)
    
    sol = 'S4 ' * bin_c[0] + 'S5 ' * bin_c[1] + 'S6 ' * bin_c[2] + 'S7 ' * bin_c[3]
    sol = sol + 'D0'

    level = Maze(start_room_index=1,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, RE],
                 doors_list=[D0],
                 fastest_solution=sol,
                 level_color=get_color(),
                 name='Network',
                 keep_proportions=True,
                 door_window_size=400,
                 random=True)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.2)
    lcolor.surrounding_color = Color.TOTAL_RED
    lcolor.contour_color = Color.TOTAL_RED
    return lcolor