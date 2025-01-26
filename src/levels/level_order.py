from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle

def f(): 
    
    Snames = ['S0', 'S1', 'S2']
    rd_shuffle(Snames)

    S0 = Switch(name=Snames[0])
    S1 = Switch(name=Snames[1])
    S2 = Switch(name=Snames[2])

    Slist = [S0, S1, S2]
    
    Tnames = ['T0', 'T1', 'T2']
    rd_shuffle(Tnames)
    
    Dnames = [name.replace('T', 'D') for name in Tnames]

    T0 = Tree(tree_list=Tree.tree_list_NOT,
                name=Tnames[0],
                switches=[S1])
    T1 = Tree(tree_list=Tree.tree_list_NOT,
                name=Tnames[1],
                switches=[S2])
    T2 = Tree(tree_list=[None],
                name=Tnames[2],
                switches=[1])
    T3 = Tree(tree_list=Tree.tree_list_AND(3),
                name='T3',
                switches=Slist,
                easy_logical_expression_PN="& S0 ( & S1 S2 ) \n= & ( S0 S1 S2 )")

    ex = 1
    ey = 1
    dx = 2
    dy = 2
    pos_list = [[-dx, -dy, ex, ey],
                [+dx, -dy, ex, ey],
                [0, -dy, ex, ey]]
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
              position=[0, +dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=True,
              tree=T0,
              name=Dnames[0],
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=True,
              tree=T1,
              name=Dnames[1],
              room_departure=R0,
              room_arrival=R2)
    D2 = Door(two_way=True,
              tree=T2,
              name=Dnames[2],
              room_departure=R3,
              room_arrival=R0)
    D3 = Door(two_way=False,
              tree=T3,
              name='D3',
              room_departure=R0,
              room_arrival=RE)
    
    sol = ' '.join([Dnames[0], Snames[0], Dnames[0],
                    Dnames[1], Snames[1], Dnames[1],
                    Dnames[2], Snames[2], Dnames[2],
                    'D3'])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, RE],
                 doors_list=[D0, D1, D2, D3],
                 fastest_solution=sol,
                 level_color=get_color(),
                 name='Order',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.6, sa=0.55, li=0.5)