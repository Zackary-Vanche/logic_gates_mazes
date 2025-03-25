from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list

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
    S16 = Switch(name='S16')
    S17 = Switch(name='S17')
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')
    S20 = Switch(name='S20')
    S21 = Switch(name='S21')
    S22 = Switch(name='S22')
    S23 = Switch(name='S23')
    S24 = Switch(name='S24')
    S25 = Switch(name='S25')
    S26 = Switch(name='S26')
    S27 = Switch(name='S27')
    S28 = Switch(name='S28')
    S29 = Switch(name='S29')
    S30 = Switch(name='S30')
    S31 = Switch(name='S31')
    S32 = Switch(name='S32')
    S33 = Switch(name='S33')
    S34 = Switch(name='S34')
    S35 = Switch(name='S35')
    
    Slist = [[S0, S1, S2, S3, S4, S5],
             [S6, S7, S8, S9, S10, S11],
             [S12, S13, S14, S15, S16, S17],
             [S18, S19, S20, S21, S22, S23],
             [S24, S25, S26, S27, S28, S29],
             [S30, S31, S32, S33, S34, S35]]
    
    Slist_flat = [S for Sl in Slist for S in Sl]
    
    Slist_T0 = []
    tree_list_T0 = ["AND"]
    
    n = 6
    
    for a in range(n):
        for b in range(n):
            Sl = []
            tl = ["OR"]
            for ij in [[0, 0],
                       [-1, -2],
                       [-1, +2],
                       [+1, -2],
                       [+1, +2],
                       [-2, -1],
                       [-2, +1],
                       [+2, -1],
                       [+2, +1]]:
                i, j = ij
                if 0 <= a+i < n and 0 <= b+j < n:
                    Sl.append(Slist[a+i][b+j])
                    tl.append([None])
            Sl = sorted(Sl, key=lambda S: int(S.name.replace('S', '')))
            Slist_T0.extend(Sl)
            tree_list_T0.append(tl)
    Slist_T0.extend(Slist_flat+[8])
    tree_list_T0.append(["INFOREQU", Tree.tree_list_SUM(36), [None]])
    
    T0 = Tree(tree_list=tree_list_T0,
                name='T0',
                switches=Slist_T0,
                cut_expression_depth_1=True)

    ex = 6
    ey = 6

    R0 = Room(name='R0',
                position=[0, 0, ex, ey],
                switches_list=Slist_flat)
    RE = Room(name='RE',
              position=[ex+1, ey/2-1/2, 1, 1],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[(ex-1/2)/ex, 1/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution="S0 S5 S14 S15 S20 S21 S30 S35 D0",
                 level_color=get_color(),
                 name="Knight's graph dominating set",
                 keep_proportions=True,
                 door_window_size=360)
    
    return level

get_color = lambda : Levels_colors_list.opposite_hues(9)