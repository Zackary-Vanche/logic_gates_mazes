from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color
from random import choice as rd_choice

def f(): 

    S0 = Switch(name='S0', value=rd_choice([0, 1]))
    S1 = Switch(name='S1', value=rd_choice([0, 1]))
    S2 = Switch(name='S2')

    tree_list_BIN = Tree.tree_list_BIN(2)
    tree_list_EQU = ['EQU', [None], [None]]
    V0 = Tree(tree_list=[None],
              name='V0',
              switches=[1])
    V1 = Tree(tree_list=tree_list_BIN,
              name='V1',
              switches=[S0, S1])
    V2 = Tree(tree_list=tree_list_EQU,
              name='V2',
              switches=[V1, 3])
    V3 = Tree(tree_list=tree_list_BIN,
              name='V3',
              switches=[V2, V0])
    V4 = Tree(tree_list=tree_list_EQU,
              name='V4',
              switches=[V3, 2])
    
    Vtest = Tree(tree_list=Tree.tree_list_NAND(2),
                 name='V5',
                 switches=[S0, S1])
    assert Vtest.get_value() == V4.get_value()

    T0 = Tree(tree_list=tree_list_EQU,
              name='T0',
              switches=[S2, V4])

    dx = 1.5
    dy = 1.5
    ex = 1
    ey = 1

    R0 = Room(name='R0',
              position=[1*dx, 0*dy, ex, dy+ey],
              switches_list=[S0, S1])
    R1 = Room(name='R1',
              position=[0*dx, 0*dy, ex, ey],
              switches_list=[S2])
    RE = Room(name='RE',
             position=[0*dx, 1*dy, ex, ey],
             is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R1,
                room_arrival=RE)
    
    solution = 'S2 '*V4.get_value() + 'D0'

    level = Maze(start_room_index=1,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, RE],
                 doors_list=[D0],
                 fastest_solution=solution,
                 level_color=get_color(),
                 name='Relay',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.2)
    lcolor.surrounding_color = Color.TOTAL_YELLOW
    lcolor.contour_color = Color.TOTAL_YELLOW
    return lcolor