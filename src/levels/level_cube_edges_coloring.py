from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list

def f():
    
    nR = 12
    N = 2
    nS = nR*N
    
    Sl = [Switch(name=f"S{i}") for i in range(nS)]
    
    Vl = [Tree(tree_list=Tree.tree_list_BIN(N),
               name=f'V{iV}',
               switches=Sl[N*iV:N*iV+N]) for iV in range(nR)]
        
    dx = 0.75
    dy = 0.75
    ex = 0.25
    ey = 0.5
    
    hu = 0.67
    sa = 0.8
    
    Rl = [Room(name=f'R{iR}',
               position=[dx*(iR%4), dy*(iR//4), ex, ey],
               switches_list=Sl[N*iR:N*iR+N],
               inside_color=Color.color_hls(hu=hu, li=0.6, sa=sa*iR/nR),
               surrounding_color=Color.IVORY) for iR in range(nR)]
    
    RE = Room(name='RE',
              position=[dx*1.5, dy*3, ex, ey],
              is_exit=True,
              inside_color=Color.color_hls(hu=hu, li=0.6, sa=sa),
              surrounding_color=Color.IVORY)
    
    Rl = Rl + [RE]
    
    #   o 8       8 o
    #   9 4       7 11
    #       o 0 o
    #       1   3
    #       o 2 o
    #   9 5       6 11
    #   o 10     10 o
    
    connections = [[0, 1, 4],
                   [1, 2, 5],
                   [2, 3, 6],
                   [0, 3, 7],
                   [4, 8, 9],
                   [5, 9, 10],
                   [6, 10, 11],
                   [7, 8, 11]
                   ]
    
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
                           switches=[Vl[iR], 4]))
        else:
            Tl.append(Tree(tree_list=["AND", Tree.tree_list_INF(2)]+tree_list,
                           name=f'T{iR}',
                           switches=[Vl[iR], 4]+Slist_T0))
    assert len(Tl) == nR
    
    Dl = [Door(two_way=False,
                tree=Tl[iR],
                name=f'D{iR}',
                room_departure=Rl[iR],
                room_arrival=Rl[iR+1],
                inside_color=Color.color_hls(hu=hu, li=0.6, sa=sa*(iR+0.5)/nR),
                surrounding_color=Color.IVORY) for iR in range(nR)]
    
    for iD in [3, 7, 11]:
        Dl[iD].relative_departure_coordinates=[1/2, 1]
        Dl[iD].relative_arrival_coordinates=[1/2, 0]
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=Rl,
                 doors_list=Dl,
                 fastest_solution="S0 D0 S3 D1 S4 D2 S7 D3 D4 D5 D6 D7 S16 D8 S19 D9 S20 D10 S23 D11",
                 level_color=get_color(),
                 name='Cube edges coloring',
                 keep_proportions=True,
                 door_window_size=550,
                 uniform_surrounding_colors=False,
                 uniform_inside_room_color=False)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.67, sa=0.1, li=0.5)