from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice

def f(): 

    S0 = Switch(name='S0', value = rd_choice([0, 1]))
    S1 = Switch(name='S1', value = rd_choice([0, 1]))
    S2 = Switch(name='S2', value = rd_choice([0, 1]))
    S3 = Switch(name='S3', value = rd_choice([0, 1]))
    S4 = Switch(name='S4', value = rd_choice([0, 1]))
    S5 = Switch(name='S5', value = rd_choice([0, 1]))
    S6 = Switch(name='S6', value = rd_choice([0, 1]))
    S7 = Switch(name='S7', value = rd_choice([0, 1]))
    S8 = Switch(name='S8', value = rd_choice([0, 1]))
    S9 = Switch(name='S9', value = rd_choice([0, 1]))
    S10 = Switch(name='S10', value = rd_choice([0, 1]))
    S11 = Switch(name='S11', value = rd_choice([0, 1]))
    S12 = Switch(name='S12', value = rd_choice([0, 1]))
    S13 = Switch(name='S13', value = rd_choice([0, 1]))
    S14 = Switch(name='S14', value = rd_choice([0, 1]))

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14]
    
    Slist_aux = [[S0, S1, S2, S3, S4],
                 [S0, S5, S6, S7, S8],
                 [S1, S5, S9, S10, S11],
                 [S2, S6, S9, S12, S13],
                 [S3, S7, S10, S12, S14],
                 [S4, S8, S11, S13, S14],]

    Slist_T0 = []
    for l in Slist_aux:
        a = 0
        for S in l:
            Slist_T0.append(S)
            a += S.get_value()
        Slist_T0.append(a)

    T0 = Tree(tree_list=["AND"] + [['EQU', Tree.tree_list_SUM(5), [None]]]*5,
              name='T0',
              switches=Slist_T0,
              cut_expression_depth_1=True)

    dx = 1
    dy = 1
    ex = 1
    ey = 1

    R0 = Room(name='R0',
              position=[0*dx, 0*dy, 3*ex, 5*ey],
              switches_list=Slist)
    RE = Room(name='RE',
              position=[1*dx, -2*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[1/2, 1])
    
    solution_list = []
    for S in Slist:
        if S.value:
            solution_list.append(S.name)
    solution_list.append("D0")
    
    for S in Slist:
        S.value = 0

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution=" ".join(solution_list),
                 level_color=Levels_colors_list.FROM_HUE(hu=0.16, sa=0.4, li=0.5),
                 name='Connectivity',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level