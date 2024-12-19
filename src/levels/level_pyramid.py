from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from Color import Color

def f(): 

    S0 = Switch(name='S0', value=rd_choice([0, 1]))
    S1 = Switch(name='S1', value=rd_choice([0, 1]))
    S2 = Switch(name='S2', value=rd_choice([0, 1]))
    S3 = Switch(name='S3', value=rd_choice([0, 1]))
    S4 = Switch(name='S4', value=rd_choice([0, 1]))
    
    tree_list_list = [Tree.tree_list_AND(2),
                      Tree.tree_list_OR(2),
                      Tree.tree_list_NAND(2),
                      Tree.tree_list_NOR(2),
                      Tree.tree_list_XOR(2),
                      Tree.tree_list_XNOR(2)]

    V0 = Tree(tree_list=rd_choice(tree_list_list),
              name='V0',
              switches=[S0, S1])
    V1 = Tree(tree_list=rd_choice(tree_list_list),
              name='V1',
              switches=[S1, S2])
    V2 = Tree(tree_list=rd_choice(tree_list_list),
              name='V2',
              switches=[S2, S3])
    V3 = Tree(tree_list=rd_choice(tree_list_list),
              name='V3',
              switches=[S3, S4])
    V4 = Tree(tree_list=rd_choice(tree_list_list),
              name='V4',
              switches=[V0, V1])
    V5 = Tree(tree_list=rd_choice(tree_list_list),
              name='V5',
              switches=[V1, V2])
    V6 = Tree(tree_list=rd_choice(tree_list_list),
              name='V6',
              switches=[V2, V3])
    V7 = Tree(tree_list=rd_choice(tree_list_list),
              name='V7',
              switches=[V4, V5])
    V8 = Tree(tree_list=rd_choice(tree_list_list),
              name='V8',
              switches=[V5, V6])
    V9 = Tree(tree_list=rd_choice(tree_list_list),
              name='V9',
              switches=[V7, V8])
    # V10 = Tree(tree_list=rd_choice(tree_list_list),
    #           name='V10',
    #           switches=[S12, S13])
    
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
    # S15 = Switch(name='S15')

    Slist = [S0, S1, S2, S3, S4,
             S5, S6, S7, S8, S9, S10, S11, S12, S13, S14]
    
    Vlist = [V0, V1, V2, V3, V4, V5, V6, V7, V8, V9]
    
    Slist0 = []
    for i in range(len(Vlist)):
        Slist0.append(Vlist[i])
        Slist0.append(Slist[i+5])

    T0 = Tree(tree_list=['AND'] + [['EQU', [None], [None]]]*5,
              name='T0',
              switches=Slist0)

    dx = 1
    dy = 1
    ex = 1
    ey = 1

    R0 = Room(name='R0',
              position=[2*dx, 1*dy, ex, 5*ey],
              switches_list=[S0, S1, S2, S3, S4])
    R1 = Room(name='R1',
              position=[0*dx, 2*dy, 1.5*ex, 4*ey],
              switches_list=[S5, S6, S7, S8, S9, S10, S11, S12, S13, S14])
    RE = Room(name='RE',
              position=[0*dx, 0*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
              tree=T0,
              name='D0',
              room_departure=R1,
              room_arrival=RE,
              relative_departure_coordinates=[1/2, 1/8])
    
    solution_list = []
    for i in range(len(Vlist)):
        V = Vlist[i]
        S = Slist[i+5]
        if V.get_value():
            solution_list.append(S.name)
    solution_list.append('D0')
    solution = ' '.join(solution_list)
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.4)
    lcolor.surrounding_color = Color.REALLY_BRIGHT_GREEN
    lcolor.contour_color = Color.REALLY_BRIGHT_GREEN

    level = Maze(start_room_index=1,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, RE],
                 doors_list=[D0],
                 fastest_solution=solution,
                 level_color=lcolor,
                 name='Pyramid',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level