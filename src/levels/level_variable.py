from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Level_color import Level_color
from Color import Color
from random import randint as rd_randint

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')

    Slist = [S0, S1, S2, S3]
    
    sol_list = []
    for i in range(len(Slist)):
        if rd_randint(0, 1):
            sol_list.append(Slist[i].name)

    V0 = Tree(tree_list=[None] if 'S0' in sol_list else Tree.tree_list_NOT,
          name='V0',
          switches=[S0])
    V1 = Tree(tree_list=[None] if 'S1' in sol_list else Tree.tree_list_NOT,
          name='V1',
          switches=[S1])
    V2 = Tree(tree_list=[None] if 'S2' in sol_list else Tree.tree_list_NOT,
          name='V2',
          switches=[S2])
    V3 = Tree(tree_list=[None] if 'S3' in sol_list else Tree.tree_list_NOT,
          name='V3',
          switches=[S3])
    T0 = Tree(tree_list=Tree.tree_list_AND(4),
                name='T0',
                switches=[V0, V1, V2, V3])

    dx = 1
    dy = 1

    R0 = Room(name='R0',
                position=[1*dx, 1*dy, 0.75, 0.75],
                switches_list=Slist)
    RE = Room(name='RE',
              position=[0*dx, 0*dy, 0.5, 0.5],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[1/3, 1/3])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution=' '.join(sol_list) + ' D0',
                 level_color=get_color(),
                 name='Variable',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def get_color():
    lcolor = Level_color(background_color=Color.color_hls(0, 0.3, 0.4),
                         room_color=Color.color_hls(0.9, 0.6, 0.4),
                         letters_color=Color.WHITE,
                         contour_color=Color.IVORY,
                         inside_room_color=Color.BLACK,
                         surrounding_color=Color.IVORY)
    return lcolor