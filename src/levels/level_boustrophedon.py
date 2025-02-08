from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice

def f(): 

    nR = 8

    Slist = [Switch(name=f'S{i}', value=rd_choice([0, 1])) for i in range(nR)]
    
    Tl = []
    
    for i in range(nR):
        Sa = Slist[i]
        if i == nR-1:
            if Sa.value:
                Tl.append(Tree(tree_list=[None],
                               name=f'T{i}',
                               switches=[Sa]))
            else:
                Tl.append(Tree(tree_list=Tree.tree_list_not,
                               name=f'T{i}',
                               switches=[Sa]))
        else:
            Sb = Slist[i+1]
            tree_list_str = "F"*Sa.value + "T"*(not Sa.value) + "T"*Sb.value + "F"*(not Sb.value)
            Tl.append(Tree(tree_list=['NOT', Tree.tree_list_from_str(tree_list_str)],
                           name=f'T{i}',
                           switches=[Sa, Sb]))

    dx = 5
    dy = 1
    ex = dx/2
    ey = dy/2

    Rl = [Room(name=f'R{i}',
               position=[dx*(i%2), dy*(i//2)+dy/2*(i%2==1), ex, ey],
               switches_list=[]) for i in range(1, nR)]
    
    R0 = Room(name='R0',
              position=[0, ey-ex/2, ex, ex/2],
              switches_list=Slist)
    
    RE = Room(name='RE',
              position=[0, dy*(nR//2), ex, ey],
              is_exit=True)
    
    Rl = [R0] + Rl + [RE]

    Dl = [Door(two_way=False,
               tree=Tl[i],
               name=f'D{i}',
               room_departure=Rl[i],
               room_arrival=Rl[i+1]) for i in range(nR)]
    
    sol_list = []
    for i, S in enumerate(Slist):
        if S.value:
            sol_list.append(S.name)
        S.value = 0
    sol = " ".join(sol_list) + " D0 D1 D2 D3 D4 D5 D6 D7"

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=Rl,
                 doors_list=Dl,
                 fastest_solution=sol,
                 level_color=get_color(),
                 name='Boustrophedon',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.15, sa=0.2, li=0.2)
    lcolor.surrounding_color = Color.color_hls(hu=0.1, sa=0.6, li=0.5)
    lcolor.contour_color = Color.color_hls(hu=0.1, sa=0.6, li=0.5)
    return lcolor