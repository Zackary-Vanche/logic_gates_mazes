from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import random as rd_random
from random import randint as rd_randint
from random import shuffle as rd_shuffle

def level_quaternary(): 

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

    Slist_0 = [S0, S1]
    Slist_1 = [S2, S3]
    Slist_2 = [S4, S5]
    Slist_3 = [S6, S7]
    Slist_4 = [S8, S9]
    Slist_5 = [S10, S11]
    Slist_6 = [S12, S13]
    
    tree_list_V7 = ["SUM", [None], ["PROD", [None], [None]]]
    
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
    V5 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_5)),
          name='V5',
          switches=Slist_5)
    V6 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_6)),
          name='V6',
          switches=Slist_6)
    V7 = Tree(tree_list=tree_list_V7,
          name='V7',
          switches=[V0, 4, V1])
    V8 = Tree(tree_list=tree_list_V7,
          name='V8',
          switches=[V2, 4, V3])
    V9 = Tree(tree_list=["SUM", [None], ["PROD", [None], [None]], ["PROD", [None], [None]]],
          name='V9',
          switches=[V4, 4, V5, 16, V6])

    Vlist = [V0, V1, V2, V3, V4, V5, V6]
    
    Slist_lhs = [S0, S1, S2, S3, S4, S5, S6, S7]
    m = rd_randint(1, 256)
    i = 0
    while m > 0:
        Slist_lhs[i].value = m % 2
        i += 1
        m = m // 2 
    
    Slist_rhs = [S8, S9, S10, S11, S12, S13]
    n = 0
    for i_S, S in enumerate(Slist_lhs):
        n += S.value * 2**(i_S%4)
    j = 0
    while n > 0:
        Slist_rhs[j].value = n % 2
        j += 1
        n = n//2
        
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13]
    
    def get_tree(i):
        tree_list = []
        Slist_T = []
        for j in range(i):
            if Vlist[i].get_value() == Vlist[j].get_value():
                tree_list.append(Tree.tree_list_EQU(2))
                Slist_T.extend([Vlist[j], Vlist[i]])
        if len(tree_list) == 0:
            return Tree(tree_list=[None],
                        name=f'T{i}',
                        switches=[1])
        elif len(tree_list) == 1:
            return Tree(tree_list=tree_list[0],
                        name=f'T{i}',
                        switches=Slist_T)
        else:
            return Tree(tree_list=["AND"] + tree_list,
                        name=f'T{i}',
                        switches=Slist_T)
                
    T0 = get_tree(0)
    T1 = get_tree(1)
    T2 = get_tree(2)
    T3 = get_tree(3)
    T4 = get_tree(4)
    T5 = get_tree(5)
    T6 = get_tree(6)
    T7 = Tree(tree_list=["AND", ['EQU', Tree.tree_list_SUM(2), [None]], Tree.tree_list_DIFF(2)],
                name='T7',
                switches=[V7, V8, V9, 0, V9])
            
    dx = 1.5
    dy = 1
    ex = 1
    ey = 0.7
    eye = 0.3

    R0 = Room(name='R0',
                position=[3*dx, 0*dy, ex, ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[3*dx, 1*dy, ex, ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[3*dx, 2*dy, ex, ey],
                switches_list=Slist_4)
    R5 = Room(name='R5',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=Slist_5)
    R6 = Room(name='R6',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=Slist_6)
    R7 = Room(name='R7',
                position=[1*dx, dy, ex, eye],
                switches_list=[])
    RE = Room(name='RE',
              position=[1*dx, 0*dy, ex, eye],
              is_exit=True,
              inside_color=Color.color_hls(hu=0, li=0.5, sa=0))
    
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
                room_arrival=R7)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R7,
                room_arrival=RE)
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.6)
    lcolor.surrounding_color = Color.IVORY
    
    a = rd_random()
    hue_list = [i/4+a for i in range(4)]
    rd_shuffle(hue_list)
    sa = 0.5
    rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE]
    doors_list=[D0, D1, D2, D3, D4, D5, D6, D7]
    for i in range(7):
        R = rooms_list[i]
        D = doors_list[i]
        hue = hue_list[Vlist[i].get_value()]
        R.inside_color=Color.color_hls(hu=hue, li=0.5, sa=sa)
        D.inside_color=Color.color_hls(hu=hue, li=0.5, sa=sa)
    hue_6 = hue_list[Vlist[6].get_value()]
    R7.inside_color=Color.color_hls(hu=hue_6, li=0.5, sa=2*0.5/3)
    D7.inside_color=Color.color_hls(hu=hue_6, li=0.5, sa=0.5/3)
    RE.inside_color=Color.color_hls(hu=hue_6, li=0.5, sa=0)
    
    
    sol_switches_binary = []
    for S in Slist:
        sol_switches_binary.append(S.value)
        S.value = 0
        
    sol_list = []
    for i in range(7):
        if sol_switches_binary[2*i]:
            sol_list.append(f"S{2*i}")
        if sol_switches_binary[2*i+1]:
            sol_list.append(f"S{2*i+1}")
        sol_list.append(f"D{i}")
    sol_list.append("D7")

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=rooms_list,
                 doors_list=doors_list,
                 fastest_solution=' '.join(sol_list),
                 level_color=lcolor,
                 name='Quaternary',
                 keep_proportions=True,
                 door_window_size=300,
                 uniform_inside_room_color=False,
                 random=True)
    
    return level
