from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from random import shuffle as rd_shuffle 

def level_conjunctive_normal_form():

    S0 = Switch(name='S0', value = rd_choice([0, 1]))
    S1 = Switch(name='S1', value = rd_choice([0, 1]))
    S2 = Switch(name='S2', value = rd_choice([0, 1]))
    S3 = Switch(name='S3', value = rd_choice([0, 1]))
    S4 = Switch(name='S4', value = rd_choice([0, 1]))
    S5 = Switch(name='S5', value = rd_choice([0, 1]))
    S6 = Switch(name='S6', value = rd_choice([0, 1]))
    S7 = Switch(name='S7', value = rd_choice([0, 1]))
    S8 = Switch(name='S8', value = rd_choice([0, 1]))

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8]
    
    CNF_expression_list = []
    Slist_T0 = []
    for k in range(40):
        rd_shuffle(Slist)
        A0, A1, A2 = Slist[:3]
        b0 = str(A0.value)
        b1 = rd_choice(['0', '1'])
        b2 = rd_choice(['0', '1'])
        l = [[A0, b0], [A1, b1], [A2, b2]]
        l.sort(key = lambda x : x[0].name)
        [[A0, b0], [A1, b1], [A2, b2]] = l
        CNF_expression_list.append(''.join([b0, b1, b2]))
        Slist_T0.extend([A0, A1, A2])

    T0 = Tree(tree_list=Tree.tree_list_from_str(' '.join(CNF_expression_list), CNF=True),
              name='T0',
              switches=Slist_T0,
              cut_expression=True)

    dx = 1
    dy = 1
    ex = 1
    ey = 1
    
    Slist.sort(key = lambda x : x.name)

    R0 = Room(name='R0',
                position=[-1*dx, 0*dy, 3*ex, ey/3],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8])
    RE = Room(name='RE',
              position=[0*dx, -1*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
              tree=T0,
              name='D0',
              room_departure=R0,
              room_arrival=RE,
              relative_departure_coordinates=[1, 0],
              relative_arrival_coordinates=[1, 1/2])
    
    solution_list = []
    for S in Slist:
        solution_list.append(S.name*S.value)
    solution_list.append('D0')
    solution = ' '.join(solution_list)
    
    for S in Slist:
        S.value = 0

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution=solution,
                 level_color=Levels_colors_list.FROM_HUE(hu=0, sa=0.4, li=0.3),
                 name='Conjunctive normal form',
                 keep_proportions=True,
                 door_window_size=222,
                 random=True)
    
    return level