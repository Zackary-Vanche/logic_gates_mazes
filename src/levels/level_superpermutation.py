from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def f():
    
    v = 0

    S0 = Switch(name='S0', value=v)
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3', value=v)
    S4 = Switch(name='S4', value=v)
    S5 = Switch(name='S5')
    S6 = Switch(name='S6', value=v)
    S7 = Switch(name='S7', value=v)
    S8 = Switch(name='S8')
    S9 = Switch(name='S9', value=v)
    S10 = Switch(name='S10', value=v)
    S11 = Switch(name='S11')
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V0',
              switches=[S0, S1])
    V1 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V1',
              switches=[S2, S3])
    V2 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V2',
              switches=[S4, S5])
    V3 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V3',
              switches=[S6, S7])
    V4 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V4',
              switches=[S8, S9])
    V5 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V5',
              switches=[S10, S11])
    
    Slist = [1, 2, 3, V0, V1, V2, V3, V4, V5]
    
    tree_list = ['INLIST'] + [[None]]*13
    
    T0 = Tree(tree_list=tree_list,
              name='T0',
              switches = [3, 1, 2, 3] + Slist)
    T1 = Tree(tree_list=tree_list,
              name='T1',
              switches = [3, 1, 3, 2] + Slist)
    T2 = Tree(tree_list=tree_list,
              name='T2',
              switches = [3, 2, 1, 3] + Slist)
    T3 = Tree(tree_list=tree_list,
              name='T3',
              switches = [3, 2, 3, 1] + Slist)
    T4 = Tree(tree_list=tree_list,
              name='T4',
              switches = [3, 3, 1, 2] + Slist)
    T5 = Tree(tree_list=tree_list,
              name='T5',
              switches = [3, 3, 2, 1] + Slist)
    
    R0 = Room(name='R0',
              position = [0, 0, 2, 6],
              switches_list = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11])
    R1 = Room(name='R1',
              position = [3, 0, 1, 1],
              switches_list = [])
    R2 = Room(name='R2',
              position = [2.25, 2.5, 1, 1],
              switches_list = [])
    R3 = Room(name='R3',
              position = [3, 5, 1, 1],
              switches_list = [])
    R4 = Room(name='R4',
              position = [5, 5, 1, 1],
              switches_list = [])
    R5 = Room(name='R5',
              position = [3.5, 2.5, 1, 1],
              switches_list = [])
    RE = Room(name='RE',
              position=[5, 0, 1, 1],
              is_exit=True)   # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1, 0.5/6],
              relative_arrival_coordinates=[0, 1/2])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=R4)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R4,
              room_arrival=R5)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R5,
              room_arrival=RE)
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5],
                 fastest_solution='S0 S3 S4 S6 S7 S9 S10 D0 D1 D2 D3 D4 D5',
                 level_color=get_color(),
                 name='Superpermutation',
                 door_window_size=400,
                 keep_proportions=True,
                 y_separation=40,
                 border=40,
                 random=False)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.55, sa=1, li=0.2)