from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import randint as rd_randint
from random import shuffle as rd_shuffle

def base2(l):
    return sum([l[i]*2**i for i in range(len(l))])

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
    S14 = Switch(name='S14')
    S15 = Switch(name='S15')
    
    N = 32
    n_bin = 8
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15]
    for S in Slist:
        S.value = rd_randint(0, 1)
    fastest_solution_list = []
    for i in range(5):
        for S in Slist:
            if S.value:
                fastest_solution_list.append(S.name)
    fastest_solution_list.append('D0')
    # fastest_solution = ' '.join(fastest_solution_list) # The fastest solution might be shorter
    
    tree_list = ['AND'] + [['EQU',
                            [None],
                            ['MOD', Tree.tree_list_BIN(n_bin), [None]]]]*N
    
    Slist0 = []
    for i in range(N):
        mod = 3
        rd_shuffle(Slist)
        Slisti = Slist[:n_bin]
        values = [S.value for S in Slisti]
        Slist0.append(base2(values)%mod)
        Slist0.extend(Slisti)
        Slist0.append(mod)
        
    T0 = Tree(tree_list=tree_list,
              name='T0',
              switches = Slist0,
              cut_expression=True,
              cut_expression_separator=' 3')
    
    R0 = Room(name='R0',
              position = [0, 4, 8, 8],
              switches_list = Slist)
    RE = Room(name='RE',
              position=[3, 0, 2, 2],
              is_exit=True)   # E pour exit ou end
    
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=RE,
              relative_departure_coordinates=[1/2, 0],
              relative_arrival_coordinates=[1/2, 1])
    
    for S in Slist:
        S.value = 0

    level = Maze(start_room_index=0, 
             exit_room_index=-1, 
             rooms_list=[R0, RE], 
             doors_list=[D0], 
             fastest_solution=None,
             level_color=get_color(),
             name='Shuffled',
             random=True,
             door_window_size = 444,
             keep_proportions = True)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.7, sa=0.1, li=0.3)