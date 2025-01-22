from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from random import shuffle as rd_shuffle

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
    
    tree_list = ['AND']
    Slist_T0 = []
    Slist_old = Slist[:]
    rd_shuffle(Slist)
    Slist_new = [Slist_old.pop(0)]
    for S_old in Slist_old:
        S_new = rd_choice(Slist_new)
        l = [S_old, S_new]
        l.sort(key = lambda x : x.name)
        Slist_T0.extend(l)
        if S_old.value == S_new.value:
            tree_list.append(Tree.tree_list_XNOR(2))
        else:
            tree_list.append(Tree.tree_list_XOR(2))
        Slist_new.append(S_old)
    rd_shuffle(Slist_new)
    [Sa, Sb] = Slist_new[:2]
    Slist_T0.extend([Sa, Sb])
    str_bool = str(int(not Sa.value)) + str(int(not Sb.value))
    tree_list.append(['NOT', Tree.tree_list_from_str(str_bool)])

    T0 = Tree(tree_list=tree_list,
              name='T0',
              switches=Slist_T0,
              cut_expression_depth_1=True)

    dx = 1
    dy = 1
    ex = 1
    ey = 1
    
    Slist.sort(key = lambda x : x.name)

    R0 = Room(name='R0',
                position=[0*dx, 0*dy+2*ey/2, 5*ex, 3*ey],
                switches_list=Slist)
    RE = Room(name='RE',
              position=[0*dx+2*ex, 0*dy, ex, ey/2],
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
    solution_list.append('D0')
    solution = ' '.join(solution_list)
    
    for S in Slist:
        S.value = 0

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution=solution,
                 level_color=get_color(),
                 name='Branches',
                 keep_proportions=True,
                 door_window_size=450)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.4, sa=0.2, li=0.5)