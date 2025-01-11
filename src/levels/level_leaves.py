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
    
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    

    Slist = [S0, S1, S2, S3, S4, S5]
    
    dx = 1
    dy = 1
    ex = 0.75
    ey = 0.75
    
    R0 = Room(name='R0',
                position=[-0.5*dx, 7.5*dy, 9*ex, ey/2],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[1*dx, 6*dy, ex, ey],
                switches_list=[S6])
    R2 = Room(name='R2',
                position=[-0.5*dx, 5*dy, ex, ey],
                switches_list=[S7])
    R3 = Room(name='R3',
                position=[1.5*dx, 2.5*dy, ex, ey],
                switches_list=[S8])
    R4 = Room(name='R4',
                position=[3.5*dx, 2.5*dy, ex, ey],
                switches_list=[S9])
    R5 = Room(name='R5',
                position=[5.5*dx, 5*dy, ex, ey],
                switches_list=[S10])
    R6 = Room(name='R6',
                position=[4*dx, 6*dy, ex, ey],
                switches_list=[S11])
    RE = Room(name='RE',
              position=[5.5*dx, 2.5*dy, ex, ey],
              is_exit=True)
    
    dico = {'S0' : R1,
            'S1' : R2,
            'S2' : R3,
            'S3' : R4,
            'S4' : R5,
            'S5' : R6}
    
    Slist_list = []
    tree_list_list = []
    Rlist_list = []
    rd_shuffle(Slist)
    Slist_old = Slist[:]
    Slist_new = [Slist_old.pop(0)]
    for S_old in Slist_old:
        S_new = rd_choice(Slist_new)
        l = [S_old, S_new]
        l.sort(key = lambda x : x.name)
        Slist_list.append(l)
        Slist_new.append(S_old)
        if S_old.value == S_new.value:
            tree_list_list.append(Tree.tree_list_XNOR(2))
        else:
            tree_list_list.append(Tree.tree_list_XOR(2))
        R_old = dico[S_old.name]
        R_new = dico[S_new.name]
        Rlist_list.append([R_old, R_new])
        
    rd_shuffle(Slist_new)
    [Sa, Sb] = Slist_new[:2]
    str_bool = str(int(not Sa.value)) + str(int(not Sb.value))
    T0 = Tree(tree_list=['NOT', Tree.tree_list_from_str(str_bool)],
              name='T0',
              switches=[Sa, Sb])

    T1 = Tree(tree_list=tree_list_list[0],
                name='T1',
                switches=Slist_list[0])
    T2 = Tree(tree_list=tree_list_list[1],
                name='T2',
                switches=Slist_list[1])
    T3 = Tree(tree_list=tree_list_list[2],
                name='T3',
                switches=Slist_list[2])
    T4 = Tree(tree_list=tree_list_list[3],
                name='T4',
                switches=Slist_list[3])
    T5 = Tree(tree_list=tree_list_list[4],
                name='T5',
                switches=Slist_list[4])
    T6 = Tree(tree_list=Tree.tree_list_AND(6),
                name='T6',
                switches=[S6, S7, S8, S9, S10, S11])
    
    Slist.sort(key = lambda x : x.name)
    
    rp = 0.5

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=Rlist_list[0][0],
                room_arrival=Rlist_list[0][1],
                relative_position=rp)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=Rlist_list[1][0],
                room_arrival=Rlist_list[1][1],
                relative_position=rp)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=Rlist_list[2][0],
                room_arrival=Rlist_list[2][1],
                relative_position=rp)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=Rlist_list[3][0],
                room_arrival=Rlist_list[3][1],
                relative_position=rp)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=Rlist_list[4][0],
                room_arrival=Rlist_list[4][1],
                relative_position=rp)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R5,
                room_arrival=RE)
    
    for S in Slist:
        S.value = 0

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Leaves',
                 keep_proportions=True,
                 door_window_size=450,
                 random=True)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.4, sa=0.25, li=0.5)