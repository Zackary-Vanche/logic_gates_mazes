from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list

def f():
    
    nR = 6
    nb = 3
    N = nb*3 # Number or switches by room
    nS = nR*N
    
    n_vertices = 8
    
    Sl = [Switch(name=f"S{i}") for i in range(nS)]
    
    Vl0 = [Tree(tree_list=Tree.tree_list_BIN(3),
               name=f'V{iV}',
               switches=Sl[nb*iV:nb*iV+nb]) for iV in range(nR*N//nb)]
    
    for iV, V in enumerate(Vl0):
        assert type(V) == Tree, str(V)
        assert V.name == f'V{iV}'
    
    Vl1 = []
    for iR in range(nR):
        for iV in range(nb):
            for jV in range(nb):
                if iV != jV:
                    Vl1.append(Tree(tree_list=["SUM", [None], Tree.tree_list_PROD(2)],
                                   name=f'V{len(Vl0)+len(Vl1)}',
                                   switches=[Vl0[nb*iR+iV], n_vertices, Vl0[nb*iR+jV]]))
                
    for V in Vl1:
        assert type(V) == Tree, str(V)
        
    Vl2 = [Tree(tree_list=Tree.tree_list_BIN(N),
                name=f'V{len(Vl0)+len(Vl1)+iV}',
                switches=Sl[N*iV:N*iV+N]) for iV in range(nR)]
        
    ex = 0.7
    ey = 0.7
    a = -0.2
    positions_list = [[2, 2, ex, ey],
                      [2+a, 1, ex, ey],
                      [2, 0, ex, ey],
                      [1, -a, ex, ey],
                      [0, 0, ex, ey],
                      [-a, 1, ex, ey],
                      [0, 2, ex, ey],
                      [1, 2+a, ex, ey-a]]
    
    Rl = [Room(name=f'R{iR}',
               position=positions_list[iR],
               switches_list=Sl[N*iR:N*iR+N],
               inside_color=Color.color_hls(hu=0.8*iR/nR, li=0.6, sa=0.3),
               surrounding_color=Color.IVORY) for iR in range(nR)]
    
    RE = Room(name='RE',
              position=positions_list[nR],
              is_exit=True,
              inside_color=Color.color_hls(hu=0.8*nR/nR, li=0.6, sa=0.3),
              surrounding_color=Color.IVORY)
    
    Rl = Rl + [RE]
    
    #          0
    #  1  2  3  4  5  6
    #          7
    
    EQUSET_list = []
    for l in [[0, 1, 2],
              [0, 3, 4],
              [0, 5, 6],
              [2, 3, 7],
              [4, 5, 7],
              [1, 6, 7],
              ]:
        for i in l:
            for j in l:
                if i != j:
                    EQUSET_list.append(i*n_vertices+j)
    EQUSET_list.sort()
    
    Tl = []
    for iR in range(nR):
        if iR == 0:
            Tl.append(Tree(tree_list=Tree.tree_list_INF(3),
                        name=f'T{iR}',
                        switches=Vl0[3*iR:3*(iR+1)]))
        elif iR == nR-1:
            Tl.append(Tree(tree_list=["AND",
                                      Tree.tree_list_INF(3),
                                      Tree.tree_list_EQUSET(2*2*3*(iR+1)),
                                      Tree.tree_list_INF(2)],
                        name=f'T{iR}',
                        switches=Vl0[3*iR:3*iR+3]+Vl1[:2*3*(iR+1)]+EQUSET_list+[Vl2[iR-1], Vl2[iR]],
                        cut_expression_depth_1=True))
        else:
            Tl.append(Tree(tree_list=["AND",
                         Tree.tree_list_INF(3),
                         Tree.tree_list_DIFF(2*3*(iR+1)),
                         Tree.tree_list_INF(2)],
                        name=f'T{iR}',
                        switches=Vl0[3*iR:3*iR+3]+Vl1[:2*3*(iR+1)]+[Vl2[iR-1], Vl2[iR]],
                        cut_expression_depth_1=True))
    assert len(Tl) == nR
    
    Dl = [Door(two_way=False,
                tree=Tl[iR],
                name=f'D{iR}',
                room_departure=Rl[iR],
                room_arrival=Rl[iR+1],
                inside_color=Color.color_hls(hu=0.8*(iR+0.5)/nR, li=0.6, sa=0.3),
                surrounding_color=Color.IVORY) for iR in range(nR)]
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=Rl,
                 doors_list=Dl,
                 fastest_solution="S3 S7 D0 S12 S13 S17 D1 S21 S23 S25 S26 D2 S28 S30 S31 S33 S34 S35 D3 S38 S39 S41 S42 S43 S44 D4 S45 S49 S50 S51 S52 S53 D5",
                 level_color=get_color(),
                 name='Hexagonal bipyramid',
                 keep_proportions=True,
                 door_window_size=400,
                 uniform_surrounding_colors=False,
                 uniform_inside_room_color=False)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.9, sa=0.1, li=0.5)