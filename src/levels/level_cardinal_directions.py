from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle

def level_cardinal_directions(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')

    Slist = [S0, S1, S2]

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[1])
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[1])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[1])
    T3 = Tree(tree_list=Tree.tree_list_OR(3),
                name='T3',
                switches=Slist,
                easy_logical_expression_PN="| S0 ( | S1 S2 ) \n= | ( S0 S1 S2 )")

    ex = 1
    ey = 1
    dx = 2
    dy = 2
    pos_list = [[-dx, 0, ex, ey],
                [+dx, 0, ex, ey],
                [0, -dy, ex, ey],
                [0, +dy, ex, ey]]
    rd_shuffle(pos_list)

    R0 = Room(name='R0',
                position=[0, 0, ex, ey],
                switches_list=[])
    R1 = Room(name='R1',
                position=pos_list[0],
                switches_list=[S0])
    R2 = Room(name='R2',
                position=pos_list[1],
                switches_list=[S1])
    R3 = Room(name='R3',
                position=pos_list[2],
                switches_list=[S2])
    RE = Room(name='RE',
              position=pos_list[3],
              is_exit=True)

    D0 = Door(two_way=False,
              tree=T0,
              name='D0',
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=True,
              tree=T1,
              name='D1',
              room_departure=R0,
              room_arrival=R2)
    D2 = Door(two_way=False,
              tree=T2,
              name='D2',
              room_departure=R3,
              room_arrival=R0)
    D3 = Door(two_way=False,
              tree=T3,
              name='D3',
              room_departure=R0,
              room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, RE],
                 doors_list=[D0, D1, D2, D3],
                 fastest_solution='D1 S1 D1 D3',
                 level_color=Levels_colors_list.FROM_HUE(hu=0.12, sa=0.6, li=0.5),
                 name='Cardinal directions',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level
