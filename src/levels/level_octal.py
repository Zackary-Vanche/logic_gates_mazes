from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle
from random import choice as rd_choice

def level_octal(): 

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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14]

    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    Slist_3 = [S9, S10, S11]
    Slist_4 = [S12, S13, S14]
    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_0)),
          name='V0',
          switches=Slist_0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_1)),
          name='V1',
          switches=Slist_1)
    V2 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_2)),
          name='V2',
          switches=Slist_2)
    V3 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_3)),
          name='V3',
          switches=Slist_3)
    V4 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_4)),
          name='V4',
          switches=Slist_4)
    
    Vlist = [V0, V1, V2, V3, V4]
    Vlist_0 = Vlist.copy()
    V_values = [i for i in range(8)]
    rd_shuffle(V_values)
    V_values = V_values[:5]
    
    tree_list_0 = ["AND"]
    Slist_T0 = []
    Sum_tot = 0
    for i in range(9):
        i_V_eq = rd_choice([i for i in range(5)])
        V_eq = Vlist_0[i_V_eq]
        V = Tree(tree_list=[None], name=f'V{len(Vlist)}', switches=[V_eq])
        Vlist.append(V)
        tree_list_0.append(Tree.tree_list_EQU(2))
        Slist_T0.extend([V, V_eq])
        Sum_tot += V_values[i_V_eq]*4**(i_V_eq%3)
    assert len(Vlist) == 5+9
    digit_sum = []    
    while Sum_tot > 0 or len(digit_sum) < 4:
        digit_sum.append(Sum_tot%8)
        Sum_tot = Sum_tot//8
    assert len(digit_sum) == 4
    print(digit_sum)
    for i_d, d in enumerate(digit_sum):
        if d in V_values:
            for i_V_eq in range(5):
                if d == V_values[i_V_eq]:
                    V_eq = Vlist_0[i_V_eq]
                    V = Tree(tree_list=[None], name=f'V{len(Vlist)}', switches=[V_eq])
                    Vlist.append(V)
                    tree_list_0.append(Tree.tree_list_EQU(2))
                    Slist_T0.extend([V, V_eq])
                    break
        else:
            V_eq = d
            V = Tree(tree_list=[None], name=f'V{len(Vlist)}', switches=[V_eq])
            Vlist.append(V)
            tree_list_0.append(Tree.tree_list_EQU(2))
            Slist_T0.extend([V, V_eq])
    assert len(Vlist) == 5+9+4, str(len(Vlist))
            
    print([V.name for V in Vlist])
            
    tree_list_19 = ["SUM", [None], Tree.tree_list_PROD(2), Tree.tree_list_PROD(2)]
    V19 = Tree(tree_list=tree_list_19,
               name="V19",
               switches=[Vlist[5], 8, Vlist[6], 64, Vlist[7]])
    V20 = Tree(tree_list=tree_list_19,
               name="V20",
               switches=[Vlist[8], 8, Vlist[9], 64, Vlist[10]])
    V21 = Tree(tree_list=tree_list_19,
               name="V21",
               switches=[Vlist[11], 8, Vlist[12], 64, Vlist[13]])
    V22 = Tree(tree_list=tree_list_19 + [Tree.tree_list_PROD(2)],
               name="V22",
               switches=[Vlist[14], 8, Vlist[15], 64, Vlist[16], 512, Vlist[17]])

    tree_list_0.extend([["EQU", Tree.tree_list_SUM(3), [None]],
                        Tree.tree_list_DIFF(2)])
    Slist_T0.extend([V19, V20, V21, V22, 0, V22])    
    T0 = Tree(tree_list=tree_list_0,
                name='T0',
                switches=Slist_T0)

    dx = 1
    dy = 1
    ex = 0.7
    ey = 0.7

    R0 = Room(name='R0',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=Slist)
    RE = Room(name='RE',
              position=[0, 0, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE)
    
    sol_list = []
    i = 0
    for value in V_values:
        digits = []
        while value > 0 or len(digits) < 3:
            digits.append(value%2)
            value = value//2
            if value%2:
                sol_list.append(f'S{i}')
            i += 1
    sol_list.append('D0')

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution=" ".join(sol_list),
                 level_color=Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.5),
                 name='Octal',
                 keep_proportions=True,
                 door_window_size=350,
                 random=True)
    
    return level