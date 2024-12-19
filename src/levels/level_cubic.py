from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color
import numpy as np

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7]

    T0 = Tree(tree_list=['AND',
                         ['SUP', Tree.tree_list_SUM(4), [None]]] + [Tree.tree_list_XOR(2)]*12,
                name='T0',
                switches=[S0, S1, S2, S4, 2,
                          S0, S1,
                          S0, S2,
                          S0, S4,
                          S1, S3,
                          S1, S5,
                          S2, S3,
                          S2, S6,
                          S3, S7,
                          S4, S5,
                          S4, S6,
                          S5, S7,
                          S6, S7])

    R0 = Room(name='R0',
                position=[0, 0, 1, 1],
                switches_list=Slist)
    r = 2
    phi = np.random.random()*np.pi*2
    RE = Room(name='RE',
              position=[r*np.cos(phi), r*np.sin(phi), 1, 1],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE)
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0.85, sa=0.6, li=0.5)
    lcolor.contour_color = Color.TOTAL_BLUE
    lcolor.surrounding_color = Color.TOTAL_BLUE

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution='S1 S2 S4 S7 D0',
                 level_color=lcolor,
                 name='Cubic',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level
