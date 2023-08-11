from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

from random import randint as rd_randint

def level_equation(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7]

    a = rd_randint(0, 2**4-1)
    b = rd_randint(0, 2**4-1)
    
    assert 0 <= a < 2**4
    assert 0 <= b < 2**4
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(4),
              empty=True,
              name='V0',
              switches=[S0, S1, S2, S3])
    V1 = Tree(tree_list=Tree.tree_list_BIN(4),
              empty=True,
              name='V1',
              switches=[S4, S5, S6, S7])
    
    tree_list_SUM = ['SUM', [None], [None]]
    tree_list_MINUS = ['SUM', [None], ['MINUS', [None]]]

    T0 = Tree(tree_list=['AND',
                         ['EQU', tree_list_SUM, [None]],
                         ['EQU', tree_list_MINUS, [None]]],
                empty=True,
                name='T0',
                switches=[V0, V1, a+b, V0, V1, a-b])

    R0 = Room(name='R0',
                position=[0, 2, 3, 3],
                switches_list=Slist)
    RE = Room(name='RE',
              position=[3, 0, 1, 1],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[5/6, 1/6])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 intermediate_values_list=[V0, V1],
                 doors_list=[D0],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0, sa=0.5, li=0.2),
                 name='Equation',
                 keep_proportions=True,
                 door_window_size=350,
                 random=True)
    
    return level    