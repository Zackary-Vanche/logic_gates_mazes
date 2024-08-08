from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice

def level_integer_factorization(): 
    
    plist = [[0, 1, 0, 0],
             [1, 1, 0, 0],
             [1, 0, 1, 0],
             [1, 1, 1, 0],
             [1, 1, 0, 1],
             [1, 0, 1, 1]]
    flist = [rd_choice(plist) for i in range(4)]

    S0 = Switch(name='S0', value=flist[0][0])
    S1 = Switch(name='S1', value=flist[0][1])
    S2 = Switch(name='S2', value=flist[0][2])
    S3 = Switch(name='S3', value=flist[0][3])
    
    S4 = Switch(name='S4', value=flist[1][0])
    S5 = Switch(name='S5', value=flist[1][1])
    S6 = Switch(name='S6', value=flist[1][2])
    S7 = Switch(name='S7', value=flist[1][3])
    
    S8 = Switch(name='S8', value=flist[2][0])
    S9 = Switch(name='S9', value=flist[2][1])
    S10 = Switch(name='S10', value=flist[2][2])
    S11 = Switch(name='S11', value=flist[2][3])
    
    S12 = Switch(name='S12', value=flist[3][0])
    S13 = Switch(name='S13', value=flist[3][1])
    S14 = Switch(name='S14', value=flist[3][2])
    S15 = Switch(name='S15', value=flist[3][3])

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15]
    
    v = 1
    for l in flist:
        k = 0
        for i, p in enumerate(l):
           k += p*2**i
        v = v*k
        
    sol = []
    
    for S in Slist:
        if S.value:
            sol.append(S.name)
        S.value = 0
    sol = ' '.join(sol) + ' D0'
    
    V0 = Tree(tree_list=['PROD'] + [Tree.tree_list_BIN(4)]*4,
              name='V0',
              switches=Slist,
              cut_expression_depth_1=True)

    T0 = Tree(tree_list=['EQU', [None], [None]],
                name='T0',
                switches=[V0, v])

    dx = 3
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, 4*ex, 4*ey],
                switches_list=Slist)
    RE = Room(name='RE',
              position=[1*dx, 0*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[3.5/4, 1.5/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution=sol,
                 level_color=Levels_colors_list.FROM_HUE(hu=0.2, sa=0.5, li=0.5),
                 name='Integer factorization',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level