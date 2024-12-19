from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list

def f():
    
    nR = 10
    N = 3
    nS = nR*N
    
    Sl = [Switch(name=f"S{i}") for i in range(nS)]
    
    Vl = [Tree(tree_list=Tree.tree_list_BIN(N),
               name=f'V{iV}',
               switches=Sl[N*iV:N*iV+N]) for iV in range(nR)]
        
    dx = 12
    dy = 9
    ex = 8
    ey = 5
    
    hu = 0.1
    sa = 0.8
    
    Rl = [Room(name=f'R{iR}',
               position=[dx*(iR%3), dy*(iR//3), ex, ey],
               switches_list=Sl[N*iR:N*iR+N],
               inside_color=Color.color_hls(hu=hu, li=0.6, sa=sa*iR/nR),
               surrounding_color=Color.IVORY) for iR in range(nR)]
    
    RE = Room(name='RE',
              position=[dx*1, dy*3, ex, ey],
              is_exit=True,
              inside_color=Color.color_hls(hu=hu, li=0.6, sa=sa),
              surrounding_color=Color.IVORY)
    
    Rl = Rl + [RE]
    
    #   A  B  C  D  E
    # A x  0  1  2  3
    # B 0  x  4  5  6
    # C 1  4  x  7  8
    # D 2  5  7  x  9
    # E 3  6  8  9  x
    
    connections = [[0, 1, 2, 3],
                   [0, 4, 5, 6],
                   [1, 4, 7, 8],
                   [2, 5, 7, 9],
                   [3, 6, 8, 9]]
    
    def is_connected(a, b):
        for connect in connections:
            if a in connect and b in connect:
                return True
        return False
    
    Tl = []
    for iR in range(nR):
        tree_list = []
        Slist_T0 = []
        for jR in range(nR):
            if is_connected(iR, jR) and jR < iR:
                tree_list.append(Tree.tree_list_DIFF(2))
                Slist_T0.extend([Vl[jR], Vl[iR]])
        if len(tree_list) == 0:
            Tl.append(Tree(tree_list=Tree.tree_list_INF(2),
                           name=f'T{iR}',
                           switches=[Vl[iR], 5]))
        else:
            Tl.append(Tree(tree_list=["AND", Tree.tree_list_INF(2)]+tree_list,
                           name=f'T{iR}',
                           switches=[Vl[iR], 5]+Slist_T0))
    assert len(Tl) == nR
    
    Dl = [Door(two_way=False,
                tree=Tl[iR],
                name=f'D{iR}',
                room_departure=Rl[iR],
                room_arrival=Rl[iR+1],
                inside_color=Color.color_hls(hu=hu, li=0.6, sa=sa*(iR+0.5)/nR),
                surrounding_color=Color.IVORY) for iR in range(nR)]
    
    for iD in [2, 5, 8]:
        Dl[iD].relative_departure_coordinates=[1/2, 1]
        Dl[iD].relative_arrival_coordinates=[1/2, 0]
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=Rl,
                 doors_list=Dl,
                 fastest_solution='S0 D0 S4 D1 S8 D2 S9 S10 D3 S14 D4 S15 S16 D5 D6 D7 S24 D8 S28 D9',
                 level_color=Levels_colors_list.FROM_HUE(hu=hu, sa=0.1, li=0.5),
                 name='K5 edges coloring',
                 keep_proportions=True,
                 door_window_size=550,
                 uniform_surrounding_colors=False,
                 uniform_inside_room_color=False)
    
    return level