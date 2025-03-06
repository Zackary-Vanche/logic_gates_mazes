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
    
    Slist = [[S0, S1, S2, S3],
             [S4, S5, S6, S7],
             [S8, S9, S10, S11]]
    
    Slist_flat = [S for Sl in Slist for S in Sl]
    
    Slist_T0 = []
    tree_list_T0 = ["AND"]
    
    for a in range(3):
        for b in range(4):
            Sl = []
            tl = ["OR"]
            for i in range(-3, 4):
                if 0 <= a-i < 3 and 0 <= b-i < 4 and not Slist[a-i][b-i] in Sl:
                    Sl.append(Slist[a-i][b-i])
                    tl.append([None])
                if 0 <= a-i < 3 and 0 <= b+i < 4 and not Slist[a-i][b+i] in Sl:
                    Sl.append(Slist[a-i][b+i])
                    tl.append([None])
                if 0 <= a+i < 3 and 0 <= b-i < 4 and not Slist[a+i][b-i] in Sl:
                    Sl.append(Slist[a+i][b-i])
                    tl.append([None])
                if 0 <= a+i < 3 and 0 <= b+i < 4 and not Slist[a+i][b+i] in Sl:
                    Sl.append(Slist[a+i][b+i])
                    tl.append([None])
            Sl = sorted(Sl, key=lambda S: int(S.name.replace('S', '')))
            Slist_T0.extend(Sl)
            tree_list_T0.append(tl)
    Slist_T0.extend(Slist_flat+[4])
    tree_list_T0.append(["INFOREQU", Tree.tree_list_SUM(12), [None]])
    
    T0 = Tree(tree_list=tree_list_T0,
                name='T0',
                switches=Slist_T0,
                cut_expression_depth_1=True)

    ex = 4
    ey = 3

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
                 fastest_solution="S0 S1 S2 S3 D0",
                 level_color=get_color(),
                 name="Bishop's graph dominating set",
                 keep_proportions=True,
                 door_window_size=395)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.6, sa=0.35, li=0.15)
    lcolor.surroungind_color = Color.color_hls(hu=0.6, sa=1, li=0.7)
    lcolor.background_color, lcolor.room_color = lcolor.room_color, lcolor.background_color
    return lcolor