from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list

def f():
    
    nR = 6
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
    
    hu = 0
    sa = 0.8
    
    Rl = [Room(name=f'R{iR}',
               position=[dx*(iR%3), dy*(iR//3), ex, ey],
               switches_list=Sl[N*iR:N*iR+N],
               inside_color=Color.color_hls(hu=hu, li=0.6, sa=sa*iR/nR),
               surrounding_color=Color.IVORY) for iR in range(nR)]
    
    RE = Room(name='RE',
              position=[dx*1, dy*2, ex, ey],
              is_exit=True,
              inside_color=Color.color_hls(hu=hu, li=0.6, sa=sa),
              surrounding_color=Color.IVORY)
    
    Rl = Rl + [RE]
    
    #       A
    #   0   1   2
    # 3 B 4 C 5 D  3
    
    connections = [[0, 1, 2],
                   [0, 3, 4],
                   [1, 4, 5],
                   [2, 3, 5]]
    
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
            Tl.append(Tree(tree_list=[None],
                           name=f'T{iR}',
                           switches=[1]))
        elif len(tree_list) == 1:
            Tl.append(Tree(tree_list=tree_list[0],
                           name=f'T{iR}',
                           switches=Slist_T0))
        else:
            Tl.append(Tree(tree_list=["AND"]+tree_list,
                           name=f'T{iR}',
                           switches=Slist_T0))
    assert len(Tl) == nR
    
    Dl = [Door(two_way=False,
                tree=Tl[iR],
                name=f'D{iR}',
                room_departure=Rl[iR],
                room_arrival=Rl[iR+1],
                inside_color=Color.color_hls(hu=hu, li=0.6, sa=sa*(iR+0.5)/nR),
                surrounding_color=Color.IVORY) for iR in range(nR)]
    
    for iD in [2, 5]:
        Dl[iD].relative_departure_coordinates=[1/2, 1]
        Dl[iD].relative_arrival_coordinates=[1/2, 0]
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=Rl,
                 doors_list=Dl,
                 fastest_solution="S0 D0 S3 D1 D2 S7 D3 D4 S10 D5",
                 level_color=Levels_colors_list.FROM_HUE(hu=hu, sa=0.1, li=0.5),
                 name='Tetrahedron edges coloring',
                 keep_proportions=True,
                 door_window_size=550,
                 uniform_surrounding_colors=False,
                 uniform_inside_room_color=False)
    
    return level