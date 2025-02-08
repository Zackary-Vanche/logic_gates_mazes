from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
# from random import shuffle as rd_shuffle
# from random import choice as rd_choice

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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14]
    
    edges_dict = {}
    k = 0
    for i in range(6):
        for j in range(i+1, 6):
            edges_dict[(i, j)] = k
            k += 1    
    
    a, b, c = 0, 2, 4
    d, e, f = 1, 3, 5
    
    Slist_T0 = []
    for i in range(6):
        for j in range(i+1, 6):
            for k in range(j+1, 6):
                if not set((i, j, k)) in [set((a, b, c)), set((d, e, f))]:
                    Slist_T0.extend([Slist[edges_dict[(i, j)]],
                                     Slist[edges_dict[(i, k)]],
                                     Slist[edges_dict[(j, k)]]])
    # Slist_T0.extend([Slist[edges_dict[(a, b)]],
    #                  Slist[edges_dict[(a, c)]],
    #                  Slist[edges_dict[(b, c)]],
    #                  rd_choice([0, 1])])
                
    tree_list = ["AND"] + [["NOT", Tree.tree_list_EQU(3)]]*18 # + [["NOT", Tree.tree_list_EQU(4)]]
    
    

    T0 = Tree(tree_list=tree_list,
              name='T0',
              switches=Slist_T0+[],
              cut_expression_depth_1=True)

    dx = 5
    dy = 1
    ex = 5
    ey = 1

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, 3*ey],
                switches_list=Slist)
    RE = Room(name='RE',
              position=[0*dx, 3*ey+1*dy, ex, 1*ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[1/2, 0])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0,],
                 fastest_solution="S0 S2 S5 S11 S12 S14 D0",
                 level_color=get_color(),
                 name="Ramsey's theorem",
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    a = 0.1
    lcolor=Levels_colors_list.FROM_HUE(hu=0.03-a, sa=0.3, li=0.3)
    color=Color.color_hls(hu=0.2-a, li=0.5, sa=1)
    lcolor.surrounding_color=color
    lcolor.contour_color=color
    return lcolor