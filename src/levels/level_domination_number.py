from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')

    Slist = [S0, S1, S2, S3, S4]

    T0 = Tree(tree_list=["AND"]+[Tree.tree_list_OR(2)]*4+[["INFOREQU", Tree.tree_list_SUM(5), [None]]],
                name='T0',
                switches=[S0, S1,
                          S1, S2,
                          S2, S3,
                          S3, S4]+Slist+[2])

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, 5*ex, ey],
                switches_list=Slist)
    RE = Room(name='RE',
              position=[1*dx, -1*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution="S1 S3 D0",
                 level_color=Levels_colors_list.FROM_HUE(hu=0.9, sa=0.2, li=0.5),
                 name='Domination number',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level