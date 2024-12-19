from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color
from random import choice as rd_choice

def f(): 
    
    plist = [[1, 0, 0, 0],
             [0, 1, 0, 0],
             [1, 1, 0, 0],
             [1, 0, 1, 0],
             [1, 1, 1, 0],
             [1, 1, 0, 1],
             [1, 0, 1, 1]]
    flist = [rd_choice(plist) for i in range(4)]
    flist.sort(key=lambda l : sum([l[i]*2**i for i in range(len(l))]))

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

    Slist = [S0, S1, S2, S3,
             S4, S5, S6, S7,
             S8, S9, S10, S11,
             S12, S13, S14, S15]
    
    v = 1
    for l in flist:
        k = 0
        for i, p in enumerate(l):
           k += p*2**i
        v = v*k
        
    sol = []
    
    for i, S in enumerate(Slist):
        if S.value:
            sol.append(S.name)
        S.value = 0
        if i%4==3:
            sol.append(f'D{i//4}')
    sol = ' '.join(sol)
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(4),
          name='V0',
          switches=Slist[0:4])
    V1 = Tree(tree_list=Tree.tree_list_BIN(4),
          name='V1',
          switches=Slist[4:8])
    V2 = Tree(tree_list=Tree.tree_list_BIN(4),
          name='V2',
          switches=Slist[8:12])
    V3 = Tree(tree_list=Tree.tree_list_BIN(4),
          name='V3',
          switches=Slist[12:16])
    
    V4 = Tree(tree_list=['PROD'] + [[None]]*4,
              name='V4',
              switches=[V0, V1, V2, V3])

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[1])
    T1 = Tree(tree_list=['INFOREQU', [None], [None]],
                name='T1',
                switches=[V0, V1])
    T2 = Tree(tree_list=['INFOREQU', [None], [None]],
                name='T2',
                switches=[V1, V2])
    T3 = Tree(tree_list=['AND',
                         ['INFOREQU', [None], [None]],
                         ['EQU', [None], [None]]],
                name='T3',
                switches=[V2, V3,
                          V4, v])

    R0 = Room(name='R0',
                position=[1, 0, 4, 1],
                switches_list=Slist[0:4])
    R1 = Room(name='R1',
                position=[5, 1, 1, 4],
                switches_list=Slist[4:8])
    R2 = Room(name='R2',
                position=[1, 5, 4, 1],
                switches_list=Slist[8:12])
    R3 = Room(name='R3',
                position=[0, 1, 1, 4],
                switches_list=Slist[12:16])
    RE = Room(name='RE',
              position=[2, 2, 2, 2],
              is_exit=True)

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
                room_arrival=RE,
                relative_departure_coordinates=[1, 1/2],
                relative_arrival_coordinates=[0, 1/2])
    
    hu = 0.2
    sa = 0.6
    lcolor = Level_color(background_color=Color.color_hls(hu, 0.4, sa),
                         room_color=Color.color_hls(hu, 0.15, 0.8 * sa),
                         letters_color=Color.BLACK,
                         contour_color=Color.color_hls(hu=0.1, li=0.7, sa=1),
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.color_hls(hu=0.1, li=0.8, sa=1))

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, RE],
                 doors_list=[D0, D1, D2, D3],
                 fastest_solution=sol,
                 level_color=lcolor,
                 name='Integer factorization',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level