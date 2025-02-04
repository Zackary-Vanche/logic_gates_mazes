from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    
    T0 = Tree(tree_list=[None],
              name='T0',
              switches=[1])
    
    tree_list_1 = ["AND", Tree.tree_list_XOR(2), Tree.tree_list_XOR(2)]
    T1 = Tree(tree_list=tree_list_1,
              name='T1',
              switches=[S0, S3, S3, S4])
    T2 = Tree(tree_list=tree_list_1,
                name='T2',
                switches=[S1, S4, S4, S5])
    T3 = Tree(tree_list=["AND", Tree.tree_list_XOR(2), [None]],
                name='T3',
                switches=[S2, S5, S5])
    
    R0 = Room(name='R0',
                position=[0, 1.5, 1, 1],
                switches_list=[S0, S1, S2])
    R1 = Room(name='R1',
                position=[1, 0, 1, 1],
                switches_list=[S3])
    R2 = Room(name='R2',
                position=[2, 1.5, 1, 1],
                switches_list=[S4])
    R3 = Room(name='R3',
                position=[3, 0, 1, 1],
                switches_list=[S5])
    RE = Room(name='RE',
              position=[4, 1.5, 1, 1],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[0, 1])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=[1, 1],
                relative_arrival_coordinates=[0, 0])
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[0, 1])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=RE,
                relative_departure_coordinates=[1, 1],
                relative_arrival_coordinates=[0, 1/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, RE],
                 doors_list=[D0, D1, D2, D3],
                 fastest_solution='D0 S3 D1 S4 D2 S5 D3',
                 level_color=get_color(),
                 name='Boolean',
                 keep_proportions=True,
                 door_window_size=400)
    
    return level

def get_color():
    lcolor=Levels_colors_list.FROM_HUE(hu=0.6, sa=0.5, li=0.6)
    lcolor.surrounding_color = Color.WHITE
    lcolor.contour_color = Color.WHITE
    return lcolor